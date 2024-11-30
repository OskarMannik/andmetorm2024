<template>
  <footer class="footer">
    <div class="footer-content">
        <p>Philip Paškov, Oskar Männik, Robin Otter, Markus Tamm</p>
    </div>
    <div class="footer-bottom">
      <p>Andmetorm 2024</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
.footer {
  background-color: #1A2D42;
  color: #C0C8CA;
  padding: 2rem 0;
  width: 100%;
  box-shadow: 0 -2px 4px rgba(0,0,0,0.1); 
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  padding: 0 1rem;
}

.footer-section {
  margin: 1rem;
  min-width: 250px;
}

.footer-section h3 {
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.footer-bottom {
  max-height: 30px;
  text-align: center;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #555;
}
</style>
