<template>
  <div>
    <b-card-group deck>
      <b-card style="max-width: 20%">
        <b-nav vertical align="center">
          <!-- <b-nav-item>'s with child routes. Note the trailing slash on the first <b-nav-item> -->
          <b-nav-item
            to="/discover/job/description"
            @click="JobDescription()"
            exact
            exact-active-class="active"
            >Description</b-nav-item
          >
          <b-nav-item
            to="/discover/job/path"
            @click="JobPath()"
            exact
            exact-active-class="active"
            >Career Paths</b-nav-item
          >
          <b-nav-item
            to="/discover/job/skill"
            @click="JobSkill()"
            exact
            exact-active-class="active"
            >Skills</b-nav-item
          >
          <b-nav-item
            to="/discover/job/listing"
            @click="JobListing()"
            exact
            exact-active-class="active"
            >Listing</b-nav-item
          >
        </b-nav>
      </b-card>

      <b-card>
        <JobDescription v-if="showJobDescription"></JobDescription>
        <JobPath v-if="showJobPath"></JobPath>
        <JobSkill v-if="showJobSkill"></JobSkill>
        <JobListing v-if="showJobListing"></JobListing>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import JobDescription from "../components/JobDescription";
import JobPath from "../components/JobPath";
import JobSkill from "../components/JobSkill";
import JobListing from "../components/JobListing";

export default {
  name: "JobDetailView",
  components: {
    JobDescription,
    JobPath,
    JobSkill,
    JobListing,
  },
  data: () => ({
    showJobDescription: true,
    showJobPath: false,
    showJobSkill: false,
    showJobListing: false,
  }),
  created() {},
  methods: {
    JobDescription() {
      if (this.$route.path == "/discover/job/description") {
        this.showJobDescription = true;
        this.showJobPath = false;
        this.showJobSkill = false;
        this.showJobListing = false;
      }
    },
    JobPath() {
      if (this.$route.path == "/discover/job/path") {
        this.showJobDescription = false;
        this.showJobPath = true;
        this.showJobSkill = false;
        this.showJobListing = false;
      }
    },
    JobSkill() {
      if (this.$route.path == "/discover/job/skill") {
        this.showJobDescription = false;
        this.showJobPath = false;
        this.showJobSkill = true;
        this.showJobListing = false;
      }
    },
    JobListing() {
      if (this.$route.path == "/discover/job/listing") {
        this.showJobDescription = false;
        this.showJobPath = false;
        this.showJobSkill = false;
        this.showJobListing = true;
      }
    },
  },
};
</script>
