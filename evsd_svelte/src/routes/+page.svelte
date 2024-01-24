<script>
    import TopMenu from '../components/TopMenu.svelte';
    import LeftSidebar from '../components/LeftSidebar.svelte';
    import RightContent from '../components/RightContent.svelte';
</script>

<TopMenu />
<div class="container">
    <LeftSidebar />
    <RightContent />
</div>


<style>
    :global(body) {
        margin: 0px;
        height: 100vh;
    }
    .container {
        display: flex;
        min-height: 95vh;
    }
</style>