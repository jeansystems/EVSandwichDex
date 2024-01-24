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
    <div class="right-content-container">
        {#if $pokemonTypeClicked === "Grass"}
        <div class="right-content-table">
            <table>
                <thead>
                    <tr>
                        <th scope="col">Pokemon</th>
                        <th scope="col">HP</th>
                        <th scope="col">Attack</th>
                        <th scope="col">Defense</th>
                        <th scope="col">Sp. Attack</th>
                        <th scope="col">Sp. Defense</th>
                        <th scope="col">Speed</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Sprigatito</th>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>0</td>
                        <td>1</td>
                    </tr>
                </tbody>
            </table>
        </div>
        {/if}
    </div>
</div>

<style>
    .right-content {
        transition: background-color 0.2s ease;
        background-color: rgba(var(--bg-color));
        overflow-y: auto;
        flex-grow: 1;
        padding: 0 20px;
    }
    .right-content-container {
        padding: 20px;
    }
</style>
