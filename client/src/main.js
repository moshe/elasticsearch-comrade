import "@mdi/font/css/materialdesignicons.css";
import Vue from "vue";
import Router from "vue-router";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import colors from "vuetify/lib/util/colors";
import "../public/materialdesignicons.css";
// import "./plugins/vuetify";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import "./style/global.css";
import "./style/smallTable.css";
Vue.use(Vuetify);

Vue.use(Router);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify: new Vuetify({
    theme: {
      dark: true,
      options: { customProperties: true },
      themes: {
        light: {
          "bg-color": "#e9e9e9"
        },
        dark: {
          "bg-color": "#595959",
          accent: colors.blueGrey
        }
      }
    }
  }),
  render: h => h(App)
}).$mount("#app");
