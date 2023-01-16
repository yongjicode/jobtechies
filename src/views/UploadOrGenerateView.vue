<template>
  <div class="wrapper">
    <h3>Resume</h3>
    <p>Uploading your resume will help us make better career recommendations</p>
    <div class="upload-resume">
      <p>
        Drag and drop your resume <br />
        or
      </p>
      <button>upload</button>
    </div>
    <div>
      <p>Don't have a resume yet? No worries!</p>
      <router-link to="/resume"><button>Generate</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "UploadOrGenerateView",
  components: {},
};
</script>

<style>
.wrapper {
  display: flex;
  width: 100%;
  align-items: center;
  flex-direction: column;
}

.upload-resume {
  border-radius: 20px;
  border: 10px dashed #ffa45b;
  height: 400px;
  width: 400px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin-bottom: 30px;
}

button {
  height: 40px;
  width: 100px;
  border-radius: 40px;
  border: 1px solid #fb770d;
  color: white;
  background-color: #fb770d;
}

button:hover {
  border: 1px solid #fb770d;
  color: #fb770d;
  background-color: #25424c;
}
</style>
