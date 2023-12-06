import httpx
import asyncio
import json
import pprint

#Breakdown of data transform according to PokeAPI lexicon:
#Pokedex URL contains species URLs ->
#   species URLs contains varieties URLs ->
#       variety URLs contain nat dex URLs (the data we want)

def get_species_urls(POKEDEX):
    resp = httpx.get(POKEDEX)
    result = resp.json()
    species_urls = [entry["pokemon_species"]["url"] for entry in result["pokemon_entries"]][19:30]
    #species_urls = [entry["pokemon_species"]["url"] for entry in result["pokemon_entries"]]
    return species_urls

async def get_pokemon_datasets(species_url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(species_url)
        #print(f"Gathering data for {species_url}")
        return resp.json()

async def get_varieties_from_datasets(species_urls):
    # Create tasks using list comprehension, sometimes executres too quickly and creates timeout errors.
    # tasks = [asyncio.create_task(get_pokemon_datasets(species_url)) for species_url in species_urls]
    # Instead, let's build a for loop that we can put a sleep in. Performance is not the priority here.
    aggregated_pokemon_entries = {}
    for species_url in species_urls:
        task = asyncio.create_task(get_pokemon_datasets(species_url))
        # here's where we can fit a sleep
        #await asyncio.sleep(1)
        result = await task
        if result:
            #here's the trick to getting an "aggregated" object of the tasks iterated in parse_varieties_urls
            aggregated_pokemon_entries.update(await parse_varieties_urls(result["varieties"]))
            #await parse_varieties_urls(result["varieties"])
        else:
            print(f"1st fail")

    return aggregated_pokemon_entries

async def get_varieties_data(varieties_url):
    pokemon_url = varieties_url["pokemon"]["url"]
    async with httpx.AsyncClient() as client:
        resp = await client.get(pokemon_url)
        return resp.status_code, resp.json()

async def parse_varieties_urls(varieties_urls):
    tasks = [asyncio.create_task(get_varieties_data(varieties_url)) for varieties_url in varieties_urls]
    pokemon_entries = {}
    for task in asyncio.as_completed(tasks):
        status_code, result = await task
        pokemon_name = result["name"]
        if status_code == 200:
            pokemon_entry = {
                "id": result["id"],
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
                ]
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

'''
async def parse_varieties_urls(varieties_urls):
    tasks = [asyncio.create_task(get_varieties_data(varieties_url)) for varieties_url in varieties_urls]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    pokemon_entries = {}

    for did in done:
        result = await did
        pokemon_name = result["name"]
        pokemon_entry = {
            "id": result["id"],
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
            ]
        }
        pokemon_entries[pokemon_name] = pokemon_entry
        print(f"processing {pokemon_name}")
    return pokemon_entries
    
    for doing in pending:
        pass

async def parse_varieties_urls(varieties_urls):
    tasks = [asyncio.create_task(get_varieties_data(varieties_url)) for varieties_url in varieties_urls]
    pokemon_entries = {}
    results = await asyncio.gather(*tasks)

    for result in results:
        pokemon_name = result["name"]
        pokemon_entry = {
            "id": result["id"],
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
            ]
        }
        pokemon_entries[pokemon_name] = pokemon_entry
        print(f"processing {pokemon_name}")
    
    return pokemon_entries 
'''

async def main():
    POKEDEX = 'https://pokeapi.co/api/v2/pokedex/32'
    species_urls = get_species_urls(POKEDEX)
    aggregated_pokemon_entries = await get_varieties_from_datasets(species_urls)
    print(json.dumps(aggregated_pokemon_entries, indent=2))
    #asyncio.run(get_varieties_from_datasets(species_urls))

asyncio.run(main())

