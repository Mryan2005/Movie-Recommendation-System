<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'

const movie = {
  id: 'dune',
  title: '沙丘2',
  year: 2024,
  genres: ['科幻', '史诗', 'IMAX'],
  summary:
    '保罗带领弗雷曼人民对抗帝国与哈克南家族，视觉与叙事兼具的科幻史诗。',
  cast: ['蒂莫西·柴勒梅德', '赞达亚', '丽贝卡·弗格森'],
}

const comments = ref([
  { user: 'FilmGeek', rating: 5, text: 'IMAX 体验震撼，配乐和场面全程高能。', time: '1 天前' },
  { user: 'Aria', rating: 4, text: '叙事更紧凑，想二刷。', time: '3 天前' },
])

const newComment = ref({
  user: '',
  rating: 5,
  text: '',
})

const avgRating = computed(() => {
  if (!comments.value.length) return 0
  const total = comments.value.reduce((sum, c) => sum + Number(c.rating || 0), 0)
  return (total / comments.value.length).toFixed(1)
})

const submitComment = () => {
  if (!newComment.value.user || !newComment.value.text) return
  comments.value.unshift({
    user: newComment.value.user,
    rating: newComment.value.rating,
    text: newComment.value.text,
    time: '刚刚',
  })
  newComment.value = { user: '', rating: 5, text: '' }
}
</script>

<template>
  <div class="two-column">
    <div class="panel">
      <header class="section-title">
        <div>
          <h2>{{ movie.title }}</h2>
          <p class="muted">{{ movie.year }} · {{ movie.genres.join(' / ') }}</p>
        </div>
        <span class="pill-blue">综合评分 {{ avgRating }}</span>
      </header>
      <p class="muted">{{ movie.summary }}</p>
      <div class="tag-row">
        <span v-for="tag in movie.genres" :key="tag" class="tag">{{ tag }}</span>
      </div>
      <div class="section-title" style="margin-top: 16px">
        <div>
          <h2>主要演员</h2>
          <p class="muted">主演阵容</p>
        </div>
      </div>
      <div class="tag-row">
        <RouterLink v-for="name in movie.cast" :key="name" class="tag link" :to="'/actor/paul'">
          {{ name }}
        </RouterLink>
      </div>
    </div>

    <div class="panel">
      <header class="section-title">
        <div>
          <h2>观众评论</h2>
          <p class="muted">分享你的观影体验</p>
        </div>
        <span class="pill">共 {{ comments.length }} 条</span>
      </header>

      <div class="comment-form">
        <div class="field">
          <label>昵称</label>
          <input v-model="newComment.user" placeholder="你的昵称" />
        </div>
        <div class="field">
          <label>评分（1-5）</label>
          <input v-model.number="newComment.rating" type="number" min="1" max="5" />
        </div>
        <div class="field">
          <label>评论</label>
          <textarea v-model="newComment.text" placeholder="写下你的想法"></textarea>
        </div>
        <div class="form-actions">
          <button class="primary-btn" type="button" @click="submitComment">发布</button>
        </div>
      </div>

      <ul class="comment-list">
        <li v-for="(comment, index) in comments" :key="index" class="comment-item">
          <div class="row">
            <strong>{{ comment.user }}</strong>
            <span class="rating">⭐ {{ comment.rating }}</span>
            <span class="muted">{{ comment.time }}</span>
          </div>
          <p class="muted">{{ comment.text }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>
