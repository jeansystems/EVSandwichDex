import { paldeaPokemon, kitakamiPokemon } from "./pokedexLookup.js";

async function retrievePaldeaPokemonStats() {
    let pokemonNames = [];
    
    for(let pokemon of paldeaPokemon) {
        const response = await fetch(pokemon);
        const result = await response.json();

        pokemonNames.push(result.name);
        console.log('Recorded ' + result.name);
    }
}

retrievePaldeaPokemonStats();