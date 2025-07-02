    1         @echo off
    2         REM 切换到您的项目目录
    3         cd /d "C:\Users\78430\ai_daily_web"
    4
    5         REM 激活您的Python环境（如果使用了conda或venv）
    6         REM 例如：call C:\path\to\your\miniconda3\Scripts\activate.bat
    7         REM 或者：call .venv\Scripts\activate.bat
    8
    9         REM 运行Python脚本，生成最新的index.html到docs文件夹
   10         python main.py
   11
   12         REM 将更改添加到Git
   13         git add .
   14
   15         REM 提交更改
   16         git commit -m "Automated daily report update: %date% %time%"
   17
   18         REM 推送更改到GitHub
   19         git push origin main
   20
   21         REM 保持窗口打开，以便查看输出（可选，调试时有用）
   22         REM pause