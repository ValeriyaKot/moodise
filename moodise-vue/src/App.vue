<template>
  <div id="app">
    <Navbar />
      <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Nav.vue";

export default {
  name: "App",
  components: {
    Navbar
  },

  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn;
    },
  },
  methods: {
    // onGoogleSignInSuccess(resp) {
    //   // console.log(resp)
    //   const token = resp.wc.access_token;
    //   // После успешного входа через Google,
    //   // отправляем токен доступа на бэкэнд и получаем взамен
    //   // пользователя и JWT токен
    //   // P.S. JWT токен в нашем примере не нужен, поэтому его не сохраняем
    //   console.log(token),
    //   axios
    //     .post("http://127.0.0.1:8000/google/", {
    //       access_token: token,
    //     })
    //     .then((resp) => {
    //       this.user = resp.data.user;
    //     })
    //     .catch((err) => {
    //       console.log(err.response);
    //     });
    // },
    // onGoogleSignInError(error) {
    //   console.log("OH NOES", error);
    // },
    // isEmpty(obj) {
    //   return Object.keys(obj).length === 0;
    // },
    // logout: function () {
    //   this.$store.dispatch("logout").then(() => {
    //     this.$router.push("/login");
    //   });
    // },
  },
};
</script>

<style>
</style>
