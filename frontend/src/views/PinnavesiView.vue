<template>
  <ImageDisplay 
    :title="title" 
    :imagePath="imagePath" 
    :visible="visible" 
  />
</template>

<script setup lang="ts">
import ImageDisplay from '../components/ImageDisplay.vue'
import { ref } from 'vue'

defineProps<{
  visible: boolean
}>()

const title = ref('Pinnavee võtt')
const imagePath = ref('../../data/image.png')
</script> 

