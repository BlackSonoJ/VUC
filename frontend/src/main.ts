import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Videos from './pages/Videos.vue';
import Images from './pages/Images.vue';
import Info from './pages/Info.vue';
import CalendarPage from './pages/CalendarPage.vue';
import Main from './pages/Main.vue';

const routes = [
  { path: '/', component: Main },
  { path: '/videos', component: Videos },
  { path: '/images', component: Images },
  { path: '/calendar', component: CalendarPage },
  { path: '/info', component: Info },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.mount('#app');
