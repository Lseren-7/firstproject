# 🗺️ Agent 开发双线学习路线

> 左线：本小程序（产品能力 + 全栈思维）　右线：Python / MySQL / Agent（技术地基）
> 两条线同时推进，互相印证。

---

## 路线总览

```
        本小程序线                    技术学习线
        ──────────                  ──────────
第〇批   装工具，认识小程序           Python：requests + JSON
第一批   TabBar + 页面路由           Python：函数、模块、import
第二批   WXML/WXSS 写界面           MySQL：SELECT/WHERE/ORDER BY
第三批   组件化思维                  Python：类 (class) 对比小程序组件
第四批   云函数 + 前后端通信         Python：Flask 写一个简单 API
第五批   表单 + 图片上传             MySQL：INSERT + Python 连 MySQL
第六批   页面跳转 + 传参            Python：URL参数、RESTful设计
第七批   用户身份 + 数据聚合         MySQL：GROUP BY + 聚合查询
第八批   分享机制                   Python：webhook / 回调机制
第九批   交互打磨                   Python：异常处理、日志

毕业项   小程序完整上线！            Python Agent Demo：「今天吃什么」
```

---

## 右线：每月技术目标

### 第 1 个月：Python 扎实 + MySQL 入门

| 周 | Python | MySQL |
|----|--------|-------|
| 1 | `print`, 变量, `if/else`, `for` | 数据库是啥？表、行、列 |
| 2 | 函数, `def`, 参数, 返回值 | `SELECT`, `WHERE`, `ORDER BY` |
| 3 | `list`, `dict`, JSON 处理 | `INSERT`, `UPDATE`, `DELETE` |
| 4 | `import`, `pip install`, `requests` 调 API | Python 连 MySQL（`pymysql`） |

**练手项目：** 用 Python 写一个脚本，从网上抓取学校食堂菜单，存到 MySQL。

### 第 2 个月：API 开发 + Agent 概念

| 周 | Python | Agent |
|----|--------|-------|
| 5 | `flask` 写一个简单 API（GET/POST） | Agent 是什么？感知 → 思考 → 行动 |
| 6 | `flask` + MySQL 连接 | Prompt Engineering 基础 |
| 7 | 错误处理 `try/except`、日志 | Function Calling 是什么 |
| 8 | RESTful 设计、JSON 返回格式 | LangChain 跑通第一个 Demo |

**练手项目：** 用 Flask 做一个「美食查询 API」，支持按窗口/评分查询。

### 第 3 个月：Agent 实战

| 周 | 内容 |
|----|------|
| 9-10 | 用 Python 给你的小程序写一个「今天吃什么」推荐 Agent |
| 11-12 | Agent 接入数据库、根据用户历史做个性化推荐 |

**毕业项目：** `food-agent/` — 一个独立 Python 项目，输入「推荐辣的、15 块以内」，Agent 查数据库并返回推荐 + 理由。

---

## 学习资源推荐

| 内容 | 资源 | 费用 |
|------|------|------|
| Python 基础 | 廖雪峰 Python 教程 | 免费 |
| MySQL | SQLZoo 在线练习 | 免费 |
| Flask | Flask 官方 Quickstart | 免费 |
| Agent | DeepLearning.AI 的 LangChain 课程 | 免费 |
| Agent | Anthropic Cookbook (GitHub) | 免费 |

---

## 学习节奏建议

- 每天 **1 小时** Python/MySQL（看书 + 敲代码）
- 每天或隔天小程序推进一批（跟我协作）
- 周末 **2 小时** 综合练习（做练手项目）

---

> 💡 关键：不要等「学完 Python」再碰 Agent。Python 学到第 4 周（能调 API、能连数据库）就可以开始看 Agent 概念了。两个世界的桥就是「API 调用」——Agent 的本质就是调用工具（API/数据库）。
