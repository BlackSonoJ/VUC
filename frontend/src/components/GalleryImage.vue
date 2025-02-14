<script setup lang="ts">
const props = defineProps({
  image: String,
});
</script>
<template>
  <div class="w-[200px] h-[200px] cursor-pointer">
    <img
      :src="props.image"
      alt="photo"
      class="w-[200px] object-cover h-[200px]"
    />
  </div>
</template>
