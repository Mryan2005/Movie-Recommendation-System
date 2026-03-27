<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { defaultActor } from '../data/actorProfiles'

const router = useRouter()
const props = defineProps({
  actor: {
    type: Object,
    default: () => defaultActor,
  },
  inline: {
    type: Boolean,
    default: false,
  },
})
const emit = defineEmits(['close'])
const modalRef = ref(null)
const closeBtnRef = ref(null)

const actor = computed(() => props.actor || defaultActor)

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
  focusModal()
})

onBeforeUnmount(() => {
  stopResizeListeners()
})

const close = () => {
  if (props.inline) {
    emit('close')
    return
  }
  router.back()
}

const handleKeydown = (event) => {
  if (!props.inline || event.key !== 'Tab') return
  const focusable = modalRef.value?.querySelectorAll(
    'button, [href], input, textarea, select, [tabindex]:not([tabindex="-1"])'
  )
  if (!focusable || focusable.length === 0) return
  const first = focusable[0]
  const last = focusable[focusable.length - 1]
  if (event.shiftKey) {
    if (document.activeElement === first) {
      event.preventDefault()
      last.focus()
    }
  } else if (document.activeElement === last) {
    event.preventDefault()
    first.focus()
  }
}

const focusModal = () => {
  if (!props.inline) return
  nextTick(() => {
    closeBtnRef.value?.focus?.()
  })
}

watch(
  () => (props.inline ? props.actor : null),
  (val) => {
    if (val) focusModal()
  }
)
</script>

<template>
  <div class="detail-backdrop">
    <div ref="modalRef" class="detail-modal actor-detail-modal" :style="modalStyle" @keydown="handleKeydown">
      <button ref="closeBtnRef" class="close-btn" type="button" aria-label="关闭" @click="close">
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
  scrollbar-color: rgba(15, 23, 42, 0.2) transparent;
}

.ad-photo {
  width: 130px;
  height: 170px;
  border-radius: 12px;
  background-size: cover;
  background-position: center;
  background-color: rgba(15, 23, 42, 0.06);
  border: 2px solid rgba(15, 23, 42, 0.12);
  flex-shrink: 0;
}

.ad-name {
  margin: 0;
  font-size: 18px;
  font-weight: 800;
  color: #0f172a;
  text-align: center;
}

.ad-en-name {
  margin: 0;
  font-size: 12px;
  color: rgba(15, 23, 42, 0.50);
  text-align: center;
}

.ad-info-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
  border-top: 1px solid rgba(15, 23, 42, 0.10);
  border-bottom: 1px solid rgba(15, 23, 42, 0.10);
  padding: 8px 0;
}

.ad-info-row {
  display: flex;
  gap: 6px;
  font-size: 12px;
  color: rgba(15, 23, 42, 0.80);
  justify-content: space-between;
}

.ad-info-label {
  color: rgba(15, 23, 42, 0.45);
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
  background: rgba(15, 23, 42, 0.07);
  border: 1px solid rgba(15, 23, 42, 0.12);
  font-size: 11px;
  color: #334155;
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
  scrollbar-color: rgba(15, 23, 42, 0.2) transparent;
}

.ad-section-head {
  margin: 0 0 8px;
  font-size: 14px;
  font-weight: 700;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 6px;
}

.ad-bio-section {
  border-bottom: 1px solid rgba(15, 23, 42, 0.10);
  padding-bottom: 12px;
}

.ad-bio {
  margin: 0;
  font-size: 13px;
  line-height: 1.7;
  color: rgba(15, 23, 42, 0.72);
}

/* ── Films ── */
.ad-films-section {
  border-bottom: 1px solid rgba(15, 23, 42, 0.10);
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
  background: rgba(15, 23, 42, 0.04);
  border-radius: 8px;
  padding: 6px 10px;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.80);
}

.ad-film-year {
  color: rgba(15, 23, 42, 0.45);
  font-size: 12px;
  min-width: 36px;
}

.ad-film-title {
  font-weight: 600;
  flex: 1;
  color: #1e293b;
}

.ad-film-role {
  font-size: 12px;
  color: rgba(15, 23, 42, 0.50);
}

/* ── Comments ── */
.ad-count-badge {
  background: rgba(15, 23, 42, 0.08);
  border-radius: 999px;
  padding: 1px 7px;
  font-size: 12px;
  font-weight: 600;
  color: #334155;
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
  border: 1px solid rgba(15, 23, 42, 0.15);
  background: rgba(15, 23, 42, 0.04);
  color: #1e293b;
  font-size: 13px;
  outline: none;
  min-width: 0;
}

.ad-input::placeholder {
  color: rgba(15, 23, 42, 0.38);
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
  border: 1px solid rgba(15, 23, 42, 0.14);
  background: rgba(15, 23, 42, 0.08);
  color: #1e293b;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.ad-submit-btn:hover {
  background: rgba(15, 23, 42, 0.14);
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

.ad-star-rating {
  color: #f59e0b;
  font-size: 12px;
}

.ad-comment-text {
  flex: 1;
  min-width: 0;
}

.ad-time {
  font-size: 11px;
  color: rgba(15, 23, 42, 0.38);
  white-space: nowrap;
}
</style>
