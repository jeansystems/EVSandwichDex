const kitakamiPokedex = "https://pokeapi.co/api/v2/pokedex/32"

async function fetchKitakamiSpeciesUrls() {

	let kitakamiSpeciesUrls = [];

	const response = await fetch(kitakamiPokedex);
	const result = await response.json();
	
	result.pokemon_entries.forEach((pokemon_entry) => {
		kitakamiSpeciesUrls.push(pokemon_entry.pokemon_species.url)
	});
	
	return kitakamiSpeciesUrls;
}

let kitakamiSpeciesUrls = await fetchKitakamiSpeciesUrls();


//https://www.samjarman.co.nz/blog/promisedotall
//Further reading on new concept to me, Promises.all()
async function fetchKitakamiPokemonUrls(kitakamiSpeciesUrls) {
    const responses = await Promise.all(kitakamiSpeciesUrls.map (async (species) => {
        const response = await fetch(species);
        const result = await response.json();
        console.log(result.varieties);
    }));
}

let kitakamiPokemon = await fetchKitakamiPokemonUrls(kitakamiSpeciesUrls);

/*
async function fetchKitakamiPokemonStats(kitakamiPokemon) {
    const urls = await Promise.all(kitakamiPokemon.map (async (species) => {
        const url = await
    }))
}

/*
//keeping old function below
async function fetchKitakamiPokemonUrls(kitakamiSpeciesUrls) {
	
	let kitakamiPokemonUrls = [];

	for(let species of kitakamiSpeciesUrls) {
		const response = await fetch(species);
		const result = await response.json()

		kitakamiPokemonUrls.push(result.name);
        console.log(result.name);
	};
}*/