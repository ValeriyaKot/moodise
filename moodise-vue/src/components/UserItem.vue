<template>
    <b-button block variant="outline-primary" id="userButton" class="p-0 m-0" @click="moveToProfile">
        <div class="container">
            <div class="row justify-content-start align-items-center">
                <div class="col-2 p-0">
                    <b-img id="userAvatarUsersPage" :src="user.profile.image" alt="userPicture" left></b-img>
                </div>
                <div class="col-5 p-0 text-left">
                    <h5>{{ user.username }}</h5>
                </div>
            </div>
        </div>
    </b-button>
</template>

<script>
export default {
    props: {
        user: Object,
        index: Number,
        title: String,
    },
    methods: {
        moveToProfile() {
            this.$router.push(`/profile/${this.user.id}`)
        },
    }}
</script>