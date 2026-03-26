<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'

const role = {
  id: 'paul-atreides',
  name: '保罗·厄崔迪',
  movie: '沙丘',
  actor: '蒂莫西·柴勒梅德',
  summary: '从贵族子弟成长为“奎萨茨哈德拉克”，背负命运与复仇的科幻史诗角色。',
  traits: ['领袖气质', '宿命感', '家族责任'],
}

const comments = ref([
  { user: 'SciFiFan', rating: 5, text: '角色弧线完整，气质契合。', time: '5 小时前' },
  { user: 'MovieLover', rating: 4, text: '内心戏与动作戏结合得很好。', time: '昨天' },
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
          <h2>{{ role.name }}</h2>
          <p class="muted">{{ role.movie }} · 扮演者：{{ role.actor }}</p>
        </div>
        <span class="pill-blue">角色评分 {{ avgRating }}</span>
      </header>
      <p class="muted">{{ role.summary }}</p>
      <div class="tag-row">
        <span v-for="tag in role.traits" :key="tag" class="tag">{{ tag }}</span>
      </div>
      <div class="inline-actions" style="margin-top: 12px">
        <RouterLink class="ghost-btn" to="/movie/dune">查看电影</RouterLink>
        <RouterLink class="ghost-btn" to="/actor/paul">查看演员</RouterLink>
      </div>
    </div>

    <div class="panel">
      <header class="section-title">
        <div>
          <h2>角色讨论</h2>
          <p class="muted">发表你的解读和评分</p>
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
        <li v-for="(comment, index) in comments" :key="comment.user + index" class="comment-item">
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
