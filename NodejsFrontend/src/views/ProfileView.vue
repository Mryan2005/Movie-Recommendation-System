<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const createThumb = (label, color = '#334155') =>
  `data:image/svg+xml,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='140' height='180'><rect width='100%' height='100%' rx='14' fill='${color}'/><text x='50%' y='55%' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='20' font-family='Inter, sans-serif'>${label}</text></svg>`
  )}`

const profile = ref({
  name: 'Mryan2005',
  email: 'mryan2005@mryan2005.top',
  gender: '男',
  avatar: createThumb('Yan', '#7c3aed'),
  bio: '热爱科幻与悬疑，偏爱大卫·芬奇的作品。',
  city: '上海',
  signature: '“故事，就是人对抗时间的方式。”',
})

const favorites = []

const watching = [
  { title: '禁闭岛', progress: '已看 100%' },
  { title: '降临', progress: '待看' },
]

const likedMovies = ref([
  {
    title: '少林足球',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('少林足球', '#0ea5e9'),
  },
  {
    title: '赌神',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('赌神', '#1f2937'),
  },
  {
    title: '六福喜事',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('六福喜事', '#475569'),
  },
  {
    title: '功夫',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('功夫', '#7c3aed'),
  },
  {
    title: '上海滩',
    genre: '民国，爱情',
    language: '粤语',
    type: '电视剧',
    image: createThumb('上海滩', '#475569'),
  },
])

const stats = computed(() => {
  const genreMap = new Map()
  const languageMap = new Map()
  const typeMap = new Map()
  likedMovies.value.forEach((m) => {
    genreMap.set(m.genre, (genreMap.get(m.genre) || 0) + 1)
    languageMap.set(m.language, (languageMap.get(m.language) || 0) + 1)
    typeMap.set(m.type, (typeMap.get(m.type) || 0) + 1)
  })
  return {
    genres: Array.from(genreMap.entries()).map(([label, count]) => ({ label, count })),
    languages: Array.from(languageMap.entries()).map(([label, count]) => ({ label, count })),
    types: Array.from(typeMap.entries()).map(([label, count]) => ({ label, count })),
  }
})
const showStats = ref(false)
const listModal = ref(null)

const favoriteRoles = ref([
  {
    name: '月代雪',
    from: '魔法少女的魔女审判',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/copilot/add-movie-recommendation-home-login-register/imgs/Tsukishiro%20Yuki.png?raw=true',
  },
  {
    name: '伊蕾娜',
    from: '魔女之旅',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/copilot/add-movie-recommendation-home-login-register/imgs/Elaina.jpg?raw=true',
  },
  {
    name: '太宰治',
    from: '文豪野犬',
    image: createThumb('太宰', '#475569'),
  },
  {
    name: '温迪',
    from: '原神',
    image: createThumb('温迪', '#0ea5e9'),
  },
  {
    name: '白钰袖',
    from: '风灵玉秀',
    image: 'https://isaacsimplusros2.mryan2005.top/img/avatar.png',
  },
  {
    name: '朝武芳乃',
    from: '千恋万花',
    image: createThumb('朝武芳乃', '#7c3aed'),
  },
  {
    name: '丛雨',
    from: '千恋万花',
    image: createThumb('丛雨', '#1f2937'),
  },
  {
    name: '东海帝王',
    from: 'Pretty Derby',
    image: createThumb('东海帝王', '#475569'),
  },
  {
    name: '秋川弥生',
    from: 'Pretty Derby',
    image: createThumb('秋川弥生', '#7c3aed'),
  },
  {
    name: '堂吉诃德',
    from: '堂吉诃德',
    image: createThumb('堂吉诃德', '#0ea5e9'),
  },
  {
    name: '卡提希娅',
    from: '鸣潮',
    image: createThumb('卡提希娅', '#475569'),
  },
  {
    name: '菲比',
    from: '鸣潮',
    image: createThumb('菲比', '#1f2937'),
  },
  {
    name: '今汐',
    from: '鸣潮',
    image: createThumb('今汐', '#7c3aed'),
  },
  {
    name: '彦卿',
    from: '崩坏：星穹铁道',
    image: createThumb('彦卿', '#0ea5e9'),
  },
  {
    name: '派蒙',
    from: '原神',
    image: createThumb('派蒙', '#475569'),
  },
  {
    name: '灰原哀',
    from: '名侦探柯南',
    image: createThumb('灰原', '#1f2937'),
  },
  {
    name: '夏洛克',
    from: '神探夏洛克',
    image: createThumb('SH', '#334155'),
  },
  {
    name: '憨豆先生',
    from: '憨豆先生',
    image: createThumb('憨豆', '#334155'),
  },
])
const cosplayRoles = ref([
  {
    name: '月代雪',
    from: '魔法少女的魔女审判',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/copilot/add-movie-recommendation-home-login-register/imgs/Tsukishiro%20Yuki.png?raw=true',
  },
  {
    name: '温迪',
    from: '原神',
    image: createThumb('温迪', '#0ea5e9'),
  },
  {
    name: '白钰袖',
    from: '风灵玉秀',
    image: 'https://isaacsimplusros2.mryan2005.top/img/avatar.png',
  },
  {
    name: '朝武芳乃',
    from: '千恋万花',
    image: createThumb('朝武芳乃', '#7c3aed'),
  },
  {
    name: '灰原哀',
    from: '名侦探柯南',
    image: createThumb('灰原', '#1f2937'),
  },
  {
    name: '堂吉诃德',
    from: '堂吉诃德',
    image: createThumb('堂吉诃德', '#0ea5e9'),
  },
  {
    name: '憨豆先生',
    from: '憨豆先生',
    image: createThumb('憨豆', '#334155'),
  },
  {
    name: '夏洛克',
    from: '神探夏洛克',
    image: createThumb('SH', '#334155'),
  },
])
const favoriteActors = ref([
  {
    name: '周星驰',
    image: createThumb('周星驰', '#7c3aed'),
  },
  { name: '周润发', image: createThumb('周润发', '#0ea5e9') },
  { name: '黄子华', image: createThumb('黄子华', '#1f2937') },
  { name: '谢君豪', image: createThumb('谢君豪', '#475569') },
  { name: '王志文', image: createThumb('王志文', '#334155') },
  { name: '林栋甫', image: createThumb('林栋甫', '#475569') },
  { name: '姜文', image: createThumb('姜文', '#475569') },
])

const newActorName = ref('')
const newActorImage = ref('')
const favoriteLanguages = ref([
  { name: '粤语', image: createThumb('粤', '#0ea5e9') },
  { name: '国语', image: createThumb('中', '#7c3aed') },
  { name: '英语', image: createThumb('EN', '#0ea5e9') },
])
const newLanguageName = ref('')
const newLanguageImage = ref('')
const newRole = ref({ name: '', from: '', image: '' })
const newCos = ref({ name: '', from: '', image: '' })
const newMovie = ref({ title: '', genre: '', language: '', type: '', image: '' })
const addModal = ref(null)
const DEFAULT_MODAL_SIZE = { width: 911, height: 568 }
const modalSize = ref({ ...DEFAULT_MODAL_SIZE })
const resizeState = ref({ active: false, startX: 0, startY: 0, startW: DEFAULT_MODAL_SIZE.width, startH: DEFAULT_MODAL_SIZE.height })
const MIN_SIZE = { width: 620, height: 360 }
const MAX_SIZE = { width: 1200, height: 800 }
const showActorEditor = ref(false)
const showLanguageEditor = ref(false)
const showRoleEditor = ref(false)
const showCosEditor = ref(false)
const showMovieEditor = ref(false)
const detailModal = ref(null)
const visibleActors = computed(() => favoriteActors.value.map((item, idx) => ({ item, idx })).slice(0, 10))
const visibleRoles = computed(() => favoriteRoles.value.map((item, idx) => ({ item, idx })).slice(0, 10))
const visibleCos = computed(() => cosplayRoles.value.map((item, idx) => ({ item, idx })).slice(0, 10))
const visibleMovies = computed(() => likedMovies.value.map((item, idx) => ({ item, idx })).slice(0, 5))

const barWidth = (list, count) => {
  const max = Math.max(...(list?.map((i) => i.count) || [1]), 1)
  return `${Math.max((count / max) * 100, 8)}%`
}

const addActor = () => {
  const name = newActorName.value.trim()
  if (!name) return false
  const image = newActorImage.value.trim() || createThumb(name)
  favoriteActors.value.push({ name, image })
  newActorName.value = ''
  newActorImage.value = ''
  return true
}

const removeActor = (index) => favoriteActors.value.splice(index, 1)

const addLanguage = () => {
  const name = newLanguageName.value.trim()
  if (!name) return false
  const image = newLanguageImage.value.trim() || createThumb(name)
  favoriteLanguages.value.push({ name, image })
  newLanguageName.value = ''
  newLanguageImage.value = ''
  return true
}

const removeLanguage = (index) => favoriteLanguages.value.splice(index, 1)

const addRole = () => {
  const name = newRole.value.name.trim()
  const from = newRole.value.from.trim()
  if (!name || !from) return false
  const image = newRole.value.image.trim() || createThumb(name)
  favoriteRoles.value.push({ name, from, image })
  newRole.value = { name: '', from: '', image: '' }
  return true
}

const removeRole = (index) => favoriteRoles.value.splice(index, 1)

const addCos = () => {
  const name = newCos.value.name.trim()
  const from = newCos.value.from.trim()
  if (!name || !from) return false
  const image = newCos.value.image.trim() || createThumb(name)
  cosplayRoles.value.push({ name, from, image })
  newCos.value = { name: '', from: '', image: '' }
  return true
}

const removeCos = (index) => cosplayRoles.value.splice(index, 1)

const addMovie = () => {
  const { title, genre, language, type } = newMovie.value
  if (!title.trim() || !genre.trim() || !language.trim() || !type.trim()) return false
  likedMovies.value.push({
    title: title.trim(),
    genre: genre.trim(),
    language: language.trim(),
    type: type.trim(),
    image: newMovie.value.image.trim() || createThumb(title.trim()),
  })
  newMovie.value = { title: '', genre: '', language: '', type: '', image: '' }
  return true
}

const removeMovie = (index) => likedMovies.value.splice(index, 1)

const openDetail = (type, item) => {
  if (!item) return
  resetModalSize()
  detailModal.value = { type, item }
}

const closeDetail = () => {
  detailModal.value = null
}

const clampModalSize = (width, height) => {
  const maxWidth = typeof window !== 'undefined' ? Math.min(MAX_SIZE.width, window.innerWidth - 32) : MAX_SIZE.width
  const maxHeight = typeof window !== 'undefined' ? Math.min(MAX_SIZE.height, window.innerHeight - 32) : MAX_SIZE.height
  return {
    width: Math.min(Math.max(width, MIN_SIZE.width), Math.max(maxWidth, MIN_SIZE.width)),
    height: Math.min(Math.max(height, MIN_SIZE.height), Math.max(maxHeight, MIN_SIZE.height)),
  }
}

const resetModalSize = () => {
  modalSize.value = clampModalSize(DEFAULT_MODAL_SIZE.width, DEFAULT_MODAL_SIZE.height)
}

const handleResizeMove = (event) => {
  if (!resizeState.value.active) return
  const deltaX = event.clientX - resizeState.value.startX
  const deltaY = event.clientY - resizeState.value.startY
  modalSize.value = clampModalSize(resizeState.value.startW + deltaX, resizeState.value.startH + deltaY)
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

const startResize = (event) => {
  event.preventDefault()
  resizeState.value = {
    active: true,
    startX: event.clientX,
    startY: event.clientY,
    startW: modalSize.value.width,
    startH: modalSize.value.height,
  }
  if (typeof window !== 'undefined') {
    window.addEventListener('mousemove', handleResizeMove)
    window.addEventListener('mouseup', stopResize)
  }
}

const detailModalStyle = computed(() => ({
  width: `${modalSize.value.width}px`,
  height: `${modalSize.value.height}px`,
}))

const resetAddForm = (type) => {
  if (type === 'actor') {
    newActorName.value = ''
    newActorImage.value = ''
  } else if (type === 'language') {
    newLanguageName.value = ''
    newLanguageImage.value = ''
  } else if (type === 'role') {
    newRole.value = { name: '', from: '', image: '' }
  } else if (type === 'cos') {
    newCos.value = { name: '', from: '', image: '' }
  } else if (type === 'movie') {
    newMovie.value = { title: '', genre: '', language: '', type: '', image: '' }
  }
}

const openAdd = (type) => {
  resetAddForm(type)
  resetModalSize()
  addModal.value = type
}

const closeAdd = () => {
  addModal.value = null
}

const addModalTitle = computed(() => {
  if (!addModal.value) return ''
  const map = {
    actor: '添加演员',
    language: '添加语种',
    role: '添加角色',
    cos: '添加想 cos 的角色',
    movie: '添加电影',
  }
  return map[addModal.value] || ''
})

const handleAddConfirm = () => {
  const type = addModal.value
  if (!type) return
  const map = {
    actor: addActor,
    language: addLanguage,
    role: addRole,
    cos: addCos,
    movie: addMovie,
  }
  const fn = map[type]
  const success = fn?.()
  if (success) closeAdd()
}

const openList = (type) => {
  resetModalSize()
  listModal.value = type
}

const closeList = () => {
  listModal.value = null
}

const listModalData = computed(() => {
  if (!listModal.value) return null
  const map = {
    actor: { title: '全部喜欢的演员', items: favoriteActors.value, type: 'actor' },
    role: { title: '全部喜欢的角色', items: favoriteRoles.value, type: 'role' },
    cos: { title: '全部想 cos 的角色', items: cosplayRoles.value, type: 'cos' },
    movie: { title: '全部看过且喜欢的电影', items: likedMovies.value, type: 'movie' },
  }
  const result = map[listModal.value]
  if (!result) return null
  return {
    ...result,
    items: result.items.map((item, idx) => ({ item, idx })),
  }
})

onMounted(() => {
  resetModalSize()
})

onBeforeUnmount(() => {
  stopResizeListeners()
})
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
      </header>
      <div class="mini-card">
        <div class="section-head">
          <h4>喜欢的演员</h4>
          <div class="section-actions">
            <button v-if="favoriteActors.length > 10" class="ghost-btn tiny" type="button" @click="openList('actor')">显示全部</button>
            <button v-if="showActorEditor" class="ghost-btn tiny" type="button" @click="openAdd('actor')">添加</button>
            <button class="ghost-btn tiny" type="button" @click="showActorEditor = !showActorEditor">
              {{ showActorEditor ? '取消编辑' : '编辑' }}
            </button>
          </div>
        </div>
        <div class="avatar-grid">
          <div
            v-for="actor in visibleActors"
            :key="actor.item.name"
            class="pill-card"
            :title="`演员：${actor.item.name}`"
            role="button"
            tabindex="0"
            @click="openDetail('actor', actor.item)"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${actor.item.image})` }"></div>
            <span>{{ actor.item.name }}</span>
            <button v-if="showActorEditor" class="ghost-btn tiny" type="button" @click.stop="removeActor(actor.idx)">移除</button>
          </div>
        </div>
      </div>
      <div class="mini-card">
        <div class="section-head">
          <h4>喜欢的语种</h4>
          <div class="section-actions">
            <button v-if="showLanguageEditor" class="ghost-btn tiny" type="button" @click="openAdd('language')">添加</button>
            <button class="ghost-btn tiny" type="button" @click="showLanguageEditor = !showLanguageEditor">
              {{ showLanguageEditor ? '取消编辑' : '编辑' }}
            </button>
          </div>
        </div>
        <div class="avatar-grid">
          <div
            v-for="(lang, index) in favoriteLanguages"
            :key="lang.name"
            class="pill-card"
            :title="`语种：${lang.name}`"
          >
            <span>{{ lang.name }}</span>
            <button v-if="showLanguageEditor" class="ghost-btn tiny" type="button" @click.stop="removeLanguage(index)">移除</button>
          </div>
        </div>
      </div>
      <div class="mini-card">
        <div class="section-head">
          <h4>喜欢的角色</h4>
          <div class="section-actions">
            <button v-if="favoriteRoles.length > 10" class="ghost-btn tiny" type="button" @click="openList('role')">
              显示全部
            </button>
            <button v-if="showRoleEditor" class="ghost-btn tiny" type="button" @click="openAdd('role')">添加</button>
            <button class="ghost-btn tiny" type="button" @click="showRoleEditor = !showRoleEditor">
              {{ showRoleEditor ? '取消编辑' : '编辑' }}
            </button>
          </div>
        </div>
        <div class="avatar-grid">
          <div
            v-for="role in visibleRoles"
            :key="role.item.name"
            class="pill-card"
            :title="`角色：${role.item.name} · 来自：${role.item.from}`"
            role="button"
            tabindex="0"
            @click="openDetail('role', role.item)"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${role.item.image})` }"></div>
            <div>
              <div>{{ role.item.name }}</div>
              <p class="muted">{{ role.item.from }}</p>
            </div>
            <button v-if="showRoleEditor" class="ghost-btn tiny" type="button" @click.stop="removeRole(role.idx)">移除</button>
          </div>
        </div>
      </div>
      <div class="mini-card">
        <div class="section-head">
          <h4>想 cos 的角色</h4>
          <div class="section-actions">
            <button v-if="cosplayRoles.length > 10" class="ghost-btn tiny" type="button" @click="openList('cos')">
              显示全部
            </button>
            <button v-if="showCosEditor" class="ghost-btn tiny" type="button" @click="openAdd('cos')">添加</button>
            <button class="ghost-btn tiny" type="button" @click="showCosEditor = !showCosEditor">
              {{ showCosEditor ? '取消编辑' : '编辑' }}
            </button>
          </div>
        </div>
        <div class="avatar-grid">
          <div
            v-for="role in visibleCos"
            :key="role.item.name"
            class="pill-card"
            :title="`角色：${role.item.name} · 来自：${role.item.from}`"
            role="button"
            tabindex="0"
            @click="openDetail('cos', role.item)"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${role.item.image})` }"></div>
            <div>
              <div>{{ role.item.name }}</div>
              <p class="muted">{{ role.item.from }}</p>
            </div>
            <button v-if="showCosEditor" class="ghost-btn tiny" type="button" @click.stop="removeCos(role.idx)">移除</button>
          </div>
        </div>
      </div>

      <div class="section-title stats-anchor" style="margin-top: 16px">
        <div>
          <h2>看过且喜欢的电影</h2>
          <p>电影列表 & 数据统计</p>
        </div>
        <div class="section-actions">
          <button v-if="likedMovies.length > 5" class="ghost-btn tiny" type="button" @click="openList('movie')">
            显示全部
          </button>
          <button v-if="showMovieEditor" class="ghost-btn tiny" type="button" @click="openAdd('movie')">添加</button>
          <button class="ghost-btn tiny" type="button" @click="showMovieEditor = !showMovieEditor">
            {{ showMovieEditor ? '取消编辑' : '编辑' }}
          </button>
          <button class="ghost-btn tiny" type="button" @click="showStats = !showStats">
            {{ showStats ? '收起统计' : '查看统计' }}
          </button>
        </div>
        <div v-if="showStats" class="stats-popover">
          <div class="field">
            <label>电影题材</label>
            <div class="bar-chart">
              <div v-for="item in stats.genres" :key="item.label" class="bar">
                <span class="bar-label">{{ item.label }} · {{ item.count }}</span>
                <div class="bar-track">
                  <div class="bar-fill" :style="{ width: barWidth(stats.genres, item.count) }"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="field">
            <label>语种</label>
            <div class="bar-chart">
              <div v-for="item in stats.languages" :key="item.label" class="bar">
                <span class="bar-label">{{ item.label }} · {{ item.count }}</span>
                <div class="bar-track">
                  <div class="bar-fill" :style="{ width: barWidth(stats.languages, item.count) }"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="field">
            <label>类型</label>
            <div class="bar-chart">
              <div v-for="item in stats.types" :key="item.label" class="bar">
                <span class="bar-label">{{ item.label }} · {{ item.count }}</span>
                <div class="bar-track">
                  <div class="bar-fill" :style="{ width: barWidth(stats.types, item.count) }"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <ul class="list">
        <li
          v-for="movie in visibleMovies"
          :key="movie.item.title"
          class="list-item"
          :title="`${movie.item.title} · ${movie.item.genre} · ${movie.item.language} · ${movie.item.type}`"
          role="button"
          tabindex="0"
          @click="openDetail('movie', movie.item)"
        >
          <div class="row">
            <div class="thumb large" :style="{ backgroundImage: `url(${movie.item.image})` }"></div>
            <div>
              <strong>{{ movie.item.title }}</strong>
              <p class="muted">{{ movie.item.genre }} · {{ movie.item.language }} · {{ movie.item.type }}</p>
            </div>
          </div>
          <div class="inline-actions">
            <span class="status-dot success"></span>
            <button v-if="showMovieEditor" class="ghost-btn tiny" type="button" @click.stop="removeMovie(movie.idx)">移除</button>
          </div>
        </li>
      </ul>

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

  <div v-if="addModal" class="detail-backdrop" @click.self="closeAdd">
    <div class="detail-modal" :style="detailModalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="closeAdd">
        <span aria-hidden="true">×</span>
      </button>
      <h3 style="margin-top: 0">{{ addModalTitle }}</h3>
      <div class="form-grid">
        <template v-if="addModal === 'actor'">
          <div class="field">
            <label>演员姓名</label>
            <input v-model="newActorName" placeholder="添加演员姓名" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newActorImage" placeholder="图片链接（可选）" />
          </div>
        </template>
        <template v-else-if="addModal === 'language'">
          <div class="field">
            <label>语种</label>
            <input v-model="newLanguageName" placeholder="添加语种，如 英语/国语" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newLanguageImage" placeholder="图片链接（可选）" />
          </div>
        </template>
        <template v-else-if="addModal === 'role'">
          <div class="field">
            <label>角色名</label>
            <input v-model="newRole.name" placeholder="角色名" />
          </div>
          <div class="field">
            <label>来源/作品</label>
            <input v-model="newRole.from" placeholder="来源/作品" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newRole.image" placeholder="图片链接（可选）" />
          </div>
        </template>
        <template v-else-if="addModal === 'cos'">
          <div class="field">
            <label>角色名</label>
            <input v-model="newCos.name" placeholder="角色名" />
          </div>
          <div class="field">
            <label>来源/作品</label>
            <input v-model="newCos.from" placeholder="来源/作品" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newCos.image" placeholder="图片链接（可选）" />
          </div>
        </template>
        <template v-else-if="addModal === 'movie'">
          <div class="field">
            <label>电影名</label>
            <input v-model="newMovie.title" placeholder="电影名" />
          </div>
          <div class="field">
            <label>题材</label>
            <input v-model="newMovie.genre" placeholder="题材" />
          </div>
          <div class="field">
            <label>语种</label>
            <input v-model="newMovie.language" placeholder="语种" />
          </div>
          <div class="field">
            <label>类型</label>
            <input v-model="newMovie.type" placeholder="类型 如 电影/动漫/电视剧" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newMovie.image" placeholder="图片链接（可选）" />
          </div>
        </template>
      </div>
      <div class="form-actions">
        <button class="primary-btn" type="button" @click="handleAddConfirm">添加</button>
        <button class="ghost-btn" type="button" @click="closeAdd">取消</button>
      </div>
      <div class="resize-handle" @mousedown="startResize"></div>
    </div>
  </div>

  <div v-if="detailModal" class="detail-backdrop" @click.self="closeDetail">
    <div class="detail-modal pd-modal" :style="detailModalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="closeDetail">
        <span aria-hidden="true">×</span>
      </button>

      <!-- ── Actor ── -->
      <div v-if="detailModal.type === 'actor'" class="pd-inner">
        <div class="pd-left">
          <div class="pd-photo" :style="{ backgroundImage: `url(${detailModal.item.image})` }"></div>
          <h3 class="pd-name">{{ detailModal.item.name }}</h3>
          <div class="pd-tags">
            <span class="pd-tag">喜欢的演员</span>
          </div>
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h4 class="pd-section-head">演员信息</h4>
            <p class="pd-body-text">暂无更多详细信息。</p>
          </div>
        </div>
      </div>

      <!-- ── Role / Cos ── -->
      <div v-else-if="detailModal.type === 'role' || detailModal.type === 'cos'" class="pd-inner">
        <div class="pd-left">
          <div class="pd-photo" :style="{ backgroundImage: `url(${detailModal.item.image})` }"></div>
          <h3 class="pd-name">{{ detailModal.item.name }}</h3>
          <div class="pd-identity">
            <div class="pd-id-row">
              <span class="pd-id-label">来源</span>
              <span>{{ detailModal.item.from }}</span>
            </div>
          </div>
          <div class="pd-tags">
            <span class="pd-tag">{{ detailModal.type === 'cos' ? '想 cos 的角色' : '喜欢的角色' }}</span>
          </div>
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h4 class="pd-section-head">角色信息</h4>
            <p class="pd-body-text">暂无更多详细信息。</p>
          </div>
        </div>
      </div>

      <!-- ── Movie ── -->
      <div v-else-if="detailModal.type === 'movie'" class="pd-inner">
        <div class="pd-left">
          <div class="pd-poster" :style="{ backgroundImage: `url(${detailModal.item.image})` }"></div>
          <div class="pd-tags">
            <span
              v-for="tag in [detailModal.item.genre, detailModal.item.language, detailModal.item.type].filter(Boolean)"
              :key="tag"
              class="pd-tag"
            >{{ tag }}</span>
          </div>
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h2 class="pd-title">{{ detailModal.item.title }}</h2>
            <p class="pd-meta">{{ [detailModal.item.genre, detailModal.item.language, detailModal.item.type].filter(Boolean).join(' · ') }}</p>
          </div>
          <div class="pd-section">
            <h4 class="pd-section-head">看过且喜欢的电影</h4>
            <p class="pd-body-text">暂无更多详细信息。</p>
          </div>
        </div>
      </div>

      <!-- ── Language / fallback ── -->
      <div v-else class="pd-inner">
        <div class="pd-left">
          <div class="pd-photo" :style="{ backgroundImage: `url(${detailModal.item.image})` }"></div>
          <h3 class="pd-name">{{ detailModal.item.name }}</h3>
          <div class="pd-tags">
            <span class="pd-tag">喜欢的语种</span>
          </div>
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h4 class="pd-section-head">语种信息</h4>
            <p class="pd-body-text">暂无更多详细信息。</p>
          </div>
        </div>
      </div>

      <div class="resize-handle" @mousedown="startResize"></div>
    </div>
  </div>

  <div v-if="listModalData" class="detail-backdrop" @click.self="closeList">
    <div class="detail-modal list-modal" :style="detailModalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="closeList">
        <span aria-hidden="true">×</span>
      </button>
      <div class="list-modal-head">
        <h3>{{ listModalData.title }}</h3>
        <p class="muted">共 {{ listModalData.items.length }} 项</p>
      </div>
      <div class="list-modal-body">
        <template v-if="['actor', 'role', 'cos'].includes(listModalData.type)">
          <div class="avatar-grid">
            <div
              v-for="entry in listModalData.items"
              :key="entry.item.name"
              class="pill-card"
              :title="listModalData.type === 'actor' ? `演员：${entry.item.name}` : `角色：${entry.item.name} · 来自：${entry.item.from}`"
              role="button"
              tabindex="0"
              @click="openDetail(listModalData.type, entry.item)"
            >
              <div class="thumb small" :style="{ backgroundImage: `url(${entry.item.image})` }"></div>
              <div>
                <div>{{ entry.item.name }}</div>
                <p v-if="listModalData.type !== 'actor'" class="muted">{{ entry.item.from }}</p>
              </div>
              <button
                v-if="listModalData.type === 'actor' && showActorEditor"
                class="ghost-btn tiny"
                type="button"
                @click.stop="removeActor(entry.idx)"
              >
                移除
              </button>
              <button
                v-else-if="listModalData.type === 'role' && showRoleEditor"
                class="ghost-btn tiny"
                type="button"
                @click.stop="removeRole(entry.idx)"
              >
                移除
              </button>
              <button
                v-else-if="listModalData.type === 'cos' && showCosEditor"
                class="ghost-btn tiny"
                type="button"
                @click.stop="removeCos(entry.idx)"
              >
                移除
              </button>
            </div>
          </div>
        </template>
        <template v-else>
          <ul class="list">
            <li
              v-for="entry in listModalData.items"
              :key="entry.item.title"
              class="list-item"
              :title="`${entry.item.title} · ${entry.item.genre} · ${entry.item.language} · ${entry.item.type}`"
              role="button"
              tabindex="0"
              @click="openDetail('movie', entry.item)"
            >
              <div class="row">
                <div class="thumb large" :style="{ backgroundImage: `url(${entry.item.image})` }"></div>
                <div>
                  <strong>{{ entry.item.title }}</strong>
                  <p class="muted">{{ entry.item.genre }} · {{ entry.item.language }} · {{ entry.item.type }}</p>
                </div>
              </div>
              <div class="inline-actions">
                <span class="status-dot success"></span>
                <button v-if="showMovieEditor" class="ghost-btn tiny" type="button" @click.stop="removeMovie(entry.idx)">
                  移除
                </button>
              </div>
            </li>
          </ul>
        </template>
      </div>
      <div class="resize-handle" @mousedown="startResize"></div>
    </div>
  </div>
