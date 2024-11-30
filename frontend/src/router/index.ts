import { createRouter, createWebHistory } from 'vue-router';
import MainPage from '../components/MainPage.vue';
import PinnavesiView from '../views/PinnavesiView.vue';
import VeekasutusView from '../views/VeekasutusView.vue';

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
    {
      path: '/veekasutus',
      name: 'veekasutus',
      component: VeekasutusView
    }
  ]
});

export default router; 