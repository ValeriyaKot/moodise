<template>
    <b-card
    :img-src="picture.image"
    img-alt="Image"
    img-top
    style="max-width: 20rem;"
    class="mb-3"
    id="picture-card"
  >
    <b-card-title>
      {{ picture.name }}
    </b-card-title>
    </b-card> 
</template>

<script>
export default {
  props: {
    picture: Object,
    index: Number,
    title: String,
  },
};
</script>