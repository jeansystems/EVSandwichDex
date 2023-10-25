const pokedexPaldea = "https://pokeapi.co/api/v2/pokedex/31";
const pokedexKitakami = "https://pokeapi.co/api/v2/pokedex/32";

export let paldeaUrls = [];
export let kitakamiUrls = [];

export async function retrievePaldeaUrls() {
	await fetch(pokedexPaldea)
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			const entries = data.pokemon_entries;
			entries.forEach((entry) => {
				paldeaUrls.push(entry.pokemon_species.url);
			})
		});
}

export async function retrieveKitakamiUrls() {
	return fetch(pokedexKitakami)
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			const entries = data.pokemon_entries;
			entries.forEach((entry) => {
				kitakamiUrls.push(entry.pokemon_species.url);
			})
			console.log(kitakamiUrls);
		});
}

//retrievePaldeaUrls();
//retrieveKitakamiUrls();