@echo off
REM 切换到您的项目目录
cd /d "C:\Users\78430\ai_daily_web"
    4
REM 激活您的Python环境（如果使用了conda或venv）
 REM 例如：call C:\path\to\your\miniconda3\Scripts\activate.bat
REM 或者：call .venv\Scripts\activate.bat
    8
REM 运行Python脚本，生成最新的index.html到docs文件夹
python main.py
   11
REM 将更改添加到Git
git add .
   14
REM 提交更改
 git commit -m "Automated daily report update: %date% %time%"
   17
REM 推送更改到GitHub
git push origin main
   20
REM 保持窗口打开，以便查看输出（可选，调试时有用）
REM pause