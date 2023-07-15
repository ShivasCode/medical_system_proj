<template>
  <nav><img class="logo" src="../assets/images/Logo.svg" alt="" /></nav>
  <div :class="{ backdrop: isActiveDoctorCard }"></div>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <div class="main-card card w-auto">
          <div
            class="active-doctor-card except"
            v-show="isActiveDoctorCard === true"
            v-click-outside="onClickOutside"
          >
            <div class="align-items-center mt-3">
              <div
                v-for="schedule in selectedDoctor"
                class="d-flex justify-content-around mb-2"
              >
                <div>
                  <button
                    v-if="!schedule.taken"
                    class="time-button btn btn-sm fw-bold"
                    :class="{
                      'btn-light': !schedule.selected,
                      'btn-warning': schedule.selected,
                    }"
                    @click="selectSchedule(schedule)"
                  >
                    {{ schedule.start_time }} - {{ schedule.end_time }}
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="card-body">
            <form @submit.prevent="submitForm">
              <div v-show="currentStep === 1">
                <h3 class="primary-text-color fw-bold mb-3">
                  Step 1: Choose appointment
                </h3>
                <div class="main-container-date">
                  <div class="container container-date">
                    <DatePicker
                      :min-date="new Date()"
                      @dayclick="testClick"
                      class=""
                      v-model="formData.date"
                    />
                  </div>
                  <div class="container-doctors">
                    <p class="fs-3 fw-bold" style="color: #4c4947">
                      Available Doctors
                    </p>
                    <div class="dropdown mb-3">
                      <p class="fs-5 fw-bold">Specialist</p>
                      <i
                        @click="toggle"
                        v-if="isActive1 == false"
                        class="bi bi-caret-right-fill"
                      ></i>
                      <i
                        @click="toggle"
                        v-if="isActive1"
                        class="bi bi-caret-down-fill"
                      ></i>
                    </div>
                    <div class="container-doctor-lst mb-3" v-if="isActive1">
                      <div
                        v-for="doctor in availableDoctors"
                        :key="doctor.id"
                        class="card doctor-card"
                        @click="toggleDoctorCard($event, doctor)"
                      >
                        <img
                          class="doctor-image"
                          src="../assets/images/jenny.jpg"
                          alt=""
                        />
                        <p class="doctor-name fs-6">
                          {{ doctor.user.first_name }}
                          {{ doctor.user.last_name }}
                        </p>
                        <p class="fs-6">{{ doctor.user.doctor_type }}</p>
                        <p class="fs-6">
                          {{ doctor.user.mobile_number }}
                        </p>
                      </div>
                    </div>
                    <div class="dropdown">
                      <p class="fs-5">Sub-specialist</p>
                      <i
                        @click="toggle2"
                        v-if="isActive2 == false"
                        class="bi bi-caret-right-fill"
                      ></i>
                      <i
                        @click="toggle2"
                        v-if="isActive2"
                        class="bi bi-caret-down-fill"
                      ></i>
                    </div>
                    <div class="container-doctor-lst" v-if="isActive2">
                      <div class="card doctor-card">
                        <img
                          class="doctor-image"
                          src="../assets/images/jenny.jpg"
                          alt=""
                        />
                        <p class="doctor-name fs-5">Jenny mercado</p>
                        <p class="fs-6">Cardiologist</p>
                        <p class="fs-6">+63 9152 345 895</p>
                      </div>
                      <div class="card doctor-card">
                        <img
                          class="doctor-image"
                          src="../assets/images/jenny.jpg"
                          alt=""
                        />
                        <p class="doctor-name fs-5">Jenny mercado</p>
                        <p class="fs-6">Cardiologist</p>
                        <p class="fs-6">+63 9152 345 895</p>
                      </div>
                      <div class="card doctor-card">
                        <img
                          class="doctor-image"
                          src="../assets/images/jenny.jpg"
                          alt=""
                        />
                        <p class="doctor-name fs-5">Jenny mercado</p>
                        <p class="fs-6">Cardiologist</p>
                        <p class="fs-6">+63 9152 345 895</p>
                      </div>
                      <div class="card doctor-card">
                        <img
                          class="doctor-image"
                          src="../assets/images/jenny.jpg"
                          alt=""
                        />
                        <p class="doctor-name fs-5">Jenny mercado</p>
                        <p class="fs-6">Cardiologist</p>
                        <p class="fs-6">+63 9152 345 895</p>
                      </div>
                    </div>
                  </div>
                </div>
                <button type="button" class="btn btn-primary" @click="nextStep">
                  Next
                </button>
              </div>
              <div v-show="currentStep === 2">
                <h3 class="primary-text-color fw-bold">
                  Step 2: Pre-Assessment
                </h3>
                <div class="mb-3">
                  <label for="name">Primary Symptoms</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="formData.primary_symptoms"
                  />
                </div>
                <div class="mb-3">
                  <label
                    >Current Medical Condition Being Treated/Past Medical
                    Condition</label
                  >
                  <input
                    type="text"
                    class="form-control"
                    v-model="formData.current_medical_condition"
                  />
                </div>
                <div class="mb-3">
                  <label for="name">Allergies </label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="formData.allergies"
                  />
                </div>
                <div class="mb-3">
                  <label
                    >How often do you have a drink containing alcohol</label
                  >
                  <input
                    type="text"
                    class="form-control"
                    v-model="formData.drink_alcohol"
                  />
                </div>
                <div class="mb-3">
                  <label>Current medications</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="formData.current_medications"
                  />
                </div>

                <div class="mb-3">
                  <label for="">Are you a smoker</label>
                  <label>
                    <input
                      type="radio"
                      name="choice-radio"
                      v-model="formData.smoker"
                      value="True"
                    />
                    Yes
                  </label>
                  <label>
                    <input
                      type="radio"
                      name="choice-radio"
                      v-model="formData.smoker"
                      value="False"
                    />
                    No
                  </label>
                </div>
                <button
                  type="button"
                  class="btn btn-primary me-2"
                  @click="previousStep"
                >
                  Previous
                </button>
                <button
                  type="button"
                  class="btn btn-primary"
                  @click="validateStep2"
                >
                  Next
                </button>
              </div>
              <div v-show="currentStep === 3">
                <h3 class="primary-text-color fw-bold">
                  Step 3: Basic Details
                </h3>
                <div class="mb-3">
                  <label for="address">Last Name</label>
                  <input
                    type="text"
                    class="form-control"
                    id="address"
                    v-model="formData.last_name"
                  />
                </div>
                <div class="mb-3">
                  <label for="address">First Name</label>
                  <input
                    type="text"
                    class="form-control"
                    id="address"
                    v-model="formData.first_name"
                  />
                </div>
                <div class="mb-3">
                  <label for="city">Middle Name</label>
                  <input
                    type="text"
                    class="form-control"
                    id="city"
                    v-model="formData.middle_name"
                  />
                  <div class="mb-3">
                    <label for="address">Date of Birth</label>
                    <input
                      type="text"
                      class="form-control"
                      id="address"
                      v-model="formData.date_of_birth"
                    />
                  </div>
                  <div class="mb-3">
                    <label for="address">Person with Disability</label>
                    <input
                      type="checkbox"
                      id="address"
                      class="form-check-input"
                      v-model="formData.person_with_disability"
                    />
                  </div>
                  <div class="mb-3">
                    <h3>Address</h3>
                    <label for="address">Address</label>
                    <input
                      type="text"
                      class="form-control"
                      id="address"
                      v-model="formData.address"
                    />
                  </div>
                  <div class="mb-3">
                    <h3>Contact Details</h3>
                    <label for="address">Mobile Number</label>
                    <input
                      type="text"
                      class="form-control"
                      id="address"
                      v-model="formData.mobile_number"
                    />
                  </div>
                  <div class="mb-3">
                    <h3>Anthropometry</h3>
                    <label for="address">Weight</label>
                    <input
                      type="text"
                      class="form-control"
                      id="address"
                      v-model="formData.weight"
                    />
                    <label for="address">Height</label>
                    <input
                      type="text"
                      class="form-control"
                      id="address"
                      v-model="formData.height"
                    />
                  </div>
                  <div class="mb-3">
                    <label for="address">Email Address</label>
                    <input
                      type="email"
                      class="form-control"
                      id="address"
                      v-model="formData.email"
                    />
                  </div>
                </div>
                <button
                  type="button"
                  class="btn btn-primary me-3"
                  @click="previousStep"
                >
                  Previous
                </button>
                <button
                  type="button"
                  class="btn btn-primary"
                  @click="validateStep3"
                >
                  Next
                </button>
              </div>
              <div v-show="currentStep === 4">
                <h3 class="primary-text-color fw-bold">Step 4: Payment</h3>
                <hr />
                <div class="payment-container mb-5">
                  <div class="d-flex align-items-center">
                    <img src="../assets/images/jenny no bg.jpg" alt="" />
                    <div>
                      <h5 class="fw-bold primary-text-color">Jenny mercado</h5>
                      <h6>Dentistry</h6>
                    </div>
                  </div>
                  <div>
                    <h5 class="fw-bold primary-text-color">
                      Appoinment Schedule
                    </h5>
                    <h6>
                      <span class="fw-bold primary-text-color">Date:</span>
                      January 10,2021
                    </h6>
                    <h6>
                      <span class="fw-bold primary-text-color">Time:</span> 10:
                      am - 11:00am
                    </h6>
                  </div>
                  <div>
                    <h5 class="fw-bold primary-text-color">Consulation Fee</h5>
                    <h6 class="fw-bold">Php 1,200</h6>
                  </div>
                </div>
                <div class="payment-container-2">
                  <p class="">
                    Select option to pay:<span class="fw-bold"> Php 1,200</span>
                  </p>
                  <div class="d-flex w-50 justify-content-around px-5">
                    <div class="form-check">
                      <input
                        class="form-check-input"
                        type="radio"
                        id="walk-in"
                        value="walk-in"
                        v-model="selectedOption"
                        name="mode"
                      />
                      <label class="form-check-label" for="walk-in"
                        >Walk-in</label
                      >
                    </div>
                    <div class="form-check">
                      <input
                        class="form-check-input"
                        type="radio"
                        id="pay-online"
                        value="pay-online"
                        v-model="selectedOption"
                        name="mode"
                      />
                      <label class="form-check-label" for="pay-online"
                        >Pay now</label
                      >
                    </div>
                  </div>
                  <button class="btn btn-primary mt-3">Submit</button>
                </div>
                <button
                  type="button"
                  class="btn btn-primary me-3"
                  @click="previousStep"
                >
                  Previous
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { Calendar, DatePicker } from "v-calendar";
import "v-calendar/style.css";
import axios from "axios";
import { vClickOutside } from "click-outside-vue3";
import { useRouter } from "vue-router";

