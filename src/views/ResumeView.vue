<template>
  <div class="wrapper p-5">
    <div class="c-left">
      <div
        @click="onSetCategory('personal')"
        :class="{
          'c-item': selectedCategory !== 'personal',
          'c-item-active': selectedCategory === 'personal',
        }"
      >
        Personal Details
      </div>
      <div
        @click="onSetCategory('education')"
        :class="{
          'c-item': selectedCategory !== 'education',
          'c-item-active': selectedCategory === 'education',
        }"
      >
        Education
      </div>
      <div
        @click="onSetCategory('experience')"
        :class="{
          'c-item': selectedCategory !== 'experience',
          'c-item-active': selectedCategory === 'experience',
        }"
      >
        Experience
      </div>
      <div
        @click="onSetCategory('cca')"
        :class="{
          'c-item': selectedCategory !== 'cca',
          'c-item-active': selectedCategory === 'cca',
        }"
      >
        CCA
      </div>
      <div
        @click="onSetCategory('volunteer')"
        :class="{
          'c-item': selectedCategory !== 'volunteer',
          'c-item-active': selectedCategory === 'volunteer',
        }"
      >
        Volunteer
      </div>
      <div
        @click="onSetCategory('skills')"
        :class="{
          'c-item': selectedCategory !== 'skills',
          'c-item-active': selectedCategory === 'skills',
        }"
      >
        Skills
      </div>
    </div>
    <b-container>
      <b-form @submit.prevent="onSubmit">
        <div
          v-if="selectedCategory == 'personal'"
          class="left mb-3 c-container"
        >
          <h4>Personal Details</h4>
          <b-row>
            <b-col sm="6">
              <b-form-group label="Name" label-for="name" label-align-sm="left">
                <b-form-input
                  v-model="formData.username"
                  type="text"
                  id="username"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="6">
              <b-form-group
                label="Email"
                label-for="email"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.email"
                  type="email"
                  id="email"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col sm="6">
              <b-form-group
                label="Phone"
                label-for="phone"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.phone"
                  type="text"
                  id="phone"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="6">
              <b-form-group
                label="Linkedin Address"
                label-for="linkedin"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.email"
                  type="url"
                  id="linkedin"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>
        </div>

        <div
          v-if="selectedCategory == 'education'"
          class="left mb-3 c-container"
        >
          <h4>Education</h4>
          <b-row>
            <b-col sm="6">
              <b-form-group
                label="School"
                label-for="school"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.school"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="6">
              <b-form-group
                label="Degree"
                label-for="degree"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.degree"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col sm="6">
              <b-form-group
                label="Phone"
                label-for="phone"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.phone"
                  type="text"
                  id="phone"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="6">
              <b-form-group label="GPA" label-for="gpa" label-align-sm="left">
                <b-form-input
                  v-model="formData.gpa"
                  type="url"
                  id="gpa"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="3">
              <b-form-group
                label="Start Date"
                label-for="startDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  size="sm"
                  v-model="formData.startDate"
                  type="text"
                  id="start-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="3">
              <b-form-group
                label="End Date "
                label-for="endDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  size="sm"
                  v-model="formData.endDate"
                  type="text"
                  id="end-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>
          <b-form-group
            label="Description"
            label-for="eduDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.eduDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>
        </div>

        <div
          v-if="selectedCategory == 'experience'"
          class="left mb-3 c-container"
        >
          <h4>Experience</h4>
          <b-row>
            <b-col sm="6">
              <b-form-group
                label="Job Title"
                label-for="jobTitle"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.jobTitle"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="6">
              <b-form-group
                label="Employer"
                label-for="employer"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.employer"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col sm="3">
              <b-form-group
                label="Start Date"
                label-for="startDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  v-model="formData.startDate"
                  type="text"
                  id="start-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="3">
              <b-form-group
                label="End Date "
                label-for="endDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  v-model="formData.endDate"
                  type="text"
                  id="end-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>

          <b-form-group
            label="Description"
            label-for="expDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.expDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>
        </div>

        <div v-if="selectedCategory == 'cca'" class="left mb-3 c-container">
          <h4>CCA</h4>
          <b-row>
            <b-col sm="6">
              <b-form-group
                label="Name"
                label-for="ccaName"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.jobTitle"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="6">
              <b-form-group label="Role" label-for="role" label-align-sm="left">
                <b-form-input
                  v-model="formData.employer"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="3">
              <b-form-group
                label="Start Date"
                label-for="startDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  v-model="formData.startDate"
                  type="text"
                  id="start-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="3">
              <b-form-group
                label="End Date "
                label-for="endDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  v-model="formData.endDate"
                  type="text"
                  id="end-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>

          <b-form-group
            label="Description"
            label-for="expDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.expDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>
        </div>
        <div
          v-if="selectedCategory == 'volunteer'"
          class="left mb-3 c-container"
        >
          <h4>Volunteer</h4>
          <b-row>
            <b-col sm="6">
              <b-form-group
                label="Name"
                label-for="ccaName"
                label-align-sm="left"
              >
                <b-form-input
                  v-model="formData.jobTitle"
                  type="text"
                  id="school"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="3">
              <b-form-group
                label="Start Date"
                label-for="startDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  v-model="formData.startDate"
                  type="text"
                  id="start-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
            <b-col sm="3">
              <b-form-group
                label="End Date "
                label-for="endDate"
                label-align-sm="left"
              >
                <b-form-datepicker
                  v-model="formData.endDate"
                  type="text"
                  id="end-date"
                  class="color-box"
                />
              </b-form-group>
            </b-col>
          </b-row>
          <b-form-group
            label="Description"
            label-for="expDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.expDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>
        </div>

        <div v-if="selectedCategory == 'skills'" class="left mb-3 c-container">
          <h4>Skills</h4>
          <b-form-group
            label="What languages are you proficient in?"
            label-for="expDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.expDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>

          <b-form-group
            label="What technical skills do you possess?"
            label-for="expDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.expDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>

          <b-form-group
            label="What are your hobbies and interests?"
            label-for="expDescription"
            label-align-sm="left"
          >
            <b-form-input
              v-model="formData.expDescription"
              type="text"
              id="eduDescription"
              class="color-box"
            />
          </b-form-group>
        </div>

        <b-form-group>
          <router-link to="/discover">
            <b-button type="submit" variant="warning" style="float: right"
              >Confirm</b-button
            >
          </router-link>
        </b-form-group>
      </b-form>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        username: "",
        email: "",
        phone: "",
        linkedin: "",
      },
      selectedCategory: "personal",
    };
  },
  methods: {
    onSubmit() {
      // logic to submit form data
    },
    onSetCategory(category) {
      this.selectedCategory = category;
    },
  },
};
</script>

<style scoped>
.wrapper {
  width: 100%;
  display: flex;
}

.c-left {
  width: 30%;
  padding: 40px;
  border-radius: 20px;
  height: 400px;
  background-color: aliceblue;
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

.c-container {
  width: 70%;
  background-color: aliceblue;
  border-radius: 10px;
  padding-left: 50px;
  padding-right: 50px;
  padding-top: 20px;
  padding-bottom: 20px;
}

.left {
  text-align: left;
  font-weight: bold;
}

.color-box {
  background-color: #fff6ef;
  border: 0px;
}
</style>
