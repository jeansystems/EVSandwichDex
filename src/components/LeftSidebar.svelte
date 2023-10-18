<script context="module">
    import { writable } from 'svelte/store';
    import pokemonTypes from '../data/pokemonTypes.json';

    export let pokemonTypeClicked = writable(null);
    export let pokemonColorClicked = writable(null);

    export function handleClick(type, color) {
        console.log('Clicked ' + type + ', has type ' + typeof type);
        pokemonTypeClicked.set(type);
        pokemonColorClicked.set(color);
    }

</script>

<div class="left-sidebar">
    {#each pokemonTypes as pokemonType}
        <button
            class="left-sidebar-buttons"
            style="--button-color: {pokemonType.color}"
            on:click={() => handleClick(pokemonType.type, pokemonType.color)}
        >
            {pokemonType.type}
            {pokemonType.color}
        </button>
    {/each}
</div>

<style>
    .left-sidebar {
        display: flex;
        flex-direction: column;
    }
    .left-sidebar-buttons {
        flex-grow: 1;
        width: 500px;
        display: block;
        box-shadow: none;
        border: 0px;
        background-color: rgba(var(--button-color));
        color: white;
        transition: opacity 0.1s;
    }
    .left-sidebar-buttons:hover {
        opacity: 0.75;
    }
    .left-sidebar-buttons:focus {
        opacity: 0.75;
        color: black;
    }
</style>