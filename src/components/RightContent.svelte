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
        background-color: rgba(var(--bg-color), 0.4);
        overflow-y: auto;
        flex-grow: 1;
    }
</style>
