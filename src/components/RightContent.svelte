<script>
    import { pokemonTypeClicked } from "./LeftSidebar.svelte";
</script>


<div class="right-content">
    {#if $pokemonTypeClicked === null}
        <p>Select a Pokemon type from the buttons on the left</p>
    {:else}
        <p>Okay, selected {$pokemonTypeClicked}</p>
    {/if}
</div>

<style>
    .right-content {
        flex-grow: 1;
        color: darkblue;
        z-index: 0;
    }
</style>
