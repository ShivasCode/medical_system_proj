<script>
import Navbar from "../components/Navbar.vue";

export default {
  name: "HomePage",
  props: {
    title: String,
    color: String,
  },
  components: {
    Navbar,
  },
};
</script>

<template>
  <Navbar />

  <body>
    <div class="body-container">
      <div class="patient-container d-flex flex-column align-items-center">
        <h2 class="text-container fw-bolder mb-5">
          <div class="first-line">We would like to know few</div>
          <div class="second-line">details about you!</div>
        </h2>
        <div class="patient-type-card shadow p-3 mb-5 bg-body-tertiary rounded">
          <h2 class="patient-type-name mt-3 fw-bolder primary-text-color">
            Patient type
          </h2>
          <div class="patient-type-logo">
            <div class="">
              <router-link :to="{ name: 'appointment' }">
                <img src="../assets/images/Checked Icon.svg" alt="" />
                <br />
                New <br />patient
              </router-link>
            </div>

            <div>
              <img src="../assets/images/Group 102.svg" alt="" />
              <p>Returning <br />patient</p>
            </div>
          </div>
          <button
            type="button"
            class="btn btn-primary btn-lg mx-auto mt-5"
            style="display: block; min-width: 250px"
          >
            Continue
          </button>
        </div>
      </div>
    </div>
  </body>
</template>

<style scoped>
a {
  line-height: normal;
  text-decoration: none;
  list-style: none;
  color: black;
}

.text-container {
  text-align: center;
}

.first-line {
  text-align: left;
}

.second-line {
  display: inline-block;
  text-align: center;
}
</style>
