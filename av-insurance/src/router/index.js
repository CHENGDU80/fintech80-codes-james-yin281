import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Dashboard from '@/views/Dashboard.vue'
import Login from '@/views/Login.vue'
import Policy from '@/views/Policy.vue'
import PolicyBoard from '@/views/PolicyBoard.vue'
import ClaimsOverview from '@/views/ClaimsOverview.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/policy',
      name: 'policy',
      component: Policy
    },
    {
      path: '/policy/:id',
      name: 'policy view',
      component: PolicyBoard
    },
    {
      path: '/claims-overview',
      name: 'claims-overview',
      component: ClaimsOverview
    }
  ]
})

export default router
