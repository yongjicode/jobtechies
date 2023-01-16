<template>
  <div class="container-fluid">
    <div class="row flex-xl-nowrap2">
      <div class="bd-sidebar border-bottom-0 col-md-3 col-xl-2 col-12">
        <nav
          id="bd-docs-nav"
          aria-label="Main navigation"
          class="c-left bd-links d-none d-md-block"
        >
          <div class="bd-toc-item active">
            <ul class="nav bd-sidenav">
              <li class="b-nav-item">
                <div
                  :class="{
                    'c-item': !showJobDescription,
                    'c-item-active': showJobDescription,
                  }"
                  to="/discover/job/description"
                  @click="JobDescription()"
                  exact
                  exact-active-class="active"
                >
                  Description
                </div>
                <div
                  :class="{
                    'c-item': !showJobPath,
                    'c-item-active': showJobPath,
                  }"
                  to="/discover/job/path"
                  @click="JobPath()"
                  exact
                  exact-active-class="active"
                >
                  Career Paths
                </div>
                <div
                  :class="{
                    'c-item': !showJobSkill,
                    'c-item-active': showJobSkill,
                  }"
                  to="/discover/job/skill"
                  @click="JobSkill()"
                  exact
                  exact-active-class="active"
                >
                  Skills Required
                </div>
                <div
                  :class="{
                    'c-item': !showJobListing,
                    'c-item-active': showJobListing,
                  }"
                  to="/discover/job/listing"
                  @click="JobListing()"
                  exact
                  exact-active-class="active"
                >
                  Job Listing
                </div>
              </li>
            </ul>
          </div>
        </nav>
      </div>

      <div class="bd-content col-md-9 col-xl-8 col-12 pb-md-3 pl-md-5">
        <div class="clearfix d-block"></div>
        <main class="bd-main bd-components">
          <b-card-group deck>
            <b-card>
              <JobDescription
                v-if="showJobDescription"
                type="Software Engineer"
                align="left"
              ></JobDescription>
              <JobPath v-if="showJobPath" type="Software Engineer"></JobPath>
              <JobSkill v-if="showJobSkill" type="Software Engineer"></JobSkill>
              <JobListing
                v-if="showJobListing"
                type="Software Engineer"
              ></JobListing>
            </b-card>
          </b-card-group>
        </main>
      </div>
    </div>
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
      this.showJobDescription = true;
      this.showJobPath = false;
      this.showJobSkill = false;
      this.showJobListing = false;
    },
    JobPath() {
      this.showJobDescription = false;
      this.showJobPath = true;
      this.showJobSkill = false;
      this.showJobListing = false;
    },
    JobSkill() {
      this.showJobDescription = false;
      this.showJobPath = false;
      this.showJobSkill = true;
      this.showJobListing = false;
    },
    JobListing() {
      this.showJobDescription = false;
      this.showJobPath = false;
      this.showJobSkill = false;
      this.showJobListing = true;
    },
  },
};
</script>

<style scoped>
.c-left {
  background-color: aliceblue;
  border-radius: 20px;
  width: max-content;
}

.c-item {
  border-radius: 40px;
  height: 30px;
  width: 200px;
  padding-left: 15px;
  padding-top: 5px;
  text-align: left;
  cursor: pointer;
}

.c-item-active {
  border-radius: 40px;
  height: 30px;
  width: 200px;
  padding-left: 15px;
  padding-top: 5px;
  text-align: left;
  cursor: pointer;
  background-color: #fb770d;
  color: white;
}
</style>
