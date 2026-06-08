<div align="center">

<img src="assets/logo.png" alt="食话 logo" width="120" />

# 🍜 食话 · FoodTruth

### *因为美食，我们成了朋友*

[![WeChat](https://img.shields.io/badge/WeChat-小程序-07C160?style=flat-square&logo=wechat&logoColor=white)](https://mp.weixin.qq.com/)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-MVP%20开发中-orange?style=flat-square)](#)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](#)

</div>

---

## 📖 这是什么？

**食话**是一个面向大学校园的美食评价微信小程序。

大众点评覆盖不到食堂窗口级别，学生不知道哪个窗口的什么菜好吃——只能靠运气踩坑。食话让每个食堂窗口、每道菜都有学生真实评价，通过微信分享在朋友间自然传播，实现真正**口口相传**。

> 💡 名字谐音「实话」，寓意评价真实不掺水。

---

## ✨ 核心特性

<table>
<tr>
  <td width="50%">

### 🔍 精细到窗口的评价
- 评价粒度到**食堂窗口 + 菜品**级别
- 不是「一食堂好吃」，是「一食堂麻辣香锅的红烧肉好吃」

### 📸 有图有真相
- 每条评价必须配实拍图
- 上传自动压缩，安全检测

### 🏷️ 标签系统
- 好吃 / 性价比高 / 排队快 / 分量足 …
- 一眼看完，不用读长文

  </td>
  <td width="50%">

### 🔗 口口相传
- 评价分享到微信群 → 朋友点开直达
- 传播链路可追踪
- 没有算法推荐，只有朋友推荐

### 🏫 单校起步
- 先在一所大学验证模式
- 数据库设计已预留多校扩展

### 🆓 零成本试运行
- 微信云开发免费额度
- 个人主体免认证费

  </td>
</tr>
</table>

---

## 🛠️ 技术栈

| 层面 | 技术 | 选型理由 |
|------|------|---------|
| 🖼️ 前端 | 微信小程序原生 | 零学习曲线（你会 HTML/CSS），性能最优 |
| ⚙️ 后端 | 微信云开发 | 免运维、免登录对接、免费额度够试跑 |
| 📦 数据库 | 云数据库（MongoDB-like） | 文档型存储，灵活适配评价结构 |
| 🖼️ 图片 | 云存储 + CDN | 自带图片压缩和安全审核 |
| 🔐 登录 | 微信静默登录 | 用户无感，打开即用 |

---

## 🗺️ 项目结构

```
食话/
├── CLAUDE.md              ← 📜 项目宪法（AI 协作规范）
├── docs/
│   └── 校园美食评价系统-实现方案.md  ← 📋 分批计划
├── miniprogram/           ← 🖼️ 小程序前端
│   ├── app.js/json/wxss   ← 应用入口 & 全局配置
│   ├── utils/api.js       ← 云函数统一调用
│   ├── components/        ← 公共组件
│   │   ├── review-card/   ← 评价卡片
│   │   ├── rating-stars/  ← 星级评分
│   │   └── tag-list/      ← 标签列表
│   ├── pages/             ← 主包页面
│   │   ├── index/         ← 首页·发现
│   │   ├── explore/       ← 浏览·窗口
│   │   └── mine/          ← 我的
│   ├── packageReview/     ← 📦 分包：评价模块
│   │   ├── publish/       ← 发布评价
│   │   ├── detail/        ← 评价详情
│   │   └── window/        ← 窗口详情
│   └── packageAux/        ← 📦 分包：辅助
│       ├── search/        ← 搜索
│       └── ranking/       ← 排行榜
├── cloudfunctions/        ← ⚙️ 云函数
│   ├── review/            ← 评价 CRUD
│   ├── user/              ← 用户数据
│   ├── venue/             ← 窗口/场馆
│   └── interaction/       ← 点赞/评论
├── database/              ← 🗄️ 数据库脚本 & 种子数据
└── assets/                ← 🎨 图标 & 设计素材
```

---

## 🚀 本地开发

### 你需要准备

1. [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)（Windows 64位稳定版）
2. 微信小程序 AppID（注册于 [mp.weixin.qq.com](https://mp.weixin.qq.com/)）
3. 开通云开发环境

### 跑起来

```bash
# 1. 克隆项目
git clone https://github.com/YOUR_USERNAME/campus-food-review.git

# 2. 打开微信开发者工具
#    → 导入项目
#    → 选择 miniprogram/ 目录
#    → 填入你的 AppID

# 3. 开通云开发
#    → 点击工具栏「云开发」按钮
#    → 创建环境（记下环境 ID）

# 4. 修改 app.js 里的环境 ID 为你的环境 ID

# 5. 编译运行
#    点击工具栏「编译」
```

---

## 📋 开发路线图

| 阶段 | 内容 | 状态 |
|------|------|------|
| 🏗️ 项目宪法 | CLAUDE.md 编码规范 | ✅ 已完成 |
| 📋 方案设计 | 产品 & 技术方案 | ✅ 已完成 |
| 第〇批 | 安装工具 · 认识项目 | ⏳ 进行中 |
| 第一批 | 项目骨架 · TabBar | ⬜ 待开始 |
| 第二批 | 首页静态布局 | ⬜ 待开始 |
| 第三批 | 组件化改造 | ⬜ 待开始 |
| 第四批 | 接入云数据库 | ⬜ 待开始 |
| 第五批 | 发布评价 | ⬜ 待开始 |
| 第六批 | 详情页 & 跳转 | ⬜ 待开始 |
| 第七批 | 个人中心 | ⬜ 待开始 |
| 第八批 | 分享传播 | ⬜ 待开始 |
| 第九批 | 互动 & 打磨 | ⬜ 待开始 |

---

## 🤝 协作方式

这是一个 **Vibecoding 项目**（AI 辅助编码）。开发方式不是一个人闷头写，而是：

```
我(AI) 科普概念 → 我写代码 → 你(人) 编译运行 → 你确认效果 → 下一批
```

所有代码规范见 [CLAUDE.md](CLAUDE.md)。欢迎通过 Issue 讨论需求。

---

## 📄 License

MIT © 2026

---

<div align="center">

**🍜 让每一顿饭都有据可循**

*这是一个 Vibecoding 项目 · 从零开始学小程序开发*

</div>
