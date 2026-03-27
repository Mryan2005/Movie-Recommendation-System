<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter, RouterLink } from 'vue-router'

const router = useRouter()

const createThumb = (label, color = '#1e3a8a') =>
  `data:image/svg+xml,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='140' height='180'><rect width='100%' height='100%' rx='12' fill='${color}'/><text x='50%' y='52%' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='22' font-family='Inter, sans-serif'>${label}</text></svg>`
  )}`

const role = {
  id: 'paul-atreides',
  name: '保罗·厄崔迪',
  enName: 'Paul Atreides',
  movie: '沙丘2',
  movieId: 'dune',
  actor: '蒂莫西·柴勒梅德',
  actorId: 'paul',
  source: '科幻小说《沙丘》弗兰克·赫伯特',
  summary:
    '阿特雷迪斯家族的贵族子弟，被命运驱使成为沙漠民族弗雷曼人的救世主"奎萨茨哈德拉克"。从一个天赋异禀的少年，背负家族复仇与救世使命，最终以强大的政治与军事力量改写了帝国格局。',
  traits: ['领袖气质', '宿命感', '家族责任', '超凡预知', '双面人格'],
  image: createThumb('保罗', '#1e3a8a'),
  appearance: '金发，蓝色眼睛（接触香料后变为蓝中带蓝），身形修长',
  abilities: ['近身格斗贝尼·杰赛里特技艺', '香料赐予的未来预知能力', '卓越的战略指挥才能'],
}

const comments = ref([
  { user: 'SciFiFan', rating: 5, text: '角色弧线完整，气质契合。', time: '5 小时前' },
  { user: 'MovieLover', rating: 4, text: '内心戏与动作戏结合得很好。', time: '昨天' },
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
    <div class="detail-modal role-detail-modal" :style="modalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="close">
        <span aria-hidden="true">×</span>
      </button>

      <div class="rd-inner">
        <!-- Left: image + identity -->
        <div class="rd-left">
          <div class="rd-image" :style="{ backgroundImage: `url(${role.image})` }"></div>
          <h3 class="rd-name">{{ role.name }}</h3>
          <p class="rd-en-name">{{ role.enName }}</p>
          <div class="rd-identity">
            <div class="rd-id-row">
              <span class="rd-id-label">来源</span>
              <span>{{ role.movie }}</span>
            </div>
            <div class="rd-id-row">
              <span class="rd-id-label">扮演者</span>
              <RouterLink :to="`/actor/${role.actorId}`" class="rd-link">{{ role.actor }}</RouterLink>
            </div>
            <div class="rd-id-row">
              <span class="rd-id-label">原著</span>
              <span>{{ role.source }}</span>
            </div>
          </div>
          <div class="rd-trait-tags">
            <span v-for="trait in role.traits" :key="trait" class="rd-tag">{{ trait }}</span>
          </div>
          <div class="rd-actions">
            <RouterLink :to="`/movie/${role.movieId}`" class="rd-action-btn">查看电影</RouterLink>
            <RouterLink :to="`/actor/${role.actorId}`" class="rd-action-btn">查看演员</RouterLink>
          </div>
        </div>

        <!-- Right: summary + abilities + comments -->
        <div class="rd-right">
          <div class="rd-summary-section">
            <h4 class="rd-section-head">角色简介</h4>
            <p class="rd-summary">{{ role.summary }}</p>
          </div>

          <div class="rd-appearance-section">
            <h4 class="rd-section-head">外貌描述</h4>
            <p class="rd-appearance">{{ role.appearance }}</p>
          </div>

          <div class="rd-abilities-section">
            <h4 class="rd-section-head">能力 / 技能</h4>
            <ul class="rd-ability-list">
              <li v-for="ability in role.abilities" :key="ability" class="rd-ability-item">
                {{ ability }}
              </li>
            </ul>
          </div>

          <div class="rd-comments">
            <h4 class="rd-section-head">
              角色讨论
              <span class="rd-count-badge">{{ comments.length }}</span>
            </h4>
            <div class="rd-comment-form">
              <input v-model="newComment.user" placeholder="昵称" class="rd-input" />
              <input
                v-model.number="newComment.rating"
                type="number"
                min="1"
                max="5"
                placeholder="1-5"
                class="rd-input rd-input-sm"
              />
              <input
                v-model="newComment.text"
                placeholder="发表你的解读…"
                class="rd-input rd-input-flex"
                @keyup.enter="submitComment"
              />
              <button class="rd-submit-btn" type="button" @click="submitComment">发布</button>
            </div>
            <ul class="rd-comment-list">
              <li v-for="(c, i) in comments" :key="i" class="rd-comment-item">
                <strong>{{ c.user }}</strong>
                <span class="rd-star-rating">{{ '★'.repeat(Number(c.rating)) }}</span>
                <span class="rd-comment-text">{{ c.text }}</span>
                <span class="rd-time">{{ c.time }}</span>
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

.role-detail-modal {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.rd-inner {
  display: flex;
  gap: 16px;
  height: 100%;
  padding-top: 8px;
  overflow: hidden;
}

/* ── Left column ── */
.rd-left {
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

.rd-image {
  width: 130px;
  height: 170px;
  border-radius: 12px;
  background-size: cover;
  background-position: center;
  background-color: rgba(255, 255, 255, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.3);
  flex-shrink: 0;
}

.rd-name {
  margin: 0;
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  text-align: center;
}

.rd-en-name {
  margin: 0;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.65);
  text-align: center;
}

.rd-identity {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 5px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  padding: 8px 0;
}

.rd-id-row {
  display: flex;
  gap: 6px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.9);
  justify-content: space-between;
  align-items: flex-start;
}

.rd-id-label {
  color: rgba(255, 255, 255, 0.55);
  flex-shrink: 0;
}

.rd-link {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.rd-trait-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  justify-content: center;
}

.rd-tag {
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.3);
  font-size: 11px;
  color: #fff;
}

.rd-actions {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
}

.rd-action-btn {
  display: block;
  text-align: center;
  padding: 6px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  transition: background 0.15s ease;
}

.rd-action-btn:hover {
  background: rgba(255, 255, 255, 0.28);
}

/* ── Right column ── */
.rd-right {
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

.rd-section-head {
  margin: 0 0 8px;
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 6px;
}

.rd-summary-section,
.rd-appearance-section,
.rd-abilities-section {
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  padding-bottom: 12px;
}

.rd-summary,
.rd-appearance {
  margin: 0;
  font-size: 13px;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.85);
}

.rd-ability-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.rd-ability-item {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 6px 10px;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.9);
}

.rd-ability-item::before {
  content: '✦ ';
  color: rgba(255, 255, 255, 0.5);
  font-size: 11px;
}

/* ── Comments ── */
.rd-count-badge {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 999px;
  padding: 1px 7px;
  font-size: 12px;
  font-weight: 600;
}

.rd-comment-form {
  display: flex;
  gap: 6px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.rd-input {
  padding: 6px 10px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  font-size: 13px;
  outline: none;
  min-width: 0;
}

.rd-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.rd-input-sm {
  width: 52px;
}

.rd-input-flex {
  flex: 1;
  min-width: 120px;
}

.rd-submit-btn {
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

.rd-submit-btn:hover {
  background: rgba(255, 255, 255, 0.35);
}

.rd-comment-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rd-comment-item {
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

.rd-star-rating {
  color: #fbbf24;
  font-size: 12px;
}

.rd-comment-text {
  flex: 1;
  min-width: 0;
}

.rd-time {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.5);
  white-space: nowrap;
}
</style>
