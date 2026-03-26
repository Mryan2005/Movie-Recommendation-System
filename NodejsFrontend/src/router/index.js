import { createRouter, createWebHistory } from 'vue-router'

const HomeView = () => import('../views/HomeView.vue')
const LoginView = () => import('../views/LoginView.vue')
const RegisterView = () => import('../views/RegisterView.vue')
const ForgotPasswordView = () => import('../views/ForgotPasswordView.vue')
const ProfileView = () => import('../views/ProfileView.vue')
const SettingsView = () => import('../views/SettingsView.vue')
const ActorDetailView = () => import('../views/ActorDetailView.vue')
const MovieDetailView = () => import('../views/MovieDetailView.vue')
const RoleDetailView = () => import('../views/RoleDetailView.vue')

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior() {
    return { top: 0 }
  },
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/register', name: 'register', component: RegisterView },
    { path: '/forgot-password', name: 'forgot', component: ForgotPasswordView },
    { path: '/profile', name: 'profile', component: ProfileView },
    { path: '/settings', name: 'settings', component: SettingsView },
    { path: '/actor/:id', name: 'actor', component: ActorDetailView },
    { path: '/movie/:id', name: 'movie', component: MovieDetailView },
    { path: '/role/:id', name: 'role', component: RoleDetailView },
  ],
})

export default router
