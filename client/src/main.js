import Vue from "vue";
import Router from "vue-router";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
// import "./plugins/vuetify";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import "./style/smallTable.css";

Vue.use(Vuetify);

Vue.use(Router);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify: new Vuetify({ theme: { dark: true } }),
  render: h => h(App)
}).$mount("#app");
