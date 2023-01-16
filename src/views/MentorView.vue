<template>
  <div>
    <b-form-group label="Search mentors by name or skill">
      <b-form-input v-model="search"></b-form-input>
    </b-form-group>
    <b-row>
      <b-col v-for="mentor in filteredMentors" :key="mentor.id" cols="3">
        <b-card class="mb-2">
          <b-card-header>
            {{ mentor.name }}
            <b-button @click="sortBy('name')" size="sm" class="float-right"
              >Sort by name</b-button
            >
          </b-card-header>
          <b-card-body>
            <p>{{ mentor.bio }}</p>
            <p>Skills: {{ mentor.skills.join(", ") }}</p>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
    <b-pagination
      v-model="currentPage"
      :total-rows="totalRows"
      :per-page="mentorsPerPage"
      aria-controls="my-table"
    ></b-pagination>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mentors: [
        {
          id: 1,
          name: "John Doe",
          bio: "John is a professional mentor with 10 years of experience in software development.",
          skills: ["JavaScript", "Vue.js", "React"],
        },
        {
          id: 2,
          name: "Jane Smith",
          bio: "Jane is a professional mentor with 8 years of experience in web design.",
          skills: ["HTML", "CSS", "Adobe XD"],
        },
        {
          id: 3,
          name: "John Doe",
          bio: "John is a professional mentor with 10 years of experience in software development.",
          skills: ["JavaScript", "Vue.js", "React"],
        },
        {
          id: 4,
          name: "John Doe",
          bio: "John is a professional mentor with 10 years of experience in software development.",
          skills: ["JavaScript", "Vue.js", "React"],
        },
        {
          id: 5,
          name: "John Doe",
          bio: "John is a professional mentor with 10 years of experience in software development.",
          skills: ["JavaScript", "Vue.js", "React"],
        },
        {
          id: 6,
          name: "John Doe",
          bio: "John is a professional mentor with 10 years of experience in software development.",
          skills: ["JavaScript", "Vue.js", "React"],
        },
        // more mentor objects
      ],
      search: "",
      currentPage: 1,
      mentorsPerPage: 8,
      sortBy: "name",
      sortDirection: "asc",
    };
  },
  computed: {
    filteredMentors() {
      // filter mentors by search term
      let filteredMentors = this.mentors.filter((mentor) => {
        return (
          mentor.name.toLowerCase().includes(this.search.toLowerCase()) ||
          mentor.skills
            .join(",")
            .toLowerCase()
            .includes(this.search.toLowerCase())
        );
      });

      // sort mentors by sortBy and sortDirection
      filteredMentors.sort((a, b) => {
        let modifier = 1;
        if (this.sortDirection === "desc") modifier = -1;
        if (a[this.sortBy] < b[this.sortBy]) return -1 * modifier;
        if (a[this.sortBy] > b[this.sortBy]) return 1 * modifier;
        return 0;
      });

      // pagination
      const indexOfLastMentor = this.currentPage * this.mentorsPerPage;
      const indexOfFirstMentor = indexOfLastMentor - this.mentorsPerPage;
      return filteredMentors.slice(indexOfFirstMentor, indexOfLastMentor);
    },
    totalRows() {
      return this.mentors.length;
    },
  },
  methods: {
    sortBy1(sortBy) {
      if (this.sortBy === sortBy) {
        this.sortDirection = this.sortDirection === "asc" ? "desc" : "asc";
      } else {
        this.sortBy = sortBy;
        this.sortDirection = "asc";
      }
    },
  },
};
</script>
