<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'

const actor = {
  id: 'paul',
  name: '蒂莫西·柴勒梅德',
  knownFor: ['沙丘', '请以你的名字呼唤我', '旺卡'],
  bio: '新生代演员代表，凭借细腻表演在科幻与文艺片中均有亮眼表现。',
  highlights: ['银幕张力强', '青年偶像', '角色塑造细腻'],
}

const comments = ref([
  { user: 'Echo', rating: 5, text: '在沙丘中的成长线非常打动我。', time: '2 小时前' },
  { user: 'Nova', rating: 4, text: '旺卡的表演很灵动，期待更多作品。', time: '昨天' },
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
          <h2>{{ actor.name }}</h2>
          <p class="muted">代表作：{{ actor.knownFor.join('、') }}</p>
        </div>
        <span class="pill-blue">评分 {{ avgRating }}</span>
      </header>
      <p class="muted">{{ actor.bio }}</p>
      <div class="tag-row">
        <span v-for="tag in actor.highlights" :key="tag" class="tag">{{ tag }}</span>
      </div>
      <div class="inline-actions" style="margin-top: 12px">
        <RouterLink class="ghost-btn" to="/movie/dune">查看相关电影</RouterLink>
        <RouterLink class="ghost-btn" to="/role/paul-atreides">查看角色</RouterLink>
      </div>
    </div>

    <div class="panel">
      <header class="section-title">
        <div>
          <h2>评论与评分</h2>
          <p class="muted">分享你对演员的看法</p>
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
