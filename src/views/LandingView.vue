<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <h1>THIS IS THE LANDING PAGE</h1>
    <HelloWorld msg="LANDINGGGG to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "LandingView",
  components: {
    HelloWorld,
  },
};
</script>
