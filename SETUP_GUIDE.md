# Article Automation Setup Guide

This guide will help you set up the automated article generation system on your new laptop.

## Overview

The system consists of:
1. **Python Article Generator** - Uses Claude API to generate data science articles with visualizations
2. **n8n Workflow** - Automates the entire process (scheduling, generation, git commit/push)
3. **GitHub Pages Integration** - Automatically publishes to your portfolio

---

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher (for n8n)
- Git configured with GitHub access
- Anthropic API key (Claude)

---

## Part 1: Python Environment Setup

### 1.1 Install Python Dependencies

```bash
# Navigate to the project directory
cd ~/hp_portfolio

# Create a virtual environment (recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows

# Install required packages
pip install -r article_generator/requirements.txt
```

### 1.2 Set Up API Keys

```bash
# Create a .env file in the project root
cat > .env << 'EOF'
# Anthropic API Key (required)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# n8n Webhook URL (optional, for manual triggers)
N8N_WEBHOOK_URL=http://localhost:5678/webhook/generate-article

# Slack Webhook (optional, for notifications)
SLACK_WEBHOOK_URL=your_slack_webhook_url_here
EOF

# Make sure to replace the placeholder values with actual keys
```

**Get your Anthropic API key:**
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key and copy it

### 1.3 Test the Article Generator

```bash
# Run a test generation
python3 article_generator/generator.py

# This should:
# - Select a random topic
# - Generate article content using Claude
# - Create visualizations
# - Save markdown and HTML files
# - Update the index.html
```

---

## Part 2: n8n Setup

### 2.1 Install n8n

```bash
# Install n8n globally via npm
npm install -g n8n

# OR use npx (no installation required)
npx n8n

# OR use Docker (recommended for production)
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 2.2 Start n8n

```bash
# Start n8n server
n8n start

# Access n8n web interface
# Open browser: http://localhost:5678
```

### 2.3 Import Workflow

1. Open n8n interface at http://localhost:5678
2. Click on "Workflows" in the left menu
3. Click "+ Add Workflow"
4. Click the menu (⋮) → "Import from File"
5. Select `n8n_workflows/article_automation_workflow.json`
6. Click "Save"

### 2.4 Configure Workflow

The workflow has two triggers:

**Schedule Trigger:**
- Runs every Monday at 9 AM
- Edit the cron expression to change timing

**Webhook Trigger:**
- Manual trigger via HTTP POST
- URL: `http://localhost:5678/webhook/generate-article`

### 2.5 Set Environment Variables in n8n

1. Go to Settings → Environment Variables
2. Add:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `SLACK_WEBHOOK_URL`: (Optional) Your Slack webhook for notifications

---

## Part 3: GitHub Configuration

### 3.1 Configure Git

```bash
# Set your git identity (if not already done)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Ensure you're on the correct branch
cd ~/hp_portfolio
git checkout claude/automate-data-science-article-011CUaXQcF2aqcAsvBFjWH9M
```

### 3.2 Test Git Push

```bash
# Create a test commit
echo "test" > test.txt
git add test.txt
git commit -m "Test commit"
git push -u origin claude/automate-data-science-article-011CUaXQcF2aqcAsvBFjWH9M

# Clean up
git rm test.txt
git commit -m "Remove test file"
git push
```

---

## Part 4: Running the System

### 4.1 Manual Execution (Python only)

```bash
# Activate virtual environment
source venv/bin/activate

# Run the generator
python3 article_generator/generator.py

# The script will:
# 1. Generate a new article
# 2. Create visualizations
# 3. Update index.html
# 4. Output files to articles/ directory

# Manually commit and push
git add articles/ index.html
git commit -m "Automated article: $(date +%Y-%m-%d)"
git push -u origin claude/automate-data-science-article-011CUaXQcF2aqcAsvBFjWH9M
```

### 4.2 Trigger via n8n Webhook

```bash
# Trigger the workflow via webhook
curl -X POST http://localhost:5678/webhook/generate-article

# This will:
# 1. Run the Python generator
# 2. Automatically commit and push to GitHub
# 3. Send notifications (if configured)
```

### 4.3 Automatic Execution (Scheduled)

Once n8n is running with the imported workflow:
- Articles will be automatically generated every Monday at 9 AM
- The system handles everything end-to-end
- You'll receive Slack notifications (if configured)

---

## Part 5: Customization

### 5.1 Add More Topics

Edit `article_generator/config.py`:

