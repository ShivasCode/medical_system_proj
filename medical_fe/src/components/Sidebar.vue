<script>
export default {
  name: "Sidebar",
  props: {
    title: String,
  },
};
</script>

<template>
  <div class="sidebar" id="side_nav">
    <div
      class="sidebar-content d-flex flex-column align-items-center text-color-white"
    >
      <img
        class="profile-image mb-3"
        src="../assets/images/jenny no bg.jpg"
        alt=""
      />
      <p class="fs-5 fw-bold mb-0">Linda Mercado</p>
      <p class="fs-6">Cardiologist</p>
      <div class="d-flex flex-column align-items-center fs-6 gap-4">
        <a href="">MDR</a>
        <a href="">Schedule</a>
        <a href="">Appointment</a>
        <a href="">Prescription</a>
        <a href="">Settings</a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-image {
  border-radius: 50%;
}

div > a {
  list-style: none;
  color: white;
  text-decoration: none;
}

div > a:hover {
  text-decoration: underline;
}
</style>
