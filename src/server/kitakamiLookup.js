//todo: create try/catch blocks for API requests

const kitakamiPokedex = "https://pokeapi.co/api/v2/pokedex/32"

//variable naming is tedious, should consider alternatives
//for now, we pull the URL of each Pokemon "species", covering variants for Pokemon with regional variants or other forms
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

//now that we have each "species", we can retrieve the URL for each Pokemon
//the URLs requested here contain the actual data we're going for: EV yields
async function fetchKitakamiPokemonUrls(kitakamiSpeciesUrls) {
	
	let kitakamiPokemonUrls = [];
	
	const responses = await Promise.all(kitakamiSpeciesUrls.map (async (species) => {
		const response = await fetch(species);
		const result = await response.json();
		return result.varieties.forEach((pokemon_species) =>
			kitakamiPokemonUrls.push(pokemon_species.pokemon.url)
	)}));
	return kitakamiPokemonUrls;
}

let kitakamiPokemon = await fetchKitakamiPokemonUrls(kitakamiSpeciesUrls);
let kitakamiPokemonSlice = kitakamiPokemon.slice(0,3);

async function fetchKitakamiStats(kitakamiPokemonSlice) {

	let kitakamiStats = [];

	const responses = await Promise.all(kitakamiPokemonSlice.map (async (pokemon_data) => {
		const response = await fetch(pokemon_data);
		const result = await response.json();
		
		const name = result.name;
		const stats = result.stats;
		kitakamiStats.push({ name, stats });
	}));
	return kitakamiStats;
}

let finalStats = await fetchKitakamiStats(kitakamiPokemonSlice);
console.log(finalStats, typeof finalStats, finalStats[0].stats);




















/*
async function fetchKitakamiStats(kitakamiPokemonSlice) {

	let kitakamiStats = [];

	const responses = await Promise.all(kitakamiPokemonSlice.map (async (pokemonUrl) => {
		const response = await fetch(pokemonUrl);
		const result = await response.json();
		return result.forEach((pokemonStats) =>
			kitakamiStats.push(pokemonStats.stats)
	)}));
	return kitakamiStats;
}

let finalStats = await fetchKitakamiStats(kitakamiSpeciesUrls);
*/