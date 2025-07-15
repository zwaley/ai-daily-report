@echo off
REM 切换到当前项目目录
cd /d "C:\Users\78430\ai_daily_web"

REM --- Step 1: Generate Report (with proxy) ---
echo "Step 1: Generating report with proxy..."
rem set http_proxy=http://127.0.0.1:33210
rem set https_proxy=http://127.0.0.1:33210
python main.py --generate-only

REM --- Step 2: Send Email (without proxy) ---
echo "Step 2: Sending email without proxy..."
REM set http_proxy=
REM set https_proxy=
python main.py --send-only

REM --- Step 3: Git Push ---
echo "Step 3: Pushing updates to GitHub..."
git add .
git commit -m "Automated daily report update: %date% %time%"
git push origin main

git push origin main

echo "Done."
REM pause