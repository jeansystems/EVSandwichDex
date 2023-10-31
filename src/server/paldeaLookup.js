//todo: create try/catch blocks for API requests

import { writeFile } from 'node:fs';

const paldeaPokedex = "https://pokeapi.co/api/v2/pokedex/31"

//variable naming is tedious, should consider alternatives
//for now, we pull the URL of each Pokemon "species", covering variants for Pokemon with regional variants or other forms
async function fetchKitakamiSpeciesUrls() {

	let paldeaSpeciesUrls = [];

	const response = await fetch(paldeaPokedex);
	const result = await response.json();
	
	result.pokemon_entries.forEach((pokemon_entry) => {
		paldeaSpeciesUrls.push(pokemon_entry.pokemon_species.url)
	});
	
	return paldeaSpeciesUrls;
}

//now that we have each "species", we can retrieve the URL for each Pokemon
//the URLs requested here contain the actual data we're going for: EV yields but we need to get those URLs first
async function fetchKitakamiPokemonUrls(paldeaSpeciesUrls) {
	
	let paldeaPokemonUrls = [];
	
	const responses = await Promise.all(paldeaSpeciesUrls.map (async (species) => {
		const response = await fetch(species);
		const result = await response.json();
		return result.varieties.forEach((pokemon_species) =>
			paldeaPokemonUrls.push(pokemon_species.pokemon.url)
	)}));
	return paldeaPokemonUrls;
}

//we've retrieved the URL for each Pokemon (including their variants)
//now to seek out their stats
async function fetchKitakamiPokemonData(paldeaPokemonSlice) {

	let paldeaPokemonData = [];

	const responses = await Promise.all(paldeaPokemonSlice.map (async (pokemon_data) => {
		const response = await fetch(pokemon_data);
		const result = await response.json();
		
		//const name = result.name;
		//const stats = result.stats;
		//paldeaStats.push({ name, stats });
		paldeaPokemonData.push(result);
	}));
	return paldeaPokemonData;
}

async function writeKitakamiData(paldeaPokemonDatasets) {

	for (let dataset of paldeaPokemonDatasets) {
		//not sure about using relative paths but sticking with it for now
		const fileName = '../data/pokemonStats/paldea/' + dataset.name + '.json';
		const fileContents = JSON.stringify(dataset, null, 2);
		writeFile(fileName, fileContents, (err) => {
			if (err) throw err;
			console.log('File saved?');
		});
	}
}

async function main() {
	await writeKitakamiData(paldeaPokemonDatasets);
}

let paldeaSpeciesUrls = await fetchKitakamiSpeciesUrls();
let paldeaPokemon = await fetchKitakamiPokemonUrls(paldeaSpeciesUrls);
//for now we're only passing through the first few items of the array for easier output handling
let paldeaPokemonSlice = paldeaPokemon.slice(0,10);
let paldeaPokemonDatasets = await fetchKitakamiPokemonData(paldeaPokemonSlice)
main();