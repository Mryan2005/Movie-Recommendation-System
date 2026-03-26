<script setup>
import { ref } from 'vue'

const email = ref('')
const sent = ref(false)
</script>

<template>
  <div class="two-column">
    <div class="panel">
      <header>
        <div class="chip">密码找回</div>
        <div class="pill">安全验证</div>
      </header>
      <p class="muted">输入注册时使用的邮箱，我们会发送重置链接。</p>
      <div class="form-grid">
        <div class="field">
          <label>邮箱</label>
          <input v-model="email" type="email" placeholder="you@example.com" />
        </div>
      </div>
      <div class="form-actions">
        <button class="primary-btn" type="button" @click="sent = true">发送重置邮件</button>
      </div>
      <p v-if="sent" class="muted">重置链接已发送，请检查邮箱（可能在垃圾箱）。</p>
    </div>

    <div class="panel">
      <header>
        <div>账号安全提示</div>
      </header>
      <ul class="list">
        <li class="list-item">
          <div>
            <strong>设置强密码</strong>
            <p class="muted">密码至少 8 位，包含字母与数字</p>
          </div>
          <span class="status-dot success"></span>
        </li>
        <li class="list-item">
          <div>
            <strong>定期更新</strong>
            <p class="muted">建议每 90 天更新一次密码</p>
          </div>
          <span class="status-dot success"></span>
        </li>
        <li class="list-item">
          <div>
            <strong>启用双重验证</strong>
            <p class="muted">保护你的观影清单与偏好数据</p>
          </div>
          <span class="status-dot success"></span>
        </li>
      </ul>
    </div>
  </div>
</template>
