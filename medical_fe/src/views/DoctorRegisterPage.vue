<template>
  <Navbar />

  <body>
    <div class="body-container">
      <div class="login-container col-lg-3">
        <div
          class="card p-3 pt-4 w-auto"
          style="
            min-height: 400px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.6);
          "
        >
          <div class="card-body">
            <form @submit.prevent="submitForm">
              <p class="text-primary fs-5 fw-bold mb-0">Get Started!</p>
              <div class="form-group mb-3">
                <label>First Name</label>
                <input
                  type="text"
                  name=""
                  id=""
                  placeholder="First Name"
                  class="form-control"
                  v-model="formData.first_name"
                />
              </div>
              <div class="form-group mb-3">
                <label for="address">Last Name</label>

                <input
                  type="text"
                  name=""
                  id=""
                  placeholder="Last Name"
                  class="form-control"
                  v-model="formData.last_name"
                />
              </div>
              <div class="form-group mb-3">
                <label>Email</label>
                <input
                  type="email"
                  name=""
                  id=""
                  placeholder="Email"
                  class="form-control"
                  v-model="formData.email"
                />
              </div>
              <div class="form-group">
                <select
                  class="form-select"
                  aria-label=".form-select-sm example"
                  v-model="formData.doctor_type"
                >
                  <option selected>Type of doctor</option>
                  <option value="Cardiologist">Cardiologist</option>
                  <option value="Neurologist">Neurologist</option>
                  <option value="Radiologist">Radiologist</option>
                  <option value="Surgeon">Surgeon</option>
                  <option value="Pediatrician">Pediatrician</option>
                  <option value="Dermatologist">Dermatologist</option>
                </select>
              </div>
              <div class="form-group mb-3">
                <label for="address">Mobile Number</label>

                <input
                  type="text"
                  name=""
                  id=""
                  placeholder="Mobile Number"
                  class="form-control"
                  v-model="formData.mobile_number"
                />
              </div>
              <div class="form-group mb-3">
                <label for="address">Password</label>
                <input
                  type="password"
                  name=""
                  id=""
                  placeholder="Enter your password"
                  class="form-control"
                  v-model="formData.password1"
                />
              </div>
              <div class="form-group mb-3">
                <label for="address">Repeat Password</label>
                <input
                  type="password"
                  name=""
                  id=""
                  placeholder="Repeat your password"
                  class="form-control"
                  v-model="formData.password2"
                />
              </div>

              <button
                class="btn btn-primary mx-auto mt-3 mb-4"
                style="display: block; min-width: 250px"
              >
                Register
              </button>

              <span class="me-1">Already have an Account?</span>
              <router-link :to="{ name: 'doctors' }" class="link-primary"
                >Sign-in here
              </router-link>
            </form>
          </div>
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
</style>

<script>
import Navbar from "../components/Navbar.vue";
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  name: "DoctorRegisterPage",
  props: {
    title: String,
    color: String,
  },
  components: {
    Navbar,
  },

  setup() {
    const formData = ref({
      first_name: "",
      last_name: "",
      email: "",
      doctor_type: "Type of doctor",
      mobile_number: "",
      password1: "",
      password2: "",
    });
    const router = useRouter();

    const submitForm = async () => {
      console.log(formData.value);

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/v1/doctor-register/",
          {
            first_name: formData.value.first_name,
            last_name: formData.value.last_name,
            email: formData.value.email,
            mobile_number: formData.value.mobile_number,
            password: formData.value.password1,
            doctor_type: formData.value.doctor_type,
          }
        );

        console.log("Form data sent: ", response.data);
        router.push("/doctors/");
      } catch (error) {
        console.log(error);
      }
    };

    return {
      formData,
      submitForm,
    };
  },
};
</script>
