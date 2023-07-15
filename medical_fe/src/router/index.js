import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import AppointmentDetails from "../views/AppointmentDetails.vue";
import DoctorsHomePage from "../views/DoctorsHomePage.vue";
import ListOfPatient from "../views/ListOfPatient.vue";
import DoctorRegisterPage from "../views/DoctorRegisterPage.vue";
import SuccessPage from "../views/SuccessPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },
    {
      path: "/register",
      name: "appointment",
      component: AppointmentDetails,
    },
    {
      path: "/doctors",
      name: "doctors",
      component: DoctorsHomePage,
    },
    {
      path: "/patients",
      name: "patients",
      component: ListOfPatient,
    },
    {
      path: "/doctors/register",
      name: "doctors-register",
      component: DoctorRegisterPage,
    },
    {
      path: "/success/",
      name: "success",
      component: SuccessPage,
    },
  ],
});

export default router;
