@echo off
REM 切换到当前项目目录
cd /d "C:\Users\78430\ai_daily_web"

REM --- Step 1: Generate Report (with proxy) ---
echo "Step 1: Generating report with proxy..."
set http_proxy=http://127.0.0.1:33210
set https_proxy=http://127.0.0.1:33210
python main.py --generate-only

REM --- Step 2: Send Email (without proxy) ---
echo "Step 2: Sending email without proxy..."
set http_proxy=
set https_proxy=
python main.py --send-only

REM --- Step 3: Git Push ---
echo "Step 3: Pushing updates to GitHub..."
git add .
git commit -m "Automated daily report update: %date% %time%"
git push origin main

echo "Done."
REM pause