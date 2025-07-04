import configparser
import datetime
import os
import sys
from news_fetcher import get_news_from_rss
from email_formatter import format_email
from email_sender import send_email

def generate_report():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # News settings
    rss_feeds = config['News']['rss_feeds'].split(',')
    # Fetch news
    rss_articles = get_news_from_rss(rss_feeds)
    # Sort articles by published date (newest first)
    rss_articles.sort(key=lambda x: (x.get('score', 0), x.get('published_parsed', datetime.datetime.min)), reverse=True)
    all_articles = rss_articles[:200] # Limit to 200 articles

    # Generate HTML and save to file
    if all_articles:
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")
        subject = f"AI Daily Report - {today_str}"
        html_content = format_email(all_articles, title=subject)
        
        output_dir = './docs'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'index.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"AI Daily Report saved to {output_file}")
    else:
        print("No new articles found in the last 24 hours.")

def send_report_email():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Email settings
    sender_email = config['Email']['sender_email']
    receiver_email = config['Email']['receiver_email'].split(',')
    smtp_server = config['Email']['smtp_server']
    smtp_port = int(config['Email']['smtp_port'])
    smtp_user = config['Email']['smtp_user']
    smtp_password = config['Email']['smtp_password']

    output_file = './docs/index.html'
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")
        subject = f"AI Daily Report - {today_str}"
        
        send_email(sender_email, receiver_email, smtp_server, smtp_port, smtp_user, smtp_password, subject, html_content)
    else:
        print(f"Error: {output_file} not found. Cannot send email.")

def main():
    if '--generate-only' in sys.argv:
        print("Generating report only...")
        generate_report()
    elif '--send-only' in sys.argv:
        print("Sending email only...")
        send_report_email()
    else:
        print("Generating report and sending email...")
        generate_report()
        send_report_email()

if __name__ == "__main__":
    main()
