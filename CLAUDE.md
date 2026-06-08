# 🍜 食话 — 项目宪法（CLAUDE.md）

> **作用：** 每次新会话自动加载。所有代码必须遵守本文件规则。
> **适用阶段：** 项目全程（第〇批 ~ 第九批及以后）

---

## 一、CSS 变量 — 禁止硬编码颜色

所有颜色、字号、圆角必须使用以下变量，禁止在样式里直接写 `#FF6B6B` 等裸值。

```css
/* 定义在 app.wxss 全局 */

page {
  --color-primary:      #FF6B6B;   /* 主色：按钮、强调、星级 */
  --color-primary-light:#FFE0E0;   /* 主色浅色：标签背景 */
  --color-text:         #333333;   /* 正文颜色 */
  --color-text-secondary:#666666;  /* 次要文字 */
  --color-text-light:   #999999;   /* 辅助文字 */
  --color-bg:           #F5F5F5;   /* 页面背景 */
  --color-white:        #FFFFFF;   /* 卡片/白色背景 */
  --color-border:       #EEEEEE;   /* 分割线 */
  --color-star:         #FFB800;   /* 星级颜色 */

  --radius-sm:          8rpx;      /* 小圆角 */
  --radius-card:        12rpx;     /* 卡片圆角 */
  --radius-round:       50%;       /* 圆形 */

  --font-title:         32rpx;     /* 标题字号 */
  --font-body:          28rpx;     /* 正文字号 */
  --font-small:         24rpx;     /* 辅助文字 / 时间 */
  --font-large:         36rpx;     /* 大标题 / 价格 */

  --spacing-xs:         8rpx;      /* 极小间距 */
  --spacing-sm:         16rpx;     /* 小间距 */
  --spacing-md:         24rpx;     /* 标准间距 */
  --spacing-lg:         32rpx;     /* 大间距 */

  --shadow-card:        0 2rpx 12rpx rgba(0,0,0,0.06); /* 卡片阴影 */
}
```

**好处：** 换主题色只改 `--color-primary` 一行。永远不需要去翻旧代码找颜色值。

---

## 二、命名规则

### 2.1 文件和目录

| 类型 | 规则 | ✅ 正确 | ❌ 错误 |
|------|------|--------|--------|
| 页面目录 | 小写单词 | `index` `mine` `publish` | `Index` `MyPage` |
| 组件目录 | 小写 + 短横线 | `review-card` `rating-stars` | `ReviewCard` `ratingStars` |
| 云函数目录 | 小写 + 短横线 | `review-list` `get-detail` | `reviewList` `getDetail` |
| JS 文件名 | 统一 `index.js` | `pages/index/index.js` | `pages/index/home.js` |
| 分包目录 | `package` + 大写开头 | `packageReview` `packageAux` | `reviewPackage` |

### 2.2 JavaScript 变量

| 类型 | 规则 | 示例 |
|------|------|------|
| 布尔值 | `is` / `has` 开头 | `isLoading` `hasMore` `isLiked` |
| 数据列表 | 复数名词 | `reviews` `dishes` `windows` `tags` |
| 计数 | `count` 结尾 | `reviewCount` `likeCount` `commentCount` |
| 常量 | 全大写 + 下划线 | `MAX_IMAGES` `PAGE_SIZE` |
| 函数 | 动词开头 | `fetchReviews()` `toggleLike()` `formatDate()` |
| 私有函数 | `_` 前缀 | `_buildQuery()` `_parseResult()` |

### 2.3 云数据库字段

数据库字段统一用**小驼峰**：

```javascript
// ✅
{ reviewCount: 32, avgRating: 4.2, createdAt: Date, windowId: "xxx" }

// ❌ 禁止下划线（review_count）禁止大写开头（ReviewCount）
```

**好处：** 看名字就知道是什么 — `isLoading` 就是「正在加载√/×」，`reviewCount` 就是「评价的数量」。三个月后回来看代码不用猜。

---

## 三、云函数标准壳

每个云函数必须按以下模板写，**三步不省略**：参数校验 → 业务逻辑 → 统一返回。

```javascript
// cloudfunctions/xxx/index.js
const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })
const db = cloud.database()

/**
 * 云函数一句话描述
 * @param {Object} event  - 入参说明
 * @returns { code: 0|400|500, data?, msg? }
 */
exports.main = async (event, context) => {
  try {
    // 获取调用者 openid
    const { OPENID } = cloud.getWXContext()

    // ---- 1. 参数校验 ----
    const { 参数1, 参数2 } = event
    if (!参数1) {
      return { code: 400, msg: '参数1 不能为空' }
    }

    // ---- 2. 业务逻辑 ----
    const result = await db.collection('xxx')
      .where({ ... })
      .orderBy('createdAt', 'desc')
      .limit(20)
      .get()

    // ---- 3. 统一返回 ----
    return { code: 0, data: result.data }

  } catch (err) {
    console.error('云函数名 错误：', err)
    return { code: 500, msg: '服务器错误，请稍后重试' }
  }
}
```

**返回码约定：**

| code | 含义 |
|------|------|
| `0` | 成功 |
| `400` | 参数错误（前端可以提示用户修正） |
| `500` | 服务器错误（前端提示「稍后重试」） |

**好处：** 每个云函数结构一模一样。你打开任何一个，从 `try` 往下看就行。前端只判断 `res.code === 0` 就是成功。

---

## 四、前端统一调用封装（api.js）

所有云函数调用必须走 `utils/api.js`，页面里**禁止直接写 `wx.cloud.callFunction()`**。

