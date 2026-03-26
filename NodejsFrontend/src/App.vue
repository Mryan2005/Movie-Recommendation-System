<script setup>
import { ref, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const isLoggedIn = ref(false)
const open = ref(false)

const menuItems = computed(() =>
  isLoggedIn.value
    ? [
        { label: '个人主页', to: '/profile' },
        { label: '设置', to: '/settings' },
      ]
    : [
        { label: '登录', to: '/login' },
        { label: '注册', to: '/register' },
      ]
)

const toggle = () => {
  open.value = !open.value
}

const close = () => {
  open.value = false
}
</script>

<template>
  <div class="app-shell">
    <header class="top-bar">
      <RouterLink to="/" class="brand">
        🎬 Movie<span>Rec</span>
      </RouterLink>
      <nav class="main-nav">
        <RouterLink to="/">首页</RouterLink>
      </nav>
      <div class="actions">
        <div class="dropdown" @mouseleave="close">
          <button class="dropdown-button" type="button" @click="toggle">
            账号
            <span class="caret">▾</span>
          </button>
          <div v-if="open" class="dropdown-menu">
            <RouterLink v-for="item in menuItems" :key="item.to" :to="item.to" class="dropdown-item" @click="close">
              {{ item.label }}
            </RouterLink>
          </div>
        </div>
      </div>
    </header>

    <main class="page">
      <RouterView />
    </main>

    <footer class="footer">
      <div>
        <div class="brand">MovieRec</div>
        <p>用个性化的推荐，帮你找到下一部必看的电影。</p>
      </div>
      <div class="footer-links">
        <RouterLink to="/">主页</RouterLink>
        <RouterLink to="/profile">个人中心</RouterLink>
        <RouterLink to="/settings">设置</RouterLink>
      </div>
    </footer>
  </div>
</template>
