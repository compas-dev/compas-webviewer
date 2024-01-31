/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from "@/plugins";

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

// /* import the fontawesome core */
// import { library } from "@fortawesome/fontawesome-svg-core";

// /* import font awesome icon component */
// import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// // import { faLinkedin, faYoutube, faInstagram } from "@fortawesome/free-brands-svg-icons";
// import { faArrowUpRightFromSquare } from "@fortawesome/pro-regular-svg-icons/faArrowUpRightFromSquare";
// import { faChevronDown } from "@fortawesome/pro-regular-svg-icons/faChevronDown";

// /* add icons to the library */
// library.add(faArrowUpRightFromSquare, faChevronDown);

// Store
import store from "./stores";

const app = createApp(App);

registerPlugins(app);

app.use(store);
// app.component("font-awesome-icon", FontAwesomeIcon);
app.mount("#app");
