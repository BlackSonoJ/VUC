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
      class="w-full object-fill h-full"
    />
  </div>
</template>
