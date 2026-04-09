export const createThumb = (label, color = '#1e3a8a') =>
  `data:image/svg+xml,${encodeURIComponent(
    `<svg xmlns='http://www.w3.org/2000/svg' width='140' height='180'><rect width='100%' height='100%' rx='12' fill='${color}'/><text x='50%' y='52%' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='22' font-family='Inter, sans-serif'>${label}</text></svg>`
  )}`

export const actorDetailMap = {
  '蒂莫西·柴勒梅德': {
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
  },
  '小罗伯特·唐尼': {
    id: 'downey',
    name: '小罗伯特·唐尼',
    enName: 'Robert Downey Jr.',
    nationality: '美国',
    birthdate: '1965-04-04',
    birthplace: '美国纽约',
    occupation: '演员 / 制片人',
    bio: '凭借《钢铁侠》系列成为全球知名影星，近年以《奥本海默》中的路易斯·施特劳斯一角获得广泛赞誉，展现了从商业大片到文艺剧情的多面演技。',
    highlights: ['奥斯卡最佳男配', '漫威宇宙灵魂', '多面演技', '银幕魅力'],
    image: createThumb('唐', '#b91c1c'),
    films: [
      { title: '奥本海默', year: 2023, role: '路易斯·施特劳斯' },
      { title: '复仇者联盟4：终局之战', year: 2019, role: '托尼·斯塔克 / 钢铁侠' },
      { title: '钢铁侠', year: 2008, role: '托尼·斯塔克 / 钢铁侠' },
      { title: '大侦探福尔摩斯', year: 2009, role: '夏洛克·福尔摩斯' },
    ],
  },
  杨紫琼: {
    id: 'michelle',
    name: '杨紫琼',
    enName: 'Michelle Yeoh',
    nationality: '马来西亚',
    birthdate: '1962-08-06',
    birthplace: '马来西亚怡保',
    occupation: '演员 / 制片人',
    bio: '以《卧虎藏龙》《瞬息全宇宙》等作品闻名，凭借坚韧与优雅的形象和扎实的动作戏获得奥斯卡最佳女主角，被视为亚洲影坛的标志性人物。',
    highlights: ['奥斯卡最佳女主角', '动作戏见长', '亚洲传奇', '气质优雅'],
    image: createThumb('杨', '#0ea5e9'),
    films: [
      { title: '瞬息全宇宙', year: 2022, role: '秀莲' },
      { title: '尚气与十环传奇', year: 2021, role: '映莉' },
      { title: '卧虎藏龙', year: 2000, role: '俞秀莲' },
      { title: '007：明日帝国', year: 1997, role: '林慧' },
    ],
  },
}

export const defaultActor = actorDetailMap['蒂莫西·柴勒梅德']

export const getActorDetail = (name) => {
  if (!name) return null
  const actor = actorDetailMap[name]
  if (!actor) {
    console.warn(`[actorDetail] 未找到演员「${name}」，请检查调用者传入的名称。`)
    return null
  }
  return actor
}
