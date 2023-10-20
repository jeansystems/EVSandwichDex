<script>
    import { pokemonTypeClicked } from "./LeftSidebar.svelte";
    import { pokemonColorClicked } from "./LeftSidebar.svelte";
</script>

<div 
    class="right-content"
    style="--bg-color: {$pokemonColorClicked}"
>
    {#if $pokemonTypeClicked === null}
        <p>Select a Pokemon type from the buttons on the left</p>
    {:else}
        <p>Okay, selected {$pokemonTypeClicked}</p>
    {/if}
</div>

<style>
    .right-content {
        transition: background-color 0.2s ease;
        background-color: rgba(var(--bg-color));
        overflow-y: auto;
        flex-grow: 1;
    }
</style>
