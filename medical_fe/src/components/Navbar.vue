<script>
export default {
  name: "Navbar",
  props: {
    title: String,
  },
};
</script>

<template>
  <nav class="shadow-sm bg-white rounded">
    <img class="logo" src="../assets/images/Logo.svg" alt="" />
    <div class="bottom-nav mt-3 me-5">
      <ul class="nav_links">
        <li><router-link :to="{ name: 'home' }" href="">HOME</router-link></li>
        <li><a href="">ABOUT US</a></li>
        <li><a href="">SERVICES</a></li>
        <li><router-link :to="{ name: 'doctors' }">DOCTORS</router-link></li>
        <li><a href="">CONTACT US</a></li>
      </ul>
    </div>
    <p></p>
  </nav>
</template>

<style scoped>
li,
a {
  color: #1779c9;
  font-size: 24px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  text-decoration: none;
  list-style: none;
}

nav {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 20px 10px;
  border-bottom: 2px solid #c4c4c4;
}

.bottom-nav {
  vertical-align: middle;
}

.nav_links li {
  display: inline-block;
  padding: 0px 10px;
}

.nav_links li a {
  transition: all 0.3s ease 0s;
}

.nav_links li a:hover {
  color: #0088a9;
}

.logo {
  max-width: 10%;
}
</style>
