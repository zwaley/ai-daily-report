import feedparser
import requests
from bs4 import BeautifulSoup
import datetime
import configparser

# Define keywords for scoring
POSITIVE_KEYWORDS = {
    "人工智能": 5, "机器学习": 5, "深度学习": 5, "算法": 4, "模型": 4, "神经网络": 4,
    "LLM": 5, "大模型": 5, "计算机视觉": 4, "自然语言处理": 4, "机器人": 4,
    "芯片": 3, "算力": 3, "框架": 3, "开源": 3, "研究": 3, "论文": 3,
    "技术突破": 5, "创新": 4, "架构": 3, "优化": 3, "伦理": 2, "安全": 2,
    "发布": 2, "推出": 2, "新品": 2 # These are positive if combined with tech terms
}

NEGATIVE_KEYWORDS = {
    "广告": -5, "促销": -5, "营销": -4, "销售": -4, "财报": -3, "融资": -2 # Adjust score for "融资" if it's a tech company news
}

MIN_SCORE_THRESHOLD = 0 # Articles with score below this will be filtered out

def calculate_article_score(title, summary):
    score = 0
    text = (title + " " + summary).lower()

    for keyword, weight in POSITIVE_KEYWORDS.items():
        if keyword in text:
            score += weight

    for keyword, weight in NEGATIVE_KEYWORDS.items():
        if keyword in text:
            # Special handling for "融资" if it's a tech company news
            if keyword == "融资" and ("科技" in text or "AI" in text or "人工智能" in text):
                score += abs(weight) / 2 # Reduce negative impact if it's tech related funding
            else:
                score += weight
    return score

def get_news_from_rss(rss_feeds):
    config = configparser.ConfigParser()
    config.read('config.ini')

    articles = []
    for feed_url in rss_feeds:
        current_source_articles = [] # To store articles for the current source
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                # Ensure published_date is a datetime object
                published_date = datetime.datetime.min
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    try:
                        published_date = datetime.datetime(*entry.published_parsed[:6])
                    except (TypeError, ValueError):
                        # Handle cases where published_parsed might be malformed
                        pass

                # Apply 24-hour filter
                if datetime.datetime.now() - published_date > datetime.timedelta(days=1):
                    continue

                title = entry.title if hasattr(entry, 'title') else ""
                summary = entry.summary if hasattr(entry, 'summary') else title

                # Calculate score
                score = calculate_article_score(title, summary)

                if score >= MIN_SCORE_THRESHOLD:
                    source_name = feed.feed.title if hasattr(feed.feed, 'title') else feed_url
                    current_source_articles.append({
                        'title': title,
                        'link': entry.link if hasattr(entry, 'link') else "#",
                        'summary': summary,
                        'published_parsed': published_date,
                        'score': score, # Add score to the article dictionary
                        'source_name': source_name # Add source name
                    })
            
            # Apply source-specific limit
            limit = 10 # Default limit
            if 'SourceLimits' in config and feed_url in config['SourceLimits']:
                try:
                    limit = int(config['SourceLimits'][feed_url])
                except ValueError:
                    print(f"Warning: Invalid limit for {feed_url} in config.ini. Using default 10.")
            
            articles.extend(current_source_articles[:limit])

        except Exception as e:
            print(f"Error parsing RSS feed {feed_url}: {e}")
    return articles

def get_news_from_twitter(query):
    # This is a placeholder for fetching news from X.
    # A more robust solution would use the X API or a dedicated library.
    # For this example, we'll simulate a search using a search engine.
    search_url = f"https://www.google.com/search?q={query}+site:twitter.com&tbs=qdr:d"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # This is a simplified parsing and might need adjustment based on Google's search results page structure.
        # It's also not guaranteed to be stable.
        # A better approach is to use a dedicated web scraping service or API.
        # For now, we will return a dummy list of articles.
        return [
            {
                'title': 'Sample AI News from X 1',
                'link': '#',
                'summary': 'This is a sample summary of AI news from X.'
            },
            {
                'title': 'Sample AI News from X 2',
                'link': '#',
                'summary': 'This is another sample summary of AI news from X.'
            }
        ]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news from Twitter: {e}")
        return []