<script setup>
import { RouterLink } from 'vue-router'
const featured = [
  { title: '沙丘2', score: 9.1, tags: ['科幻', '史诗', 'IMAX'] },
  { title: '奥本海默', score: 8.9, tags: ['传记', '剧情', '诺兰'] },
  { title: '瞬息全宇宙', score: 8.7, tags: ['奇幻', '动作', '家庭'] },
]

const picks = [
  { name: '心理惊悚', count: 24, desc: '紧张刺激的反转故事' },
  { name: '治愈喜剧', count: 18, desc: '轻松放松的周末时光' },
  { name: '奥斯卡获奖', count: 12, desc: '高口碑电影合集' },
  { name: '国片精选', count: 8, desc: '近年国产佳作盘点' },
]

const actors = [
  { name: '蒂莫西·柴勒梅德', role: '保罗·厄崔迪', film: '沙丘2' },
  { name: '小罗伯特·唐尼', role: '路易斯·施特劳斯', film: '奥本海默' },
  { name: '杨紫琼', role: '秀莲', film: '瞬息全宇宙' },
]
</script>

<template>
  <div class="page-stack">
    <div class="hero-card">
      <div>
        <p class="chip">AI 推荐 · 影院热映</p>
        <h1 class="hero-title">探索你的下一部高分电影</h1>
        <p class="hero-sub">
          基于你喜欢的题材、演员和观影记录，给出个性化的电影推荐。开启沉浸式的观影旅程。
        </p>
        <div class="search-bar">
          <span class="chip">🔍</span>
          <input placeholder="搜索电影、演员或标签..." />
          <a class="primary-btn" href="#hot">发现热榜</a>
        </div>
        <div class="tag-row">
          <span class="chip">🔥 科幻</span>
          <span class="chip">🎭 剧情</span>
          <span class="chip">🕵️‍♀️ 悬疑</span>
        </div>
      </div>
      <div class="panel">
        <header>
          <div>今日精选</div>
          <span class="pill">高分必看</span>
        </header>
        <ul class="list">
          <li v-for="item in featured" :key="item.title" class="list-item">
            <div>
              <div class="row">
                <strong>{{ item.title }}</strong>
                <span class="pill-blue">评分 {{ item.score }}</span>
              </div>
              <div class="tag-row">
                <span v-for="tag in item.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
            </div>
            <span class="status-dot success"></span>
          </li>
        </ul>
      </div>
    </div>

    <div id="hot" class="section-title">
      <div>
        <h2>热门推荐</h2>
        <p>根据口碑、热度与个性偏好实时刷新</p>
      </div>
      <a class="ghost-btn" href="#login">登录后同步我的偏好</a>
    </div>

    <div class="card-grid">
      <div v-for="pick in picks" :key="pick.name" class="panel">
        <header>
          <span>{{ pick.name }}</span>
          <span class="pill">{{ pick.count }} 部</span>
        </header>
        <p>{{ pick.desc }}</p>
        <div class="tag-row">
          <span class="tag">智能排序</span>
          <span class="tag">相似口味</span>
        </div>
      </div>
    </div>

    <div class="section-title">
      <div>
        <h2>演员关注</h2>
        <p>你关注的角色与演员动态</p>
      </div>
      <RouterLink class="link" to="/profile">管理我的清单</RouterLink>
    </div>

    <div class="card-grid">
      <div v-for="actor in actors" :key="actor.name" class="panel">
        <header>
          <span>{{ actor.name }}</span>
          <span class="pill">{{ actor.film }}</span>
        </header>
        <p>代表角色：{{ actor.role }}</p>
        <div class="tag-row">
          <span class="tag">关注</span>
          <span class="tag">订阅新片</span>
        </div>
      </div>
    </div>
  </div>
</template>
