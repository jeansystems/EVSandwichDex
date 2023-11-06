import httpx
import asyncio

def get_species_urls(POKEDEX):
    resp = httpx.get(POKEDEX)
    result = resp.json()
    #extract key "pokemon_species"
    #remove splice to pull all pokedex entries
    species_urls = [entry["pokemon_species"]["url"] for entry in result["pokemon_entries"]]
    return species_urls

async def get_pokemon_urls(species_url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(species_url)
        return resp.json()

async def finish(species_urls):
    tasks = [asyncio.create_task(get_pokemon_urls(species_url)) for species_url in species_urls]

    results = await asyncio.gather(*tasks)

    for result in results:
        for index in result["varieties"]:
            url = index["pokemon"]["url"]
        #varieties = [index["pokemon"]["url"] for index in result["varieties"]]
        print(url, type(url))

POKEDEX = 'https://pokeapi.co/api/v2/pokedex/32'
species_urls = get_species_urls(POKEDEX)
asyncio.run(finish(species_urls))