import "@mdi/font/css/materialdesignicons.css";
import Vue from "vue";
import Router from "vue-router";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import colors from "vuetify/es5/util/colors";
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
  vuetify: new Vuetify({
    theme: {
      dark: true,
      options: { customProperties: true },
      themes: {
        light: {
          blue1: colors.lightBlue.darken1,
          blue2: colors.lightBlue.lighten1
        },
        dark: {
          blue1: colors.lightBlue.darken1,
          blue2: colors.lightBlue.darken2
        }
      }
    }
  }),
  render: h => h(App)
}).$mount("#app");
