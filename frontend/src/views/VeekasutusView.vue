<template>
  <div class="main-container">
    <ChatBot ref="chatBot" />
    <ImageDisplay 
      title="Graafi kirjeldus" 
      imagePath="../../data/image.png"
      :isVisible="chatBot?.showImage"
    />
  </div>
</template>

<script setup lang="ts">
import ChatBot from '../components/ChatBot.vue'
import ImageDisplay from '../components/ImageDisplay.vue'
import { ref } from 'vue'

const chatBot = ref()
</script>

<style scoped>
.main-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 20px;
}
</style> 