</template>

<style scoped>
/* ── Profile detail modal — two-column layout ── */
.pd-modal {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.pd-inner {
  display: flex;
  gap: 16px;
  height: 100%;
  padding-top: 8px;
  overflow: hidden;
}

/* ── Left column ── */
.pd-left {
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

.pd-photo {
  width: 130px;
  height: 170px;
  border-radius: 12px;
  background-size: cover;
  background-position: center;
  background-color: rgba(15, 23, 42, 0.06);
  border: 2px solid rgba(15, 23, 42, 0.12);
  flex-shrink: 0;
}

.pd-poster {
  width: 130px;
  height: 185px;
  border-radius: 10px;
  background-size: cover;
  background-position: center;
  background-color: rgba(15, 23, 42, 0.06);
  border: 2px solid rgba(15, 23, 42, 0.12);
  flex-shrink: 0;
}

.pd-name {
  margin: 0;
  font-size: 18px;
  font-weight: 800;
  color: #0f172a;
  text-align: center;
}

.pd-identity {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 5px;
  border-top: 1px solid rgba(15, 23, 42, 0.10);
  border-bottom: 1px solid rgba(15, 23, 42, 0.10);
  padding: 8px 0;
}

.pd-id-row {
  display: flex;
  gap: 6px;
  font-size: 12px;
  color: rgba(15, 23, 42, 0.80);
  justify-content: space-between;
  align-items: flex-start;
}

.pd-id-label {
  color: rgba(15, 23, 42, 0.45);
  flex-shrink: 0;
}

.pd-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  justify-content: center;
}

.pd-tag {
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.07);
  border: 1px solid rgba(15, 23, 42, 0.12);
  font-size: 11px;
  color: #334155;
}

/* ── Right column ── */
.pd-right {
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

.pd-section {
  padding-bottom: 12px;
}

.pd-section-sep {
  border-bottom: 1px solid rgba(15, 23, 42, 0.10);
}

.pd-section-head {
  margin: 0 0 8px;
  font-size: 14px;
  font-weight: 700;
  color: #0f172a;
}

.pd-title {
  margin: 0 0 4px;
  font-size: 22px;
  font-weight: 800;
  color: #0f172a;
}

.pd-meta {
  margin: 0;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.55);
}

.pd-body-text {
  margin: 0;
  font-size: 13px;
  line-height: 1.7;
  color: rgba(15, 23, 42, 0.60);
}
</style>
