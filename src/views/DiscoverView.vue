<template>
  <div class="jobrole">
    <h3 class="mt-5" align="left">Your Recommended Career Tracks:</h3>
    <div>
      <b-card-group deck>
        <CareerTrack track="Software and Applications"></CareerTrack>
        <CareerTrack track="Data and Artificial Intelligence"></CareerTrack>
      </b-card-group>
    </div>
    <h3 class="mt-5" align="left">Your Recommended Job Roles:</h3>
    <div>
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
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import JobRole from "@/components/JobRole.vue";
import CareerTrack from "@/components/CareerTrack.vue";

export default {
  name: "DiscoverView",
  components: {
    JobRole,
    CareerTrack,
  },
  methods: {
    showJobDetail() {
      this.$route.push({ path: "/discover/job/description" });
    },
  },
};
</script>
