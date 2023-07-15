<template>
  <Navbar />

  <body>
    <div class="body-container">
      <div class="login-container col-lg-3">
        <div
          class="card p-3 pt-4 w-auto mb-3"
          style="
            min-height: 400px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.6);
          "
        >
          <div class="card-body d-flex flex-column align-items-center">
            <p class="fs-4 fw-bold text-primary">Appointment Successful!</p>
            <img src="../assets/images/checked 1.svg" alt="" />
            <hr />
            <div class="fs-5 fw-bold mb-3">Thank you for choosing us</div>
            <div class="first-line">
              Your conference link will be sent to your declered email account.
              Open your link
            </div>
            <div class="second-line mb-3">
              on the scheduled date. See you there!
            </div>
            <button class="btn btn-primary">Make another appointment</button>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { ref } from "vue";

export default {
  name: "SuccessPage",
  props: {
    title: String,
    color: String,
  },
  components: {
    Navbar,
  },
  setup() {},
};
</script>

<style scoped>
a {
  line-height: normal;
  text-decoration: none;
  list-style: none;
  color: black;
}
.first-line {
  text-align: left;
}

.second-line {
  display: inline-block;
  text-align: center;
}
</style>
