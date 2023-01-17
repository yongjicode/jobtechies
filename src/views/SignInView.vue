<template>
  <div class="home">
    <div class="landing-page-text">
      <h1><b>Sign in to TechUp</b></h1>
      <b-form @submit.prevent="submitForm">
        <b-form-group
          label="Username:"
          label-for="username"
          :state="usernameValid"
        >
          <input
            id="username"
            v-model="username"
            placeholder="Enter your username"
            :state="usernameValid"
            @input="validateUsername"
          />
        </b-form-group>
        <b-form-group
          label="Password:"
          label-for="password"
          :state="passwordValid"
        >
          <input
            id="password"
            type="password"
            placeholder="Enter your password"
            v-model="password"
            :state="passwordValid"
            @input="validatePassword"
          />
        </b-form-group>
        <router-link to="/discover">
          <button type="submit" variant="primary">Login</button>
        </router-link>
        <router-link to="/questionaire">
          <button type="submit" variant="primary" style="margin-left: 15px">
            Sign Up
          </button>
        </router-link>
      </b-form>
      <div class="below-form">
        <p>Or continue with:</p>
        <div class="icons">
          <img src="../assets/linkedin.png" alt="linkedin logo" />
          <img src="../assets/google.png" alt="google logo" />
        </div>
      </div>
    </div>
    <div class="img-container">
      <img
        class="landing-page-img"
        alt="Landing Page Logo"
        src="../assets/sign in.png"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "SignInView",
  data() {
    return {
      username: "",
      password: "",
      usernameValid: null,
      passwordValid: null,
    };
  },
  methods: {
    validateUsername() {
      if (this.username.length === 0) {
        this.usernameValid = false;
      } else {
        this.usernameValid = true;
      }
    },
    validatePassword() {
      if (this.password.length === 0) {
        this.passwordValid = false;
      } else {
        this.passwordValid = true;
      }
    },
    submitForm() {
      if (this.usernameValid && this.passwordValid) {
        // Send the username and password to the server
        // for authentication
      } else {
        // Display an error message
        alert("Please enter a valid username and password.");
      }
    },
  },
};
</script>

<style scoped>
.icons {
  display: flex;
  gap: 20px;
  justify-content: flex-start;
  width: 100%;
}

.below-form {
  padding-top: 20px;
}

input:hover,
input:focus {
  box-shadow: none;
  outline: none;
}

input {
  border: none;
  border-bottom: 2px solid #25424c;
  width: 100%;
}

button {
  height: 40px;
  width: 150px;
  border-radius: 10px;
  border: 1px solid #25424c;
  color: #25424c;
  background-color: transparent;
}

button:hover {
  border: 1px solid #25424c;
  color: white;
  background-color: #25424c;
}

.home {
  margin-top: 10%;
  background-color: white;
  position: relative;
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.landing-page-text {
  text-align: left;
  width: 50%;
  align-items: center;
}

h1 {
  font-size: 3rem;
}

p {
  font-size: 1rem;
}

h1,
p {
  text-align: left;
}

/* .landing-page-img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
} */
</style>
