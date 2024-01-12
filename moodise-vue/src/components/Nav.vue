<template>
  <div>
    <b-navbar class="p-0 m-0" toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand class="pl-3" href="#">Moodise</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto align-items-center">
          <b-button id="nav-button" href="#">About</b-button>
          <b-button id="nav-button" href="#">Business</b-button>
          <b-nav-item-dropdown id="nav-button" class="p-0 pr-3 pl-3ƒ" right no-caret>
            <template #button-content>
              <img class="avatar" src="./../assets/white_user.png" /></template>

            <b-dropdown-item v-if="authUser" class="text-center" :href="`/profile/${authUser.id}`">Profile</b-dropdown-item>
            <b-dropdown-item class="text-center" href="/users">Friends</b-dropdown-item>
            <b-dropdown-item class="text-center" @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from "vuex"


export default {
  data() {
    return {
    }
  },
  computed: mapGetters(['authUser']),
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    }
  },
  mounted() {
  }
}
</script>

