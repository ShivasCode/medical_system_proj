<template>
  <div class="container">
    
    <div v-if="appointment" class="appointment-details">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Appointment Details</h5>
          <div class="details">
            <div class="detail">
              <label>Patient Name:</label>
              <div class="text-box">{{ appointment['user'].first_name }} {{ appointment['user'].last_name }}</div>
            </div>
            <div class="detail">
              <label>Email:</label>
              <div class="text-box">{{ appointment['user'].email }}</div>
            </div>
            <div class="detail">
              <label>Date of Consultation:</label>
              <div class="text-box">{{ appointment.date }}</div>
            </div>
            <div class="detail">
              <label>Start Time:</label>
              <div class="text-box">{{ appointment.start_time }}</div>
            </div>
            <div class="detail">
              <label>End Time:</label>
              <div class="text-box">{{ appointment.end_time}}</div>
            </div>
            <div class="detail">
              <label>Primary Symptoms:</label>
              <div class="text-box">{{ appointment['pre_assessment'].primary_symptoms }}</div>
            </div>
            <div class="detail">
              <label>Current Medical or Past Medical Conditions:</label>
              <div class="text-box">{{ appointment['pre_assessment'].current_medical_or_past_medical }}</div>
            </div>
            <div class="detail">
              <label>Drinks Alcohol:</label>
              <div class="text-box">{{ appointment['pre_assessment'].drink_alcohol }}</div>
            </div>
            <div class="detail">
              <label>Current Medications:</label>
              <div class="text-box">{{ appointment['pre_assessment'].current_medications }}</div>
            </div>
            <div class="detail">
              <label>Smoker:</label>
              <div class="text-box">{{ appointment['pre_assessment'].smoker }}</div>
            </div>
          </div>
        </div>
        
      </div>
      <div class="back-button">
      <button class="btn btn-primary mt-2" @click="goBack">Back to List of Patients</button>
    </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "AppointmentRetrieve",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const appointment = ref(null);
    const router = useRouter();

    onMounted(async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/appointments/${props.id}`);
        appointment.value = response.data;
      } catch (error) {
        console.error("Error fetching appointment details:", error);
      }
    });

    const goBack = () => {
      router.push("/patients");
    };

    return { appointment, goBack };
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.back-button {
  margin-bottom: 20px;
}

.card {
  width: 70%;
 width: 800px;
  margin-top: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.details {
  display: flex;
  flex-direction: column;
}

.detail {
  margin-bottom: 10px;
}

label {
  font-weight: bold;
}

.text-box {
  border-bottom: 1px solid #ccc;
  padding: 5px;
}
</style>
