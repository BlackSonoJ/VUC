<script setup lang="ts">
const props = defineProps({
  image: String,
});
</script>
<template>
  <div class="w-full h-full cursor-pointer">
    <img
      :src="props.image"
      alt="photo"
      class="w-full object-cover h-full"
    />
  </div>
</template>
