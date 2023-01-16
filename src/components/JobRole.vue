<template>
  <div @click="navigateToDetails" class="jobrole" style="max-width: 33.3%">
    <b-card no-body border-variant="warning" class="job-card" align="left">
      <b-card-body>
        <p class="mb-2">Job Role</p>
        <b-card-title>{{ job }}</b-card-title>
        <p class="mt-3 mb-2">Track</p>
        <b-card-title>{{ track }}</b-card-title>

        <b-card-text>
          {{ description }}
        </b-card-text>
        <p class="mt-3 mb-2">Career Fit</p>
        <b-badge class="ml-1 mr-1 c-success" pill href="#" variant="success"
          >Interest Fit</b-badge
        >
        <b-badge class="ml-1 mr-1 c-warning" pill href="#" variant="warning"
          >Skills Fit</b-badge
        >
        <b-badge class="ml-1 mr-1 c-danger" pill href="#" variant="danger"
          >Job Demand</b-badge
        >
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "JobRole",
  props: {
    job: String,
    track: String,
    description: String,
  },
  methods: {
    navigateToDetails() {
      // Perform any additional logic before navigating
      this.$router.push("/discover/job/");
    },
  },
};
</script>

<style scoped>
.job-card:hover {
  background-color: #ffa45b;
  color: white;
  cursor: pointer;
  transform: translateY(-5px);
}

.job-card {
  transition: transform 0.5s ease;
}

.c-success {
  color: black;
  background-color: #b0f1b6;
  border: 1px solid #68d473;
}

.c-warning {
  color: black;
  background-color: #f4e980;
  border: 1px solid #cebc10;
}

.c-danger {
  color: black;
  background-color: #f8a4a4;
  border: 1px solid #d46868;
}
</style>
