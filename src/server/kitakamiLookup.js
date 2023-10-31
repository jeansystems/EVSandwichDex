//todo: create try/catch blocks for API requests

import { writeFile } from 'node:fs';

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
//the URLs requested here contain the actual data we're going for: EV yields but we need to get those URLs first
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
//for now we're only passing through the first few items of the array for easier output handling
let kitakamiPokemonSlice = kitakamiPokemon.slice(0,3);

//we've retrieved the URL for each Pokemon (including their variants)
//now to seek out their stats
async function fetchKitakamiPokemonData(kitakamiPokemonSlice) {

	let kitakamiPokemonData = [];

	const responses = await Promise.all(kitakamiPokemonSlice.map (async (pokemon_data) => {
		const response = await fetch(pokemon_data);
		const result = await response.json();
		
		//const name = result.name;
		//const stats = result.stats;
		//kitakamiStats.push({ name, stats });
		kitakamiPokemonData.push(result);
	}));
	return kitakamiPokemonData;
}

let kitakamiPokemonDatasets = await fetchKitakamiPokemonData(kitakamiPokemonSlice)

async function writeKitakamiData(kitakamiPokemonDatasets) {

	for (let dataset of kitakamiPokemonDatasets) {
		//not sure about using relative paths but sticking with it for now
		const fileName = '../data/pokemonStats/' + dataset.name + '.json';
		const fileContents = JSON.stringify(dataset, null, 2);
		writeFile(fileName, fileContents, (err) => {
			if (err) throw err;
			console.log('File saved?');
		});
	}
}

async function main() {
	await writeKitakamiData(kitakamiPokemonDatasets);
}

main();

/*
//const kitakamiStatsArrays = await fetchKitakamiData(kitakamiPokemonSlice);
//const finalStatsJson = JSON.stringify(finalStats);
//proof of concept, we should see the name and stats of the first Pokemon returned!
//console.log(finalStats[0].name, finalStats[0].stats);
//finalStats.forEach((statsArray) => {
//	console.log(statsArray.name);
//})
//we need to pass each item of the finalStats array 
*/