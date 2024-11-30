<script setup lang="ts">
defineProps<{ 
  title: string,
  imagePath: string 
}>()
</script>

<template>
  <div class="main-content">
    <div class="image-container">
      <p class="text">{{ title }}</p>
      <img :src="imagePath" alt="graph" class="image">
    </div>
  </div>
</template>

<style scoped>
.text {
  font-size: 2.0rem;
  color: #1A2D42;
  top: 10px;
  left: 10px;
  margin: 0;
  z-index: 1;
  align-self: flex-start;
}

.main-content {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.image-container {
  width: 100%;
  max-width: 800px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.image {
  width: 100%;
  height: auto;
  border-radius: 15px;
  object-fit: contain;
}

.main-image {
  max-width: 100%;
  height: auto;
}
</style> 