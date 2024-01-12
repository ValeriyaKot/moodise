import Vuex from 'vuex'
import Vue from 'vue'
import post from './modules/post'
import picture from './modules/picture'
import user from './modules/user'



Vue.use(Vuex);

export default new Vuex.Store({
  
    modules: {
        post,
        picture,
        user
    }
})