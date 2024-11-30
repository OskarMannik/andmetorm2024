<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import ChatBot from './components/ChatBot.vue'
</script>

<template>
  <div class="app-container">
    <Sidebar />
    <Header />
    <main class="main-content">
      <div class="content-container">
        <router-view></router-view>
        <ChatBot />
      </div>
    </main>
    <Footer />
  </div>
</template>

<style scoped>

.app-container {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 20px;
  margin-top: 60px; /* Space for header */
  padding-left: 60px; /* Space for hamburger button */
}

.content-container {
  max-width: 650px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
