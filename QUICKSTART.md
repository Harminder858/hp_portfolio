# Quick Start Guide - Split Repository Setup

**Goal**: Set up private article automation that publishes to your public GitHub Pages website.

---

## 🎯 Overview

You'll have **2 repositories**:

1. **hp_portfolio** (PUBLIC) ← You're here
   - Website only
   - Generated articles
   - GitHub Pages hosting

2. **hp_portfolio_automation** (PRIVATE) ← Create this
   - AI article generator
   - n8n workflows
   - API keys & secrets

---

## ⚡ Quick Setup (5 Minutes)

### Step 1: Create Private Repo on GitHub

1. Go to https://github.com/new
2. Repository name: `hp_portfolio_automation`
3. Description: "Private article automation"
4. **Visibility: Private** ⚠️ IMPORTANT!
5. Click "Create repository"

### Step 2: Push Private Repo

```bash
cd ~/hp_portfolio_automation

# Link to your new private repo
git remote add origin https://github.com/Harminder858/hp_portfolio_automation.git

# Push
git push -u origin master
```

### Step 3: Clean Up Public Repo

```bash
cd ~/hp_portfolio

# Run cleanup script
./cleanup_for_split.sh

# Push changes
git push
```

### Step 4: Configure Private Repo

```bash
cd ~/hp_portfolio_automation

# Set up environment
cp .env.example .env
nano .env  # Add your ANTHROPIC_API_KEY

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 5: Test It!

```bash
cd ~/hp_portfolio_automation

# Run complete workflow
./run_and_sync.sh
```

This will:
- ✅ Generate an article
- ✅ Sync to public repo
- ✅ Push to GitHub Pages
- ✅ Update your live website!

---

## 🎉 You're Done!

**What you have now:**

✅ **Public repo** - Clean portfolio website
✅ **Private repo** - Powerful automation
✅ **Free hosting** - GitHub Pages works!
✅ **Secure** - API keys stay private
✅ **Automated** - Articles publish weekly

---

## 📅 Ongoing Usage

### Automatic (Set and Forget)

Set up n8n once:
```bash
cd ~/hp_portfolio_automation
n8n start
# Import workflow, set schedule
```

Articles generate **every Monday at 9 AM** automatically!

### Manual (On Demand)

```bash
cd ~/hp_portfolio_automation
./run_and_sync.sh
```

---

## 📂 Quick Reference

**Locations:**
- Public: `~/hp_portfolio`
- Private: `~/hp_portfolio_automation`

**Commands:**
```bash
# Generate + publish article
cd ~/hp_portfolio_automation && ./run_and_sync.sh

# Just generate (no publish)
cd ~/hp_portfolio_automation && ./run_generator.sh

# Just sync existing articles
cd ~/hp_portfolio_automation && python3 sync_to_public.py
```

**URLs:**
- Live site: https://harminder858.github.io/hp_portfolio/
- Public repo: https://github.com/Harminder858/hp_portfolio
- Private repo: https://github.com/Harminder858/hp_portfolio_automation

---

## ❓ Common Questions

**Q: Where do I edit the website?**
A: In the **public repo** (`hp_portfolio/index.html`)

**Q: Where do I run the generator?**
A: Always in the **private repo** (`hp_portfolio_automation/`)

**Q: How do I add article topics?**
A: Edit `article_generator/config.py` in the **private repo**

**Q: Can I make the public repo private?**
A: Yes, but you'll need GitHub Pro ($4/month) for Pages to work

---

## 🆘 Troubleshooting

**"Public repo not found"**
```bash
cd ~/hp_portfolio_automation
export PUBLIC_REPO_PATH="/home/user/hp_portfolio"
```

**"API key not set"**
```bash
cd ~/hp_portfolio_automation
nano .env  # Add ANTHROPIC_API_KEY
```

**"Sync failed"**
```bash
cd ~/hp_portfolio_automation
python3 config_repos.py  # Verify paths
```

---

## 📖 Full Documentation

- **SPLIT_REPO_SETUP.md** - Detailed architecture guide
- **Private repo README** - Complete automation docs
- **Public repo README** - Portfolio info

---

**Need help?** Check the detailed guides or open an issue!

---

**Last Updated**: January 2025
