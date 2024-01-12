import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import GSignInButton from 'vue-google-signin-button'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import '../scss/custom.scss'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(GSignInButton)

Vue.prototype.$http = axios;
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store,
}).$mount('#app')
