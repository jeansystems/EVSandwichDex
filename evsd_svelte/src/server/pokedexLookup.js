//functions that take paldeaPokedex (list of Pokemon in order of regional dex)
//creates and returns array of <region>Url to function
//declares and calls <region>Pokemon variable for us to pass later
//URLs retrieved from this can call to PokeAPI's detailed entries at https://pokeapi.co/api/v2/pokemon/
//fetch paldea  URLs -> pokemon-species URLs -> pokemon URLs
//fetch kitakami URLs -> pokemon_species URLs -> pokemon URLs

const paldeaPokedex = "https://pokeapi.co/api/v2/pokedex/31";
const KitakamiPokedex = "https://pokeapi.co/api/v2/pokedex/32"

async function fetchPaldeaSpeciesUrls() {

	let paldeaSpeciesUrls = [];

	const response = await fetch(paldeaPokedex);
	const result = await response.json();
	
	result.pokemon_entries.forEach((pokemon_entry) => {
		paldeaSpeciesUrls.push(pokemon_entry.pokemon_species.url)
	});
	
	return paldeaSpeciesUrls;

}

async function fetchKitakamiSpeciesUrls() {

	let kitakamiSpeciesUrls = [];

	const response = await fetch(KitakamiPokedex);
	const result = await response.json();
	
	result.pokemon_entries.forEach((pokemon_entry) => {
		KitakamiSpeciesUrls.push(pokemon_entry.pokemon_species.url)
	});
	
	return kitakamiSpeciesUrls;

}

let paldeapeciesUrls  = await fetchPaldeaSpeciesUrls();
let kitakamiSpeciesUrls = await fetchKitakamiSpeciesUrls();

async function fetchPaldeaPokemonUrls(paldeaSpeciesUrls) {
	
	let paldeaPokemonUrls = [];

	for(let species of paldeaSpeciesUrls) {
		const response = await fetch(species);
		const result = await response.json();

		paldeaPokemonUrls.push(result.name);
	};
}

async function fetchkitakamiPokemonUrls(kitakamiSpeciesUrls) {
	
	let kitakamiPokemonUrls = [];

	for(let species of kitakamiSpeciesUrls) {
		const response = await fetch(kitakamiSpeciesUrls);
		const result = await response.json()

		kitakamiPokemonUrls.push(result.name);
	}
}