//outline to parse through each url provided by functions in pokedexLookup
//this will carry out a lot of API calls so I'm building it with a small amount of URLs in the array first
//also should look into caching 

function retrievePaldeaStats() {
	const pokedexUrls = ["https://pokeapi.co/api/v2/pokemon/906", "https://pokeapi.co/api/v2/pokemon/909", "https://pokeapi.co/api/v2/pokemon/912"];

    pokedexUrls.forEach((url) => {
        fetch(url)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            pokemonName = data.name;
            console.log(pokemonName);
        })
    });
};

retrievePaldeaStats();