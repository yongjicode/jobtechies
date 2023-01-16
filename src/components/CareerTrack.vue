<template>
  <div class="careertrack" style="width: 33.3%">
    <b-card
      overlay
      img-src="https://images.yourstory.com/cs/1/b3cc3444ab5e11e88691f70342131e20/Whatissoftwareandtypesofsoftwarewithexamples1575272423828jpg"
      img-alt="Card Image"
      text-variant="white"
    >
      <b-card-title>{{ track }}</b-card-title>
      <b-card-body>
        Some quick example text to build on the card and make up the bulk of the
        card's content.
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "JobRole",
  props: {
    track: String,
  },
};
</script>
