<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const form = ref({
  email: '',
  password: '',
  remember: true,
})
</script>

<template>
  <div id="login" class="two-column">
    <div class="panel">
      <header>
        <div>
          <div class="chip">安全登录</div>
          <h2>欢迎回来</h2>
        </div>
        <RouterLink class="link" to="/register">还没有账号？</RouterLink>
      </header>
      <form class="form-grid">
        <div class="field">
          <label>邮箱</label>
          <input v-model="form.email" type="email" placeholder="you@example.com" />
        </div>
        <div class="field">
          <label>密码</label>
          <input v-model="form.password" type="password" placeholder="••••••••" />
        </div>
        <div class="field">
          <label class="row">
            <input v-model="form.remember" type="checkbox" /> 记住我
          </label>
        </div>
        <div class="form-actions">
          <RouterLink class="ghost-btn" to="/forgot-password">忘记密码？</RouterLink>
          <button class="primary-btn" type="button">登录</button>
        </div>
      </form>
    </div>

    <div class="panel">
      <header>
        <div>推荐摘要</div>
        <span class="pill">预览</span>
      </header>
      <p class="muted">登录后将根据你的偏好实时刷新推荐列表。</p>
      <ul class="list">
        <li class="list-item">
          <div>
            <strong>个性化首页</strong>
            <p class="muted">基于历史观影生成的主页卡片</p>
          </div>
          <span class="status-dot success"></span>
        </li>
        <li class="list-item">
          <div>
            <strong>关注演员更新</strong>
            <p class="muted">订阅演员/角色的新片档期</p>
          </div>
          <span class="status-dot success"></span>
        </li>
        <li class="list-item">
          <div>
            <strong>跨端同步</strong>
            <p class="muted">云端保存偏好与观影清单</p>
          </div>
          <span class="status-dot success"></span>
        </li>
      </ul>
    </div>
  </div>
</template>
