<template>
  <div id="app">
    <nav
      style="width: 100%; display: flex; justify-content: space-between"
      v-if="!$route.meta.hideNavbar"
    >
      <div class="nav-left">
        <img style="height: 30px" src="./assets/brand.png" />
      </div>
      <div class="nav-center">
        <router-link to="/discover">Discover</router-link>
        <router-link to="/explore">Explore</router-link>
        <router-link to="/mentor">Mentor</router-link>
        <router-link to="/resume">Resume</router-link>
      </div>
      <div class="nav-right">
        <router-link to="/">Logout</router-link>
      </div>
    </nav>
    <div>
      <router-view style="max-width: 100%" />
    </div>
  </div>
</template>

<style>
/* @import "~bootstrap/dist/css/bootstrap.css";
@import url("https://jthemes.net/themes/html/wizard-form/documentation/images/favicon.ico");
@import url("https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.9.0/css/bootstrap-datepicker.css");
@import "~bootstrap/dist/css/font-awesome.min.css";
@import "~bootstrap/dist/css/stroke.css";
@import "~bootstrap/dist/css/animate1.css";
@import "~bootstrap/dist/css/fontawesome-all.css";
@import "~bootstrap/dist/css/style8.css";
@import "~bootstrap/dist/css/switch1.css"; */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  padding: 10px;
}

nav a.router-link-exact-active {
  color: #fb770d;
}
</style>