export default {
  name: "MultistepForm",
  data() {
    return {
      availableDoctors: [],
    };
  },
  components: {
    Calendar,
    DatePicker,
  },

  setup() {
    const availableDoctors = ref([]);
    const isActive1 = ref(false);
    const isActive2 = ref(false);
    const isActiveDoctorCard = ref(false);
    const selectedDoctor = ref([]);

    const isActivePayment = ref(false);
    const selectedOption = ref(null);
    const currentStep = ref(1);
    const formData = ref({
      last_name: "",
      first_name: "",
      middle_name: "",
      date_of_birth: "",
      person_with_disability: null,
      address: "",
      mobile_number: "",
      weight: "",
      height: "",
      email: "",
      address: "",
      city: "",
      primary_symptoms: "",
      current_medical_condition: "",
      allergies: "",
      drink_alcohol: "",
      current_medications: "",
      smoker: "",
      start_time: "",
      end_time: "",
      weekday: "",
      date: "",
      schedule_id: "",
    });

    const nextStep = () => {
      currentStep.value++;
    };

    const previousStep = () => {
      currentStep.value--;
    };

    const validateStep2 = () => {
      if (
        true
        // formData.value.primary_symptoms &&
        // formData.value.current_medical_condition &&
        // formData.value.allergies &&
        // formData.value.drink_alcohol &&
        // formData.value.current_medications &&
        // formData.value.smoker
      ) {
        nextStep();
      } else {
        alert("Please fill in all required fields.");
      }
    };

    const validateStep3 = () => {
      if (
        true
        // formData.value.last_name &&
        // formData.value.first_name &&
        // formData.value.middle_name &&
        // formData.value.date_of_birth &&
        // formData.value.person_with_disability &&
        // formData.value.address &&
        // formData.value.mobile_number &&
        // formData.value.weight &&
        // formData.value.height &&
        // formData.value.email_address
      ) {
        nextStep();
      } else {
        alert("Please fill in all required fields.");
      }
    };

    const toggle = () => {
      isActive1.value = !isActive1.value;
    };

    const toggle2 = () => {
      isActive2.value = !isActive2.value;
    };

    const toggleDoctorCard = (event, doctor) => {
      event.stopPropagation();
      isActiveDoctorCard.value = !isActiveDoctorCard.value;
      console.log(doctor.schedules);
      selectedDoctor.value = doctor.schedules;

      // try {
      //   const response = await axios.get(

      //   )
      // }
    };

    const onClickOutside = (event) => {
      isActiveDoctorCard.value = false;
      console.log();
    };

    const testClick = async (day) => {
      console.log(day);
      const weekdayno = day.weekday;
      formData.value.weekday = day.weekday;
      formData.value.date = day.id;
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/v1/available-doctors/",
          {
            params: {
              weekday: weekdayno,
            },
          }
        );

        availableDoctors.value = response.data;
        console.log("Available Doctors:", availableDoctors.value);
      } catch (error) {
        console.error("Error:", error);
      }
    };

    const selectSchedule = (schedule) => {
      schedule.selected = !schedule.selected;
      formData.value.start_time = schedule.start_time;
      formData.value.end_time = schedule.end_time;
      formData.value.schedule_id = schedule.id;
    };

    const router = useRouter();

    const submitForm = async () => {
      console.log(formData.value);

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/v1/register/",
          {
            first_name: formData.value.first_name,
            last_name: formData.value.last_name,
            middle_name: formData.value.middle_name,
            date_of_birth: formData.value.date_of_birth,
            person_with_disability: formData.value.person_with_disability,
            address: formData.value.address,
            email: formData.value.email,
            schedule_id: formData.value.schedule_id,
            mobile_number: formData.value.mobile_number,
            weight: formData.value.weight,
            height: formData.value.height,
            address: formData.value.address,
            primary_symptoms: formData.value.primary_symptoms,
            current_medical_condition: formData.value.current_medical_condition,
            allergies: formData.value.allergies,
            drink_alcohol: formData.value.drink_alcohol,
            current_medical_or_past_medical: formData.value.current_medications,
            start_time: formData.value.start_time,
            end_time: formData.value.end_time,
            weekday: formData.value.weekday,
            date: formData.value.date,
          }
        );

        console.log("Form data sent: ", response.data);
        router.push("/success/");
      } catch (error) {
        console.log(error);
      }
    };

    const submitModeValue = () => {
      let data = null;
      if (selectedOption.value == "pay-online") {
        data = selectedOption.value;
      } else if (selectedOption.value == "walk-in") {
        data = selectedOption.value;
      }
      console.log(data);
    };

    return {
      currentStep,
      formData,
      selectedOption,
      nextStep,
      availableDoctors,
      previousStep,
      validateStep2,
      validateStep3,
      submitForm,
      testClick,
      submitModeValue,
      //toggles
      toggle,
      toggle2,
      isActive1,
      isActive2,
      isActiveDoctorCard,
      toggleDoctorCard,
      onClickOutside,
      selectedDoctor,
      selectSchedule,
    };
  },
};
</script>

