#!/bin/bash

# Article Generator Runner Script
# This script sets up the environment and runs the article generator

set -e  # Exit on error

echo "🚀 Article Generator - Starting..."
echo "=================================="

# Navigate to script directory
cd "$(dirname "$0")"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "   Please copy .env.example to .env and fill in your API keys"
    echo "   cp .env.example .env"
    exit 1
fi

# Load environment variables
echo "📝 Loading environment variables..."
set -a
source .env
set +a

# Check for required API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ Error: ANTHROPIC_API_KEY not set in .env file"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -q -r article_generator/requirements.txt

# Run the article generator
echo ""
echo "✍️  Generating article..."
echo "=================================="
python3 article_generator/generator.py

# Check if generation was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo "✅ Article generated successfully!"
    echo ""

    # Ask if user wants to commit and push
    read -p "Do you want to commit and push to GitHub? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📤 Committing and pushing to GitHub..."
        git add articles/ index.html
        git commit -m "Automated article: $(date +%Y-%m-%d)"
        git push -u origin claude/automate-data-science-article-011CUaXQcF2aqcAsvBFjWH9M
        echo "✅ Pushed to GitHub successfully!"
    else
        echo "ℹ️  Skipping git push. You can commit manually later."
    fi
else
    echo "❌ Article generation failed!"
    exit 1
fi

# Deactivate virtual environment
deactivate

echo ""
echo "🎉 Done!"
