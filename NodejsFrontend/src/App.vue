<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-shell">
    <header class="top-bar">
      <RouterLink to="/" class="brand">
        🎬 Movie<span>Rec</span>
      </RouterLink>
      <nav class="main-nav">
        <RouterLink to="/">首页</RouterLink>
        <RouterLink to="/login">登录</RouterLink>
        <RouterLink to="/register">注册</RouterLink>
        <RouterLink to="/profile">用户资料</RouterLink>
        <RouterLink to="/settings">设置</RouterLink>
      </nav>
      <div class="actions">
        <RouterLink class="ghost-btn" to="/forgot-password">忘记密码</RouterLink>
        <RouterLink class="primary-btn" to="/login">进入系统</RouterLink>
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
