const paldeaPokedex = "https://pokeapi.co/api/v2/pokedex/31";

async function fetchPaldeaSpeciesUrls() {

	let paldeaSpeciesUrls = [];

	const response = await fetch(paldeaPokedex);
	const result = await response.json();
	
	result.pokemon_entries.forEach((pokemon_entry) => {
		paldeaSpeciesUrls.push(pokemon_entry.pokemon_species.url)
	});
	
	return paldeaSpeciesUrls;

}

let paldeapeciesUrls  = await fetchPaldeaSpeciesUrls();

async function fetchPaldeaPokemonUrls(paldeaSpeciesUrls) {
	
	let paldeaPokemonUrls = [];

	for(let species of paldeaSpeciesUrls) {
		const response = await fetch(species);
		const result = await response.json();

		paldeaPokemonUrls.push(result.name);
	};
}