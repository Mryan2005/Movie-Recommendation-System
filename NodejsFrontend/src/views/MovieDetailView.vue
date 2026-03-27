<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const createThumb = (label, color = '#1e3a8a') =>
  `data:image/svg+xml,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='140' height='200'><rect width='100%' height='100%' rx='10' fill='${color}'/><text x='50%' y='52%' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='16' font-family='Inter, sans-serif'>${label}</text></svg>`
  )}`

const movie = {
  id: 'dune',
  title: '沙丘2',
  originalTitle: 'Dune: Part Two',
  year: 2024,
  duration: '166 分钟',
  genres: ['科幻', '史诗', 'IMAX'],
  director: '丹尼斯·维伦纽瓦',
  rating: 8.2,
  ratingCount: '182,443 人评价',
  summary:
    '保罗·厄崔迪联手弗雷曼人民，踏上一条复仇之路，同时阻止唯一能够拯救他家族的恐怖命运。当他面临在挚爱与宇宙命运之间做出抉择时，他预知成为救世主将带来一场残酷的圣战。保罗带领弗雷曼人民对抗帝国与哈克南家族，视觉与叙事兼具的科幻史诗。',
  cast: [
    { name: '蒂莫西·柴勒梅德', role: '保罗·厄崔迪', image: createThumb('柴', '#1e3a8a') },
    { name: '赞达亚', role: '契尼', image: createThumb('赞', '#1e3a5f') },
    { name: '丽贝卡·弗格森', role: '拉蒂嘉夫人', image: createThumb('丽', '#1e40af') },
    { name: '奥斯汀·巴特勒', role: '费德-罗萨', image: createThumb('巴', '#1e3a8a') },
    { name: '弗洛伦丝·皮尤', role: '伊鲁兰公主', image: createThumb('皮', '#1e3a5f') },
  ],
  image: createThumb('沙丘2', '#1e3a8a'),
  country: '美国',
  language: '英语',
  releaseDate: '2024-03-01（中国大陆）',
}

const comments = ref([
  { user: 'FilmGeek', rating: 5, text: 'IMAX 体验震撼，配乐和场面全程高能。', time: '1 天前' },
  { user: 'Aria', rating: 4, text: '叙事更紧凑，想二刷。', time: '3 天前' },
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

const starsForRating = (r) => {
  const filled = Math.round(r / 2)
  return '★'.repeat(filled) + '☆'.repeat(5 - filled)
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
    <div class="detail-modal movie-detail-modal" :style="modalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="close">
        <span aria-hidden="true">×</span>
      </button>

      <div class="md-inner">
        <!-- Left: poster + score -->
        <div class="md-left">
          <div class="md-poster" :style="{ backgroundImage: `url(${movie.image})` }"></div>
          <div class="md-score-block">
            <span class="md-score">{{ movie.rating }}</span>
            <div class="md-stars">{{ starsForRating(movie.rating) }}</div>
            <span class="md-score-count">{{ movie.ratingCount }}</span>
          </div>
          <div class="md-genre-tags">
            <span v-for="g in movie.genres" :key="g" class="md-tag">{{ g }}</span>
          </div>
        </div>

        <!-- Right: details + cast + comments -->
        <div class="md-right">
          <div class="md-title-block">
            <h2 class="md-title">{{ movie.title }}</h2>
            <p class="md-original-title">{{ movie.originalTitle }}</p>
            <div class="md-meta">
              <span>{{ movie.year }}</span>
              <span>{{ movie.duration }}</span>
              <span>{{ movie.country }}</span>
              <span>{{ movie.language }}</span>
            </div>
          </div>

          <div class="md-info">
            <p><span class="info-label">导演</span>{{ movie.director }}</p>
            <p><span class="info-label">上映</span>{{ movie.releaseDate }}</p>
            <p class="md-synopsis">{{ movie.summary }}</p>
          </div>

          <div class="md-cast">
            <h4 class="md-section-head">主演</h4>
            <div class="md-cast-list">
              <div v-for="actor in movie.cast" :key="actor.name" class="md-cast-item">
                <div class="md-cast-thumb" :style="{ backgroundImage: `url(${actor.image})` }"></div>
                <div class="md-cast-name">{{ actor.name }}</div>
                <div class="md-cast-role">{{ actor.role }}</div>
              </div>
            </div>
          </div>

          <div class="md-comments">
            <h4 class="md-section-head">
              观众评论
              <span class="md-count-badge">{{ comments.length }}</span>
            </h4>
            <div class="md-comment-form">
              <input v-model="newComment.user" placeholder="昵称" class="md-input" />
              <input
                v-model.number="newComment.rating"
                type="number"
                min="1"
                max="5"
                placeholder="1-5"
                class="md-input md-input-sm"
              />
              <input
                v-model="newComment.text"
                placeholder="写下你的想法…"
                class="md-input md-input-flex"
                @keyup.enter="submitComment"
              />
              <button class="md-submit-btn" type="button" @click="submitComment">发布</button>
            </div>
            <ul class="md-comment-list">
              <li v-for="(c, i) in comments" :key="i" class="md-comment-item">
                <strong>{{ c.user }}</strong>
                <span class="md-star-rating">{{ '★'.repeat(Number(c.rating)) }}</span>
                <span class="md-comment-text">{{ c.text }}</span>
                <span class="md-time">{{ c.time }}</span>
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

.movie-detail-modal {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.md-inner {
  display: flex;
  gap: 16px;
  height: 100%;
  padding-top: 8px;
  overflow: hidden;
}

/* ── Left column ── */
.md-left {
  width: 190px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.md-poster {
  width: 130px;
  height: 185px;
  border-radius: 10px;
  background-size: cover;
  background-position: center;
  background-color: rgba(15, 23, 42, 0.06);
  border: 2px solid rgba(15, 23, 42, 0.12);
  flex-shrink: 0;
}

.md-score-block {
  text-align: center;
}

.md-score {
  font-size: 36px;
  font-weight: 800;
  color: #1e293b;
  line-height: 1;
}

.md-stars {
  font-size: 16px;
  color: #f59e0b;
  letter-spacing: 2px;
  margin: 2px 0;
}

.md-score-count {
  font-size: 11px;
  color: rgba(15, 23, 42, 0.5);
}

.md-genre-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  justify-content: center;
}

.md-tag {
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.07);
  border: 1px solid rgba(15, 23, 42, 0.12);
  font-size: 12px;
  color: #334155;
}

/* ── Right column ── */
.md-right {
  flex: 1;
  min-width: 0;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding-right: 4px;
  scrollbar-width: thin;
  scrollbar-color: rgba(15, 23, 42, 0.2) transparent;
}

.md-title {
  margin: 0 0 2px;
  font-size: 22px;
  font-weight: 800;
  color: #0f172a;
}

.md-original-title {
  margin: 0 0 6px;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.5);
}

.md-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.65);
}

.md-meta span::after {
  content: '·';
  margin-left: 8px;
  opacity: 0.5;
}

.md-meta span:last-child::after {
  content: '';
}

.md-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.80);
  border-top: 1px solid rgba(15, 23, 42, 0.10);
  padding-top: 10px;
}

.md-info p {
  margin: 0;
}

.info-label {
  display: inline-block;
  width: 32px;
  color: rgba(15, 23, 42, 0.45);
  margin-right: 6px;
}

.md-synopsis {
  margin-top: 4px !important;
  line-height: 1.6;
  color: rgba(15, 23, 42, 0.70) !important;
}

.md-section-head {
  margin: 0 0 8px;
  font-size: 14px;
  font-weight: 700;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 6px;
}

.md-count-badge {
  background: rgba(15, 23, 42, 0.08);
  border-radius: 999px;
  padding: 1px 7px;
  font-size: 12px;
  font-weight: 600;
  color: #334155;
}

/* ── Cast ── */
.md-cast {
  border-top: 1px solid rgba(15, 23, 42, 0.10);
  padding-top: 10px;
}

.md-cast-list {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.md-cast-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  width: 68px;
  text-align: center;
}

.md-cast-thumb {
  width: 52px;
  height: 52px;
  border-radius: 8px;
  background-size: cover;
  background-position: center;
  background-color: rgba(15, 23, 42, 0.06);
  border: 1px solid rgba(15, 23, 42, 0.10);
}

.md-cast-name {
  font-size: 11px;
  font-weight: 600;
  color: #1e293b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 68px;
}

.md-cast-role {
  font-size: 10px;
  color: rgba(15, 23, 42, 0.50);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 68px;
}

/* ── Comments ── */
.md-comments {
  border-top: 1px solid rgba(15, 23, 42, 0.10);
  padding-top: 10px;
}

.md-comment-form {
  display: flex;
  gap: 6px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.md-input {
  padding: 6px 10px;
  border-radius: 8px;
  border: 1px solid rgba(15, 23, 42, 0.15);
  background: rgba(15, 23, 42, 0.04);
  color: #1e293b;
  font-size: 13px;
  outline: none;
  min-width: 0;
}

.md-input::placeholder {
  color: rgba(15, 23, 42, 0.38);
}

.md-input-sm {
  width: 52px;
}

.md-input-flex {
  flex: 1;
  min-width: 120px;
}

.md-submit-btn {
  padding: 6px 14px;
  border-radius: 8px;
  border: 1px solid rgba(15, 23, 42, 0.14);
  background: rgba(15, 23, 42, 0.08);
  color: #1e293b;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.md-submit-btn:hover {
  background: rgba(15, 23, 42, 0.14);
}

.md-comment-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.md-comment-item {
  background: rgba(15, 23, 42, 0.04);
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.80);
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
}

.md-star-rating {
  color: #f59e0b;
  font-size: 12px;
}

.md-comment-text {
  flex: 1;
  min-width: 0;
}

.md-time {
  font-size: 11px;
  color: rgba(15, 23, 42, 0.38);
  white-space: nowrap;
}
</style>
