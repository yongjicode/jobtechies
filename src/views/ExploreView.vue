<template>
  <div class="wrapper">
    <div class="image-container">
      <div
        @click="setCurrentTrack(track.name)"
        v-for="track in tracks"
        :key="track.name"
        class="circular-container"
      >
        <div :class="track.color" />
        <div class="title">{{ track.name }}</div>
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
        { name: "DATA & AI", color: "c-ai" },
        { name: "INFRASTRUCTURE", color: "c-infra" },
        { name: "SOFTWARE", color: "c-software" },
        { name: "STRATEGY & GOVERNANCE", color: "c-strat" },
        { name: "OPERATIONS & SUPPORT", color: "c-ops" },
        { name: "CYBERSECURITY", color: "c-cyber" },
        { name: "SALES & MARKETING", color: "c-sales" },
      ],
    };
  },
  methods: {
    setCurrentTrack(track) {
      console.log(this.currentTrack);
      this.currentTrack = track;
    },
  },
};
</script>

<style scoped>
.image-container {
  margin-top: 30px;
  padding-top: 20px;
  background-color: #f5f5f5;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.circular-container {
  position: relative;
  height: 50px;
  margin: 0 auto;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.c-ai {
  background-color: #056c9f;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.c-infra {
  background-color: #01a8c8;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.c-software {
  background-color: #d63626;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.c-ops {
  background-color: #eb921b;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.c-strat {
  background-color: #008074;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.c-cyber {
  background-color: #653a94;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.c-sales {
  background-color: #ad1f8f;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.title {
  text-align: left;
  font-size: 0.8rem;
  width: 100%;
}

.screenshot-container {
  padding-top: 30px;
}
</style>
