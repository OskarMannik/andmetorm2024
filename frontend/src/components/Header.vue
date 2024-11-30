<template>
  <header class="header">
    <div class="header-content">
      <div class="headline">
        <h1>Luup</h1>
      </div>
      <div class="logo">
        <img src="../../log.png" alt="Luup logo" class="logo-image">
      </div>
      
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
.logo-image {
  width: 75px;
  height: 75px;
  border-radius: 50%;
}

.logo{
    align-items: right;

}

.header {
  background-color: #1A2D42;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  padding: 1rem 0;
  position: fixed;
  color: #C0C8CA;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.headline h1 {
  font-size: 3rem;
  color: #C0C8CA;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  margin: 0;
  font-weight: 700;
  letter-spacing: 1px;
  padding-left: 3rem;
}


</style>
