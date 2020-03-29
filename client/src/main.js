import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';
import vuetify from './plugins/vuetify';

import VueSocketio from 'vue-socket.io';



// Vue.use(VueSocketio, `//${window.location.host}`, store);
Vue.use(new VueSocketio({
  debug: true,
  connection: `//${window.location.host}`,
  vuex: {
      store,
      actionPrefix: 'socket_',
      mutationPrefix: 'socket_'
  }
}))

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
