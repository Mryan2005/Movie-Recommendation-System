<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'

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

const likedMovies = ref([
  {
    title: '少林足球',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('少林足球', '#0ea5e9'),
    year: 2001,
    director: '周星驰',
    summary: '一群怀揣绝技的少林弟子与落魄足球教练合力组队，凭借少林武功踢遍强敌，笑料百出又热血励志，是周星驰无厘头喜剧的巅峰之作之一。',
  },
  {
    title: '赌神',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('赌神', '#1f2937'),
    year: 1989,
    director: '王晶',
    summary: '周润发饰演赌神高进，因失忆而被人利用，最终凭借天赋与智慧重夺赌神宝座。影片将赌博技艺与情义江湖融为一体，是香港赌片的奠基之作。',
  },
  {
    title: '六福喜事',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('六福喜事', '#475569'),
    year: 1992,
    director: '高志森',
    summary: '香港贺岁喜剧经典，融合家庭温情与爆笑情节，展现香港市井生活的温暖与幽默，是本港电影文化的重要代表作之一。',
  },
  {
    title: '功夫',
    genre: '喜剧',
    language: '粤语',
    type: '电影',
    image: createThumb('功夫', '#7c3aed'),
    year: 2004,
    director: '周星驰',
    summary: '以1940年代上海为背景，小混混阿星阴差阳错卷入帮派恩怨，最终觉醒武学天赋。周星驰将功夫、喜剧与热血融为一炉，视觉奇观与情感共鸣兼具。',
  },
  {
    title: '上海滩',
    genre: '民国，爱情',
    language: '粤语',
    type: '电视剧',
    image: createThumb('上海滩', '#475569'),
    year: 1980,
    director: '招振强',
    summary: '许文强与冯程程的乱世情缘，在上海滩的枪林弹雨与权谋角力中展开，是华语电视剧史上最经典的民国传奇，主题曲《上海滩》至今传唱不衰。',
  },
  {
    title: '文豪野犬',
    genre: '动画，悬疑',
    language: '日语',
    type: '电视剧',
    image: createThumb('文豪野犬', '#475569'),
    year: 2016,
    director: '五十嵐卓哉',
    summary: '以太宰治、芥川龙之介等文豪为主角的原创故事，融合了悬疑与超能力元素，展现了文豪们在现代社会中的奋斗与成长。',
  },
  {
    title: '文豪野犬 第二季',
    genre: '动画，悬疑',
    language: '日语',
    type: '电视剧',
    image: createThumb('文豪野犬 第二季', '#475569'),
    year: 2016,
    director: '五十嵐卓哉',
    summary: '《文豪野犬 第二季》继续讲述文豪们在现代社会中的奋斗与成长，融入更多悬疑与超能力元素，带来全新的故事体验。',
  },
  {
    title: '文豪野犬 第三季',
    genre: '动画，悬疑', 
    language: '日语',
    type: '电视剧',
    image: createThumb('文豪野犬 第三季', '#475569'),
    year: 2019,
    director: '五十嵐卓哉',
    summary: '《文豪野犬 第三季》继续深入文豪们的内心世界，探讨他们在现代社会中的挣扎与成长，融入更多悬疑与超能力元素，带来全新的故事体验。',
  },
  {
    title: '文豪野犬 第四季',
    genre: '动画，悬疑',
    language: '日语',
    type: '电视剧',
    image: createThumb('文豪野犬 第四季', '#475569'),
    year: 2023,
    director: '五十嵐卓哉',
    summary: '《文豪野犬 第四季》继续探索文豪们的内心世界，揭示他们在现代社会中的挣扎与成长，融入更多悬疑与超能力元素，带来全新的故事体验。',
  },
  {
    title: '文豪野犬 第五季',
    genre: '动画，悬疑',
    language: '日语',
    type: '电视剧',
    image: createThumb('文豪野犬 第五季', '#475569'),
    year: 2023,
    director: '五十嵐卓哉',
    summary: '《文豪野犬 第五季》继续讲述文豪们在现代社会中的奋斗与成长，融入更多悬疑与超能力元素，带来全新的故事体验。',
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
const roleStats = computed(() => {
  const traitMap = new Map()
  const sourceMap = new Map()
  favoriteRoles.value.forEach((role) => {
    if (role.from) {
      sourceMap.set(role.from, (sourceMap.get(role.from) || 0) + 1)
    }
    ;(role.traits || []).forEach((trait) => {
      traitMap.set(trait, (traitMap.get(trait) || 0) + 1)
    })
  })
  return {
    traits: Array.from(traitMap.entries()).map(([label, count]) => ({ label, count })),
    sources: Array.from(sourceMap.entries()).map(([label, count]) => ({ label, count })),
  }
})
const statsModal = ref(null)
const listModal = ref(null)
const listSearch = ref('')
const expandedStats = ref({})

const favoriteRoles = ref([
  {
    name: '月代雪',
    from: '魔法少女的魔女审判',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Tsukishiro%20Yuki.png?raw=true',
    summary: '月代雪是《魔法少女的魔女审判》中的核心角色，外表清冷温柔却拥有坚定的内心，在魔法与审判的世界里始终坚守自己的信念与情感。',
    traits: ['清冷温柔', '内心坚定', '正义感强', '友情至上'],
  },
  {
    name: '伊蕾娜',
    from: '魔女之旅',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Elaina.jpg?raw=true',
    summary: '灰发灰眸的独行魔女，才华横溢却略显孤傲，以旅行者的身份游历各地，经历了无数温柔与残酷交织的故事，是《魔女之旅》的精神内核。',
    traits: ['独立自主', '才华横溢', '淡定从容', '灰发美少女'],
  },
  {
    name: '太宰治',
    from: '文豪野犬',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/dazai.jpg?raw=true',
    summary: '武装侦探社干部，以"人间失格"为异能名，外表玩世不恭实则背负着深重的过去，在生死边缘游走，是《文豪野犬》中最复杂的角色之一。',
    traits: ['玩世不恭', '智谋深沉', '内心复杂', '反差萌'],
  },
  {
    name: '温迪',
    from: '原神',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/venti.png?raw=true',
    summary: '蒙德城的风神芭巴托斯化身，以行吟诗人的身份游走人间，酷爱美酒与自由，是七神中最随性洒脱的一位，象征着风与自由的精神。',
    traits: ['自由奔放', '爱好美酒', '温柔善良', '风神化身'],
  },
  {
    name: '白钰袖',
    from: '风灵玉秀',
    image: 'https://isaacsimplusros2.mryan2005.top/img/avatar.png',
    summary: '《风灵玉秀》中的温婉角色，以灵秀的气质与深厚的情感深受喜爱，是一位在命运与情感中挣扎前行的少女形象。',
    traits: ['温婉灵秀', '情感丰富', '坚韧不拔'],
  },
  {
    name: '朝武芳乃',
    from: '千恋万花',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/yoshino.jpg?raw=true',
    summary: '《千恋万花》中的女主角之一，来自古老神社世家，外表传统端庄，内心温柔细腻，是日式传统美少女的典型形象。',
    traits: ['传统端庄', '温柔细腻', '神社巫女', '家族责任'],
  },
  {
    name: '丛雨',
    from: '千恋万花',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/congyu.jpg?raw=true',
    summary: '《千恋万花》中的另一位主要角色，性格活泼可爱，偶有腹黑，与朝武芳乃形成鲜明对比，给故事增添了不少活力与趣味。',
    traits: ['活泼可爱', '偶有腹黑', '元气满满', '反差萌'],
  },
  {
    name: '东海帝王',
    from: 'Pretty Derby',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Tokai%20Teio.jpg?raw=true',
    summary: '《赛马娘 Pretty Derby》中的人气角色，以强大的竞技精神和粗犷帅气的外形著称，是一位不甘平凡、热血励志的赛马娘。',
    traits: ['热血励志', '竞技精神强', '粗犷帅气', '自强不息'],
  },
  {
    name: '秋川弥生',
    from: 'Pretty Derby',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/akikawayayoi.png?raw=true',
    summary: '《赛马娘 Pretty Derby》中的训练师角色，以认真负责的工作态度和对赛马娘的深切关怀著称，是游戏中重要的支持角色。',
    traits: ['认真负责', '关怀备至', '专业训练师', '温柔坚强'],
  },
  {
    name: '堂吉诃德',
    from: '堂吉诃德',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/tangjihede.png?raw=true',
    summary: '塞万提斯笔下的经典文学角色，沉迷骑士小说的乡绅，骑着瘦马手持长矛行侠仗义，将风车当作巨人，是文学史上最著名的理想主义者形象。',
    traits: ['理想主义', '骑士精神', '脱离现实', '文学经典'],
  },
  {
    name: '卡提希娅',
    from: '鸣潮',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Cartethyia.png?raw=true',
    summary: '《鸣潮》中的角色，以独特的气质与战斗风格受到玩家喜爱，在鸣潮的世界观中扮演着重要的角色，其背景故事充满深度。',
    traits: ['独特气质', '战斗力强', '故事深度'],
  },
  {
    name: '菲比',
    from: '鸣潮',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/feibi.jpg?raw=true',
    summary: '《鸣潮》中的知名角色，活泼可爱的外表下隐藏着不为人知的力量与秘密，是鸣潮世界中深受玩家喜爱的人物之一。',
    traits: ['外表活泼', '隐藏力量', '可爱', '神秘'],
  },
  {
    name: '今汐',
    from: '鸣潮',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/jinxi.jpg?raw=true',
    summary: '《鸣潮》中以优雅沉静著称的角色，拥有独特的水系能力，举止高雅，在鸣潮的世界观中是极具辨识度的人气角色。',
    traits: ['优雅沉静', '水系能力', '高雅气质', '人气角色'],
  },
  {
    name: '彦卿',
    from: '崩坏：星穹铁道',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/yinqing.jpg?raw=true',
    summary: '《崩坏：星穹铁道》中的高人气角色，以凌厉的剑法和高冷外表著称，背后藏着深厚的情感与故事，是米哈游旗下作品中极受欢迎的角色之一。',
    traits: ['高冷剑客', '剑法凌厉', '内心深沉', '高人气'],
  },
  {
    name: '派蒙',
    from: '原神',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Paimon.jpg?raw=true',
    summary: '《原神》中旅行者的小伙伴，圆滚滚、爱吃饭的可爱精灵，外表幼小却常常承担向导的角色，是原神世界的标志性形象之一。',
    traits: ['爱吃饭', '可爱圆滚', '向导角色', '梗文化代表'],
  },
  {
    name: '灰原哀',
    from: '名侦探柯南',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Haibara%20Ai.png?raw=true',
    summary: '《名侦探柯南》中的重要人物，原本是黑衣组织的科学家，服用APTX4869后变成小孩，以灰原哀之名与柯南共同行动，冷静聪慧，形象深入人心。',
    traits: ['冷静聪慧', '神秘气质', '前组织成员', '反差萌'],
  },
  {
    name: '夏洛克·福尔摩斯',
    from: '大侦探福尔摩斯',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Sherlock%20Holmes.jpg?raw=true',
    summary: '阿瑟·柯南·道尔笔下的经典侦探角色，以超凡的推理能力和独特的个性著称，是文学史上最著名的侦探形象之一，影响了无数后续的侦探作品。',
    traits: ['天才推理', '高冷怪咖', '经典侦探', '文学巨匠'],
  },
  {
    name: '憨豆先生',
    from: '憨豆先生',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/mrbean.jpg?raw=true',
    summary: '英国喜剧演员罗温·艾金森饰演的经典角色，以夸张的肢体语言和几乎不开口的无声喜剧风格享誉全球，是跨越语言文化的喜剧符号。',
    traits: ['无声喜剧', '肢体夸张', '跨文化喜剧符号', '经典形象'],
  },
])
const cosplayRoles = ref([
  {
    name: '月代雪',
    from: '魔法少女的魔女审判',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Tsukishiro%20Yuki.png?raw=true',
    summary: '月代雪是《魔法少女的魔女审判》中的核心角色，外表清冷温柔却拥有坚定的内心，在魔法与审判的世界里始终坚守自己的信念与情感。',
    traits: ['清冷温柔', '内心坚定', '正义感强', '友情至上'],
  },
  {
    name: '太宰治',
    from: '文豪野犬',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/dazai.jpg?raw=true',
    summary: '武装侦探社干部，以"人间失格"为异能名，外表玩世不恭实则背负着深重的过去，在生死边缘游走，是《文豪野犬》中最复杂的角色之一。',
    traits: ['玩世不恭', '智谋深沉', '内心复杂', '反差萌'],
  },
  {
    name: '温迪',
    from: '原神',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/venti.png?raw=true',
    summary: '蒙德城的风神芭巴托斯化身，以行吟诗人的身份游走人间，酷爱美酒与自由，是七神中最随性洒脱的一位，象征着风与自由的精神。',
    traits: ['自由奔放', '爱好美酒', '温柔善良', '风神化身'],
  },
  {
    name: '白钰袖',
    from: '风灵玉秀',
    image: 'https://isaacsimplusros2.mryan2005.top/img/avatar.png',
    summary: '《风灵玉秀》中的温婉角色，以灵秀的气质与深厚的情感深受喜爱，是一位在命运与情感中挣扎前行的少女形象。',
    traits: ['温婉灵秀', '情感丰富', '坚韧不拔'],
  },
  {
    name: '朝武芳乃',
    from: '千恋万花',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/yoshino.jpg?raw=true',
    summary: '《千恋万花》中的女主角之一，来自古老神社世家，外表传统端庄，内心温柔细腻，是日式传统美少女的典型形象。',
    traits: ['传统端庄', '温柔细腻', '神社巫女', '家族责任'],
  },
  {
    name: '灰原哀',
    from: '名侦探柯南',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/Haibara%20Ai.png?raw=true',
    summary: '《名侦探柯南》中的重要人物，原本是黑衣组织的科学家，服用APTX4869后变成小孩，以灰原哀之名与柯南共同行动，冷静聪慧，形象深入人心。',
    traits: ['冷静聪慧', '神秘气质', '前组织成员', '反差萌'],
  },
  {
    name: '堂吉诃德',
    from: '堂吉诃德',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/tangjihede.png?raw=true',
    summary: '塞万提斯笔下的经典文学角色，沉迷骑士小说的乡绅，骑着瘦马手持长矛行侠仗义，将风车当作巨人，是文学史上最著名的理想主义者形象。',
    traits: ['理想主义', '骑士精神', '脱离现实', '文学经典'],
  },
  {
    name: '憨豆先生',
    from: '憨豆先生',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/mrbean.jpg?raw=true',
    summary: '英国喜剧演员罗温·艾金森饰演的经典角色，以夸张的肢体语言和几乎不开口的无声喜剧风格享誉全球，是跨越语言文化的喜剧符号。',
    traits: ['无声喜剧', '肢体夸张', '跨文化喜剧符号', '经典形象'],
  },
])
const favoriteActors = ref([
  {
    name: '周星驰',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/xingye.png?raw=true',
    bio: '香港著名喜剧演员、编剧与导演，以无厘头喜剧风格闻名华语影坛。代表作涵盖《大话西游》《少林足球》《功夫》《喜剧之王》等，是华语电影史上最具影响力的喜剧人之一。',
    highlights: ['无厘头喜剧', '演而优则导', '港产片传奇', '国际知名'],
    films: [
      { title: '少林足球', year: 2001, role: '强雄' },
      { title: '功夫', year: 2004, role: '阿星' },
      { title: '大话西游之月光宝盒', year: 1995, role: '至尊宝' },
      { title: '喜剧之王', year: 1999, role: '尹天仇' },
    ],
  },
  {
    name: '周润发',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/fa_ge.jpg?raw=true',
    bio: '香港著名演员，以《英雄本色》一举成名，凭借《上海滩》《赌神》《监狱风云》等确立其影坛地位，后赴好莱坞主演多部国际电影，是亚洲最具国际影响力的华人演员之一。',
    highlights: ['港产英雄片代表', '儒雅大气', '赌神形象深入人心', '国际影星'],
    films: [
      { title: '英雄本色', year: 1986, role: '小马哥' },
      { title: '赌神', year: 1989, role: '高进' },
      { title: '监狱风云', year: 1987, role: '阿正' },
    ],
  },
  {
    name: '黄子华',
    image: 'https://github.com/Mryan2005/Movie-Recommendation-System/blob/main/imgs/zihua.jpg?raw=true',
    bio: '香港栋笃笑（单口喜剧）表演者、演员，以犀利幽默的社会观察著称，主演电影《饭戏攻心》打破香港票房纪录，深受本地观众喜爱。',
    highlights: ['栋笃笑宗师', '社会观察犀利', '本土文化代表', '实力演员'],
    films: [
      { title: '饭戏攻心', year: 2022, role: '大哥' },
      { title: '毒舌大状', year: 2023, role: '林涼水' },
    ],
  },
  {
    name: '谢君豪',
    image: createThumb('谢君豪', '#475569'),
    bio: '香港著名舞台剧与电影演员，凭借《南海十三郎》荣获香港电影金像奖最佳男主角，是香港舞台剧界最具代表性的演员之一。',
    highlights: ['舞台剧大师', '金像影帝', '表演张力极强'],
    films: [
      { title: '南海十三郎', year: 1997, role: '唐涤生' },
    ],
  },
  {
    name: '王志文',
    image: createThumb('王志文', '#334155'),
    bio: '中国著名演员，以《围城》《年轮》等早期影视作品奠定地位，以其内敛沉稳的表演风格著称，是中国电视剧领域的实力派代表人物。',
    highlights: ['内敛沉稳', '文艺气质', '实力派', '经典角色塑造'],
    films: [
      { title: '围城', year: 1990, role: '方鸿渐' },
      { title: '年轮', year: 1994, role: '王雁' },
    ],
  },
  {
    name: '林栋甫',
    image: createThumb('林栋甫', '#475569'),
    bio: '香港知名性格演员，活跃于影视与舞台剧之间，以其稳健的表演功力与百变造型著称，是香港影视界不可或缺的配角人才。',
    highlights: ['性格演员', '舞台影视两栖', '百变造型'],
    films: [],
  },
  {
    name: '姜文',
    image: createThumb('姜文', '#475569'),
    bio: '中国著名演员与导演，以《阳光灿烂的日子》《鬼子来了》《让子弹飞》等奠定其大师地位，表演风格强烈个性化，作品充满独特的历史与人文关怀。',
    highlights: ['演导兼修', '强烈个人风格', '历史人文关怀', '影坛奇才'],
    films: [
      { title: '阳光灿烂的日子', year: 1994, role: '马小军' },
      { title: '让子弹飞', year: 2010, role: '张牧之' },
      { title: '鬼子来了', year: 2000, role: '马大三' },
    ],
  },
])

const newActorName = ref('')
const newActorImage = ref('')
const favoriteLanguages = ref([
  {
    name: '粤语',
    image: createThumb('粤', '#0ea5e9'),
    description: '广东话，香港与广东地区的母语，在影视作品中有着独特的韵律与文化底蕴。尤其港产片的粤语原声充满感染力，配音中蕴含的市井气与情义之美是其他语言难以复刻的。',
    examples: ['少林足球', '赌神', '上海滩', '功夫', '无间道', '英雄本色'],
  },
  {
    name: '国语',
    image: createThumb('中', '#7c3aed'),
    description: '普通话，中国大陆的通用语言，是华语电影与电视剧的主要语言，涵盖了大量优秀的文艺片与院线大作，是了解中国文化的重要窗口。',
    examples: ['阳光灿烂的日子', '让子弹飞', '围城', '年轮'],
  },
  {
    name: '英语',
    image: createThumb('EN', '#0ea5e9'),
    description: '世界上使用最广泛的语言之一，汇聚了好莱坞与英国影视的精华。英语原声作品往往拥有精彩的台词与表演，是欣赏西方影视文化的最佳方式。',
    examples: ['神探夏洛克', '憨豆先生', '沙丘', '权力的游戏'],
  },
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

const closePopovers = () => {
  statsModal.value = null
}

const openStats = (type) => {
  closePopovers()
  statsModal.value = type
}

const closeStats = () => {
  statsModal.value = null
}

const statsModalData = computed(() => {
  if (statsModal.value === 'movie') {
    return { title: '影视数据统计', data: stats.value, type: 'movie' }
  }
  if (statsModal.value === 'role') {
    return { title: '角色数据统计', data: roleStats.value, type: 'role' }
  }
  return null
})

const statsSections = computed(() => {
  if (!statsModalData.value) return []
  if (statsModalData.value.type === 'movie') {
    return [
      { key: 'genres', label: '题材', items: statsModalData.value.data.genres, empty: '暂无数据' },
      { key: 'languages', label: '语种', items: statsModalData.value.data.languages, empty: '暂无数据' },
      { key: 'types', label: '类型', items: statsModalData.value.data.types, empty: '暂无数据' },
    ]
  }
  return [
    { key: 'traits', label: '角色特征', items: statsModalData.value.data.traits, empty: '暂无特征统计' },
    { key: 'sources', label: '出处', items: statsModalData.value.data.sources, empty: '暂无出处统计' },
  ]
})

const defaultExpanded = (type) => {
  if (type === 'movie') return { genres: true, languages: true, types: true }
  if (type === 'role') return { traits: true, sources: true }
  return {}
}

const toggleStatsSection = (key) => {
  expandedStats.value = { ...expandedStats.value, [key]: !expandedStats.value?.[key] }
}

const isSectionExpanded = (key) => expandedStats.value?.[key] !== false

const openDetail = (type, item) => {
  if (!item) return
  closePopovers()
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
  closePopovers()
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
    movie: '添加影视',
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
  closePopovers()
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
    movie: { title: '全部看过且喜欢的影视', items: likedMovies.value, type: 'movie' },
  }
  const result = map[listModal.value]
  if (!result) return null
  return {
    ...result,
    items: result.items.map((item, idx) => ({ item, idx })),
  }
})

const filteredListItems = computed(() => {
  if (!listModalData.value) return []
  const keyword = listSearch.value.trim().toLowerCase()
  if (!keyword) return listModalData.value.items
  return listModalData.value.items.filter(({ item }) => {
    if (listModalData.value.type === 'actor') {
      const textLower = [item.name, ...(item.highlights || []), item.bio].filter(Boolean).join(' ').toLowerCase()
      return textLower.includes(keyword)
    }
    if (listModalData.value.type === 'role' || listModalData.value.type === 'cos') {
      const textLower = [item.name, item.from, ...(item.traits || []), item.summary].filter(Boolean).join(' ').toLowerCase()
      return textLower.includes(keyword)
    }
    const textLower = [
      item.title,
      item.genre,
      item.language,
      item.type,
      item.director,
      item.summary,
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()
    return textLower.includes(keyword)
  })
})

watch(listModal, () => {
  // Clear search whenever the show-all modal changes or closes
  if (!listModal.value) {
    listSearch.value = ''
    return
  }
  listSearch.value = ''
})

watch(
  () => statsModal.value,
  (val) => {
    if (!val) {
      expandedStats.value = {}
      return
    }
    expandedStats.value = defaultExpanded(val)
  }
)

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
        <div class="section-head stats-anchor">
          <h4>喜欢的角色</h4>
          <div class="section-actions">
            <button v-if="favoriteRoles.length > 10" class="ghost-btn tiny" type="button" @click="openList('role')">
              显示全部
            </button>
            <button v-if="showRoleEditor" class="ghost-btn tiny" type="button" @click="openAdd('role')">添加</button>
            <button class="ghost-btn tiny" type="button" @click="showRoleEditor = !showRoleEditor">
              {{ showRoleEditor ? '取消编辑' : '编辑' }}
            </button>
          <button class="ghost-btn tiny" type="button" @click="openStats('role')">
            查看统计
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
          <h2>看过且喜欢的影视</h2>
          <p>影视列表 & 数据统计</p>
        </div>
        <div class="section-actions">
          <button v-if="likedMovies.length > 5" class="ghost-btn tiny" type="button" @click="openList('movie')">
            显示全部
          </button>
          <button v-if="showMovieEditor" class="ghost-btn tiny" type="button" @click="openAdd('movie')">添加</button>
          <button class="ghost-btn tiny" type="button" @click="showMovieEditor = !showMovieEditor">
            {{ showMovieEditor ? '取消编辑' : '编辑' }}
          </button>
          <button class="ghost-btn tiny" type="button" @click="openStats('movie')">
            查看统计
          </button>
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
    </div>
  </div>

  <div v-if="addModal" class="detail-backdrop add-layer" @click.self="closeAdd">
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
            <label>影视名称</label>
            <input v-model="newMovie.title" placeholder="影视名称" />
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

  <div v-if="detailModal" class="detail-backdrop detail-layer" @click.self="closeDetail">
    <div class="detail-modal pd-modal" :style="detailModalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="closeDetail">
        <span aria-hidden="true">×</span>
      </button>

      <!-- ── Actor ── -->
      <div v-if="detailModal.type === 'actor'" class="pd-inner">
        <div class="pd-left">
          <div class="pd-photo" :style="{ backgroundImage: `url(${detailModal.item.image})` }"></div>
          <h3 class="pd-name">{{ detailModal.item.name }}</h3>
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h4 class="pd-section-head">关于演员</h4>
            <p class="pd-body-text">{{ detailModal.item.bio || '暂无介绍。' }}</p>
          </div>
          <div v-if="detailModal.item.highlights?.length" class="pd-section pd-section-sep">
            <h4 class="pd-section-head">特点</h4>
            <div class="pd-tags">
              <span v-for="tag in detailModal.item.highlights" :key="tag" class="pd-tag">{{ tag }}</span>
            </div>
          </div>
          <div v-if="detailModal.item.films?.length" class="pd-section">
            <h4 class="pd-section-head">代表作品</h4>
            <ul class="pd-film-list">
              <li v-for="film in detailModal.item.films" :key="film.title" class="pd-film-item">
                <span class="pd-film-year">{{ film.year }}</span>
                <span class="pd-film-title">{{ film.title }}</span>
                <span v-if="film.role" class="pd-film-role">饰 {{ film.role }}</span>
              </li>
            </ul>
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
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h4 class="pd-section-head">角色简介</h4>
            <p class="pd-body-text">{{ detailModal.item.summary || '暂无简介。' }}</p>
          </div>
          <div v-if="detailModal.item.traits?.length" class="pd-section">
            <h4 class="pd-section-head">性格特点</h4>
            <div class="pd-tags">
              <span v-for="trait in detailModal.item.traits" :key="trait" class="pd-tag">{{ trait }}</span>
            </div>
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
            <div class="pd-movie-meta-row">
              <span v-if="detailModal.item.year" class="pd-meta-tag">{{ detailModal.item.year }}</span>
              <span v-if="detailModal.item.director" class="pd-meta-tag">导演：{{ detailModal.item.director }}</span>
            </div>
          </div>
          <div class="pd-section">
            <h4 class="pd-section-head">剧情简介</h4>
            <p class="pd-body-text">{{ detailModal.item.summary || '暂无简介。' }}</p>
          </div>
        </div>
      </div>

      <!-- ── Language / fallback ── -->
      <div v-else class="pd-inner">
        <div class="pd-left">
          <div class="pd-photo" :style="{ backgroundImage: `url(${detailModal.item.image})` }"></div>
          <h3 class="pd-name">{{ detailModal.item.name }}</h3>
        </div>
        <div class="pd-right">
          <div class="pd-section pd-section-sep">
            <h4 class="pd-section-head">关于{{ detailModal.item.name }}</h4>
            <p class="pd-body-text">{{ detailModal.item.description || '暂无介绍。' }}</p>
          </div>
          <div v-if="detailModal.item.examples?.length" class="pd-section">
            <h4 class="pd-section-head">代表作品</h4>
            <ul class="pd-example-list">
              <li v-for="ex in detailModal.item.examples" :key="ex" class="pd-example-item">{{ ex }}</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="resize-handle" @mousedown="startResize"></div>
    </div>
  </div>

  <div v-if="listModalData" class="detail-backdrop list-layer" @click.self="closeList">
    <div class="detail-modal list-modal" :style="detailModalStyle">
      <button class="close-btn" type="button" aria-label="关闭" @click="closeList">
        <span aria-hidden="true">×</span>
      </button>
      <div class="list-modal-head">
        <h3>{{ listModalData.title }}</h3>
        <p class="muted">共 {{ listModalData.items.length }} 项</p>
      </div>
      <div class="list-search">
        <input
          v-model="listSearch"
          type="search"
          placeholder="搜索名字、出处或标签"
          aria-label="搜索列表"
        />
      </div>
      <div class="list-modal-body">
        <template v-if="['actor', 'role', 'cos'].includes(listModalData.type)">
          <div class="avatar-grid">
            <div
              v-for="entry in filteredListItems"
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
          <p v-if="!filteredListItems.length" class="muted">没有匹配的项目</p>
        </template>
        <template v-else>
          <ul class="list">
            <li
              v-for="entry in filteredListItems"
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
          <p v-if="!filteredListItems.length" class="muted">没有匹配的项目</p>
        </template>
      </div>
      <div class="resize-handle" @mousedown="startResize"></div>
    </div>
  </div>

  <div v-if="statsModalData" class="detail-backdrop stats-layer" @click.self="closeStats">
    <div class="detail-modal stats-modal">
      <button class="close-btn" type="button" aria-label="关闭" @click="closeStats">
        <span aria-hidden="true">×</span>
      </button>
      <h3 style="margin-top: 0">{{ statsModalData.title }}</h3>
      <div class="stats-grid">
        <div v-for="section in statsSections" :key="section.key" class="field collapsible-field">
          <button class="collapse-head" type="button" @click="toggleStatsSection(section.key)">
            <span>{{ section.label }}</span>
            <span class="caret" :class="{ open: isSectionExpanded(section.key) }">⌄</span>
          </button>
          <div v-show="isSectionExpanded(section.key)" class="bar-chart">
            <div v-for="item in section.items" :key="item.label" class="bar">
              <span class="bar-label">{{ item.label }} · {{ item.count }}</span>
              <div class="bar-track">
                <div class="bar-fill" :style="{ width: barWidth(section.items, item.count) }"></div>
              </div>
            </div>
            <p v-if="!section.items.length" class="muted">{{ section.empty }}</p>
          </div>
        </div>
      </div>
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

/* ── Film list (actor detail) ── */
.pd-film-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.pd-film-item {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-size: 13px;
  color: rgba(15, 23, 42, 0.80);
}

.pd-film-year {
  font-size: 11px;
  color: rgba(15, 23, 42, 0.40);
  flex-shrink: 0;
  min-width: 32px;
}

.pd-film-title {
  font-weight: 600;
  color: #0f172a;
}

.pd-film-role {
  font-size: 12px;
  color: rgba(15, 23, 42, 0.50);
}

/* ── Movie meta row ── */
.pd-movie-meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 6px;
}

.pd-meta-tag {
  padding: 2px 8px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.06);
  border: 1px solid rgba(15, 23, 42, 0.10);
  font-size: 12px;
  color: #334155;
}

/* ── Language example list ── */
.pd-example-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.pd-example-item {
  padding: 3px 10px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.05);
  border: 1px solid rgba(15, 23, 42, 0.10);
  font-size: 12px;
  color: #334155;
}

.stats-anchor {
  position: relative;
}
</style>
