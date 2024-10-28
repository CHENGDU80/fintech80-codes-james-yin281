<script setup>
import { RouterView } from 'vue-router';
import TopBar from './components/TopBar.vue';
import NavBar from './components/NavBar.vue';
</script>

<template>
  <TopBar></TopBar>
  <NavBar></NavBar>
  <div class="outbox">
    <RouterView />
  </div>
</template>
<script>
export default {

}
</script>