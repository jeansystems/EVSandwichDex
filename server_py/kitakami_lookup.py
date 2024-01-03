import os
import httpx
import asyncio
import json

#Breakdown of data transform according to PokeAPI lexicon:
#Pokedex URL contains species URLs ->
#   species URLs contains varieties URLs ->
#       variety URLs contain nat dex URLs (the data we want)
#I'm leaving various print statements in the code to demonstrate "breaks" where validation can be tested

def get_species_urls(POKEDEX):
    resp = httpx.get(POKEDEX)
    result = resp.json()
    species_urls = [entry["pokemon_species"]["url"] for entry in result["pokemon_entries"]][0:5]
    return species_urls

async def get_pokemon_datasets(species_url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(species_url)
        result = resp.json()

        pokedex_numbers = result["pokedex_numbers"]
        for pokedex_number in pokedex_numbers:
            if pokedex_number["pokedex"]["name"] == "national":
                natdex_number = pokedex_number["entry_number"]
        for pokedex_number in pokedex_numbers:
            if pokedex_number["pokedex"]["name"] == "kitakami":
                kitdex_number = pokedex_number["entry_number"]

        return result, natdex_number, kitdex_number

async def get_varieties_from_datasets(species_urls):
    # Create tasks using list comprehension, sometimes executres too quickly and creates timeout errors.
    # tasks = [asyncio.create_task(get_pokemon_datasets(species_url)) for species_url in species_urls]
    # Instead, let's build a for loop that we can put a sleep in. Performance is not the priority here.
    aggregated_pokemon_entries = {}
    for species_url in species_urls:
        task = asyncio.create_task(get_pokemon_datasets(species_url))
        # here's where we can fit a sleep
        #await asyncio.sleep(1)
        result, natdex_number, kitdex_number = await task
        if result:
            #here's the trick to getting an "aggregated" object of the tasks iterated in parse_varieties_urls
            aggregated_pokemon_entries.update(await parse_varieties_urls(result["varieties"], natdex_number, kitdex_number))
            #await parse_varieties_urls(result["varieties"])
        else:
            print(f"1st fail")

    return aggregated_pokemon_entries

async def get_varieties_data(varieties_url):
    pokemon_url = varieties_url["pokemon"]["url"]
    async with httpx.AsyncClient() as client:
        resp = await client.get(pokemon_url)
        return resp.status_code, resp.json()

async def parse_varieties_urls(varieties_urls, natdex_number, kitdex_number):
    tasks = [asyncio.create_task(get_varieties_data(varieties_url)) for varieties_url in varieties_urls]
    pokemon_entries = {}
    for task in asyncio.as_completed(tasks):
        status_code, result = await task
        pokemon_name = result["name"]
        if status_code == 200:
            pokemon_entry = {
                "dex_numbers": {
                "national": natdex_number,
                "kitakami": kitdex_number,
                "species_id": result["order"]
                },
                "types": [
                    {
                        "slot": type_entry["slot"], 
                        "name": type_entry["type"]["name"]
                    } 
                        for type_entry in result["types"]
                ],
                "stats": [
                    {
                        "name": stat_entry["stat"]["name"],
                        "yield": stat_entry["effort"]
                    }
                        for stat_entry in result["stats"]
                ],
                "status_code": status_code
            }

            pokemon_entries[pokemon_name] = pokemon_entry
        else:
            bad_entry = {
                "status_code": status_code
            }
            pokemon_entries[pokemon_name] = bad_entry
        #print(f"Processing {pokemon_name}...")
        #print(f"{pokemon_name} returned with status {status_code}")
    return pokemon_entries

async def main():
    POKEDEX = 'https://pokeapi.co/api/v2/pokedex/32'
    species_urls = get_species_urls(POKEDEX)
    aggregated_pokemon_entries = await get_varieties_from_datasets(species_urls)
    aggregated_json = json.dumps(aggregated_pokemon_entries, indent=2)
    print(aggregated_json)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = '../src/data/kitakami.json'
    output_path = os.path.normpath(os.path.join(script_dir,relative_path))
    with open(output_path, "w") as file:
        file.write(aggregated_json)

asyncio.run(main())