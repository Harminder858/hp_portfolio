"""
HTML Builder for Articles
Converts markdown articles to HTML and updates the portfolio index page
"""

import json
import markdown
import re
from typing import Dict
from pathlib import Path
from datetime import datetime

from config import ARTICLE_CONFIG


def markdown_to_html(content: str, images: list) -> str:
    """Convert markdown content to HTML"""

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'codehilite',
        'tables',
        'nl2br'
    ])

    html_content = md.convert(content)

    # Replace [VISUALIZATION: ...] placeholders with actual images
    viz_pattern = r'\[VISUALIZATION:([^\]]+)\]'
    matches = re.findall(viz_pattern, html_content)

    for i, match in enumerate(matches):
        if i < len(images):
            img_html = f'''
            <div class="visualization">
                <img src="../{images[i]}" alt="{match.strip()}" />
                <p class="caption">{match.strip()}</p>
            </div>
            '''
            html_content = html_content.replace(f'[VISUALIZATION:{match}]', img_html, 1)

    return html_content


def generate_article_html(article_data: Dict, content: str):
    """Generate standalone HTML page for article"""

    # Convert markdown to HTML
    html_content = markdown_to_html(content, article_data.get('images', []))

    # Create HTML template
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{article_data['title']} - Data Science Article">
    <meta name="keywords" content="{', '.join(article_data['keywords'])}">
    <meta name="author" content="Harminder Puri">
    <title>{article_data['title']} | Harminder Puri</title>

    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>

    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.7;
        }}

        .article-content {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .article-content h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #1a202c;
        }}

        .article-content h2 {{
            font-size: 1.875rem;
            font-weight: 600;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            color: #2d3748;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
        }}

        .article-content h3 {{
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 0.75rem;
            color: #4a5568;
        }}

        .article-content p {{
            margin-bottom: 1.25rem;
            color: #2d3748;
            font-size: 1.125rem;
        }}

        .article-content code {{
            background-color: #f7fafc;
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
            font-size: 0.9em;
            color: #e53e3e;
        }}

        .article-content pre {{
            background-color: #1a202c;
            color: #e2e8f0;
            padding: 1.5rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin-bottom: 1.5rem;
        }}

        .article-content pre code {{
            background-color: transparent;
            color: inherit;
            padding: 0;
        }}

        .article-content img {{
            max-width: 100%;
            height: auto;
            border-radius: 0.5rem;
            margin: 2rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .visualization {{
            margin: 2.5rem 0;
            text-align: center;
        }}

        .visualization img {{
            margin: 1rem auto;
        }}

        .caption {{
            font-style: italic;
            color: #718096;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        .article-meta {{
            color: #718096;
            font-size: 0.95rem;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #e2e8f0;
        }}

        .tag {{
            display: inline-block;
            background-color: #edf2f7;
            color: #2d3748;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }}

        .back-link {{
            display: inline-block;
            margin-bottom: 2rem;
            color: #3182ce;
            text-decoration: none;
            font-weight: 500;
        }}

        .back-link:hover {{
            color: #2c5282;
            text-decoration: underline;
        }}

        .article-content ul, .article-content ol {{
            margin-bottom: 1.25rem;
            padding-left: 2rem;
        }}

        .article-content li {{
            margin-bottom: 0.5rem;
        }}

        .article-content blockquote {{
            border-left: 4px solid #3182ce;
            padding-left: 1rem;
            margin: 1.5rem 0;
            color: #4a5568;
            font-style: italic;
        }}

        .article-content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
        }}

        .article-content th, .article-content td {{
            border: 1px solid #e2e8f0;
            padding: 0.75rem;
            text-align: left;
        }}

        .article-content th {{
            background-color: #f7fafc;
            font-weight: 600;
        }}
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <header class="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-6">
        <div class="container mx-auto px-4">
            <a href="../index.html" class="back-link text-white hover:text-gray-200">
                <i class="fas fa-arrow-left"></i> Back to Portfolio
            </a>
        </div>
    </header>

    <!-- Article Content -->
    <main class="container mx-auto px-4 py-8">
        <article class="article-content bg-white rounded-lg shadow-lg p-8">
            <h1>{article_data['title']}</h1>

            <div class="article-meta">
                <p>
                    <i class="far fa-calendar"></i> {datetime.fromisoformat(article_data['date']).strftime('%B %d, %Y')}
                    &nbsp;•&nbsp;
                    <i class="far fa-clock"></i> {article_data['word_count'] // 200} min read
                    &nbsp;•&nbsp;
                    <i class="fas fa-chart-bar"></i> {article_data['focus'].title()}
                </p>
                <div class="mt-2">
                    {' '.join([f'<span class="tag">{keyword}</span>' for keyword in article_data['keywords']])}
                </div>
            </div>

            {html_content}

            <!-- Author Bio -->
            <div class="mt-12 pt-8 border-t border-gray-200">
                <div class="flex items-start">
                    <div class="flex-1">
                        <h3 class="text-xl font-semibold mb-2">About the Author</h3>
                        <p class="text-gray-600">
                            Harminder Puri is a Data Scientist and Analytics Expert specializing in
                            machine learning, predictive analytics, and data-driven decision making.
                        </p>
                        <div class="mt-4">
                            <a href="https://www.linkedin.com/in/harminderpuri/" class="text-blue-600 hover:text-blue-800 mr-4">
                                <i class="fab fa-linkedin"></i> LinkedIn
                            </a>
                            <a href="https://github.com/Harminder858" class="text-blue-600 hover:text-blue-800">
                                <i class="fab fa-github"></i> GitHub
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </article>

        <!-- Related Articles -->
        <div class="mt-8 text-center">
            <a href="../index.html#articles" class="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
                View More Articles
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-6 mt-12">
        <div class="container mx-auto px-4 text-center">
            <p>&copy; 2024 Harminder Puri. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Syntax highlighting
        document.addEventListener('DOMContentLoaded', (event) => {{
            document.querySelectorAll('pre code').forEach((block) => {{
                hljs.highlightBlock(block);
            }});
        }});
    </script>
</body>
</html>'''

    # Save HTML file
    html_path = article_data['html_file']
    Path(html_path).parent.mkdir(parents=True, exist_ok=True)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ HTML generated: {html_path}")


def update_index_page():
    """Update the main portfolio index.html with new articles"""

    # Load articles database
    data_file = ARTICLE_CONFIG["data_file"]
    if not Path(data_file).exists():
        print("⚠️  No articles database found")
        return

    with open(data_file, 'r') as f:
        articles = json.load(f)

    # Read current index.html
    index_path = "index.html"
    with open(index_path, 'r', encoding='utf-8') as f:
        index_html = f.read()

    # Generate article cards HTML
    articles_html = ""
    # Show latest 6 articles
    for article in articles[:6]:
        date_str = datetime.fromisoformat(article['date']).strftime('%b %d, %Y')
        read_time = article['word_count'] // 200

        articles_html += f'''
                <div class="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
                    <div class="flex items-center text-sm text-gray-500 mb-3">
                        <i class="far fa-calendar mr-2"></i>
                        <span>{date_str}</span>
                        <span class="mx-2">•</span>
                        <i class="far fa-clock mr-2"></i>
                        <span>{read_time} min read</span>
                    </div>
                    <h3 class="text-xl font-semibold mb-3">{article['title']}</h3>
                    <div class="mb-4">
                        {' '.join([f'<span class="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded mr-2 mb-2">{kw}</span>' for kw in article['keywords'][:3]])}
                    </div>
                    <p class="text-gray-600 mb-4">Explore {article['focus']} with practical examples and visualizations.</p>
                    <a href="{article['html_file']}" class="text-blue-600 font-semibold hover:text-blue-800">
                        Read Article <i class="fas fa-arrow-right ml-1"></i>
                    </a>
                </div>'''

    # Find and replace the articles section
    # Look for the articles section and replace its content
    articles_section_pattern = r'(<section id="articles"[^>]*>.*?<div class="grid[^"]*">)(.*?)(</div>\s*</section>)'

    replacement = r'\1' + articles_html + r'\3'

    updated_html = re.sub(articles_section_pattern, replacement, index_html, flags=re.DOTALL)

    # Write updated index.html
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print(f"✅ Updated index.html with {len(articles[:6])} articles")


if __name__ == "__main__":
    # Test the update
    update_index_page()
