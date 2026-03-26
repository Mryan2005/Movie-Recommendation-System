<script setup>
import { ref, computed } from 'vue'

const step = ref(1)

const account = ref({
  username: '',
  email: '',
  password: '',
  confirm: '',
})

const interests = ref({
  genres: ['科幻', '悬疑'],
  titles: ['沙丘', '银翼杀手2049'],
})

const people = ref({
  roles: ['乔纳森·诺兰', '新海诚'],
  actors: ['蒂莫西·柴勒梅德', '杨紫琼', '艾玛·斯通'],
})

const steps = [
  { id: 1, title: '账号与密码', desc: '填写基本登录信息' },
  { id: 2, title: '感兴趣的电影', desc: '喜欢的题材/片单' },
  { id: 3, title: '角色与演员', desc: '关注的角色/演员' },
]

const isLastStep = computed(() => step.value === steps.length)

const next = () => {
  if (step.value < steps.length) step.value += 1
}

const prev = () => {
  if (step.value > 1) step.value -= 1
}
</script>

<template>
  <div class="panel">
    <header class="section-title">
      <div>
        <h2>注册新账号</h2>
        <p>完善信息后即可获得精准推荐</p>
      </div>
      <div class="pill">共 {{ steps.length }} 步</div>
    </header>

    <div class="steps">
      <div v-for="item in steps" :key="item.id" class="step" :class="{ active: step >= item.id }">
        <strong>{{ item.title }}</strong>
        <p class="muted">{{ item.desc }}</p>
      </div>
    </div>

    <div v-if="step === 1" class="form-grid" style="margin-top: 16px">
      <div class="field">
        <label>用户名</label>
        <input v-model="account.username" placeholder="取一个喜欢的名字" />
      </div>
      <div class="field">
        <label>邮箱</label>
        <input v-model="account.email" type="email" placeholder="you@example.com" />
      </div>
      <div class="field">
        <label>密码</label>
        <input v-model="account.password" type="password" placeholder="至少 8 位" />
      </div>
      <div class="field">
        <label>确认密码</label>
        <input v-model="account.confirm" type="password" placeholder="再次输入密码" />
      </div>
    </div>

    <div v-else-if="step === 2" class="form-grid" style="margin-top: 16px">
      <div class="field">
        <label>喜欢的电影题材</label>
        <textarea :value="interests.genres.join('、')" readonly></textarea>
        <p class="muted">示例：科幻、悬疑、喜剧...</p>
      </div>
      <div class="field">
        <label>最喜欢的电影</label>
        <textarea :value="interests.titles.join('、')" readonly></textarea>
        <p class="muted">我们会优先推荐同风格的影片</p>
      </div>
    </div>

    <div v-else class="form-grid" style="margin-top: 16px">
      <div class="field">
        <label>关注的导演/编剧</label>
        <textarea :value="people.roles.join('、')" readonly></textarea>
      </div>
      <div class="field">
        <label>喜欢的演员</label>
        <textarea :value="people.actors.join('、')" readonly></textarea>
      </div>
    </div>

    <div class="form-actions">
      <button class="ghost-btn" type="button" @click="prev" :disabled="step === 1">上一步</button>
      <button class="primary-btn" type="button" @click="next">
        {{ isLastStep ? '提交注册' : '下一步' }}
      </button>
    </div>
  </div>
</template>
