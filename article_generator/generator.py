"""
Main Article Generator using LLM API
Generates data science articles with illustrative visuals and graphs
"""

import os
import json
import random
from datetime import datetime
from typing import Dict, List, Optional
import anthropic
from pathlib import Path

from config import (
    ANTHROPIC_API_KEY,
    ARTICLE_TOPICS,
    WRITING_STYLE,
    ARTICLE_CONFIG,
    GITHUB_CONFIG
)
from visualizations import create_article_visualizations
from html_builder import generate_article_html, update_index_page


class ArticleGenerator:
    """Automated article generator with LLM integration"""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the article generator"""
        self.api_key = api_key or ANTHROPIC_API_KEY
        if not self.api_key:
            raise ValueError("Anthropic API key is required. Set ANTHROPIC_API_KEY environment variable.")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.ensure_directories()

    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        Path(ARTICLE_CONFIG["output_dir"]).mkdir(exist_ok=True)
        Path(ARTICLE_CONFIG["images_dir"]).mkdir(exist_ok=True)

    def select_topic(self) -> Dict:
        """Select a topic from the pool"""
        # Load existing articles to avoid duplicates
        existing_topics = self.get_existing_topics()

        # Filter out recently used topics
        available_topics = [
            topic for topic in ARTICLE_TOPICS
            if topic["title"] not in existing_topics[-5:]  # Avoid last 5 topics
        ]

        if not available_topics:
            available_topics = ARTICLE_TOPICS

        return random.choice(available_topics)

    def get_existing_topics(self) -> List[str]:
        """Get list of existing article topics"""
        data_file = ARTICLE_CONFIG["data_file"]
        if not os.path.exists(data_file):
            return []

        with open(data_file, 'r') as f:
            articles = json.load(f)

        return [article["title"] for article in articles]

    def generate_article_content(self, topic: Dict) -> str:
        """Generate article content using Claude API"""

        prompt = f"""You are a data science writer creating an insightful article.

Topic: {topic["title"]}
Keywords: {", ".join(topic["keywords"])}
Focus: {topic["focus"]}

Writing Style Guidelines:
- Tone: {WRITING_STYLE["tone"]}
- Target Audience: {WRITING_STYLE["target_audience"]}
- Technical Depth: {WRITING_STYLE["technical_depth"]}

Key Characteristics:
{chr(10).join(f"- {char}" for char in WRITING_STYLE["characteristics"])}

Structure:
{chr(10).join(f"{i+1}. {section}" for i, section in enumerate(WRITING_STYLE["structure"]))}

Requirements:
1. Write a comprehensive article (1500-2500 words)
2. Use markdown format
3. Include code examples where relevant (Python preferred)
4. Mention where visualizations should be placed using: [VISUALIZATION: description]
5. Start with a compelling hook related to business impact
6. Use real-world examples from retail, e-commerce, or business domains
7. Balance technical depth with accessibility
8. Include mathematical formulas using LaTeX notation when needed
9. End with actionable takeaways

Write the complete article now:"""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return message.content[0].text

        except Exception as e:
            print(f"Error generating article with Claude API: {e}")
            raise

    def save_article(self, topic: Dict, content: str, images: List[str]) -> Dict:
        """Save article to file and update metadata"""

        # Generate article metadata
        article_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        article_slug = topic["title"].lower().replace(" ", "-").replace(":", "")

        article_data = {
            "id": article_id,
            "title": topic["title"],
            "slug": article_slug,
            "keywords": topic["keywords"],
            "focus": topic["focus"],
            "date": datetime.now().isoformat(),
            "content_file": f"articles/{article_slug}.md",
            "html_file": f"articles/{article_slug}.html",
            "images": images,
            "word_count": len(content.split())
        }

        # Save markdown content
        md_path = f"{ARTICLE_CONFIG['output_dir']}{article_slug}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Update articles database
        self.update_articles_database(article_data)

        return article_data

    def update_articles_database(self, article_data: Dict):
        """Update the articles JSON database"""
        data_file = ARTICLE_CONFIG["data_file"]

        # Load existing data
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                articles = json.load(f)
        else:
            articles = []

        # Add new article
        articles.insert(0, article_data)  # Add to beginning

        # Save updated data
        with open(data_file, 'w') as f:
            json.dump(articles, f, indent=2)

    def generate_complete_article(self) -> Dict:
        """Generate a complete article with visualizations"""

        print("🚀 Starting article generation...")

        # Step 1: Select topic
        topic = self.select_topic()
        print(f"📝 Selected topic: {topic['title']}")

        # Step 2: Generate content
        print("✍️  Generating article content with Claude API...")
        content = self.generate_article_content(topic)

        # Step 3: Create visualizations
        print("📊 Creating visualizations...")
        images = create_article_visualizations(topic, content)

        # Step 4: Save article
        print("💾 Saving article...")
        article_data = self.save_article(topic, content, images)

        # Step 5: Generate HTML
        print("🌐 Generating HTML version...")
        generate_article_html(article_data, content)

        # Step 6: Update index page
        print("🔄 Updating portfolio index page...")
        update_index_page()

        print(f"✅ Article generated successfully: {article_data['title']}")
        print(f"   - Markdown: {article_data['content_file']}")
        print(f"   - HTML: {article_data['html_file']}")
        print(f"   - Images: {len(images)} visualizations")

        return article_data


def main():
    """Main execution function"""
    try:
        # Check for API key
        if not ANTHROPIC_API_KEY:
            print("❌ Error: ANTHROPIC_API_KEY not set in environment variables")
            print("   Please set it using: export ANTHROPIC_API_KEY='your-key-here'")
            return

        # Generate article
        generator = ArticleGenerator()
        article_data = generator.generate_complete_article()

        # Print summary
        print("\n" + "="*60)
        print("📰 ARTICLE GENERATION SUMMARY")
        print("="*60)
        print(f"Title: {article_data['title']}")
        print(f"Words: {article_data['word_count']}")
        print(f"Date: {article_data['date']}")
        print(f"Files created: {len(article_data['images']) + 2}")
        print("="*60)

        return article_data

    except Exception as e:
        print(f"❌ Error during article generation: {e}")
        raise


if __name__ == "__main__":
    main()
