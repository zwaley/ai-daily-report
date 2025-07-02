import configparser
import datetime
import os # Import os for file operations

from news_fetcher import get_news_from_rss, get_news_from_twitter
from email_formatter import format_email
# from email_sender import send_email # Comment out email_sender import

def main():
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
        html_content = format_email(all_articles)
        output_dir = './docs'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'index.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"AI Daily Report saved to {output_file}")
    else:
        print("No new articles found in the last 24 hours.")

if __name__ == "__main__":
    main()
