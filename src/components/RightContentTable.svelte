<script>
    import { pokemonTypeClicked } from "./LeftSidebar.svelte";
    import { pokemonColorClicked } from "./LeftSidebar.svelte";
</script>

<div class="right-content-table">
    <p>Okay, selected {$pokemonTypeClicked}</p>
</div>

<style>
    .right-content-table {
        height: 100%;
        width: 100%;
        border: solid antiquewhite 5px;
        box-sizing: border-box;
    }
    p {
        margin: 0px;
    }
</style>