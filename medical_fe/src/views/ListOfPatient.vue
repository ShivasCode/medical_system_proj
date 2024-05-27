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
              <th scope="col">Date of Consultation</th>
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
    <button v-if="!patient.appointment[0].approved" class="btn btn-success me-2" @click="appointment_approval(patient.appointment[0].id)">
        Approve
    </button>
    <button v-if="!patient.appointment[0].approved" class="btn btn-danger me-2" @click="appointment_disapproval(patient.appointment[0].id)">
        Disapprove
    </button>
    <button class="btn btn-primary" @click="view_appointment(patient.appointment[0].id)">
        View
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
import AppointmentRetrieve from "../components/AppointmentRetrieve.vue";

import { useRouter } from "vue-router";

export default {
  name: "DoctorPatients",
  components: {
    Sidebar,
    SimpleNavbar,
    AppointmentRetrieve
  },
  setup() {
    const patients = ref([]);
    const token = localStorage.getItem("token");
    const router = useRouter();
    const appointment = ref(null);

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
    const view_appointment = (appointmentId) => {
      router.push({ 
        name: "AppointmentRetrieve", 
        params: { id: appointmentId }
      });
    };

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
    const appointment_approval = async (id) => {
        try {
            const response = await axios.post(
                `http://127.0.0.1:8000/api/v1/appointment-approval/${id}/`,
                null,
                {
                    headers: {
                        Authorization: `Token ${token}`,
                    },
                }
            ).then((response) => {
          location.reload();
        });
        } catch (error) {
            console.error(error);
        }
    };
    return { patients, appointment_disapproval,appointment_approval,view_appointment,appointment  };
  },
};
</script>

<style scoped>
.table-row > th {
  background-color: rgba(23, 121, 201, 1);
  color: rgba(255, 255, 255, 1);
}
</style>
