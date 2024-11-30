import { createRouter, createWebHistory } from 'vue-router';
import MainPage from '../components/MainPage.vue';
import PinnavesiView from '../views/PinnavesiView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainPage,
    },
    {
      path: '/pinnavesi',
      name: 'pinnavesi',
      component: PinnavesiView
    },

  ]
});

export default router; 