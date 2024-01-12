import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login'
import Home from './views/Home'
import Profile from './views/Profile'
import Users from './views/Users'
import Registration from './views/Registration'
import resetPassword from './views/ResetPassword'





Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/login',
            component: Login
        },
        {
            path: '/',
            component: Home
        },
        {
            path: '/profile/:userId',
            component: Profile
        },
        {
            path: '/users',
            component: Users
        },
        {
            path: '/registration',
            component: Registration
        },
        {
            path: '/reset-password',
            component: resetPassword
        },
    ]
})