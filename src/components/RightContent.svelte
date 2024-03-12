<script>
    import { pokemonTypeClicked } from "./LeftSidebar.svelte";
    import { pokemonColorClicked } from "./LeftSidebar.svelte";

    import RightTable from '../components/RightContentTable.svelte'
</script>

<div class="right-content" style="--bg-color: {$pokemonColorClicked}">
    {#if $pokemonTypeClicked === null}
        <p>Select a Pokemon type from the buttons on the left</p>
    {:else}
        <div class="right-content-table">
            <RightTable />
        </div>
    {/if}
</div>


<style>
    .right-content {
        height: 100%;
        transition: background-color 0.2s ease;
        background-color: rgba(var(--bg-color));
        display: flex;
    }
    .right-content p {
        margin-top: 0px;
        margin-bottom: 0px;
    }
</style>
