<template>
  <div class="content-container">
    <ImageDisplay 
      title="Pinnavee võtt" 
      imagePath="../../data/image.png"
    />
  </div>
</template>

<script setup lang="ts">
import ImageDisplay from '../components/ImageDisplay.vue'
</script>

<style scoped>
.content-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}
</style> 
