<script setup>
import { ref } from 'vue'

const toggles = ref({
  newsletter: true,
  alert: true,
  privacy: false,
})
</script>

<template>
  <div class="two-column">
    <div class="panel">
      <header>
        <div>通知设置</div>
        <span class="pill">即时推送</span>
      </header>
      <div class="toggle-row">
        <div>
          <strong>新品推荐邮件</strong>
          <p class="muted">每周精选影片与演员动态</p>
        </div>
        <span
          class="switch"
          :class="{ on: toggles.newsletter }"
          @click="toggles.newsletter = !toggles.newsletter"
        ></span>
      </div>
      <div class="toggle-row">
        <div>
          <strong>上映提醒</strong>
          <p class="muted">关注的电影/演员有新动态时提醒</p>
        </div>
        <span class="switch" :class="{ on: toggles.alert }" @click="toggles.alert = !toggles.alert"></span>
      </div>
      <div class="toggle-row">
        <div>
          <strong>隐私保护</strong>
          <p class="muted">隐藏公开片单与评分</p>
        </div>
        <span class="switch" :class="{ on: toggles.privacy }" @click="toggles.privacy = !toggles.privacy"></span>
      </div>
      <div class="form-actions">
        <button class="primary-btn" type="button">保存偏好</button>
      </div>
    </div>

    <div class="panel">
      <header>
        <div>账户安全</div>
        <span class="pill-blue">安全等级：高</span>
      </header>
      <ul class="list">
        <li class="list-item">
          <div>
            <strong>密码最后更新</strong>
            <p class="muted">30 天前 · 建议定期更换</p>
          </div>
          <span class="status-dot success"></span>
        </li>
        <li class="list-item">
          <div>
            <strong>双重验证</strong>
            <p class="muted">短信 + 邮箱</p>
          </div>
          <span class="status-dot success"></span>
        </li>
        <li class="list-item">
          <div>
            <strong>设备管理</strong>
            <p class="muted">3 台设备已登录</p>
          </div>
          <span class="status-dot danger"></span>
        </li>
      </ul>
      <div class="form-actions">
        <button class="ghost-btn" type="button">退出所有设备</button>
      </div>
    </div>
  </div>
</template>
