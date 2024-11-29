<template>
  <div class="hello">
  <button @click="counter++">Add 1</button>
  <p>Count is: {{ counter }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const counter = ref(0)
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
