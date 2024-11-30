<template>
  <header class="header">
      <div class="headline">
        <h1>Pealkiri</h1>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
.header {
  background-color: #1A2D42;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Enhanced shadow */
  padding: 1rem 0;
  position: fixed;
  color: #C0C8CA;
  justify-content: center;
  align-items: center;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000; /* Add high z-index to ensure header stays on top */
}

.headline h1 {
  margin-left: 12%;
  font-size: 2.0rem;
  color: #C0C8CA;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Added text shadow */
}

.navigation ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 2rem;
}

.navigation a {
  text-decoration: none;
  color: #C0C8CA;
  font-weight: 500;
  transition: color 0.3s ease;
}

.navigation a:hover {
  color: #666;
}
</style>
