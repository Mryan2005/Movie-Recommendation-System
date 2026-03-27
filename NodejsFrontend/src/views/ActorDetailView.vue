<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const createThumb = (label, color = '#1e3a8a') =>
  `data:image/svg+xml,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='140' height='180'><rect width='100%' height='100%' rx='12' fill='${color}'/><text x='50%' y='52%' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='22' font-family='Inter, sans-serif'>${label}</text></svg>`
  )}`

const actor = {
  id: 'paul',
  name: '蒂莫西·柴勒梅德',
  enName: 'Timothée Chalamet',
  nationality: '美国',
  birthdate: '1995-12-27',
  birthplace: '美国纽约',
  occupation: '演员',
  bio: '出生于纽约，曾就读哥伦比亚大学戏剧系，2017 年以《请以你的名字呼唤我》一举成名，成为当时最年轻的奥斯卡影帝提名者之一。凭借细腻而充满张力的表演风格，在科幻史诗与文艺片中均有亮眼表现，是新生代演员的代表人物。',
  highlights: ['银幕张力强', '青年偶像', '角色塑造细腻', '奥斯卡提名'],
  image: createThumb('柴', '#1e3a8a'),
  films: [
    { title: '沙丘2', year: 2024, role: '保罗·厄崔迪' },
    { title: '旺卡', year: 2023, role: '旺卡' },
    { title: '沙丘', year: 2021, role: '保罗·厄崔迪' },
    { title: '小妇人', year: 2019, role: '劳里' },
    { title: '请以你的名字呼唤我', year: 2017, role: '以利奥' },
  ],
}

const comments = ref([
  { user: 'Echo', rating: 5, text: '在沙丘中的成长线非常打动我。', time: '2 小时前' },
  { user: 'Nova', rating: 4, text: '旺卡的表演很灵动，期待更多作品。', time: '昨天' },
])

const newComment = ref({ user: '', rating: 5, text: '' })

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

const DEFAULT_SIZE = { width: 911, height: 568 }
const MIN_SIZE = { width: 620, height: 360 }
const MAX_SIZE = { width: 1200, height: 800 }

const modalSize = ref({ ...DEFAULT_SIZE })
const resizeState = ref({ active: false, startX: 0, startY: 0, startW: 0, startH: 0 })

const clampSize = (w, h) => {
  const maxW = typeof window !== 'undefined' ? Math.min(MAX_SIZE.width, window.innerWidth - 32) : MAX_SIZE.width
  const maxH = typeof window !== 'undefined' ? Math.min(MAX_SIZE.height, window.innerHeight - 32) : MAX_SIZE.height
  return {
    width: Math.min(Math.max(w, MIN_SIZE.width), Math.max(maxW, MIN_SIZE.width)),
    height: Math.min(Math.max(h, MIN_SIZE.height), Math.max(maxH, MIN_SIZE.height)),
  }
}

const handleResizeMove = (e) => {
  if (!resizeState.value.active) return
  const dx = e.clientX - resizeState.value.startX
  const dy = e.clientY - resizeState.value.startY
  modalSize.value = clampSize(resizeState.value.startW + dx, resizeState.value.startH + dy)
}

const stopResizeListeners = () => {
  if (typeof window === 'undefined') return
  window.removeEventListener('mousemove', handleResizeMove)
  window.removeEventListener('mouseup', stopResize)
}

const stopResize = () => {
  resizeState.value.active = false
  stopResizeListeners()
}

const startResize = (e) => {
  e.preventDefault()
  resizeState.value = {
    active: true,
    startX: e.clientX,
    startY: e.clientY,
    startW: modalSize.value.width,
    startH: modalSize.value.height,
  }
  if (typeof window !== 'undefined') {
    window.addEventListener('mousemove', handleResizeMove)
    window.addEventListener('mouseup', stopResize)
  }
}

const modalStyle = computed(() => ({
  width: `${modalSize.value.width}px`,
  height: `${modalSize.value.height}px`,
}))

onMounted(() => {
  modalSize.value = clampSize(DEFAULT_SIZE.width, DEFAULT_SIZE.height)
})

onBeforeUnmount(() => {
  stopResizeListeners()
})

const close = () => router.back()
</script>

<template>
  <div class="detail-backdrop">
    <div class="detail-modal actor-detail-modal" :style="modalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="close">
        <span aria-hidden="true">×</span>
      </button>

      <div class="ad-inner">
        <!-- Left: photo + basic info -->
        <div class="ad-left">
          <div class="ad-photo" :style="{ backgroundImage: `url(${actor.image})` }"></div>
          <h3 class="ad-name">{{ actor.name }}</h3>
          <p class="ad-en-name">{{ actor.enName }}</p>
          <div class="ad-info-list">
            <div class="ad-info-row">
              <span class="ad-info-label">国籍</span>
              <span>{{ actor.nationality }}</span>
            </div>
            <div class="ad-info-row">
              <span class="ad-info-label">生日</span>
              <span>{{ actor.birthdate }}</span>
            </div>
            <div class="ad-info-row">
              <span class="ad-info-label">出生地</span>
              <span>{{ actor.birthplace }}</span>
            </div>
            <div class="ad-info-row">
              <span class="ad-info-label">职业</span>
              <span>{{ actor.occupation }}</span>
            </div>
          </div>
          <div class="ad-tags">
            <span v-for="tag in actor.highlights" :key="tag" class="ad-tag">{{ tag }}</span>
          </div>
        </div>

        <!-- Right: bio + filmography + comments -->
        <div class="ad-right">
          <div class="ad-bio-section">
            <h4 class="ad-section-head">简介</h4>
            <p class="ad-bio">{{ actor.bio }}</p>
          </div>

          <div class="ad-films-section">
            <h4 class="ad-section-head">主要作品</h4>
            <ul class="ad-film-list">
              <li v-for="film in actor.films" :key="film.title" class="ad-film-item">
                <span class="ad-film-year">{{ film.year }}</span>
                <span class="ad-film-title">{{ film.title }}</span>
                <span class="ad-film-role">饰 {{ film.role }}</span>
              </li>
            </ul>
          </div>

          <div class="ad-comments">
            <h4 class="ad-section-head">
              评论与评分
              <span class="ad-count-badge">{{ comments.length }}</span>
            </h4>
            <div class="ad-comment-form">
              <input v-model="newComment.user" placeholder="昵称" class="ad-input" />
              <input
                v-model.number="newComment.rating"
                type="number"
                min="1"
                max="5"
                placeholder="1-5"
                class="ad-input ad-input-sm"
              />
              <input
                v-model="newComment.text"
                placeholder="写下你对演员的看法…"
                class="ad-input ad-input-flex"
                @keyup.enter="submitComment"
              />
              <button class="ad-submit-btn" type="button" @click="submitComment">发布</button>
            </div>
            <ul class="ad-comment-list">
              <li v-for="(c, i) in comments" :key="i" class="ad-comment-item">
                <strong>{{ c.user }}</strong>
                <span class="ad-star-rating">{{ '★'.repeat(Number(c.rating)) }}</span>
                <span class="ad-comment-text">{{ c.text }}</span>
                <span class="ad-time">{{ c.time }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="resize-handle" @mousedown="startResize"></div>
    </div>
  </div>
</template>

<style scoped>
.detail-backdrop {
  cursor: default;
}

.actor-detail-modal {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.ad-inner {
  display: flex;
  gap: 16px;
  height: 100%;
  padding-top: 8px;
  overflow: hidden;
}

/* ── Left column ── */
.ad-left {
  width: 200px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.3) transparent;
}

.ad-photo {
  width: 130px;
  height: 170px;
  border-radius: 12px;
  background-size: cover;
  background-position: center;
  background-color: rgba(255, 255, 255, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.3);
  flex-shrink: 0;
}

.ad-name {
  margin: 0;
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  text-align: center;
}

.ad-en-name {
  margin: 0;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.65);
  text-align: center;
}

.ad-info-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  padding: 8px 0;
}

.ad-info-row {
  display: flex;
  gap: 6px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.9);
  justify-content: space-between;
}

.ad-info-label {
  color: rgba(255, 255, 255, 0.55);
  flex-shrink: 0;
}

.ad-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  justify-content: center;
}

.ad-tag {
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.3);
  font-size: 11px;
  color: #fff;
}

/* ── Right column ── */
.ad-right {
  flex: 1;
  min-width: 0;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding-right: 4px;
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.3) transparent;
}

.ad-section-head {
  margin: 0 0 8px;
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 6px;
}

.ad-bio-section {
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  padding-bottom: 12px;
}

.ad-bio {
  margin: 0;
  font-size: 13px;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.85);
}

/* ── Films ── */
.ad-films-section {
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  padding-bottom: 12px;
}

.ad-film-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ad-film-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 6px 10px;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.9);
}

.ad-film-year {
  color: rgba(255, 255, 255, 0.55);
  font-size: 12px;
  min-width: 36px;
}

.ad-film-title {
  font-weight: 600;
  flex: 1;
}

.ad-film-role {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
}

/* ── Comments ── */
.ad-count-badge {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 999px;
  padding: 1px 7px;
  font-size: 12px;
  font-weight: 600;
}

.ad-comment-form {
  display: flex;
  gap: 6px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.ad-input {
  padding: 6px 10px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  font-size: 13px;
  outline: none;
  min-width: 0;
}

.ad-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.ad-input-sm {
  width: 52px;
}

.ad-input-flex {
  flex: 1;
  min-width: 120px;
}

.ad-submit-btn {
  padding: 6px 14px;
  border-radius: 8px;
  border: none;
  background: rgba(255, 255, 255, 0.25);
  color: #fff;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.ad-submit-btn:hover {
  background: rgba(255, 255, 255, 0.35);
}

.ad-comment-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ad-comment-item {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.9);
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
}

.ad-star-rating {
  color: #fbbf24;
  font-size: 12px;
}

.ad-comment-text {
  flex: 1;
  min-width: 0;
}

.ad-time {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.5);
  white-space: nowrap;
}
</style>
