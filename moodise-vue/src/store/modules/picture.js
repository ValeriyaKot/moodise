import axios from 'axios'

export default {
    state: {
        pictures: []
    },
    getters: {
        allPictures(state) {
            return state.pictures
        } 
    },
    actions: {
        getPictures({commit}) {
                    axios.get('http://localhost:8000/pictures/')
                        .then(response => {
                            commit('setPictures', response.data)
                    })   
                },
        // createPost({commit},payload) {
        //             axios.post('http://localhost:8000/boards/', payload);
        //             commit('addPost', payload);
        //          },
    },
    mutations: {
        setPictures(state, pictures) {
                    state.pictures = pictures
                },
        // addPost(state, newPost) {
        //     state.posts.push(newPost)
        // }
    },
}