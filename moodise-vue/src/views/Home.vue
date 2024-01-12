<template>
  <div class="container">
    <div class="container mt-5 mb-3">
      <div class="row border-bottom border-secondary">
      </div>
    </div>
    <b-card-group columns>
      <PictureItem v-for="picture in allPictures" :key="picture.id" :picture="picture" />

    </b-card-group>

  </div>
</template>

<script>
import PictureItem from "../components/PictureItem.vue";
import {mapGetters, mapActions} from "vuex"

export default {
  name: "Pictures",
  data() {
    return {
      pictures: [],
    };
  },
  components: {
    PictureItem,
  },
  computed: mapGetters(['allPictures', 'getUserInfo']),
  methods: mapActions(['getPictures']),
  mounted() {
      this.getPictures()
  },
};
</script>