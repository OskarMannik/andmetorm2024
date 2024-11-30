<template>
  <div class="sidebar" :class="{ 'sidebar-open': isOpen }">
    
    <nav class="navigation">
      <ul>
        <li><router-link to="/">Avaleht</router-link></li>
        <li><router-link to="/pinnavesi">Pinnavee võtt</router-link></li>
        <li><router-link to="/veekasutus">Veekasutus</router-link></li>
      </ul>
    </nav>
  </div>
  <button class="hamburger" @click="toggleSidebar">
    <div class="hamburger-icon">☰</div>
  </button>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isOpen = ref(false)
const toggleSidebar = () => {
  isOpen.value = !isOpen.value
}
</script>

<style scoped>
.sidebar {
  background-color: #2E4156;
  box-shadow: 2px 0 4px rgba(0,0,0,0.1);
  color: #C0C8CA;
  width: 250px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: -250px;
  padding: 2rem 0;
  transition: left 0.3s ease;
  z-index: 1000;
  padding-top: 15%;
}

.sidebar-open {
  left: 0;
}

.hamburger {
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 1001;
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
  
}

.hamburger-icon {
  font-size: 24px;
  color: #C0C8CA;
}

.logo {
  padding: 0 1.5rem;
  margin-bottom: 2rem;
}

.logo h1 {
  margin: 0;
  font-size: 1.5rem;
  color: #C0C8CA;
}

.navigation ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.navigation li {
  margin-bottom: 0.5rem;
}

.navigation a {
  display: block;
  padding: 0.75rem 1.5rem;
  text-decoration: none;
  color: #C0C8CA;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.navigation a:hover {
  background-color: #1A2D42;
}

@media screen and (max-height: 700px) and (max-width: 1200px) {
    .sidebar {
  padding-top: 20%;
  width: 150px;

}
  
  .navigation {
    margin-top: 60px;
  }
}

@media screen and (max-height: 400px) {
  .sidebar {
    padding-top: 35%;
  }
  
  .navigation {
    margin-top: 80px;
  }
}
</style> 