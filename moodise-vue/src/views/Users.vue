<template>
    <div class="container mt-5">
        <div class="row justify-content-center border-top border-secondary ">
            <div class="col-8 mt-3">
                <div class="container border-bottom border-secondary p-0">
                    <UserItem v-for="(user, index) in allUsers" :key="user.id" :user="user" :index="index" />
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import UserItem from "../components/UserItem.vue";
import { mapGetters, mapActions } from "vuex"

export default {
    name: "Users",
    data() {
        return {
            users: [],
        };
    },
    components: {
        UserItem
    },
    computed: mapGetters(['allUsers']),
    methods: {
        ...mapActions(['getUsers']),
    },
    mounted() {
        this.getUsers()
    },
};
</script>