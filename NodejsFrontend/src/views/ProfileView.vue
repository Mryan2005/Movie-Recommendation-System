<script setup>
import { ref } from 'vue'

const profile = ref({
  name: 'Echo',
  email: 'echo@example.com',
  gender: '女',
  avatar: 'https://avatars.githubusercontent.com/u/1?v=4',
  bio: '热爱科幻与悬疑，偏爱大卫·芬奇的作品。',
  city: '上海',
  signature: '“故事，就是人对抗时间的方式。”',
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

const likedMovies = [
  { title: '沙丘2', genre: '科幻', language: '英语', type: '电影' },
  { title: '孤注一掷', genre: '犯罪', language: '国语', type: '电影' },
  { title: '我的三体', genre: '科幻', language: '国语', type: '动漫' },
  { title: '想见你', genre: '爱情', language: '国语', type: '电视剧' },
]

const stats = {
  genres: [
    { label: '科幻', count: 2 },
    { label: '犯罪', count: 1 },
    { label: '爱情', count: 1 },
  ],
  languages: [
    { label: '英语', count: 1 },
    { label: '国语', count: 3 },
  ],
  types: [
    { label: '电影', count: 2 },
    { label: '动漫', count: 1 },
    { label: '电视剧', count: 1 },
  ],
}

const favoriteRoles = ['保罗·厄崔迪（沙丘）', '小丑（黑暗骑士）', '夏洛克（神探夏洛克）']
const cosplayRoles = ['阿狸（英雄联盟）', '薇尔莉特（紫罗兰永恒花园）']
const favoriteActors = ['蒂莫西·柴勒梅德', '赞达亚', '任素汐', '梁朝伟']
</script>

<template>
  <div class="two-column">
    <div class="panel">
      <header>
        <div class="row">
          <div
            class="avatar"
            :style="profile.avatar ? { backgroundImage: `url(${profile.avatar})`, color: '#fff', backgroundSize: 'cover' } : {}"
          >
            {{ profile.name?.[0] || 'U' }}
          </div>
          <div>
            <strong>{{ profile.name }}</strong>
            <p class="muted">{{ profile.email }}</p>
            <p class="muted">性别：{{ profile.gender }}</p>
            <p class="muted">个性签名：{{ profile.signature }}</p>
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
        <div class="field">
          <label>性别</label>
          <input v-model="profile.gender" />
        </div>
        <div class="field">
          <label>头像链接</label>
          <input v-model="profile.avatar" />
        </div>
        <div class="field" style="grid-column: 1 / -1">
          <label>个性签名</label>
          <input v-model="profile.signature" />
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
      <div class="mini-card">
        <h4>喜欢的角色</h4>
        <p class="muted">{{ favoriteRoles.join('、') }}</p>
      </div>
      <div class="mini-card">
        <h4>想 cos 的角色</h4>
        <p class="muted">{{ cosplayRoles.join('、') }}</p>
      </div>
      <div class="mini-card">
        <h4>喜欢的演员</h4>
        <p class="muted">{{ favoriteActors.join('、') }}</p>
      </div>

      <div class="section-title" style="margin-top: 16px">
        <div>
          <h2>看过且喜欢的电影</h2>
          <p>电影列表 & 数据统计</p>
        </div>
      </div>
      <ul class="list">
        <li v-for="movie in likedMovies" :key="movie.title" class="list-item">
          <div>
            <strong>{{ movie.title }}</strong>
            <p class="muted">{{ movie.genre }} · {{ movie.language }} · {{ movie.type }}</p>
          </div>
          <span class="status-dot success"></span>
        </li>
      </ul>

      <div class="section-title" style="margin-top: 16px">
        <div>
          <h2>偏好统计</h2>
          <p class="muted">题材 / 语种 / 类型</p>
        </div>
      </div>
      <div class="form-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));">
        <div class="field">
          <label>电影题材</label>
          <div class="tag-row">
            <span v-for="item in stats.genres" :key="item.label" class="tag">
              {{ item.label }} · {{ item.count }}
            </span>
          </div>
        </div>
        <div class="field">
          <label>语种</label>
          <div class="tag-row">
            <span v-for="item in stats.languages" :key="item.label" class="tag">
              {{ item.label }} · {{ item.count }}
            </span>
          </div>
        </div>
        <div class="field">
          <label>类型</label>
          <div class="tag-row">
            <span v-for="item in stats.types" :key="item.label" class="tag">
              {{ item.label }} · {{ item.count }}
            </span>
          </div>
        </div>
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
