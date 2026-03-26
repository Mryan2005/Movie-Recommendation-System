<script setup>
import { ref } from 'vue'

const profile = ref({
  name: 'Echo',
  email: 'echo@example.com',
  bio: '热爱科幻与悬疑，偏爱大卫·芬奇的作品。',
  city: '上海',
})

const favorites = [
  { title: '社交网络', tag: '传记 / 剧情' },
  { title: '银翼杀手2049', tag: '科幻 / 视觉' },
  { title: '无间道', tag: '犯罪 / 港片' },
]

const watching = [
  { title: '禁闭岛', progress: '已看 70%' },
  { title: '降临', progress: '待看' },
]
</script>

<template>
  <div class="two-column">
    <div class="panel">
      <header>
        <div class="row">
          <div class="avatar">E</div>
          <div>
            <strong>{{ profile.name }}</strong>
            <p class="muted">{{ profile.email }}</p>
          </div>
        </div>
        <span class="pill">观影偏好</span>
      </header>
      <div class="form-grid">
        <div class="field">
          <label>昵称</label>
          <input v-model="profile.name" />
        </div>
        <div class="field">
          <label>城市</label>
          <input v-model="profile.city" />
        </div>
        <div class="field" style="grid-column: 1 / -1">
          <label>自我介绍</label>
          <textarea v-model="profile.bio"></textarea>
        </div>
      </div>
      <div class="form-actions">
        <button class="primary-btn" type="button">保存资料</button>
      </div>
    </div>

    <div class="panel">
      <header>
        <div>偏好摘要</div>
        <span class="pill-blue">实时同步</span>
      </header>
      <div class="mini-card">
        <h4>收藏的演员 & 角色</h4>
        <p class="muted">蒂莫西·柴勒梅德、玛格特·罗比、任素汐</p>
      </div>
      <div class="section-title" style="margin-top: 16px">
        <div>
          <h2>我的片单</h2>
          <p>在多个设备间同步</p>
        </div>
      </div>
      <ul class="list">
        <li v-for="movie in favorites" :key="movie.title" class="list-item">
          <div>
            <strong>{{ movie.title }}</strong>
            <p class="muted">{{ movie.tag }}</p>
          </div>
          <span class="status-dot success"></span>
        </li>
      </ul>

      <div class="section-title" style="margin-top: 16px">
        <div>
          <h2>继续观看</h2>
          <p>同步你的播放进度</p>
        </div>
      </div>
      <ul class="list">
        <li v-for="item in watching" :key="item.title" class="list-item">
          <div>
            <strong>{{ item.title }}</strong>
            <p class="muted">{{ item.progress }}</p>
          </div>
          <span class="status-dot" :class="{ success: item.progress !== '待看' }"></span>
        </li>
      </ul>
    </div>
  </div>
</template>