```python
ARTICLE_TOPICS = [
    {
        "title": "Your New Topic Title",
        "keywords": ["keyword1", "keyword2", "keyword3"],
        "focus": "your focus area"
    },
    # ... add more topics
]
```

### 5.2 Change Schedule

Edit the n8n workflow:
1. Click on "Schedule Trigger" node
2. Modify the cron expression
   - `0 9 * * 1` = Every Monday at 9 AM
   - `0 14 * * 3` = Every Wednesday at 2 PM
   - `0 10 1 * *` = First day of month at 10 AM

### 5.3 Customize Writing Style

Edit `article_generator/config.py`:

```python
WRITING_STYLE = {
    "tone": "your preferred tone",
    "characteristics": [
        "Your style characteristic 1",
        "Your style characteristic 2",
        # ...
    ]
}
```

---

## Part 6: Troubleshooting

### Issue: "ANTHROPIC_API_KEY not found"

**Solution:**
```bash
# Load environment variables
export ANTHROPIC_API_KEY='your-key-here'

# OR create .env file and load it
source .env
```

### Issue: "Permission denied" when pushing to Git

**Solution:**
```bash
# Set up SSH key or use HTTPS with token
gh auth login

# OR configure SSH
ssh-keygen -t ed25519 -C "your_email@example.com"
# Add the key to GitHub
```

### Issue: n8n workflow fails

**Solution:**
1. Check n8n logs: `~/.n8n/logs/`
2. Verify API keys in n8n environment variables
3. Test Python script independently first
4. Check file permissions for article_generator/ directory

### Issue: Visualizations not generating

**Solution:**
```bash
# Install additional dependencies
pip install matplotlib seaborn plotly numpy pandas

# Check matplotlib backend
python3 -c "import matplotlib; print(matplotlib.get_backend())"
```

---

## Part 7: Production Deployment

### 7.1 Run n8n as a Service (Linux)

```bash
# Create systemd service
sudo nano /etc/systemd/system/n8n.service
```

Add:
```ini
[Unit]
Description=n8n workflow automation
After=network.target

[Service]
Type=simple
User=your_username
ExecStart=/usr/local/bin/n8n start
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable n8n
sudo systemctl start n8n
sudo systemctl status n8n
```

### 7.2 Use PM2 (Alternative)

```bash
# Install PM2
npm install -g pm2

# Start n8n with PM2
pm2 start n8n

# Set to start on boot
pm2 startup
pm2 save
```

---

## Part 8: Monitoring & Maintenance

### 8.1 View Generated Articles

- **Markdown**: `articles/*.md`
- **HTML**: `articles/*.html`
- **Images**: `articles/images/*.png`
- **Database**: `articles/articles_data.json`

### 8.2 Check Logs

```bash
# Python script output
python3 article_generator/generator.py 2>&1 | tee logs/generator.log

# n8n logs
tail -f ~/.n8n/logs/n8n.log
```

### 8.3 Backup

```bash
# Backup articles database
cp articles/articles_data.json articles/articles_data.json.backup

# Backup entire articles directory
tar -czf articles_backup_$(date +%Y%m%d).tar.gz articles/
```

---

## Quick Start Summary

```bash
# 1. Install dependencies
pip install -r article_generator/requirements.txt
npm install -g n8n

# 2. Set API key
export ANTHROPIC_API_KEY='your-key-here'

# 3. Test article generation
python3 article_generator/generator.py

# 4. Start n8n
n8n start

# 5. Import workflow
# Open http://localhost:5678 and import n8n_workflows/article_automation_workflow.json

# 6. Trigger manually
curl -X POST http://localhost:5678/webhook/generate-article

# Done! Articles will now generate automatically every Monday at 9 AM
```

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review n8n documentation: https://docs.n8n.io/
3. Check Anthropic API docs: https://docs.anthropic.com/

---

## Project Structure

```
hp_portfolio/
├── article_generator/
│   ├── config.py              # Configuration and settings
│   ├── generator.py           # Main article generator
│   ├── visualizations.py      # Visualization creator
│   ├── html_builder.py        # HTML converter
│   └── requirements.txt       # Python dependencies
├── n8n_workflows/
│   └── article_automation_workflow.json  # n8n workflow
├── articles/
│   ├── *.md                   # Generated markdown articles
│   ├── *.html                 # Generated HTML articles
│   ├── images/                # Article visualizations
│   └── articles_data.json     # Articles database
├── index.html                 # Main portfolio page (auto-updated)
├── .env                       # Environment variables (create this)
└── SETUP_GUIDE.md            # This file
```

Happy automating! 🚀
