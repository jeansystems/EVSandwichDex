import httpx
import asyncio
import json

#Breakdown of data transform according to PokeAPI lexicon:
#Pokedex URL contains species URLs ->
#   species URLs contains varieties URLs ->
#       variety URLs contain nat dex URLs (the data we want)

def get_species_urls(POKEDEX):
    resp = httpx.get(POKEDEX)
    result = resp.json()
    species_urls = [entry["pokemon_species"]["url"] for entry in result["pokemon_entries"]][45:47]
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
    for species_url in species_urls:
        task = asyncio.create_task(get_pokemon_datasets(species_url))
        # here's where we can fit a sleep
        #await asyncio.sleep(1)
        result = await task
        if result:
            await parse_varieties_urls(result["varieties"])
        else:
            print(f"1st fail")

async def get_varieties_data(varieties_url):
    pokemon_url = varieties_url["pokemon"]["url"]
    async with httpx.AsyncClient() as client:
        resp = await client.get(pokemon_url)
        return resp.json()

async def parse_varieties_urls(varieties_urls):
    tasks = [asyncio.create_task(get_varieties_data(varieties_url)) for varieties_url in varieties_urls]
    pokemon_entries = {}
    #for coro in asyncio.as_completed(tasks):
    for task in asyncio.as_completed(tasks):
        result = await task

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
        return pokemon_entries
 

POKEDEX = 'https://pokeapi.co/api/v2/pokedex/32'
species_urls = get_species_urls(POKEDEX)
asyncio.run(get_varieties_from_datasets(species_urls))

'''
        id = results["id"]
        name = results["name"]

        variety = {
            "id": id,
            "name": name,
            "types": []
        }

        for type_entry in result["types"]:
            type_slot = type_entry["slot"]
            type_name = type_entry["type"]["name"]
            type_list = {"slot": type_slot, "name": type_name}
            variety["types"].append(type_list)
        print(variety)
'''

