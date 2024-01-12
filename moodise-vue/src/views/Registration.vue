<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-6 p-0">
                <b-img src="https://i.pinimg.com/564x/23/dc/4c/23dc4c3bbe714124713bfe6eeed6346a.jpg" alt="kdfkl" right>
                </b-img>
            </div>
            <div class="col-4 p-3 align-self-center">
                <div id="login-group-form" class="container">
                    <h1 style="color: #B2BF4E" class="text-center">Welcome!</h1>
                    <p class="text-center">Register your account!</p>

                    <b-form>
                        <b-form-group>
                            <b-form-group id="input-group-1" label="Username" label-for="input-1">
                                <b-form-input id="input-1" v-model="form.username" type="text"
                                    placeholder="Type your username" required trim></b-form-input>

                                <b-form-text v-for="(message, index) in errorMessages.username" :key="index"
                                    :id="`input-1-error-${index}`">
                                    <span class="error-message">{{ message }}</span>
                                </b-form-text>
                            </b-form-group>

                            <b-form-group id="input-group-2" label="First name" label-for="input-2">
                                <b-form-input id="input-2" v-model="form.first_name" type="text"
                                    placeholder="Enter first name" trim></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Last name" label-for="input-3">
                                <b-form-input id="input-3" v-model="form.last_name" type="text"
                                    placeholder="Enter last name" trim></b-form-input>
                            </b-form-group>


                            <b-form-group id="input-group-4" label="Password" label-for="input-4">
                                <b-form-input v-model="form.password" type="password" id="input-4"
                                    placeholder="Type your password" description="Your password must be 8-20 characters long, contain letters and
            numbers, and must not contain spaces, special characters, or emoji." trim>
                                </b-form-input>

                                <b-form-text v-for="(message, index) in errorMessages.password" :key="index"
                                    :id="`input-4-error-${index}`">
                                    <span class="error-message">{{ message }}</span>
                                </b-form-text>
                            </b-form-group>
                            <b-form-group id="input-group-5" label="Email address" label-for="input-5">
                                <b-form-input id="input-5" v-model="form.email" type="email"
                                    description="We'll never share your email with anyone else."
                                    placeholder="Enter email" required trim></b-form-input>

                                <b-form-text v-for="(message, index) in errorMessages.email" :key="index"
                                    :id="`input-5-error-${index}`">
                                    <span class="error-message">{{ message }}</span>
                                </b-form-text>
                            </b-form-group>
                        </b-form-group>
                    </b-form>
                    <a class="link" href="/login">Log in your account</a>
                    <div class="row mt-4 justify-content-center">
                        <b-button id="submit-button" v-on:click.prevent="register" variant="secondary">Submit</b-button>
                    </div>


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

export default {
    props: {
        isLoggedIn: Boolean,
    },
    data() {
        return {
            form: {
                email: "",
                username: "",
                first_name: "",
                last_name: "",
                password: "",
            },
            errorMessages: {},
        };
    },
    components: {
    },
    methods: {
        register: function () {
            const form = this.form;
            this.$store
                .dispatch("register", form)
                .then(() => this.$router.push("/"))
                .catch((err) => console.log(err));
            this.form = {}
        },
    },
};
</script>
