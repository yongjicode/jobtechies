<template>
  <div>
    <h3 style="text-align: center">Resume Enhancer</h3>
    <div class="wrapper p-3">
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
        <b-form
          style="display: flex; flex-direction: column; align-items: flex-start"
          @submit.prevent="onSubmit"
        >
          <div style="height: 420px; width: 100%">
            <div class="c-outer" v-if="selectedCategory == 'personal'">
              <h4 style="text-align: left">Personal Details</h4>
              <div class="left mb-3 c-container">
                <b-row>
                  <b-col sm="6">
                    <b-form-group
                      label="Name"
                      label-for="name"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.info.one"
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
                        v-model="formData.info.three"
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
                        v-model="formData.info.two"
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
                        v-model="formData.info.four"
                        type="url"
                        id="linkedin"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                </b-row>
              </div>
            </div>

            <div class="c-outer" v-if="selectedCategory == 'education'">
              <h4 style="text-align: left">Education</h4>
              <div class="left mb-3 c-container">
                <b-row>
                  <b-col sm="6">
                    <b-form-group
                      label="School"
                      label-for="school"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.education.one"
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
                        v-model="formData.education.two"
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
                      label="GPA"
                      label-for="gpa"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.education.three"
                        type="url"
                        id="gpa"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col sm="5">
                    <b-form-group
                      label="Start Date"
                      label-for="startDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        size="sm"
                        v-model="eduStartDate"
                        type="text"
                        id="start-date"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                  <b-col sm="5">
                    <b-form-group
                      label="End Date "
                      label-for="endDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        size="sm"
                        v-model="eduEndDate"
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
                    v-model="formData.education.five"
                    type="text"
                    id="eduDescription"
                    class="color-box"
                  />
                </b-form-group>
              </div>
            </div>

            <div class="c-outer" v-if="selectedCategory == 'experience'">
              <h4 style="text-align: left">Experience</h4>
              <div class="left mb-3 c-container">
                <b-row>
                  <b-col sm="6">
                    <b-form-group
                      label="Job Title"
                      label-for="jobTitle"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.experience.two"
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
                        v-model="formData.experience.one"
                        type="text"
                        id="school"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                </b-row>

                <b-row>
                  <b-col sm="5">
                    <b-form-group
                      label="Start Date"
                      label-for="startDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        v-model="expStartDate"
                        type="text"
                        id="start-date"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                  <b-col sm="5">
                    <b-form-group
                      label="End Date "
                      label-for="endDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        v-model="expEndDate"
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
                    v-model="formData.experience.four"
                    type="text"
                    id="eduDescription"
                    class="color-box"
                  />
                </b-form-group>
              </div>
            </div>

            <div class="c-outer" v-if="selectedCategory == 'cca'">
              <h4 style="text-align: left">CCA</h4>
              <div class="left mb-3 c-container">
                <b-row>
                  <b-col sm="6">
                    <b-form-group
                      label="Name"
                      label-for="ccaName"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.cca.one"
                        type="text"
                        id="school"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                  <b-col sm="6">
                    <b-form-group
                      label="Role"
                      label-for="role"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.cca.two"
                        type="text"
                        id="school"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col sm="5">
                    <b-form-group
                      label="Start Date"
                      label-for="startDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        v-model="ccaStartDate"
                        type="text"
                        id="start-date"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                  <b-col sm="5">
                    <b-form-group
                      label="End Date "
                      label-for="endDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        v-model="ccaEndDate"
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
                    v-model="formData.cca.four"
                    type="text"
                    id="eduDescription"
                    class="color-box"
                  />
                </b-form-group>
              </div>
            </div>

            <div class="c-outer" v-if="selectedCategory == 'volunteer'">
              <h4 style="text-align: left">Volunteer</h4>
              <div class="left mb-3 c-container">
                <b-row>
                  <b-col sm="6">
                    <b-form-group
                      label="Name"
                      label-for="ccaName"
                      label-align-sm="left"
                    >
                      <b-form-input
                        v-model="formData.volunteer.one"
                        type="text"
                        id="school"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                  <b-col sm="5">
                    <b-form-group
                      label="Start Date"
                      label-for="startDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        v-model="volunteerStartDate"
                        type="text"
                        id="start-date"
                        class="color-box"
                      />
                    </b-form-group>
                  </b-col>
                  <b-col sm="5">
                    <b-form-group
                      label="End Date "
                      label-for="endDate"
                      label-align-sm="left"
                    >
                      <b-form-datepicker
                        v-model="volunteerEndDate"
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
                    v-model="formData.volunteer.three"
                    type="text"
                    id="eduDescription"
                    class="color-box"
                  />
                </b-form-group>
              </div>
            </div>

            <div class="c-outer" v-if="selectedCategory == 'skills'">
              <h4 style="text-align: left">Skills</h4>
              <div class="left mb-3 c-container">
                <b-form-group
                  label="What languages are you proficient in?"
                  label-for="expDescription"
                  label-align-sm="left"
                >
                  <b-form-input
                    v-model="formData.skillsInterest.one"
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
                    v-model="formData.skillsInterest.two"
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
                    v-model="formData.skillsInterest.three"
                    type="text"
                    id="eduDescription"
                    class="color-box"
                  />
                </b-form-group>
              </div>
            </div>
          </div>
          <div style="display: flex; gap: 10">
            <b-button
              v-if="selectedCategory != 'personal'"
              @click="goPrev"
              variant="warning"
              style="margin-right: 10px"
              >Prev</b-button
            >
            <b-button
              v-if="selectedCategory != 'skills'"
              @click="goNext"
              variant="warning"
              style="margin-right: 10px"
              >Next</b-button
            >
            <b-button
              v-if="selectedCategory == 'skills'"
              type="submit"
              variant="warning"
              @click="onSubmit"
              >Confirm</b-button
            >
          </div>
        </b-form>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    console.log("mounted");
    const fileName = localStorage.getItem("fileName");
    if (fileName) {
      console.log("success: ", fileName);
      this.readFile(fileName);
      localStorage.clear();
    }
  },
  data() {
    return {
      eduStartDate: "",
      eduEndDate: "",
      expStartDate: "",
      expEndDate: "",
      ccaStartDate: "",
      ccaEndDate: "",
      volunteerStartDate: "",
      volunteerEndDate: "",
      formData: {
        info: { one: "", two: "", three: "", four: "" },
        education: { one: "", two: "", three: "", four: "", five: "" },
        experience: { one: "", two: "", three: "", four: "" },
        cca: { one: "", two: "", three: "", four: "" },
        volunteer: { one: "", two: "", three: "" },
        skillsInterest: { one: "", two: "", three: "" },
      },
      selectedCategory: "personal",
      categories: [
        "personal",
        "education",
        "experience",
        "cca",
        "volunteer",
        "skillsInterest",
      ],
    };
  },
  methods: {
    readFile(name) {
      window.open(`./assets/static/${name}_Resume.docx`, "_blank");
    },
    async onSubmit() {
      this.formData.education["four"] =
        this.eduStartDate + " - " + this.eduEndDate;
      this.formData.experience["three"] =
        this.expStartDate + " - " + this.expEndDate;
      this.formData.cca["three"] = this.ccaStartDate + " - " + this.ccaEndDate;
      this.formData.volunteer["two"] =
        this.volunteerStartDate + " - " + this.volunteerEndDate;
      for (var key in this.formData) {
        for (var key2 in this.formData[key]) {
          if (key2 == "one") {
            this.formData[key]["1"] = this.formData[key][key2];
          } else if (key2 == "two") {
            this.formData[key]["2"] = this.formData[key][key2];
          } else if (key2 == "three") {
            this.formData[key]["3"] = this.formData[key][key2];
          } else if (key2 == "four") {
            this.formData[key]["4"] = this.formData[key][key2];
          } else if (key2 == "five") {
            this.formData[key]["5"] = this.formData[key][key2];
          }
        }
      }
      var name = this.formData["info"]["1"];
      console.log(this.formData);
      localStorage.setItem("fileName", name);
      const res = await fetch("http://127.0.0.1:5000/convert", {
        method: "post",
        body: JSON.stringify(this.formData),
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      const data = await res.json();
      console.log(data);

      // .then((data) => {
      //   console.log(name, " coming: ", data);
      //   // setTimeout(() => {
      //   //   this.readFile(name);
      //   //   console.log(name, " success");
      //   // }, 5000);
      // });
    },
    onSetCategory(category) {
      console.log(category);
      this.selectedCategory = category;
    },
    goPrev() {
      for (let i = 0; i < this.categories.length; i++) {
        if (this.categories[i] == this.selectedCategory) {
          this.selectedCategory = this.categories[i - 1];
          break;
        }
      }
    },
    goNext() {
      console.log("hello");
      for (let i = 0; i < this.categories.length; i++) {
        if (this.categories[i] == this.selectedCategory) {
          this.selectedCategory = this.categories[i + 1];
          break;
        }
      }
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
  height: max-content;
  background-color: #f5f5f5;
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
  background-color: #f5f5f5;
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
  background-color: white;
  border: 0px;
}
</style>
