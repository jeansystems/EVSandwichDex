<script context="module">
    import { writable } from 'svelte/store';
    import pokemonTypes from '../data/pokemonTypes.json';

    export let pokemonTypeClicked = writable(null);
    export let pokemonColorClicked = writable(null);

    export function handleClick(type, color) {
        console.log('Clicked ' + type + ', has type ' + typeof type);
        console.log('RGBA color selected (' + color + ') has type ' + typeof color);
        pokemonTypeClicked.set(type);
        pokemonColorClicked.set(color);
    }

</script>
<div class="left-container">
    <div class="left-sidebar">
        {#each pokemonTypes as pokemonType}
            <button
                class="left-sidebar-buttons"
                style="--button-color: {pokemonType.color}"
                on:click={() => handleClick(pokemonType.type, pokemonType.color)}
            >
                {pokemonType.type}
            </button>
        {/each}
    </div>
    <div class="left-divider">
        &nbsp;
    </div>
</div>
<style>
    .left-container {
        display: flex;
        flex-direction: row;
    }
    .left-sidebar {
        display: flex;
        flex-direction: column;
        overflow-y: hidden;
    }
    .left-sidebar-buttons {
        flex-grow: 1;
        width: 500px;
        display: block;
        box-shadow: none;
        border: 0px;
        background-color: rgba(var(--button-color));
        color: white;
        font-weight: bolder;
        font-size: large;
        transition: opacity 0.1s;
    }
    .left-sidebar-buttons:hover {
        opacity: 0.75;
    }
    .left-sidebar-buttons:focus {
        color: black;
    }
    .left-divider {
        background-color: rgb(204, 186, 17);
        width: .25vw;
    }
</style>