<template>
  <div class="wrapper clearfix">
    <div class="wizard-part-title">
      <h3></h3>
    </div>
    <!--multisteps-form-->
    <div class="multisteps-form">
      <!--progress bar-->
      <div class="row">
        <div class="col-12 col-lg-12 ml-auto mr-auto mb-0 mt-0">
          <div class="multisteps-form__progress" style="padding: 0 0 0 0"></div>
        </div>
      </div>
      <!--form panels-->
      <div class="row">
        <div class="col-12 col-lg-12 m-auto">
          <form
            class="multisteps-form__form clearfix"
            action="#"
            method="post"
            id="wizard"
          >
            <!--single form panel-->
            <div
              class="multisteps-form__panel js-active"
              data-animation="slideVert"
              v-if="currentPage === 0"
            >
              <div class="inner pb-100">
                <div class="wizard-topper">
                  <div class="wizard-progress">
                    <span>1 of 5 Completed</span>
                    <div class="progress">
                      <div class="progress-bar"></div>
                    </div>
                  </div>
                </div>
                <div class="wizard-content-item text-center">
                  <p>Your friends would describe you as …</p>
                </div>
                <div class="wizard-content-form">
                  <div class="wizard-form-field">
                    <div class="identity-option wizard-content-form">
                      <ul>
                        <li>
                          <label>
                            <input
                              type="checkbox"
                              class="identity-check"
                              checked="checked"
                            />
                            <span class="identity-label"></span>Skeptical
                            <span class="checkmark-border"></span>
                          </label>
                        </li>
                        <li>
                          <label>
                            <input type="checkbox" class="identity-check" />
                            <span class="identity-label"></span>Empathetic
                            <span class="checkmark-border"></span>
                          </label>
                        </li>
                        <li>
                          <label>
                            <input type="checkbox" class="identity-check" />
                            <span class="identity-label"></span>A Storyteller
                            <span class="checkmark-border"></span>
                          </label>
                        </li>
                        <li>
                          <label>
                            <input type="checkbox" class="identity-check" />
                            <span class="identity-label"></span>A Problem-Solver
                            <span class="checkmark-border"></span>
                          </label>
                        </li>
                        <li>
                          <label>
                            <input type="checkbox" class="identity-check" />
                            <span class="identity-label"></span>A Leader
                            <span class="checkmark-border"></span>
                          </label>
                        </li>
                        <li>
                          <label>
                            <input type="checkbox" class="identity-check" />
                            <span class="identity-label"></span>An Agreeable
                            Person
                            <span class="checkmark-border"></span>
                          </label>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="wizard-footer">
                  <div class="wizard-imgbg">
                    <img src="@/assets/v3.png" alt="" />
                  </div>
                  <div class="actions" @click="nextPage()">
                    <ul>
                      <li>
                        <span class="js-btn-next" title="NEXT"
                          >NEXT <i class="fa fa-arrow-right"></i
                        ></span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!--single form panel-->
            <div
              class="multisteps-form__panel"
              data-animation="slideVert"
              v-if="currentPage === 1"
            >
              <div class="inner pb-100">
                <div class="wizard-topper">
                  <div class="wizard-progress">
                    <span>2 of 5 Completed</span>
                    <div class="progress">
                      <div class="progress-bar" style="width: 45%"></div>
                    </div>
                  </div>
                </div>
                <div class="wizard-content-item text-center">
                  <p>What’s your favorite type of project?</p>
                </div>
                <div class="wizard-option-list wizard-content-form">
                  <div class="taxable-area">
                    <div class="row" style="margin-bottom: 40px">
                      <div class="col-md-4">
                        <label>
                          <input
                            type="checkbox"
                            class="tax-check"
                            value="Taxable in the US?"
                          />
                          <span class="checkbo-box-border"></span>
                          <span class="texable-option">
                            Make a diorama project
                          </span>
                        </label>
                      </div>
                      <div class="col-md-4">
                        <label>
                          <input
                            type="checkbox"
                            class="tax-check"
                            value="Taxable in the US?"
                          />
                          <span class="checkbo-box-border"></span>
                          <span class="texable-option">
                            Write a research paper
                          </span>
                        </label>
                      </div>
                      <div class="col-md-4">
                        <label>
                          <input
                            type="checkbox"
                            class="tax-check"
                            value="Taxable in the US?"
                          />
                          <span class="checkbo-box-border"></span>
                          <span class="texable-option">
                            Give a presentation
                          </span>
                        </label>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-4">
                        <label>
                          <input
                            type="checkbox"
                            class="tax-check"
                            value="Taxable in the US?"
                          />
                          <span class="checkbo-box-border"></span>
                          <span class="texable-option">
                            Automate workflows
                          </span>
                        </label>
                      </div>
                      <div class="col-md-4">
                        <label>
                          <input
                            type="checkbox"
                            class="tax-check"
                            value="Taxable in the US?"
                          />
                          <span class="checkbo-box-border"></span>
                          <span class="texable-option">
                            Plan a program initiative
                          </span>
                        </label>
                      </div>
                      <div class="col-md-4">
                        <label>
                          <input
                            type="checkbox"
                            class="tax-check"
                            value="Taxable in the US?"
                          />
                          <span class="checkbo-box-border"></span>
                          <span class="texable-option">
                            Organize a discussion group
                          </span>
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="wizard-footer">
                  <div class="wizard-imgbg">
                    <img src="@/assets/v2.png" alt="" />
                  </div>
                  <div class="actions">
                    <ul>
                      <li @click="previousPage()">
                        <span class="js-btn-prev" title="BACK"
                          ><i class="fa fa-arrow-left"></i> BACK</span
                        >
                      </li>
                      <li @click="nextPage()">
                        <span class="js-btn-next" title="NEXT"
                          >NEXT <i class="fa fa-arrow-right"></i
                        ></span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!--single form panel-->
            <div
              class="multisteps-form__panel"
              data-animation="slideVert"
              v-if="currentPage === 2"
            >
              <div class="inner pb-100">
                <div class="wizard-topper">
                  <div class="wizard-progress">
                    <span>3 of 5 Completed</span>
                    <div class="progress">
                      <div class="progress-bar" style="width: 65%"></div>
                    </div>
                  </div>
                </div>
                <div class="wizard-content-item text-center">
                  <p>How do you make important decisions?</p>
                </div>
                <div class="wizard-identity wizard-content-form">
                  <ul>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >After carefully analyzing every option and the
                            predicted results</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >After checking with friends</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >I make an executive decision and everyone follows
                            along</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>

                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >I make an executive decision and everyone follows
                            along</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>

                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title">Gut instinct</span>
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>

                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >Come up with the simplest possible solution</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="wizard-footer">
                  <div class="wizard-imgbg">
                    <img src="@/assets/v3.png" alt="" />
                  </div>
                  <div class="actions">
                    <ul>
                      <li @click="previousPage()">
                        <span class="js-btn-prev" title="BACK"
                          ><i class="fa fa-arrow-left"></i> BACK</span
                        >
                      </li>
                      <li @click="nextPage()">
                        <span class="js-btn-next" title="NEXT"
                          >NEXT <i class="fa fa-arrow-right"></i
                        ></span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!--single form panel-->
            <div
              class="multisteps-form__panel"
              data-animation="slideVert"
              v-if="currentPage === 3"
            >
              <div class="inner pb-100">
                <div class="wizard-topper">
                  <div class="wizard-progress">
                    <span>4 of 5 Completed</span>
                    <div class="progress">
                      <div class="progress-bar" style="width: 65%"></div>
                    </div>
                  </div>
                </div>
                <div class="wizard-content-item text-center">
                  <p>When you picture your ideal job, what are you doing?</p>
                </div>
                <div class="wizard-identity wizard-content-form">
                  <ul>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >Working in a fast-paced role that pushes me to
                            produce results</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >Getting creative and coming up with new ideas</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >Getting creative and coming up with new ideas</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>

                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >Figuring out how the company operates, and finding
                            ways to do it better</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>

                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title">Leading a team</span>
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="wizard-footer">
                  <div class="wizard-imgbg">
                    <img src="@/assets/v4.png" alt="" />
                  </div>
                  <div class="actions">
                    <ul>
                      <li @click="previousPage()">
                        <span class="js-btn-prev" title="BACK"
                          ><i class="fa fa-arrow-left"></i> BACK</span
                        >
                      </li>
                      <li @click="nextPage()">
                        <span class="js-btn-next" title="NEXT"
                          >NEXT <i class="fa fa-arrow-right"></i
                        ></span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!--single form panel-->
            <div
              class="multisteps-form__panel"
              data-animation="slideVert"
              v-if="currentPage === 4"
            >
              <div class="inner pb-100">
                <div class="wizard-topper">
                  <div class="wizard-progress">
                    <span>5 of 5 Completed</span>
                    <div class="progress">
                      <div class="progress-bar" style="width: 100%"></div>
                    </div>
                  </div>
                </div>
                <div class="wizard-content-item text-center">
                  <p>Share with us more about you!</p>
                </div>
                <div class="wizard-submit-file-content wizard-content-form">
                  <ul>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >I have mastered more than 3 programming
                            languages</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >I like working with a group, as long as I can take
                            the lead.</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                    <li class="no-arrow active" style="margin-bottom: 20px">
                      <div class="n-activity">
                        <label>
                          <span class="n-title"
                            >I value more of chance of improvements than
                            rewards.</span
                          >
                          <input type="checkbox" class="net-check" />
                          <span class="net-check-border"></span>
                        </label>
                      </div>
                    </li>
                  </ul>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="n-select-option">
                        <select>
                          <option>
                            Which of these is your strongest skill?
                          </option>
                          <option>Stroytelling</option>
                          <option>Logical Thinking</option>
                          <option>Creativity</option>
                          <option>Troubleshooting</option>
                          <option>Math & Statistics</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="n-select-option">
                        <select>
                          <option>Working Experience</option>
                          <option>Less than 1 Year</option>
                          <option>1-3 Year</option>
                          <option>3-5 Year</option>
                          <option>5 Year plus</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="wizard-footer">
                  <div class="wizard-imgbg float-left">
                    <img src="@/assets/v5.png" alt="" />
                  </div>
                  <div class="actions">
                    <ul>
                      <li>
                        <span class="js-btn-prev" title="BACK"
                          ><i class="fa fa-arrow-left"></i> BACK</span
                        >
                      </li>
                      <li>
                        <button type="submit" id="submit-form" title="NEXT">
                          SUMBIT <i class="fa fa-arrow-right"></i>
                        </button>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import $ from "jquery";
