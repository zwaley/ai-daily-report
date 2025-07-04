# AI Daily Web Report (AI 日报网页版)

这是一个自动抓取、筛选、整理并生成 AI 领域高质量新闻的工具，最终以网页形式展示，并可部署到 GitHub Pages 实现自动更新。

## 项目简介

本项目旨在帮助用户高效获取 AI 领域的最新动态和深度技术文章，过滤掉冗余信息和广告内容，并以简洁美观的网页形式呈现。通过自动化部署，您可以拥有一个每日更新的个性化 AI 资讯网站。

## 功能特性

*   **多源聚合：** 从多个国内外知名 AI/科技 RSS 订阅源抓取最新文章。
*   **智能筛选：** 基于关键词评分机制，自动识别并筛选出与 AI 技术强相关、高质量的文章。
    *   **正向关键词：** 优先选择包含“人工智能”、“机器学习”、“深度学习”、“LLM”、“大模型”、“技术突破”、“创新”、“架构”、“算法优化”等技术向关键词的文章。
    *   **负向过滤：** 排除包含“广告”、“促销”、“营销”、“销售”、“财报”等非技术或商业推广性质的内容。
    *   **重磅新品关注：** 即使是新品发布，只要与核心 AI 技术相关，也会被保留。
*   **文章排序：** 抓取到的文章会根据其质量评分和发布时间进行智能排序，确保重要内容优先展示。
*   **数量限制：** 可配置对特定 RSS 源的文章数量进行限制（例如 ArXiv），避免单一来源占据过多版面，保证内容多样性。
*   **网页展示：** 将整理好的日报内容生成为静态 HTML 网页，方便浏览和分享。
*   **自动化部署：** 可通过 Windows 任务计划程序配合 Git，实现每日自动生成并更新到 GitHub Pages。
*   **邮件通知（可选）：** 可配置通过邮件发送日报，并支持发送到多个收件人（已验证中文显示正常）。

## 技术栈

*   **Python 3.x**
*   **`feedparser`：** 用于解析 RSS/Atom 订阅源。
*   **`requests`：** 用于发送 HTTP 请求获取网页内容。
*   **`BeautifulSoup4`：** 用于解析 HTML 内容（主要用于摘要清洗）。
*   **`configparser`：** 用于读取和管理配置文件。
*   **`datetime`：** 用于日期和时间处理。

## 快速开始

### 1. 克隆或下载项目

如果您还没有项目文件，请从 GitHub 克隆或下载本项目。

```bash
git clone https://github.com/yourusername/ai-daily-report.git
cd ai-daily-report
```

### 2. 安装依赖

确保您的 Python 环境已安装所有必要的库。

```bash
pip install -r requirements.txt
```
（如果 `requirements.txt` 不存在，请手动安装上述“技术栈”中列出的库）

### 3. 配置 `config.ini`

打开 `config.ini` 文件，根据您的需求进行配置。

```ini
[Email]
sender_email = your_qq_email@qq.com
receiver_email = your_qq_email@qq.com
smtp_server = smtp.qq.com
smtp_port = 465
smtp_user = your_qq_email@qq.com
smtp_password = your_qq_email_auth_code # QQ邮箱授权码

[News]
# 逗号分隔的RSS订阅源列表，中文源已优先放置
rss_feeds = https://sspai.com/feed,http://www.geekpark.net/rss,https://www.ifanr.com/feed,https://36kr.com/feed,https://www.jiqizhixin.com/rss,http://www.ruanyifeng.com/blog/atom.xml,https://tech.meituan.com/feed/,https://www.technologyreview.com/c/artificial-intelligence/feed/,https://www.theverge.com/rss/index.xml,https://techcrunch.com/category/artificial-intelligence/feed/,https://arxiv.org/rss/cs.AI,https://venturebeat.com/category/ai/feed/,https://ai.googleblog.com/feeds/posts/default,https://deepmind.google/blog/feed/,https://openai.com/blog/rss/,https://medium.com/feed/towards-data-science,https://machinelearningmastery.com/feed/,https://www.analyticsvidhya.com/feed/
twitter_query = AI OR artificial intelligence # Twitter抓取功能目前为占位符，不影响网页生成

[SourceLimits]
# 可选：为特定RSS源设置文章数量限制，例如：
https://arxiv.org/rss/cs.AI = 10
# 如果未设置，默认限制为10篇
```

### 4. 生成日报网页

在项目根目录下运行 `main.py` 脚本。它将抓取、筛选文章，并生成 `index.html` 文件到 `docs/` 文件夹。

```bash
python main.py
```

运行成功后，您会在 `docs/` 文件夹中找到 `index.html` 文件。

## 部署到 GitHub Pages

本项目设计为可轻松部署到 GitHub Pages，实现每日自动更新。

### 1. 创建 GitHub 仓库

*   在 GitHub 上创建一个**公开**的新仓库（例如 `ai-daily-report`）。
*   **不要**勾选“添加 README 文件”等选项。

### 2. 推送代码到 GitHub

在本地项目目录中，初始化 Git 仓库并推送代码到您的 GitHub 仓库。

```bash
cd C:\Users\78430\ai_daily_web # 确保在项目根目录
git init
git add .
git commit -m "Initial commit for AI Daily Web Report"
git remote add origin https://github.com/yourusername/ai-daily-report.git # 替换为您的仓库URL
git branch -M main
git push -u origin main
```

### 3. 配置 GitHub Pages

*   访问您的 GitHub 仓库页面，点击 **"Settings"** -> **"Pages"**。
*   在 "Build and deployment" 部分：
    *   "Source" 选择 **"Deploy from a branch"**。
    *   "Branch" 选择 **`main`** (或您推送的分支)。
    *   "Folder" 选择 **`/docs`**。
*   点击 **"Save"**。

等待几分钟，您的网站将部署到 `https://yourusername.github.io/ai-daily-report/` (替换为您的实际 URL)。

### 4. 设置每日自动更新 (Windows 任务计划程序)

为了让网站每日自动更新，您可以使用 Windows 任务计划程序。

1.  **创建 `run_daily_report.bat` 文件：**
    在 `C:\Users\78430\ai_daily_web` 目录下创建 `run_daily_report.bat` 文件，内容如下：
    ```batch
    @echo off
    cd /d "C:\Users\78430\ai_daily_web"
    REM 激活您的Python环境（如果使用了conda或venv，请取消注释并修改路径）
    REM 例如：call C:\path\to\your\miniconda3\Scripts\activate.bat
    REM 或者：call .venv\Scripts\activate.bat
    python main.py
    git add .
git commit -m "Automated daily report update: %date% %time%"
git push origin main
    REM pause
    ```
    **重要：** 确保您的 Git 凭据已在系统中缓存，否则 `git push` 可能会失败。

2.  **配置 Windows 任务计划程序：**
    *   打开“任务计划程序”。
    *   点击“创建基本任务...”。
    *   **名称：** 例如“每日AI新闻日报更新”。
    *   **触发器：** 选择“每天”，设置您希望运行的时间。
    *   **操作：** 选择“启动程序”。
    *   **程序/脚本：** 浏览并选择 `C:\Users\78430\ai_daily_web\run_daily_report.bat`。
    *   **起始于(可选)：** 填写 `C:\Users\78430\ai_daily_web`。
    *   完成向导。

## 贡献

如果您有任何改进建议或发现问题，欢迎提交 Pull Request 或 Issue。

## 许可证

[选择一个开源许可证，例如 MIT License]

