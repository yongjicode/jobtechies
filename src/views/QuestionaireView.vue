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
    <div>
      <router-link to="/uploadorgenerate">
        <button>Submit</button>
      </router-link>
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
          text: "Your friends would describe you as…",
          options: [
            "Skeptical",
            "Empathetic",
            "A Storyteller",
            "A Problem-Solver",
            "A Leader",
          ],
        },
        {
          id: 2,
          text: "What's your favorite type of project?",
          options: [
            "Making a diorama/art project",
            "Writing a research paper",
            "Preparing or giving a presentation",
            "Automating workflows / making something work",
            "Planning a new program initiative or organizing a discussion group.",
          ],
        },
        {
          id: 3,
          text: "How do you make important decisions?",
          options: [
            "After carefully analyzing every option and the predicted results",
            "After checking with friends",
            "I make an executive decision and everyone follows along",
            "Create a poll and ask social media",
            "Gut instinct",
            "Come up with the simplest solution",
          ],
        },
        {
          id: 4,
          text: "What does success mean for you?",
          options: [
            "Earning a high income",
            "Autonomy to make high-level decisions",
            "Ability to balance work and life",
            "Creative control of my projects",
          ],
        },
        {
          id: 5,
          text: "When you picture your ideal job, what are you doing?",
          options: [
            "Working in a fast-paced role that pushes me to produce results",
            "Getting creative and coming up with new ideas",
            "Thinking big-picture and solving problems",
            "Figuring out how the company operates, and finding ways to do it better",
            "Leading a team",
          ],
        },
        {
          id: 6,
          text: "How do you feel about working in groups?",
          options: [
            "I love working in groups!",
            "I like working with a group, as long as I can take the lead",
            "I can adapt to any situation",
            "I prefer to work by myself most of the time",
          ],
        },
        {
          id: 7,
          text: "Do you consider yourself an introvert or extrovert",
          options: [
            "Extrovert all the way",
            "Mostly extroverted",
            "A balance between both",
            "Mostly introverted",
            "Introvert all the way",
          ],
        },
        {
          id: 8,
          text: "Which of these is your strongest skill?",
          options: [
            "Storytelling",
            "Logical Thinking",
            "Creativity",
            "Troubleshooting",
            "Persusive Communication",
            "Math & Statistics",
          ],
        },
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