<style>
.container {
  margin-top: 50px;
}

.container-date {
  display: block;
  text-align: center;
}

.main-card {
  position: relative;
}

input[type="text"],
textarea {
  background-color: #d1d1d1;
}

input[type="email"],
textarea {
  background-color: #d1d1d1;
}

.payment-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.payment-container-2 {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-container-date {
  display: flex;
}

.dropdown {
  width: 300px;
  height: 35px;
  background: #f2f2f2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}

.dropdown > p {
  padding-left: 10px;
  padding-top: 15px;
}

.container-doctor-lst {
  display: grid;
  grid-template-columns: auto auto;
  gap: 20px;
}

.container-doctor-lst > div {
  width: 163px;
  height: 200px;
  background-image: url("../assets/images/Mask 1.svg");
  background-repeat: no-repeat;
  background-color: rgba(23, 121, 201, 1);
  align-items: center;
  justify-content: center;
}

.active-doctor-card {
  width: 350px;
  height: 200px;
  background-color: rgba(23, 121, 201, 1);
  position: absolute;
  left: 20%;
  top: 30%;
  z-index: 100;
  border-radius: 5%;
}

.doctor-card > p {
  color: white;
}

.doctor-image {
  width: 61px;
  height: 61px;
  flex-shrink: 0;
}

.doctor-name {
  font-weight: bold;
}

nav {
  padding: 20px 10px;
  border-bottom: 2px outset rgba(0, 0, 0, 0.2);
}

.logo {
  margin-left: 5%;
  max-width: 10%;
}
.except {
  /* position: relative; */
  z-index: 9999;
}

.backdrop {
  position: fixed;
  z-index: 9998;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: #33333377;
  backdrop-filter: blur(4px);
}

.time-button {
}
</style>
