"""
Configuration for the Automated Article Generator System
"""

import os
from typing import List, Dict

# API Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Article Topics Pool - Rotates through different data science topics
ARTICLE_TOPICS = [
    {
        "title": "Understanding Customer Lifetime Value in Retail",
        "keywords": ["CLTV", "customer value", "retail analytics", "predictive modeling"],
        "focus": "business metrics and analytics"
    },
    {
        "title": "Time Series Forecasting with LSTM Networks",
        "keywords": ["LSTM", "time series", "neural networks", "forecasting"],
        "focus": "deep learning applications"
    },
    {
        "title": "A/B Testing: Statistical Significance in Product Analytics",
        "keywords": ["A/B testing", "hypothesis testing", "statistics", "product analytics"],
        "focus": "experimentation and statistics"
    },
    {
        "title": "Feature Engineering for Machine Learning Success",
        "keywords": ["feature engineering", "machine learning", "data preprocessing", "model performance"],
        "focus": "ML best practices"
    },
    {
        "title": "Clustering Techniques for Customer Segmentation",
        "keywords": ["clustering", "k-means", "customer segmentation", "unsupervised learning"],
        "focus": "unsupervised learning"
    },
    {
        "title": "Recommendation Systems: From Collaborative Filtering to Deep Learning",
        "keywords": ["recommendation systems", "collaborative filtering", "neural networks", "personalization"],
        "focus": "recommender systems"
    },
    {
        "title": "Natural Language Processing for Sentiment Analysis",
        "keywords": ["NLP", "sentiment analysis", "text analytics", "transformers"],
        "focus": "NLP applications"
    },
    {
        "title": "Gradient Boosting: XGBoost vs LightGBM vs CatBoost",
        "keywords": ["gradient boosting", "XGBoost", "LightGBM", "CatBoost", "ensemble methods"],
        "focus": "ensemble learning"
    },
    {
        "title": "Data Quality: The Foundation of Machine Learning",
        "keywords": ["data quality", "data cleaning", "data validation", "ML pipeline"],
        "focus": "data engineering"
    },
    {
        "title": "Explainable AI: Making Black Box Models Transparent",
        "keywords": ["XAI", "SHAP", "LIME", "model interpretability", "explainability"],
        "focus": "model interpretability"
    }
]

# Writing Style Guidelines (based on Medium article)
WRITING_STYLE = {
    "tone": "professional yet accessible",
    "structure": [
        "Introduction with context and hook",
        "Problem statement or motivation",
        "Core concepts explanation with examples",
        "Technical implementation details",
        "Real-world applications",
        "Code examples or demonstrations",
        "Visualizations and graphs",
        "Key takeaways and conclusions"
    ],
    "characteristics": [
        "Start with business context before diving into technical details",
        "Use real-world examples from retail/business domains",
        "Balance theory with practical implementation",
        "Include mathematical formulas when relevant but explain them clearly",
        "Use analogies to explain complex concepts",
        "Incorporate data visualizations to illustrate points",
        "Include code snippets with explanations",
        "End with actionable insights"
    ],
    "technical_depth": "intermediate to advanced",
    "target_audience": "data scientists, analysts, and business stakeholders"
}

# Visualization Settings
VISUALIZATION_CONFIG = {
    "style": "seaborn-v0_8-darkgrid",
    "color_palette": "deep",
    "figure_size": (10, 6),
    "dpi": 300,
    "formats": ["png", "svg"],
    "save_path": "articles/images/"
}

# Article Output Settings
ARTICLE_CONFIG = {
    "output_dir": "articles/",
    "images_dir": "articles/images/",
    "data_file": "articles/articles_data.json",
    "html_template": "article_generator/templates/article_template.html",
    "min_length": 1500,  # words
    "max_length": 3000,  # words
}

# GitHub Settings
GITHUB_CONFIG = {
    "repo": "harminder858/hp_portfolio",
    "branch": "claude/automate-data-science-article-011CUaXQcF2aqcAsvBFjWH9M",
    "auto_commit": True,
    "commit_message_prefix": "Automated article:"
}

# n8n Webhook Settings
N8N_CONFIG = {
    "webhook_url": os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook/generate-article"),
    "schedule": "0 9 * * 1",  # Every Monday at 9 AM (cron format)
}
