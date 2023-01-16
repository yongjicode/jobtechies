<template>
  <div class="wrapper">
    <div class="jobrole">
      <h3 class="mt-5" align="left">Your Recommended Career Tracks:</h3>
      <div class="card-container">
        <div class="card">
          <div class="card-image"></div>
          <div class="card-title">Data and AI</div>
        </div>
        <div class="card">
          <div class="card-image"></div>
          <div class="card-title">Infrastructure</div>
        </div>
        <div class="card">
          <div class="card-image"></div>
          <div class="card-title">Cybersecurity</div>
        </div>
        <div class="card">
          <div class="card-image"></div>
          <div class="card-title">Data and AI</div>
        </div>
      </div>
      <h3 class="mt-5" align="left">Your Recommended Job Roles:</h3>
      <!-- <div>
        <router-link to="/discover/job/description">JOB ROLE</router-link>
        <b-card-group deck>
          <JobRole
            job="Software Engineer"
            track="Software and Applications"
            description="A software engineer sits and code"
          />
          <JobRole
            job="Data Analyst"
            track="Data and Artificial Analyst"
            description="A data analyst uses excel sheets"
          />
          <JobRole
            job="Cyber Engineer"
            track="Cyber Security"
            description="A cyber engineer sits and protects computers"
          />
        </b-card-group>
      </div> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import JobRole from "@/components/JobRole.vue";

export default {
  name: "DiscoverView",
  components: {
    // JobRole,
  },
  methods: {
    showJobDetail() {
      this.$route.push({ path: "/discover/job/description" });
    },
  },
};
</script>

<style>
.wrapper {
  padding-left: 30px;
  padding-right: 30px;
  overflow-x: hidden;
}

.card-container::-webkit-scrollbar {
  width: 2px;
  background-color: transparent;
}
.card-container::-webkit-scrollbar-thumb {
  width: 2px;
  background-color: #ffa45b;
}

.card-container {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.card-container {
  width: 100%;
  overflow-x: scroll;
  padding: 10px;
  display: flex;
}

.card {
  min-width: 496px;
  width: 496px;
  height: 209px;
  margin-right: 16px; /* space between cards */
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
  position: relative;
}

.card-image {
  width: 100%;
  height: 100%;
  background-image: url("../assets/ai.png");
  background-position: center;
  background-size: cover;
}

.card-title {
  position: absolute;
  top: 30%;
  color: white;
  font-size: 2rem;
  text-align: center;
}
</style>
