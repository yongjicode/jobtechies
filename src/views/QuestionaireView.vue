<template>
  <div>
    <div v-for="(question, index) in filteredQuestions" :key="index">
      <h3>{{ question.text }}</h3>
      <div v-for="(option, optionIndex) in question.options" :key="optionIndex">
        <input
          type="radio"
          :value="option"
          :name="question.id"
          v-model="userAnswers[question.id]"
        />
        {{ option }}
      </div>
    </div>
    <div>
      <button @click="previousPage" :disabled="currentPage === 0">
        Previous
      </button>
      <button
        @click="nextPage"
        :disabled="currentPage === questions.length - 1"
      >
        Next
      </button>
      <p>Page {{ currentPage + 1 }} of {{ questions.length }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionaireView",
  data() {
    return {
      currentPage: 0,
      userAnswers: {},
      questions: [
        {
          id: 1,
          text: "Question 1",
          options: ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
        },
        {
          id: 2,
          text: "Question 2",
          options: ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
        },
        // And so on for the remaining 6 questions
      ],
    };
  },
  computed: {
    filteredQuestions() {
      return this.questions.filter(
        (question, index) => this.currentPage === index
      );
    },
  },
  methods: {
    nextPage() {
      this.currentPage++;
    },
    previousPage() {
      this.currentPage--;
    },
  },
};
</script>
