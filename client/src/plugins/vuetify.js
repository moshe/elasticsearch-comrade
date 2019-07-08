import Vue from "vue";
import colors from "vuetify/es5/util/colors";
import Vuetify from "vuetify/lib";
import "vuetify/src/stylus/app.styl";

Vue.use(Vuetify, { theme: { primary: colors.lightBlue.darken1 } });
