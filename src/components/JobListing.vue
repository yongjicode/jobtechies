<template>
  <div class="explore" align="center">
    <b-card
      no-body
      style="max-width: 80%"
      img-src="https://placekitten.com/380/200"
      img-alt="Image"
      img-top
    >
      <b-list-group flush>
        <b-list-group-item>Cras justo odio</b-list-group-item>
        <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
        <b-list-group-item>Vestibulum at eros</b-list-group-item>
      </b-list-group>

      <b-card-body>
        <a href="#" class="card-link">Card link</a>
        <a href="#" class="card-link">Another link</a>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "JobListing",
  props: {
    type: String,
  },
  data: () => ({
    current: null,
    softwareEngineer: {
      trend: "There is a rising trend for software engineers since 2015",
      description:
        "A Software Engineer is an IT professional who designs, develops and maintains computer software at a company. They use their creativity and technical skills and apply the principles of software engineering to help solve new and ongoing problems for an organization.",
      pathDescription:
        "The diagram shows the possible career paths one may take as a software engineer",
      listing: [
        {
          company: "Institute of Technical Education",
          role: "Software System Engineer",
          skills: ["Azure", "VMware"],
        },
      ],
    },
  }),
  mounted() {
    if (this.type == "Software Engineer") {
      this.current = this.softwareEngineer;
    }
  },
};
</script>
