<template>
  <div class="container mt-5 border-bottom border-secondary">
    <div class="row mb-3">
      <div class="col-5 p-0">
        <b-img v-if="userInfo.profile.image" id="userAvatar" :src="userInfo.profile.image" alt="userPicture" right></b-img>
        <b-img v-else id="userAvatar" src="https://i.pinimg.com/564x/23/dc/4c/23dc4c3bbe714124713bfe6eeed6346a.jpg" alt="userPicture" right></b-img>
      </div>
      <div class="col-5 text-center p-0 mb-0">
        <h2>{{ userInfo.username }}</h2>
        <div class="row">
          <div class="col-6 text-right" style="color: #707062">
            <em> Followers: {{ userInfo.follow_info.followers_quantity }} </em>
          </div>
          <div class="col-6 text-left" style="color: #707062">
            <em> Followings: {{ userInfo.follow_info.followings_quantity }} </em>
          </div>
        </div>
        <p class="mt-2">{{ userInfo.profile.status }}</p>
        <b-button id="submit-button" v-on:click.prevent="follow" variant="secondary">Follow</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Profile",
  data() {
    return {
    };
  },
  components: {},
  computed: mapGetters(['userInfo']),
  methods: {
    ...mapActions(['getUserInfo']),
    follow() {
      const profileId = this.userInfo.profile.id;
      this.$store
        .dispatch("follow", profileId)
        // .then(() => this.$router.push("/"))
        .catch((err) => console.log(err));
    },
  },
  mounted() {
    this.getUserInfo(this.$route.params.userId);
  },
};
</script>