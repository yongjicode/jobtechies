<template>
  <div>
    <div class="top-banner">
      <div class="inner-container">
        <h3 class="mt-5" align="left">Your Recommended Career Tracks:</h3>
        <div class="c-card-container">
          <div class="c-card">
            <img src="../assets/ai.png" class="card-image" />
            <div class="c-card-title">DATA AND AI</div>
          </div>
          <div class="c-card">
            <img src="../assets/infrastructure.png" class="card-image" />
            <div class="c-card-title">INFRASTRUCTURE</div>
          </div>
          <!-- <div class="card">
            <img src="../assets/cybersecurity.png" class="card-image" />
            <div class="card-title">Cybersecurity</div>
          </div>
          <div class="card">
            <img src="../assets/software.png" class="card-image" />
            <div class="card-title">Software and Applications</div>
          </div>
          <div class="card">
            <img src="../assets/sales.png" class="card-image" />
            <div class="card-title">Sales and Marketing</div>
          </div>
          <div class="card">
            <img src="../assets/support.png" class="card-image" />
            <div class="card-title">Operations and Support</div>
          </div>
          <div class="card">
            <img src="../assets/strategy.png" class="card-image" />
            <div class="card-title">Strategy and Governance</div>
          </div> -->
        </div>
      </div>
    </div>
    <div class="job-role-section">
      <h3 class="mt-5" align="left">Your Recommended Job Roles:</h3>
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
</template>

<script>
// @ is an alias to /src
import JobRole from "@/components/JobRole.vue";

export default {
  name: "DiscoverView",
  components: {
    JobRole,
  },
  methods: {
    showJobDetail() {
      this.$route.push({ path: "/discover/job/description" });
    },
  },
};
</script>

<style>
.job-role-section {
  margin-top: 50px;
  padding: 30px;
}

.top-banner {
  height: 305px;
  width: 100%;
  background-color: #ffa45b;
  position: relative;
}

.inner-container {
  padding-left: 30px;
  width: 100%;
  position: absolute;
  top: 50px;
  overflow-x: hidden;
}

.c-card-container::-webkit-scrollbar {
  width: 2px;
  background-color: transparent;
}

.c-card-container::-webkit-scrollbar-thumb {
  width: 2px;
  background-color: #ffa45b;
}

.c-card-container {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.c-card-container {
  width: 100%;
  overflow-x: scroll;
  padding: 10px;
  display: flex;
}

.c-card {
  min-width: 496px;
  border-radius: 20px;
  width: 496px;
  height: 209px;
  margin-right: 16px; /* space between cards */
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  transition: transform 0.5s ease;
}

.c-card:hover {
  cursor: pointer;
  transform: translateY(-5px);
  box-shadow: 0 0 20px orange;
}

.card-image {
  width: 100%;
  height: 100%;
  background-position: center;
  background-size: cover;
  border-radius: 20px;
}

.c-card-title {
  font-weight: 800;
  position: absolute;
  top: 40%;
  text-shadow: 4px 4px 8px #333;
  color: white;
  font-size: 2rem;
  text-align: center;
}
</style>
