<script>
    import { pokemonTypeClicked } from "./LeftSidebar.svelte";
    import { pokemonColorClicked } from "./LeftSidebar.svelte";
</script>

<p>Okay, selected {$pokemonTypeClicked}</p>

<style>
    p {
        margin: 0px;
        background-color: antiquewhite;
    }
</style>