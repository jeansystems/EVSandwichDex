import asyncio
import httpx 

kitakami_dex = 'https://pokeapi.co/api/v2/pokedex/32'

async def get_kitakami_species(kitakami_dex):
    async with httpx.AsyncClient() as client:
        response = await client.get(kitakami_dex)
        result = response.json()
        kitakami_species_urls =  [pokemon_entry["pokemon_species"]["url"] for pokemon_entry in result["pokemon_entries"]]
        return kitakami_species_urls

async def get_kitakami_pokemon(kitakami_species_urls):
    async with httpx.AsyncClient() as client:
        response = await client.gather(kitakami_species_urls)
        result = response.json
        print(result["varieties"])



#define main
async def main():
    kitakami_species_urls = await get_kitakami_species(kitakami_dex)
    await get_kitakami_pokemon(kitakami_species_urls)

if __name__ == '__main__':
    asyncio.run(main())