import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/main.css";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import { setupCalendar } from "v-calendar";
import vClickOutside from "click-outside-vue3";

const app = createApp(App);

app.use(router);
app.use(vClickOutside);

app.use(setupCalendar, {});

app.mount("#app");
