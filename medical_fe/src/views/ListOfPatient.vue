<template>
  <div class="main-container d-flex">
    <Sidebar />
    <div class="content">
      <SimpleNavbar />
      <div class="container p-5">
        <h5 class="primary-text-color fw-bold">List of Patients</h5>
        <table class="table">
          <thead class="border table-borderless">
            <tr class="table-row">
              <th scope="col">Patient Name</th>
              <th scope="col">Date Consulted</th>
              <th></th>
            </tr>
          </thead>
          <tbody class="border table-borderless">
            <tr v-for="patient in patients">
              <td>
                {{ patient.appointment[0].user.first_name }}
                {{ patient.appointment[0].user.last_name }}
              </td>
              <td>
                {{ patient.appointment[0].date }} /
                {{ patient.appointment[0].start_time }} -
                {{ patient.appointment[0].end_time }}
              </td>
              <td>
                <button
                  class="btn btn-primary"
                  @click="appointment_disapproval(patient.appointment[0].id)"
                >
                  Disapprove
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";
import Sidebar from "../components/Sidebar.vue";
import SimpleNavbar from "../components/SimpleNavbar.vue";

export default {
  name: "DoctorPatients",
  components: {
    Sidebar,
    SimpleNavbar,
  },
  setup() {
    const patients = ref([]);
    const token = localStorage.getItem("token");

    onMounted(async () => {
      try {
        console.log(token);
        const response = await axios.get(
          "http://127.0.0.1:8000/api/v1/doctors/patients/",
          {
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );
        console.log(response.data);
        patients.value = response.data;
      } catch (error) {
        console.error(error);
      }
    });

    const appointment_disapproval = async (id) => {
      const response = await axios
        .post(`http://127.0.0.1:8000/api/v1/appointment-disapproval/${id}/`, {
          headers: {
            Authorization: `Token ${token}`,
          },
        })
        .then((response) => {
          location.reload();
        });

      console.log(response.data);
    };

    return { patients, appointment_disapproval };
  },
};
</script>

<style scoped>
.table-row > th {
  background-color: rgba(23, 121, 201, 1);
  color: rgba(255, 255, 255, 1);
}
</style>
