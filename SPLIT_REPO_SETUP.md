# Split Repository Setup Guide

This guide explains how to set up the split repository architecture where:
- **hp_portfolio** (PUBLIC) - Contains website and published articles
- **hp_portfolio_automation** (PRIVATE) - Contains automation code and secrets

---

## 🎯 Why Split?

**Benefits:**
- ✅ Keep automation code and API keys private
- ✅ Free GitHub Pages hosting (works with public repos)
- ✅ Show only polished content publicly
- ✅ Best of both worlds

---

## 📦 What's in Each Repo

### Public Repo (hp_portfolio)
```
hp_portfolio/                    ← THIS REPO (PUBLIC)
├── index.html                   ✅ Portfolio homepage
├── articles/                    ✅ Generated articles
│   ├── *.md                     ✅ Markdown files
│   ├── *.html                   ✅ HTML articles
│   ├── images/                  ✅ Visualizations
│   └── articles_data.json       ✅ Article metadata
├── *.css                        ✅ Stylesheets (if any)
├── *.js                         ✅ Scripts (if any)
└── README.md                    ✅ Public readme
```

### Private Repo (hp_portfolio_automation)
```
hp_portfolio_automation/         ← SEPARATE REPO (PRIVATE)
├── article_generator/           🔒 Generator code
├── n8n_workflows/               🔒 Automation workflows
├── sync_to_public.py            🔒 Sync script
├── run_and_sync.sh              🔒 Workflow script
├── .env                         🔒 API keys
└── README.md                    🔒 Private readme
```

---

## 🚀 Setup Instructions

### Step 1: Keep This Repo (Public)

This repository (`hp_portfolio`) will remain **PUBLIC** for GitHub Pages.

**Clean up automation files** (they'll be in the private repo):

```bash
cd ~/hp_portfolio

# Remove automation files from public repo
git rm -r article_generator/
git rm -r n8n_workflows/
git rm run_generator.sh
git rm push_to_public.sh
git rm .env.example
git rm SETUP_GUIDE.md

# Keep only website files
git add index.html articles/
git commit -m "Remove automation code (moved to private repo)"
git push
```

### Step 2: Set Up Private Repo

The private repo has already been created at `/home/user/hp_portfolio_automation`.

**Create the GitHub repository:**

```bash
# Go to GitHub.com and create a new PRIVATE repository
# Name: hp_portfolio_automation
# Visibility: PRIVATE

# Then link your local repo:
cd ~/hp_portfolio_automation

git remote add origin https://github.com/Harminder858/hp_portfolio_automation.git
git push -u origin master
```

### Step 3: Configure the Connection

Edit `config_repos.py` in the private repo:

```bash
cd ~/hp_portfolio_automation
nano config_repos.py
```

Update the path:
```python
PUBLIC_REPO_PATH = "/home/user/hp_portfolio"  # or wherever it is
```

### Step 4: Set Up API Keys

```bash
cd ~/hp_portfolio_automation

cp .env.example .env
nano .env
# Add your ANTHROPIC_API_KEY
```

### Step 5: Test the Setup

```bash
cd ~/hp_portfolio_automation

# Test sync
python3 sync_to_public.py

# Generate article and sync
./run_and_sync.sh
```

---

## 🔄 Daily Workflow

### Automatic (n8n)

1. n8n runs on schedule (Monday 9 AM)
2. Generates article in **private repo**
3. Syncs to **public repo**
4. Pushes to GitHub Pages
5. Website updates automatically!

### Manual

```bash
# In private repo
cd ~/hp_portfolio_automation
./run_and_sync.sh
```

This will:
- Generate article with AI
- Create visualizations
- Sync to public repo
- Push to GitHub Pages

---

## 📂 Repository Locations

**Local paths:**
- Public: `~/hp_portfolio`
- Private: `~/hp_portfolio_automation`

**GitHub URLs:**
- Public: `https://github.com/Harminder858/hp_portfolio` (PUBLIC)
- Private: `https://github.com/Harminder858/hp_portfolio_automation` (PRIVATE)

**Website URL:**
- Live site: `https://harminder858.github.io/hp_portfolio/`

---

## 🔒 Security

**Public repo contains:**
- ✅ Website HTML/CSS/JS
- ✅ Published articles
- ✅ Article images
- ❌ NO automation code
- ❌ NO API keys

**Private repo contains:**
- 🔒 All automation code
- 🔒 API keys (in .env)
- 🔒 n8n workflows
- 🔒 Generator algorithms

---

## 🛠️ Maintenance

### Update Article Topics

Edit in **private repo**:
```bash
cd ~/hp_portfolio_automation
nano article_generator/config.py
```

### Update Website Design

Edit in **public repo**:
```bash
cd ~/hp_portfolio
nano index.html
```

### View Logs

All generation happens in private repo:
```bash
cd ~/hp_portfolio_automation
./run_and_sync.sh 2>&1 | tee logs/run.log
```

---

## ❓ FAQ

**Q: Can I still edit the public repo directly?**
A: Yes! You can edit `index.html` and other website files directly in the public repo.

**Q: Where do I add new article topics?**
A: In the **private repo**: `article_generator/config.py`

**Q: Where do I run the generator?**
A: Always in the **private repo**: `~/hp_portfolio_automation`

**Q: What if I want to make the public repo private?**
A: Then you'd need GitHub Pro ($4/month) for GitHub Pages to work.

**Q: Can others see my automation code?**
A: No, only the private repo contains automation code, and it's set to PRIVATE.

---

## 🎉 Benefits of This Setup

✅ **Free hosting** - GitHub Pages works with public repos
✅ **Privacy** - Automation code is private
✅ **Security** - API keys never exposed
✅ **Clean public repo** - Only polished content visible
✅ **Full control** - Automation in private repo
✅ **Best of both worlds**

---

## 📞 Need Help?

Check:
1. Private repo README: `~/hp_portfolio_automation/README.md`
2. Test sync: `python3 sync_to_public.py`
3. Verify paths: `python3 config_repos.py`

---

**Last Updated**: January 2025
