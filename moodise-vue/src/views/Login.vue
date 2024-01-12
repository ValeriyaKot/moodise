<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-6 p-0">
        <b-img src="https://i.pinimg.com/564x/23/dc/4c/23dc4c3bbe714124713bfe6eeed6346a.jpg" alt="kdfkl" right></b-img>
      </div>
      <div class="col-4 p-3 align-self-center">
        <div id="login-group-form" class="container">
          <h1 style="color: #B2BF4E" class="text-center">Welcome!</h1>
          <p class="text-center">Sign in to your account!</p>

          <b-form>
            <b-form-group class="m-0">
              <b-form-group id="input-group-1" label="Username" label-for="input-1">
                <b-form-input id="input-1" v-model="form.username" type="text" placeholder="Type your username" required
                  trim></b-form-input>

                <b-form-text v-for="(message, index) in errorMessages.username" :key="index"
                  :id="`input-1-error-${index}`">
                  <span class="error-message">{{ message }}</span>
                </b-form-text>
              </b-form-group>

              <b-form-group id="input-group-2" label="Password" label-for="input-2">
                <b-form-input v-model="form.password" type="password" id="input-2" placeholder="Type your password"
                  trim>
                </b-form-input>

                <b-form-text v-for="(message, index) in errorMessages.password" :key="index"
                  :id="`input-2-error-${index}`">
                  <span class="error-message">{{ message }}</span>
                </b-form-text>
              </b-form-group>
            </b-form-group>
          </b-form>
          <div class="container" id="loginStatusForm">
            <div class="row align-self-cente">
              <div class="col-6 text-left p-0">
                <b-form-checkbox id="checkbox-1" v-model="status" name="checkbox-1" value="accepted"
                  unchecked-value="not_accepted">
                  Remember me
                </b-form-checkbox>
              </div>
              <div class="col-6 text-right p-0">
                <a class="link">Forgot password?</a>
              </div>
            </div>
          </div>

          <div class="row pt-4 justify-content-center">
            <b-button id="submit-button" v-on:click.prevent="login" variant="secondary">Submit</b-button>
          </div>
          <div class="row">
            <div class="col-12 text-center pt-3">
              <a>or</a>
            </div>
          </div>
          <div class="row pb-3 m-0 border-bottom border-secondary">
            <div class="col-12 text-center">
              <b-button id="socialMediaBtn">
                <img id="socialMediaIcon"
                  src="../assets/instagram.png">
              </b-button>

              <b-button id="socialMediaBtn">
                <img id="socialMediaIcon"
                  src="../assets/google.png">
              </b-button>
              <b-button id="socialMediaBtn">
                <img id="socialMediaIcon"
                  src="../assets/facebook.png">
              </b-button>
            </div>
          </div>
          <div class="col-12 text-center pt-3" style="font-size: 15px;">
            <a>Not registred yet? <a class="link" href="/registration">Sign up</a></a>
          </div>
          <span v-if="isLoggedIn"> | <a @click="logout">Logout</a></span>

          <b-modal id="error-modal" hide-header hide-footer>
            <div class="d-block text-center">
              <h4 class="mb-4">Error</h4>
              <div v-for="(message, index) in this.errorMessages" :key="index">
                {{ message }}
              </div>
            </div>
            <b-button class="mt-4" block @click="$bvModal.hide('error-modal')">Ok</b-button>
          </b-modal>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {
      user: {},
      status: '',
      form: {
        username: "",
        password: "",
      },
      errorMessages: {},
    };
  },
  components: {
  },
  methods: {
    onGoogleSignInSuccess(resp) {
      const token = resp.wc.access_token;
      console.log(token),
        this.$store
          .dispatch("loginGoogle", token)
          .then(() => this.$router.push("/"))
          .catch((err) => console.log(err));
    },
    onGoogleSignInError(error) {
      console.log("OH NOES", error);
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
    logout: function () {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    },
    ...mapActions(["getUserInfo"]),
    login: function () {
      const form = this.form;
      this.$store
        .dispatch("login", form)
        .then(() => this.$router.push("/"))
        .catch((err) => console.log(err));
      this.form.username = this.form.password = ''
    },
  },
};
</script>