$("#files").change(function () {
  var filename = this.files[0].name;
  console.log(filename);
});
$(function () {
  $(".wizard > .steps li a").click(function () {
    $(this).parent().addClass("checked");
    $(this).parent().prevAll().addClass("checked");
    $(this).parent().nextAll().removeClass("checked");
  });
  $(":checkbox").on("click", function () {
    $(this).parent().parent().toggleClass("checked");
  });
  // Custome Jquery Step Button
  $(".forward").click(function () {
    $("#wizard").steps("next");
  });
  $(".backward").click(function () {
    $("#wizard").steps("previous");
  });
  // Select Dropdown
  $("html").click(function () {
    $(".select .dropdown").hide();
  });
  $(".select").click(function (event) {
    event.stopPropagation();
  });
  $(".select .select-control").click(function () {
    $(this).parent().next().toggle();
  });
  $(".select .dropdown li").click(function () {
    $(this).parent().toggle();
    var text = $(this).attr("rel");
    $(this).parent().prev().find("div").text(text);
  });

  $(".wizard-option-list ul li ").click(function () {
    $(".wizard-option-list ul li").removeClass("active");
    $(this).addClass("active");
  });
  $(".texable-option ").click(function () {
    $(".texable-option").removeClass("active");
    $(this).addClass("active");
  });

  updateContainer();
  $(window).resize(function () {
    updateContainer();
  });
});

