<template>
  <div class="home">
    <div class="landing-page-text">
      <h1><b>TECHUP</b></h1>
      <p>
        End to end guidance for your career in tech. Discover your interests,
        chart your career pathways to land your dream tech job.
      </p>
      <div class="buttons">
        <router-link to="/explore">
          <button class="button1">Get Started</button>
        </router-link>
        <router-link to="/signin">
          <button class="button2" href="/login">Login</button>
        </router-link>
      </div>
    </div>
    <img
      class="landing-page-img"
      alt="Landing Page Logo"
      src="../assets/techfest landing page pic 1.png"
    />
  </div>
</template>

<script>
// @ is an alias to /src
// import JobContainer from "@/components/JobContainer.vue";
// import LogIn from "@/components/LogIn.vue";

export default {
  name: "LandingView",
  // components: { JobContainer, LogIn },
};
</script>

<style scoped>
.nav-item::before {
  content: "";
  position: absolute;
  width: 0%;
  height: 2px;
  bottom: -2px;
  left: 0;
  background-color: #fb770d;
  transition: width 0.3s ease-in-out;
}

.nav-item:hover::before {
  width: 100%;
}

.nav-item:hover {
  color: white;
}

.nav-item {
  text-decoration: none;
  position: relative;
  cursor: pointer;
}

.navbar {
  position: fixed;
  display: flex;
  width: 100%;
  justify-content: space-around;
}

.nav-center {
  display: flex;
  width: 30%;
  justify-content: space-evenly;
}

.nav-right {
  width: 10%;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

button {
  height: 40px;
  width: 150px;
  border-radius: 40px;
}

.button2 {
  border: 1px solid #25424c;
  color: #25424c;
  background-color: transparent;
}

button:hover {
  border: 1px solid #fb770d;
  color: #fb770d;
  background-color: white;
}

.button1 {
  background-color: #25424c;
  border: 1px solid #25424c;
  color: white;
}

.home {
  background-color: #ffa45b;
  height: 100vh;
  position: relative;
}

.landing-page-text {
  padding: 10% 10% 10% 10%;
  text-align: left;
  width: 50%;
  align-items: center;
}

h1 {
  font-size: 6rem;
}

p {
  font-size: 1rem;
}

h1,
p {
  text-align: left;
}

.buttons {
  display: flex;
  gap: 10px;
}

a {
  color: #42b983;
}

.landing-page-img {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 60%;
}
</style>
