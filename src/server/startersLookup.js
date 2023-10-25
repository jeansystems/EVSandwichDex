//outline to parse through each url provided by functions in pokedexLookup
//this will carry out a lot of API calls so I'm building it with a small amount of URLs in the array first
//also should look into caching 

import { paldeaUrls, kitakamiUrls } from "./pokedexLookup.js";
import { retrievePaldeaUrls, retrieveKitakamiUrls } from "./pokedexLookup.js";

async function retrievePaldeaStats() {
	//const pokedexUrls = ["https://pokeapi.co/api/v2/pokemon/906", "https://pokeapi.co/api/v2/pokemon/909", "https://pokeapi.co/api/v2/pokemon/912"];
    await retrievePaldeaUrls();
    let pokedexUrls = paldeaUrls.slice(0,3);

    pokedexUrls.forEach((url) => {
        fetch(url)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let pokemonName = data.name;
            console.log(pokemonName);
        })
    });
};

retrievePaldeaStats();