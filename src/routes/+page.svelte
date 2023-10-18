<script>
    import LeftSidebar from '../components/LeftSidebar.svelte';
    import RightContent from '../components/RightContent.svelte';
    import TopMenu from '../components/TopMenu.svelte';
</script>

<div class="full-container">
    <div class="top-menu">
        <TopMenu />
    </div>
    <div class="vertical-container">
        <LeftSidebar />
        <RightContent />
    </div>
</div>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
    }
    .vertical-container {
        display: flex;
        min-height: 100vh;
    }
</style>