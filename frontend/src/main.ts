import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Videos from './pages/Videos.vue';
import Images from './pages/Images.vue';
import Calendar from './pages/Calendar.vue';
import Info from './pages/Info.vue';

const routes = [
  { path: '/', component: App },
  { path: '/videos', component: Videos },
  { path: '/images', component: Images },
  { path: '/calendar', component: Calendar },
  { path: '/info', component: Info },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.mount('#app');
