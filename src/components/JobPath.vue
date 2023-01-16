<template>
  <div class="explore">
    <b-card no-body style="max-width: 100%">
      <img src="@/assets/swe.png" />
      <b-card-body>
        <b-card-title>{{ type }} Career Paths</b-card-title>
        <b-card-text>
          {{ current.pathDescription }}
        </b-card-text>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "JobPath",
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
