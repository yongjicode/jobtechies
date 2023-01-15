<template>
  <!-- <div> -->
  <!-- <LogIn />
    <JobContainer /> -->
  <div class="home">
    <div class="navbar">
      <div class="nav-left">logo</div>
      <div class="nav-center">
        <div>Explore</div>
        <div>Discover</div>
        <div>About</div>
      </div>
      <div class="nav-right">
        <div>Sign up</div>
        <div>Login</div>
      </div>
    </div>
    <div class="landing-page-text">
      <h1><b>TECHUP</b></h1>
      <p>
        End to end guidance for your career in tech. Discover your interests,
        chart your career pathways to land your dream tech job.
      </p>
      <div class="buttons">
        <button class="button1">Get Started</button>
        <button class="button2" href="/login">Login</button>
      </div>
    </div>
    <img
      class="landing-page-img"
      alt="Landing Page Logo"
      src="../assets/techfest landing page pic 1.png"
    />
  </div>
  <!-- </div> -->
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
  display: flex;
  justify-content: space-between;
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