function updateContainer() {
  //multi form ===================================
  //DOM elements
  const DOMstrings = {
    stepsBtnClass: "multisteps-form__progress-btn",
    stepsBtns: document.querySelectorAll(`.multisteps-form__progress-btn`),
    stepsBar: document.querySelector(".multisteps-form__progress"),
    stepsForm: document.querySelector(".multisteps-form__form"),
    stepFormPanelClass: "multisteps-form__panel",
    stepFormPanels: document.querySelectorAll(".multisteps-form__panel"),
    stepPrevBtnClass: "js-btn-prev",
    stepNextBtnClass: "js-btn-next",
  };

  //remove class from a set of items
  const removeClasses = (elemSet, className) => {
    elemSet.forEach((elem) => {
      elem.classList.remove(className);
    });
  };

  //return exect parent node of the element
  const findParent = (elem, parentClass) => {
    let currentNode = elem;
    console.log(currentNode.classList);
    console.log(parentClass);
    return currentNode;
  };

  //get active button step number
  const getActiveStep = (elem) => {
    return Array.from(DOMstrings.stepsBtns).indexOf(elem);
  };

  //set all steps before clicked (and clicked too) to active
  const setActiveStep = (activeStepNum) => {
    //remove active state from all the state
    removeClasses(DOMstrings.stepsBtns, "js-active");

    //set picked items to active
    DOMstrings.stepsBtns.forEach((elem, index) => {
      if (index <= activeStepNum) {
        elem.classList.add("js-active");
      }
    });
  };

  //get active panel
  const getActivePanel = () => {
    let activePanel;

    DOMstrings.stepFormPanels.forEach((elem) => {
      if (elem.classList.contains("js-active")) {
        activePanel = elem;
      }
    });

    return activePanel;
  };

  //open active panel (and close unactive panels)
  const setActivePanel = (activePanelNum) => {
    const animation = $(DOMstrings.stepFormPanels, "js-active").attr(
      "data-animation"
    );

    //remove active class from all the panels
    removeClasses(DOMstrings.stepFormPanels, "js-active");
    removeClasses(DOMstrings.stepFormPanels, animation);
    removeClasses(DOMstrings.stepFormPanels, "animate__animated");

    //show active panel
    DOMstrings.stepFormPanels.forEach((elem, index) => {
      if (index === activePanelNum) {
        elem.classList.add("js-active");
        // stepFormPanels
        elem.classList.add("animate__animated", animation);

        setTimeout(function () {
          removeClasses(
            DOMstrings.stepFormPanels,
            "animate__animated",
            animation
          );
        }, 1200);

        setFormHeight(elem);
      }
    });
  };

  //set form height equal to current panel height
  const formHeight = (activePanel) => {
    const activePanelHeight = activePanel.offsetHeight;

    DOMstrings.stepsForm.style.height = `${activePanelHeight}px`;
  };

  const setFormHeight = () => {
    const activePanel = getActivePanel();

    formHeight(activePanel);
  };

  //STEPS BAR CLICK FUNCTION
  DOMstrings.stepsBar.addEventListener("click", (e) => {
    //check if click target is a step button
    const eventTarget = e.target;

    if (!eventTarget.classList.contains(`${DOMstrings.stepsBtnClass}`)) {
      return;
    }

    //get active button step number
    const activeStep = getActiveStep(eventTarget);

    //set all steps before clicked (and clicked too) to active
    setActiveStep(activeStep);

    //open active panel
    setActivePanel(activeStep);
  });

  //PREV/NEXT BTNS CLICK
  DOMstrings.stepsForm.addEventListener("click", (e) => {
    const eventTarget = e.target;

    //check if we clicked on `PREV` or NEXT` buttons
    if (
      !(
        eventTarget.classList.contains(`${DOMstrings.stepPrevBtnClass}`) ||
        eventTarget.classList.contains(`${DOMstrings.stepNextBtnClass}`)
      )
    ) {
      return;
    }

    //find active panel
    const activePanel = findParent(
      eventTarget,
      `${DOMstrings.stepFormPanelClass}`
    );

    let activePanelNum = Array.from(DOMstrings.stepFormPanels).indexOf(
      activePanel
    );

    //set active step and active panel onclick
    if (eventTarget.classList.contains(`${DOMstrings.stepPrevBtnClass}`)) {
      activePanelNum--;
    } else {
      activePanelNum++;
    }

    setActiveStep(activePanelNum);
    setActivePanel(activePanelNum);
  });

  //SETTING PROPER FORM HEIGHT ONLOAD
  window.addEventListener("load", setFormHeight, true);

  //SETTING PROPER FORM HEIGHT ONRESIZE
  window.addEventListener("resize", setFormHeight, true);
}

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
