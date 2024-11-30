<script setup lang="ts">
import ImageDisplay from './ImageDisplay.vue'

defineProps<{ msg: string }>()
</script>

<template>
  <h1>{{ msg }}</h1>
  <ImageDisplay 
    title="Graafi kirjeldus" 
    imagePath="../../data/image.png"
  />
</template>

<style scoped>
.main {
  width: 100%;
  background-color: #C0C8CA;
}

.text {
  font-size: 2.0rem;
  color: #1A2D42;
  top: 10px;
  left: 10px;
  margin: 0 0 30px 0; /* Added bottom margin to increase gap */
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
  padding: 0;
}

.image-container {
  width: 100%;
  max-width: 800px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px; /* Added gap between elements */
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
