import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/chart.js'

import { createStore } from 'vuex'

const store = createStore({
    state () {
      return {
        account: {
            username : "",
            jwtToken : ""
        }
      }
    },
    mutations: {
      set_user (state, account) {
        state.user_account.set(account);
      }
    }
  })

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
