import axios from 'axios'

export default {
    state: {
        users: [],
        status: '',
        token: localStorage.getItem('token') || '',
        authUser: JSON.parse(localStorage.getItem('user')),
        userInfo: []
    },
    getters: {
        allUsers(state) {
            return state.users
        },
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
        userInfo(state) {
            return state.userInfo
        },
        authUser(state) {
            return state.authUser
        },

    },
    actions: {
        getUsers({ commit }) {
            axios.get('http://localhost:8000/users/')
                .then(response => {
                    commit('setUsers', response.data)
                })
        },
        getUserInfo({ commit }, userId) {
            axios.get(`http://localhost:8000/users/${userId}/`)
                .then(response => {
                    commit('setUserInfo', response.data)
                })
        },
        login({ commit }, form) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios.post('http://localhost:8000/auth/login/', form)
                    .then(resp => {
                        const token = `Bearer ${resp.data.auth_token.access}`
                        const user = resp.data
                        localStorage.setItem('token', token)
                        localStorage.setItem('username', user.username)
                        localStorage.setItem('user', JSON.stringify(user))

                        axios.defaults.headers.common['Authorization'] = token
                        commit('authSuccess', resp.data)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        loginGoogle({ commit }, token) {
            return new Promise((resolve, reject) => {
                axios.post('http://localhost:8000/google/', {
                    access_token: token,
                })
                    .then(resp => {
                        const user = resp.data.user
                        localStorage.setItem('token', token)
                        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
                        commit('authSuccess', token, user)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        logout({ commit }) {
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        },
        register({ commit }, form) {
                axios.post('http://localhost:8000/auth/register/', form)
                    .then(resp => {
                        const token = `Bearer ${resp.data.auth_token.access}`
                        const user = resp.data
                        localStorage.setItem('token', token)
                        localStorage.setItem('username', user.username)
                        localStorage.setItem('user', JSON.stringify(user))

                        axios.defaults.headers.common['Authorization'] = token
                        commit('authSuccess', resp.data)
                    })
                    .catch(err => {
                        commit('auth_error')
                        console.log(err)
                        localStorage.removeItem('token')
                    })
        },
        resetPassword({ commit }, form) {
            axios.post('http://localhost:8000/auth/password_change/', form)
                .then(resp => {
                    commit('authSuccess', resp.data)
                })
                .catch(err => {
                    commit('auth_error')
                    console.log(err)
                })
    },
        follow({ commit }, profileId) {

            axios.post(`http://localhost:8000/profile/${profileId}/follow/`)
                .then(resp => {
                    commit('followSuccess', resp.data)
                })
                .catch(error => {
                    console.log(error)
                    commit('followError')
                })
        },
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading'
        },
        authSuccess(state) {
            state.status = 'success'
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        setUsers(state, users) {
            state.users = users
        },
        setUserInfo(state, userInfo) {
            state.userInfo = userInfo
        },
        followSuccess(state) {
            state.status = 'success'
        },
        followError(state) {
            state.status = 'error'
        },

    },
}