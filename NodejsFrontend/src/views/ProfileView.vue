<script setup>
import { ref, computed } from 'vue'

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
        <div v-if="showActorEditor" class="edit-popover">
          <div class="field">
            <label>演员姓名</label>
            <input v-model="newActorName" placeholder="添加演员姓名" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newActorImage" placeholder="图片链接（可选）" />
          </div>
          <div class="form-actions">
            <button class="primary-btn tiny" type="button" @click="addActor">添加</button>
          </div>
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
        <div v-if="showLanguageEditor" class="edit-popover">
          <div class="field">
            <label>语种</label>
            <input v-model="newLanguageName" placeholder="添加语种，如 英语/国语" />
          </div>
          <div class="field">
            <label>图片链接（可选）</label>
            <input v-model="newLanguageImage" placeholder="图片链接（可选）" />
          </div>
          <div class="form-actions">
            <button class="primary-btn tiny" type="button" @click="addLanguage">添加</button>
          </div>
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
        <div v-if="showRoleEditor" class="edit-popover">
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
          <div class="form-actions">
            <button class="primary-btn tiny" type="button" @click="addRole">添加</button>
          </div>
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
        <div v-if="showCosEditor" class="edit-popover">
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
          <div class="form-actions">
            <button class="primary-btn tiny" type="button" @click="addCos">添加</button>
          </div>
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
