<script context="module">
    import { writable } from 'svelte/store';
    import pokemonTypes from '../data/pokemonTypes.json';

    export let pokemonTypeClicked = writable(null);

    export function handleClick(type) {
        console.log('Clicked ' + type + ', has type ' + typeof type);
        pokemonTypeClicked.set(type);
    }

</script>

<div class="left-sidebar">
    {#each pokemonTypes as pokemonType}
        <button
            class="left-sidebar-buttons"
            style="--theme-color: {pokemonType.color}"
            on:click={() => handleClick(pokemonType.type)}
        >
            {pokemonType.type}
        </button>
    {/each}
</div>

<style>
    .left-sidebar {
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        height: 100vh;
        width: 800px;
        background-color: powderblue;
        z-index: 0;
    }
    .left-sidebar-buttons {
        flex-grow: 1;
        display: block;
        padding: 0px;
        border: 0px; 
        background-color: var(--theme-color);
        color: white;
        font-weight: bold;
        box-shadow: none;
    }
    .left-sidebar-buttons:hover {
        opacity: 75%;
    }
    .left-sidebar-buttons:focus {
        opacity: 75%;
        color: black;
    }
</style>