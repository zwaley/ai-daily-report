def format_email(articles, title="Daily AI News Report"):
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{ font-family: sans-serif; }}
            .card {{ border: 1px solid #eee; border-radius: 5px; padding: 20px; margin-bottom: 20px; }}
            .card h2 {{ margin-top: 0; }}
            .card a {{ color: #007bff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
    """

    for article in articles:
        html += f"""
        <div class="card">
            <h2><a href="{{article['link']}}">{article['title']}</a></h2>
            <p>{article['summary']}</p>
            <p style="font-size: 0.8em; color: #666;">来源: {article['source_name']}</p>
        </div>
        """

    html += """
    </body>
    </html>
    """
    return html
