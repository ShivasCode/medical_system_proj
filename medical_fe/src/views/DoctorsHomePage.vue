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
          <div class="card-body">
            <form @submit.prevent="submitForm">
              <p class="text-primary fs-5 fw-bold mb-0">Welcome!</p>
              <p class="fs-6 mb-4">Enter your email and password to log in</p>
              <div class="form-group mb-3">
                <input
                  type="email"
                  name=""
                  id=""
                  placeholder="email@gmail.com"
                  class="form-control"
                  v-model="formData.email"
                />
              </div>
              <div class="form-group mb-3">
                <input
                  type="password"
                  name=""
                  id=""
                  placeholder="Enter your password"
                  class="form-control"
                  v-model="formData.password"
                />
              </div>
              <a href="" class="link-primary">Forgot your password?</a>

              <button
                class="btn btn-primary mx-auto mt-4"
                style="display: block; min-width: 250px"
              >
                Sign in
              </button>
            </form>
          </div>
        </div>
        <div class="">
          <p class="text-center text-primary">Don't have an account?</p>
          <router-link :to="{ name: 'doctors-register' }">
            <button
              class="btn btn-outline-primary mx-auto mt-4"
              style="display: block; min-width: 250px"
            >
              Sign up
            </button>
          </router-link>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  name: "HomePage",
  props: {
    title: String,
    color: String,
  },
  components: {
    Navbar,
  },
  setup() {
    const formData = ref({
      email: "",
      password: "",
    });
    const router = useRouter();

    const submitForm = async () => {
      console.log(formData.value);

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api-auth/token/login/",
          {
            email: formData.value.email,
            password: formData.value.password,
          }
        );

        console.log("Form data sent: ", response.data);
        localStorage.setItem("token", response.data.auth_token); // Store the token in local storage
        router.push("/patients/");
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

<style scoped>
a {
  line-height: normal;
  text-decoration: none;
  list-style: none;
  color: black;
}
</style>
