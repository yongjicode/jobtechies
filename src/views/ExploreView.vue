<template>
  <div class="wrapper">
    <div class="image-container">
      <div
        @click="setCurrentTrack(track)"
        v-for="track in tracks"
        :key="track"
        class="circular-container"
      >
        <img src="../assets/ai.png" class="circular-image" alt="image" />
        <div class="title">{{ track }}</div>
      </div>
    </div>
    <div class="screenshot-container">
      <img v-if="currentTrack == 'DATA & AI'" src="../assets/aiss.jpg" />
      <img
        v-if="currentTrack == 'INFRASTRUCTURE'"
        src="../assets/infrastructuress.jpg"
      />
      <img v-if="currentTrack == 'SOFTWARE'" src="../assets/softwaress.jpg" />
      <img
        v-if="currentTrack == 'STRATEGY & GOVERNANCE'"
        src="../assets/strategyss.jpg"
      />
      <img
        v-if="currentTrack == 'OPERATIONS & SUPPORT'"
        src="../assets/operationsss.jpg"
      />
      <img v-if="currentTrack == 'CYBERSECURITY'" src="../assets/cyberss.jpg" />
      <img
        v-if="currentTrack == 'SALES & MARKETING'"
        src="../assets/salesss.jpg"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "ExploreView",
  data() {
    return {
      currentTrack: "DATA & AI",
      tracks: [
        "DATA & AI",
        "INFRASTRUCTURE",
        "SOFTWARE",
        "STRATEGY & GOVERNANCE",
        "OPERATIONS & SUPPORT",
        "CYBERSECURITY",
        "SALES & MARKETING",
      ],
    };
  },
  methods: {
    setCurrentTrack(track) {
      this.currentTrack = track;
    },
  },
};
</script>

<style scoped>
.image-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.circular-container {
  position: relative;
  height: 150px;
  margin: 0 auto;
}

.circular-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.title {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 0.8rem;
  padding: 10px;
}
</style>
