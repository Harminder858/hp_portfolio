#!/bin/bash

# Script to push generated articles to public portfolio repo
# Use this when automation is in a separate private repo

set -e

echo "📤 Pushing generated articles to public portfolio..."

# Configuration
PUBLIC_REPO_PATH="/path/to/hp_portfolio"  # Update this path
ARTICLES_SOURCE="./articles"
INDEX_SOURCE="./generated_index.html"

# Check if public repo exists
if [ ! -d "$PUBLIC_REPO_PATH" ]; then
    echo "❌ Error: Public repo not found at $PUBLIC_REPO_PATH"
    echo "   Please update PUBLIC_REPO_PATH in this script"
    exit 1
fi

# Copy generated articles
echo "📁 Copying articles..."
cp -r $ARTICLES_SOURCE/* $PUBLIC_REPO_PATH/articles/

# Update index.html in public repo
echo "📝 Updating index.html..."
# You would need to extract just the articles section
# For now, manual update or use html_builder.py directly on public repo

# Commit and push from public repo
cd $PUBLIC_REPO_PATH

git add articles/ index.html
git commit -m "Update articles: $(date +%Y-%m-%d)"
git push origin main

echo "✅ Articles published to public repository!"
