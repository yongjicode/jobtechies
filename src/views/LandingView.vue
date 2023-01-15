<template>
  <!-- <div> -->
  <!-- <LogIn />
    <JobContainer /> -->
  <div class="home">
    <div class="landing-page-text">
      <h1><b>TECHUP</b></h1>
      <p>
        End to end guidance for your career in tech. Discover your interests,
        chart your career pathways to land your dream tech job.
      </p>
      <div class="buttons">
        <b-button class="button" pill>Get Started</b-button>
        <b-button class="button" pill href="/login">Login</b-button>
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
.home {
  background-color: #ffa45b;
}

.landing-page-text {
  padding: 10% 10% 10% 10%;
  text-align: left;
  width: 50%;
  align-items: center;
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
  /* position: absolute; */
  float: right;
}
</style>
