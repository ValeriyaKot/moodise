import axios from 'axios'

export default {
    state: {
        posts: []
    },
    getters: {
        validPosts(state){
            return state.posts.filter(p=> {
                return p.title && p.body
            })
        },
        allPosts(state) {
            return state.posts
        } 
    },
    actions: {
        getPosts({commit}, limit=3) {
                    axios.get('https://jsonplaceholder.typicode.com/posts?_limit=' + limit)
                        .then(response => {
                            commit('SET_POSTS', response.data)
                    })   
                },
        createPost({commit},payload) {
                    axios.post('http://localhost:8000/boards/', payload);
                    commit('addPost', payload);
                 },
    },
    mutations: {
        SET_POSTS(state, posts) {
                    state.posts = posts
                },
        addPost(state, newPost) {
            state.posts.push(newPost)
        }
    },
}