import httpx
import asyncio

#Breakdown of data transform according to PokeAPI lexicon:
#Pokedex URL contains species URLs ->
#   species URLs contains varieties URLs ->
#       variety URLs contain nat dex URLs (the data we want)

def get_species_urls(POKEDEX):
    resp = httpx.get(POKEDEX)
    result = resp.json()
    species_urls = [entry["pokemon_species"]["url"] for entry in result["pokemon_entries"]]
    return species_urls

async def get_pokemon_datasets(species_url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(species_url)
        return resp.json()

async def get_varieties_from_datasets(species_urls):
    #tasks = [asyncio.create_task(get_pokemon_datasets(species_url)) for species_url in species_urls]
    tasks = [asyncio.create_task(get_pokemon_datasets(species_url)) for species_url in species_urls[0:3]]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        if result:
            await parse_varieties_urls(result["varieties"])
        else:
            print(f"1st fail")

async def get_varieties_stats(variety_url):
    pokemon_url = variety_url["pokemon"]["url"]
    async with httpx.AsyncClient() as client:
        resp = await client.get(pokemon_url)
        return resp.json()


async def parse_varieties_urls(varieties_urls):
    tasks = [asyncio.create_task(get_varieties_stats(variety_url)) for variety_url in varieties_urls]
    results = await asyncio.gather(*tasks)
    #finally we can build objects with the correct data from proper pokemon entries
    for result in results:
        print(result["stats"])

POKEDEX = 'https://pokeapi.co/api/v2/pokedex/32'
species_urls = get_species_urls(POKEDEX)
asyncio.run(get_varieties_from_datasets(species_urls))

