<template>
  <div class="job-container">
    <b-card class="job-nav-container" title="Explore">
      <a href="#" @click="changeInfo('About')" class="card-link">About</a><br />
      <a href="#" @click="changeInfo('Career Pathways')" class="card-link"
        >Career Pathways</a
      ><br />
      <a href="#" @click="changeInfo('Skills')" class="card-link">Skills</a
      ><br />
      <a href="#" @click="changeInfo('Job Listings')" class="card-link"
        >Job Listings</a
      ><br />
    </b-card>

    <b-card class="job-content-container">
      <div v-if="info == 'About'">
        This is some content within the default
        <samp>&lt;b-card-body&gt;</samp> block of the
        <samp>&lt;b-card&gt;</samp> component. Notice the padding between the
        card's border and this gray <samp>&lt;div&gt;</samp>. This is some
        content within the default <samp>&lt;b-card-body&gt;</samp> block of the
        <samp>&lt;b-card&gt;</samp> component. Notice the padding between the
        card's border and this gray <samp>&lt;div&gt;</samp>. This is some
        content within the default <samp>&lt;b-card-body&gt;</samp> block of the
        <samp>&lt;b-card&gt;</samp> component. Notice the padding between the
        card's border and this gray <samp>&lt;div&gt;</samp>. This is some
        content within the default <samp>&lt;b-card-body&gt;</samp> block of the
        <samp>&lt;b-card&gt;</samp> component. Notice the padding between the
        card's border and this gray <samp>&lt;div&gt;</samp>.
      </div>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "JobContainer",
  props: {
    msg: String,
  },
  data() {
    return {
      info: "About",
    };
  },
  methods: {
    changeInfo: function (info) {
      console.log(info);
      this.info = info;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  text-align: left;
}

.job-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin: 10px 10px;
}

.job-nav-container {
  display: flex;
  flex-direction: column;
  width: 20%;
  background-color: #ffebdb;
}
.job-content-container {
  width: 70%;
  background-color: #ffebdb;
}
</style>
