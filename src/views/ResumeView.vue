<template>
  <b-container>
    <b-form @submit.prevent="onSubmit">
      <div class="left">Personal Details</div>
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
          <b-form-group label="Email" label-for="email" label-align-sm="left">
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
          <b-form-group label="Phone" label-for="phone" label-align-sm="left">
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

      <div class="left">Education</div>
      <b-row>
        <b-col sm="6">
          <b-form-group label="School" label-for="school" label-align-sm="left">
            <b-form-input
              v-model="formData.school"
              type="text"
              id="school"
              class="color-box"
            />
          </b-form-group>
        </b-col>
        <b-col sm="6">
          <b-form-group label="Degree" label-for="degree" label-align-sm="left">
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
          <b-form-group label="Phone" label-for="phone" label-align-sm="left">
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
      <div class="left">Experience</div>
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

      <div class="left">CCA</div>
      <b-row>
        <b-col sm="6">
          <b-form-group label="Name" label-for="ccaName" label-align-sm="left">
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
      <div class="left">Volunteer</div>
      <b-row>
        <b-col sm="6">
          <b-form-group label="Name" label-for="ccaName" label-align-sm="left">
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

      <div class="left">Skills</div>
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

      <b-form-group>
        <b-button type="submit" variant="warning" style="float: right"
          >Confirm</b-button
        >
      </b-form-group>
    </b-form>
  </b-container>
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
    };
  },
  methods: {
    onSubmit() {
      // logic to submit form data
    },
  },
};
</script>

<style scoped>
.left {
  text-align: left;
  font-weight: bold;
}

.color-box {
  background-color: #eff2f9;
}
</style>