```javascript
// utils/api.js

function call(name, data = {}) {
  return wx.cloud.callFunction({ name, data })
    .then(res => {
      const result = res.result
      if (result.code !== 0) {
        wx.showToast({ title: result.msg || '请求失败', icon: 'none' })
        throw new Error(result.msg)
      }
      return result.data
    })
}

// ---- 评价 ----
export const getReviews    = (filter)        => call('review-list', filter)
export const getReviewDetail = (reviewId)    => call('review-detail', { reviewId })
export const createReview  = (data)          => call('review-create', data)
export const deleteReview  = (reviewId)      => call('review-delete', { reviewId })

// ---- 窗口/场馆 ----
export const getWindows    = (canteenId)     => call('venue-listWindows', { canteenId })

// ---- 用户 ----
export const getUserProfile = ()             => call('user-profile')
export const getMyReviews  = (cursor)        => call('user-myReviews', { cursor })

// ---- 互动 ----
export const toggleLike    = (targetType, targetId) => call('interaction-toggleLike', { targetType, targetId })
```

**好处：** 换云函数名只改 `api.js` 一处。页面里写 `api.getReviews({ windowId: 'xxx' })`，IDE 补全云函数名。

---

## 五、页面标准骨架

每个页面必须包含以下状态处理：

```javascript
// pages/xxx/index.js
const api = require('../../utils/api.js')

Page({
  data: {
    loading: true,          // ← 必有
    error: null,            // ← 必有
    list: [],               // ← 数据列表
    hasMore: true,          // 分页用
  },

  onLoad(options) {
    // 接收 URL 参数
    // const id = options.id
    this.fetchData()
  },

  async fetchData() {
    this.setData({ loading: true, error: null })
    try {
      const data = await api.xxx()
      this.setData({ list: data.list, hasMore: data.hasMore, loading: false })
    } catch (err) {
      this.setData({ error: err.message || '加载失败', loading: false })
    }
  },

  onPullDownRefresh() {
    this.fetchData().then(() => wx.stopPullDownRefresh())
  },

  onReachBottom() {
    if (!this.data.hasMore || this.data.loading) return
    // 加载更多...
  },
})
```

**对应的 WXML 必须处理三种状态：**

```html
<view wx:if="{{loading}}" class="state-container">
  <text>加载中...</text>
</view>

<view wx:elif="{{error}}" class="state-container">
  <text>{{error}}</text>
  <button bindtap="fetchData">重试</button>
</view>

<view wx:else>
  <view wx:for="{{list}}" wx:key="_id">
    <!-- 正常内容 -->
  </view>
  <view wx:if="{{!hasMore}}" class="end-tip">没有更多了</view>
</view>
```

**好处：** 永远有三种状态（加载中 / 出错+重试 / 正常显示），用户不会看到白屏。新页面像做填空题，骨架已有，只填业务逻辑。

---

## 六、数据库分页规则

所有列表必须用**游标分页**，禁止用 `skip()`。

```javascript
// ✅ 游标分页
db.collection('reviews')
  .where({ ... })
  .orderBy('createdAt', 'desc')
  .limit(20)
  .get()

// 加载更多时传入上一页最后一条的 createdAt 作为 cursor
// 云函数里：
// if (event.cursor) {
//   where.createdAt = _.lt(new Date(event.cursor))
// }

// ❌ 禁止：.skip(20).limit(20)
```

**好处：** 微信云开发里 `skip()` 超过一定数量会巨慢。游标分页永远走索引，快且稳。

---

## 七、图片处理规则

1. 上传前压缩（宽度不超过 1080px）
2. 评价图片最少 1 张、最多 9 张
3. 图片必须通过云开发**图片安全检测**后再入库

```javascript
// 图片安全检测（在云函数 review-create 中）
const res = await cloud.openapi.security.imgSecCheck({
  media: {
    contentType: 'image/png',
    value: buffer
  }
})
```

**好处：** 压缩省流量（免费额度更耐用），安全检测是微信审核要求。

---

## 八、注释规则

```javascript
// ❌ 废话注释：解释「是什么」（代码本身已经说清楚了）
const count = 0  // 定义count变量为0

// ✅ 意图注释：解释「为什么」「会被谁用」
let count = 0    // 评价图片数，提交时校验 >= 1，传给云函数

// ✅ 文件头注释：说明输入输出
/**
 * 评价列表云函数
 * 入参：{ windowId?, cursor?, pageSize? }
 * 返回：{ code: 0, data: { list: Review[], hasMore: boolean, nextCursor: string } }
 */
```

**好处：** 三个月后看到代码，意图注释能帮你回忆「当初为什么这样写」。

---

## 九、版本记录

每次重大变更在此记录，格式：`日期 + 谁做的 + 做了什么 + 为什么`。

```markdown
## 变更记录
| 日期 | 变更 | 原因 |
|------|------|------|
| 2026-06-08 | 创建本文件 | 项目启动，确立规则 |
```

**好处：** 不是给你看的，是给我（新会话的 AI）看的——一眼知道项目经历了什么变化。

---

## 十、不优化过度原则

| 阶段 | 优先级 |
|------|--------|
| 试跑期（当前） | **先跑通，功能对** |
| 有种子用户后 | 修 bug、根据反馈改体验 |
| 有一定量后 | 针对性优化性能 |

**当前不做的：** 虚拟列表、缓存策略、防抖节流、CDN 配置、复杂动画。

**好处：** 你不会被「高级写法」淹没。每行代码你问「这行干嘛的」，我都能用人话解释清楚。

---

> 📌 **以上规则随项目推进可随时增补。每次新增规则在变更记录中登记。**
