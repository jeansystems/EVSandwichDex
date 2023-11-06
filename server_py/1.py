import asyncio
from datetime import timedelta
import time
import httpx
from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    types: list[str]

def parse_pokemon(pokemon_data: dict) -> Pokemon:
    print(f"parsing...")

    poke_types = []
    for poke_type in pokemon_data["types"]:
        poke_types.append(poke_type["type"]["name"])

    return Pokemon(name=pokemon_data['name'], types=poke_types)

async def get_pokemon(name: str) -> dict | None: 
    async with httpx.AsyncClient() as client:
        print(f"querying '{name}'")
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        print(f"response recieved for '{name}'")

        try:
            response.raise_for_status()

        except httpx.HTTPStatusError as err:
            if err.response.status_code == 404:
                return None
            raise

        else:
            return response.json()
        
async def get_all(*names: str):
    started_at = time.time()

    for name in names:
        data = await get_pokemon(name)
        if data:
            pokemon = parse_pokemon(data)
            print(f"{pokemon.name} is of type(s) {','.join(pokemon.types)}")
        else:
            print(f"No data found for {name}")

    finished_at = time.time()
    elapsed_time = finished_at - started_at
    print(f"Done in timedelta(seconds = {elapsed_time}s)")

POKE_NAMES = ["blaziken", "pikachu", "lugia", "bad_name"]
asyncio.run(get_all(*POKE_NAMES))