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
                    <p class="text-center">Reset your password!</p>

                    <b-form>
                        <b-form-group>

                            <b-form-group id="input-group-4" label="Current password" label-for="input-1">
                                <b-form-input v-model="form.current_password" type="password" id="input-1"
                                    placeholder="Type your  current password" description="Your password must be 8-20 characters long, contain letters and
            numbers, and must not contain spaces, special characters, or emoji." trim>
                                </b-form-input>

                                <b-form-text v-for="(message, index) in errorMessages.password" :key="index"
                                    :id="`input-1-error-${index}`">
                                    <span class="error-message">{{ message }}</span>
                                </b-form-text>
                            </b-form-group>
                            <b-form-group id="input-group-4" label="New password" label-for="input-2">
                                <b-form-input v-model="form.new_password" type="password" id="input-2"
                                    placeholder="Type your new password" description="Your password must be 8-20 characters long, contain letters and
            numbers, and must not contain spaces, special characters, or emoji." trim>
                                </b-form-input>

                                <b-form-text v-for="(message, index) in errorMessages.password" :key="index"
                                    :id="`input-2-error-${index}`">
                                    <span class="error-message">{{ message }}</span>
                                </b-form-text>
                            </b-form-group>

                        </b-form-group>
                    </b-form>
                    <div class="row mt-4 justify-content-center">
                        <div class="col-6 text-right">
                            <b-button id="submit-button" variant="secondary" href="/login">Cancel</b-button>
                        </div>
                    <div class="col-6 text-left">
                            <b-button id="submit-button" v-on:click.prevent="resetPassword" variant="secondary">Submit
                            </b-button>
                        </div>
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
                current_password: '',
                new_password: "",
            },
            errorMessages: {},
        };
    },
    components: {
    },
    methods: {
        resetPassword: function () {
            const form = this.form;
            this.$store
                .dispatch("resetPassword", form)
                // .then(() => this.$router.push("/login"))
                .catch((err) => console.log(err));
            this.form = {}
        },
    },
};
</script>
