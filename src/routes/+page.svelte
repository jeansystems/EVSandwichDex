<script>

    import { onMount } from 'svelte';

    import Left from '../components/LeftSidebar.svelte';
    import Right from '../components/RightContent.svelte';

    import sandwich from "../public/sandwich.png";

    export let topHeight;

    export function getTopHeight(){
        const top = document.getElementById('top');
        topHeight = top.offsetHeight;
        console.log('top bar height is ' + topHeight);
    }
    onMount(() => {
        getTopHeight();
    })

</script>

<div class="app" style="--topHeight: {topHeight}px;">
    <div id="top" class="top">
        <div class="top-logo">
            <img src={sandwich} alt="sandwich" />
        </div>
        <div class="top-banner">
            <h2>EVSD</h2>
        </div>
    </div>
    <div class="content" >
        <div class="left-content">
            <Left />
        </div>
        <div class="right-content">
            <div class="right-container">
                <Right />
            </div>>
            <div class="right-footer"></div>
        </div>
    </div>
</div>

<style>
    :global(body) {
        margin: 0px;
        height: 100vh;
        display: flex;
        flex-direction: column;
        background-color: #000000;
    }
    .top {
        background-color: gold;
        position: fixed;
        top: 0;
        width: 100vw;
        height: var(--topHeight);
        display: flex;
    }
    .top-logo {
        display: flex;
        align-items: center;
    }
    .top-logo img {
        max-width: 50%;
        height: auto;
    }
    .top-banner {
        margin: auto;
        padding: 0;
    }
    .content {
        display: flex;
        flex-direction: row;
        margin-top: var(--topHeight);
    }
    .left-content {
        position: fixed;
        width: 17.5em;
        height: calc(100vh - var(--topHeight));
    }
    .right-content {
        margin-left: 17.5em;
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    .right-container {
        min-height: calc(100vh - var(--topHeight));
        background-color: #222526;
        margin: 16px;
    }
    .right-footer {
        height: 64px;
        background-color: #222526;
        margin-left: 16px;
        margin-right: 16px;
    }
</style>