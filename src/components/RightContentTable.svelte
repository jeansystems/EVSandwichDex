<script>
    import {createTable, Render, Subscribe } from 'svelte-headless-table';
    import { readable } from 'svelte/store'

    import { pokemonTypeClicked } from "./LeftSidebar.svelte";
    import { pokemonColorClicked } from "./LeftSidebar.svelte";

    const data = readable([
        { name: 'spinarak', type1: 'bug', type2: 'poison', paldea: 'N/A', kitakami: 1, blueberry: 'N/A', hp: 0, atk: 2, def: 0, spa: 0, spd: 0, spe: 0 },
        { name: 'ariados', type1: 'bug', type2: 'poison', paldea: 'N/A', kitakami: 2, blueberry: 'N/A', hp: 0, atk: 2, def: 0, spa: 0, spd: 0, spe: 0 },
        { name: 'yanma', type1: 'bug', type2: 'flying', paldea: 'N/A', kitakami: 3, blueberry: 'N/A', hp: 0, atk: 0, def: 0, spa: 0, spd: 0, spe: 1 },
        { name: 'yanmega', type1: 'bug', type2: 'flying', paldea: 'N/A', kitakami: 4, blueberry: 'N/A', hp: 0, atk: 0, def: 0, spa: 0, spd: 0, spe: 1 },

    ]);

    const table = createTable(data);

    const columns = table.createColumns([
        table.column({
            header: 'Name',
            accessor: 'name',
        }),
        table.column({
            header: 'Type 1',
            accessor: 'type1',
        }),
        table.column({
            header: 'Type 2',
            accessor: 'type2',
        }),
        table.column({
            header: 'Paldea',
            accessor: 'paldea',
        }),
        table.column({
            header: 'Kitakami',
            accessor: 'kitakami',
        }),
        table.column({
            header: 'Blueberry',
            accessor: 'blueberry',
        }),
        table.column({
            header: 'HP',
            accessor: 'hp',
        }),
        table.column({
            header: 'Atk',
            accessor: 'atk',
        }),
        table.column({
            header: 'Def',
            accessor: 'def',
        }),
        table.column({
            header: 'SpA',
            accessor: 'spa',
        }),
        table.column({
            header: 'SpD',
            accessor: 'spd',
        }),
        table.column({
            header: 'Spe',
            accessor: 'spe',
        }),
    ]);

    const {
        headerRows,
        rows,
        tableAttrs,
        tableBodyAttrs,
    } = table.createViewModel(columns);
</script>

<div class="right-content-table-box">
    <!--
        <p>Okay, selected {$pokemonTypeClicked}</p>
    -->
    <table class="right-content-table" {...$tableAttrs}>
        <thead>
          {#each $headerRows as headerRow (headerRow.id)}
            <Subscribe rowAttrs={headerRow.attrs()} let:rowAttrs>
              <tr {...rowAttrs}>
                {#each headerRow.cells as cell (cell.id)}
                  <Subscribe attrs={cell.attrs()} let:attrs>
                    <th {...attrs}>
                      <Render of={cell.render()} />
                    </th>
                  </Subscribe>
                {/each}
              </tr>
            </Subscribe>
          {/each}
        </thead>
        <tbody {...$tableBodyAttrs}>
          {#each $rows as row (row.id)}
            <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
              <tr {...rowAttrs}>
                {#each row.cells as cell (cell.id)}
                  <Subscribe attrs={cell.attrs()} let:attrs>
                    <td {...attrs}>
                      <Render of={cell.render()} />
                    </td>
                  </Subscribe>
                {/each}
              </tr>
            </Subscribe>
          {/each}
        </tbody>
      </table>
</div>

<style>
    .right-content-table-box {
        height: 100%;
        width: 100%;
        /*border: solid antiquewhite 5px; /* demonstrates working border */
        box-sizing: border-box;
    }
    .right-content-table {
        width: 100%;
        border: 1px solid;
        border-collapse: collapse;
    }
    .right-content-table th, td {
        border: 1px solid black;
    }
    .right-content-table th {
        background: rgba(0, 0, 0, 0.5);
        color: lightgray;
    }
    .right-content-table td {
        background: rgba(256, 256, 256, 0.75)
    }
    p {
        margin: 0px;
    }
</style>