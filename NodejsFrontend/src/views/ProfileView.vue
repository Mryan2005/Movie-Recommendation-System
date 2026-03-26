<script setup>
import { ref, computed } from 'vue'

const createThumb = (label, color = '#334155') =>
  `data:image/svg+xml,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='140' height='180'><rect width='100%' height='100%' rx='14' fill='${color}'/><text x='50%' y='55%' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='20' font-family='Inter, sans-serif'>${label}</text></svg>`
  )}`

const profile = ref({
  name: 'Echo',
  email: 'echo@example.com',
  gender: '女',
  avatar: createThumb('E', '#7c3aed'),
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

const likedMovies = ref([
  {
    title: '沙丘2',
    genre: '科幻',
    language: '英语',
    type: '电影',
    image: createThumb('Dune 2', '#0ea5e9'),
  },
  {
    title: '孤注一掷',
    genre: '犯罪',
    language: '国语',
    type: '电影',
    image: createThumb('孤注', '#1f2937'),
  },
  {
    title: '我的三体',
    genre: '科幻',
    language: '国语',
    type: '动漫',
    image: createThumb('三体', '#475569'),
  },
  {
    title: '想见你',
    genre: '爱情',
    language: '国语',
    type: '电视剧',
    image: createThumb('想见你', '#7c3aed'),
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

const favoriteRoles = ref([
  {
    name: '保罗·厄崔迪',
    from: '沙丘',
    image: createThumb('Paul', '#0ea5e9'),
  },
  {
    name: '小丑',
    from: '黑暗骑士',
    image: createThumb('Joker', '#7c3aed'),
  },
  {
    name: '夏洛克',
    from: '神探夏洛克',
    image: createThumb('SH', '#334155'),
  },
])
const cosplayRoles = ref([
  {
    name: '阿狸',
    from: '英雄联盟',
    image: createThumb('Ahri', '#f97316'),
  },
  {
    name: '薇尔莉特',
    from: '紫罗兰永恒花园',
    image: createThumb('Violet', '#14b8a6'),
  },
])
const favoriteActors = ref([
  {
    name: '蒂莫西·柴勒梅德',
    image: createThumb('TC', '#7c3aed'),
  },
  { name: '赞达亚', image: createThumb('Zendaya', '#0ea5e9') },
  { name: '任素汐', image: createThumb('任', '#1f2937') },
  { name: '梁朝伟', image: createThumb('梁', '#475569') },
])

const newActorName = ref('')
const newActorImage = ref('')
const favoriteLanguages = ref([
  { name: '英语', image: createThumb('EN', '#0ea5e9') },
  { name: '国语', image: createThumb('中', '#7c3aed') },
])
const newLanguageName = ref('')
const newLanguageImage = ref('')
const newRole = ref({ name: '', from: '', image: '' })
const newCos = ref({ name: '', from: '', image: '' })
const newMovie = ref({ title: '', genre: '', language: '', type: '', image: '' })
const showActorEditor = ref(false)
const showLanguageEditor = ref(false)
const showRoleEditor = ref(false)
const showCosEditor = ref(false)
const showMovieEditor = ref(false)

const barWidth = (list, count) => {
  const max = Math.max(...(list?.map((i) => i.count) || [1]), 1)
  return `${Math.max((count / max) * 100, 8)}%`
}

const addActor = () => {
  const name = newActorName.value.trim()
  if (!name) return
  const image = newActorImage.value.trim() || createThumb(name)
  favoriteActors.value.push({ name, image })
  newActorName.value = ''
  newActorImage.value = ''
}

const removeActor = (index) => favoriteActors.value.splice(index, 1)

const addLanguage = () => {
  const name = newLanguageName.value.trim()
  if (!name) return
  const image = newLanguageImage.value.trim() || createThumb(name)
  favoriteLanguages.value.push({ name, image })
  newLanguageName.value = ''
  newLanguageImage.value = ''
}

const removeLanguage = (index) => favoriteLanguages.value.splice(index, 1)

const addRole = () => {
  const name = newRole.value.name.trim()
  const from = newRole.value.from.trim()
  if (!name || !from) return
  const image = newRole.value.image.trim() || createThumb(name)
  favoriteRoles.value.push({ name, from, image })
  newRole.value = { name: '', from: '', image: '' }
}

const removeRole = (index) => favoriteRoles.value.splice(index, 1)

const addCos = () => {
  const name = newCos.value.name.trim()
  const from = newCos.value.from.trim()
  if (!name || !from) return
  const image = newCos.value.image.trim() || createThumb(name)
  cosplayRoles.value.push({ name, from, image })
  newCos.value = { name: '', from: '', image: '' }
}

const removeCos = (index) => cosplayRoles.value.splice(index, 1)

const addMovie = () => {
  const { title, genre, language, type } = newMovie.value
  if (!title.trim() || !genre.trim() || !language.trim() || !type.trim()) return
  likedMovies.value.push({
    title: title.trim(),
    genre: genre.trim(),
    language: language.trim(),
    type: type.trim(),
    image: newMovie.value.image.trim() || createThumb(title.trim()),
  })
  newMovie.value = { title: '', genre: '', language: '', type: '', image: '' }
}

const removeMovie = (index) => likedMovies.value.splice(index, 1)
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
        <div class="section-head">
          <h4>喜欢的演员</h4>
          <button class="ghost-btn tiny" type="button" @click="showActorEditor = !showActorEditor">
            {{ showActorEditor ? '收起编辑' : '编辑' }}
          </button>
        </div>
        <div class="avatar-grid">
          <div
            v-for="(actor, index) in favoriteActors"
            :key="actor.name"
            class="pill-card"
            :title="`演员：${actor.name}`"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${actor.image})` }"></div>
            <span>{{ actor.name }}</span>
            <button class="ghost-btn tiny" type="button" @click="removeActor(index)">移除</button>
          </div>
        </div>
        <div v-if="showActorEditor" class="inline-form">
          <input v-model="newActorName" placeholder="添加演员姓名" />
          <input v-model="newActorImage" placeholder="图片链接（可选）" />
          <button class="primary-btn tiny" type="button" @click="addActor">添加</button>
        </div>
      </div>
      <div class="mini-card">
        <div class="section-head">
          <h4>喜欢的语种</h4>
          <button class="ghost-btn tiny" type="button" @click="showLanguageEditor = !showLanguageEditor">
            {{ showLanguageEditor ? '收起编辑' : '编辑' }}
          </button>
        </div>
        <div class="avatar-grid">
          <div
            v-for="(lang, index) in favoriteLanguages"
            :key="lang.name"
            class="pill-card"
            :title="`语种：${lang.name}`"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${lang.image})` }"></div>
            <span>{{ lang.name }}</span>
            <button class="ghost-btn tiny" type="button" @click="removeLanguage(index)">移除</button>
          </div>
        </div>
        <div v-if="showLanguageEditor" class="inline-form">
          <input v-model="newLanguageName" placeholder="添加语种，如 英语/国语" />
          <input v-model="newLanguageImage" placeholder="图片链接（可选）" />
          <button class="primary-btn tiny" type="button" @click="addLanguage">添加</button>
        </div>
      </div>
      <div class="mini-card">
        <div class="section-head">
          <h4>喜欢的角色</h4>
          <button class="ghost-btn tiny" type="button" @click="showRoleEditor = !showRoleEditor">
            {{ showRoleEditor ? '收起编辑' : '编辑' }}
          </button>
        </div>
        <div class="avatar-grid">
          <div
            v-for="(role, index) in favoriteRoles"
            :key="role.name"
            class="pill-card"
            :title="`角色：${role.name} · 来自：${role.from}`"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${role.image})` }"></div>
            <div>
              <div>{{ role.name }}</div>
              <p class="muted">{{ role.from }}</p>
            </div>
            <button class="ghost-btn tiny" type="button" @click="removeRole(index)">移除</button>
          </div>
        </div>
        <div v-if="showRoleEditor" class="inline-form">
          <input v-model="newRole.name" placeholder="角色名" />
          <input v-model="newRole.from" placeholder="来源/作品" />
          <input v-model="newRole.image" placeholder="图片链接（可选）" />
          <button class="primary-btn tiny" type="button" @click="addRole">添加</button>
        </div>
      </div>
      <div class="mini-card">
        <div class="section-head">
          <h4>想 cos 的角色</h4>
          <button class="ghost-btn tiny" type="button" @click="showCosEditor = !showCosEditor">
            {{ showCosEditor ? '收起编辑' : '编辑' }}
          </button>
        </div>
        <div class="avatar-grid">
          <div
            v-for="(role, index) in cosplayRoles"
            :key="role.name"
            class="pill-card"
            :title="`角色：${role.name} · 来自：${role.from}`"
          >
            <div class="thumb small" :style="{ backgroundImage: `url(${role.image})` }"></div>
            <div>
              <div>{{ role.name }}</div>
              <p class="muted">{{ role.from }}</p>
            </div>
            <button class="ghost-btn tiny" type="button" @click="removeCos(index)">移除</button>
          </div>
        </div>
        <div v-if="showCosEditor" class="inline-form">
          <input v-model="newCos.name" placeholder="角色名" />
          <input v-model="newCos.from" placeholder="来源/作品" />
          <input v-model="newCos.image" placeholder="图片链接（可选）" />
          <button class="primary-btn tiny" type="button" @click="addCos">添加</button>
        </div>
      </div>

      <div class="section-title stats-anchor" style="margin-top: 16px">
        <div>
          <h2>看过且喜欢的电影</h2>
          <p>电影列表 & 数据统计</p>
        </div>
        <div class="section-actions">
          <button class="ghost-btn tiny" type="button" @click="showMovieEditor = !showMovieEditor">
            {{ showMovieEditor ? '收起编辑' : '编辑' }}
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
          v-for="(movie, index) in likedMovies"
          :key="movie.title"
          class="list-item"
          :title="`${movie.title} · ${movie.genre} · ${movie.language} · ${movie.type}`"
        >
          <div class="row">
            <div class="thumb large" :style="{ backgroundImage: `url(${movie.image})` }"></div>
            <div>
              <strong>{{ movie.title }}</strong>
              <p class="muted">{{ movie.genre }} · {{ movie.language }} · {{ movie.type }}</p>
            </div>
          </div>
          <div class="inline-actions">
            <span class="status-dot success"></span>
            <button class="ghost-btn tiny" type="button" @click="removeMovie(index)">移除</button>
          </div>
        </li>
      </ul>
      <div v-if="showMovieEditor" class="inline-form">
        <input v-model="newMovie.title" placeholder="电影名" />
        <input v-model="newMovie.genre" placeholder="题材" />
        <input v-model="newMovie.language" placeholder="语种" />
        <input v-model="newMovie.type" placeholder="类型 如 电影/动漫/电视剧" />
        <input v-model="newMovie.image" placeholder="图片链接（可选）" />
        <button class="primary-btn tiny" type="button" @click="addMovie">添加</button>
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
