#!/bin/bash

# Cleanup Script for Public Repo
# Removes automation files that now live in the private repo

set -e

echo "🧹 CLEANING UP PUBLIC REPO FOR SPLIT ARCHITECTURE"
echo "=================================================="
echo ""
echo "This script will remove automation files from this public repo."
echo "These files now live in the PRIVATE hp_portfolio_automation repo."
echo ""

read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

cd "$(dirname "$0")"

echo ""
echo "📁 Removing automation files..."

# Remove automation directories
if [ -d "article_generator" ]; then
    git rm -r article_generator/
    echo "   ✓ Removed article_generator/"
fi

if [ -d "n8n_workflows" ]; then
    git rm -r n8n_workflows/
    echo "   ✓ Removed n8n_workflows/"
fi

# Remove automation scripts
files_to_remove=(
    "run_generator.sh"
    "push_to_public.sh"
    ".env.example"
    "SETUP_GUIDE.md"
)

for file in "${files_to_remove[@]}"; do
    if [ -f "$file" ]; then
        git rm "$file"
        echo "   ✓ Removed $file"
    fi
done

# Keep these files for the public repo:
# - index.html
# - articles/
# - README.md (will be updated)
# - SPLIT_REPO_SETUP.md
# - .gitignore

echo ""
echo "📝 Files to keep in public repo:"
echo "   ✓ index.html"
echo "   ✓ articles/ (generated content)"
echo "   ✓ README.md"
echo "   ✓ SPLIT_REPO_SETUP.md"
echo "   ✓ .gitignore"

echo ""
echo "💾 Committing changes..."

git commit -m "Clean up: Move automation code to private repository

Removed automation files that now live in hp_portfolio_automation (private repo):
- article_generator/ - AI article generation code
- n8n_workflows/ - Automation workflows
- run_generator.sh - Generator script
- .env.example - Environment template
- SETUP_GUIDE.md - Setup guide

This public repository now contains only:
- Website files (index.html)
- Generated articles
- Public documentation

Automation code is now in a separate private repository.
See SPLIT_REPO_SETUP.md for details."

echo ""
echo "✅ Cleanup complete!"
echo ""
echo "Next steps:"
echo "1. Review the changes: git status"
echo "2. Push to GitHub: git push"
echo "3. Set up private repo (see SPLIT_REPO_SETUP.md)"
echo ""
