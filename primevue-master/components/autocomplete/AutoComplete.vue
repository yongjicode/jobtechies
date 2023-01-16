<template>
    <div class="jobrole" style="max-width: 33.3%">
      <b-card no-body border-variant="light" align="left">
        <img class="w-100" src="@/assets/ai.png" />
        <b-card-body>
          <b-card-sub-title class="mb-2">Job Role</b-card-sub-title>
          <b-card-title>{{ job }}</b-card-title>
          <b-card-sub-title class="mt-3 mb-2">Track</b-card-sub-title>
          <b-card-title>{{ track }}</b-card-title>
  
          <b-card-text>
            {{ description }}
          </b-card-text>
          <b-card-sub-title class="mt-3 mb-2">Career Fit</b-card-sub-title>
          <b-badge class="ml-1 mr-1" pill href="#" variant="success"
            >Interest Fit</b-badge
          >
          <b-badge class="ml-1 mr-1" pill href="#" variant="warning"
            >Skills Fit</b-badge
          >
          <b-badge class="ml-1 mr-1" pill href="#" variant="danger"
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
  };
  </script>
  