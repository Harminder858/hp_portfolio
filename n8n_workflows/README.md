# n8n Workflow Setup

This directory contains the n8n workflow configuration for automated article generation.

## Quick Setup

### 1. Install n8n

```bash
# Option 1: Install globally via npm
npm install -g n8n

# Option 2: Run with npx (no installation)
npx n8n

# Option 3: Use Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 2. Start n8n

```bash
n8n start
```

Open your browser to: http://localhost:5678

### 3. Import Workflow

1. Click "Workflows" in the left sidebar
2. Click "+ Add Workflow"
3. Click the menu icon (⋮) → "Import from File"
4. Select `article_automation_workflow.json`
5. Click "Save"

### 4. Configure Environment Variables

In n8n Settings → Environment Variables, add:

- `ANTHROPIC_API_KEY` - Your Anthropic API key (required)
- `SLACK_WEBHOOK_URL` - Your Slack webhook URL (optional)

### 5. Activate the Workflow

1. Click the workflow you just imported
2. Click the toggle switch in the top right to activate
3. The workflow is now running!

## Workflow Overview

The workflow has two triggers:

### Schedule Trigger (Automatic)
- Runs every Monday at 9 AM
- Fully automated article generation and publishing
- No manual intervention required

### Webhook Trigger (Manual)
- URL: `http://localhost:5678/webhook/generate-article`
- Trigger on-demand via HTTP POST
- Useful for testing or generating articles anytime

## Workflow Steps

1. **Trigger** - Schedule or webhook activates
2. **Generate Article** - Runs Python script to create article
3. **Check Success** - Validates generation completed
4. **Git Commit & Push** - Commits and pushes to GitHub
5. **Notification** - Sends success/error notification (optional)
6. **Response** - Returns webhook response (for manual triggers)

## Manual Trigger Examples

### Using curl

```bash
curl -X POST http://localhost:5678/webhook/generate-article
```

### Using Python

```python
import requests

response = requests.post('http://localhost:5678/webhook/generate-article')
print(response.json())
```

### Using JavaScript

```javascript
fetch('http://localhost:5678/webhook/generate-article', {
  method: 'POST'
})
.then(response => response.json())
.then(data => console.log(data));
```

## Customization

### Change Schedule

Edit the Schedule Trigger node:
- Click on "Schedule Trigger" node
- Modify the cron expression

**Common Cron Patterns:**
- `0 9 * * 1` - Every Monday at 9 AM
- `0 14 * * 3` - Every Wednesday at 2 PM
- `0 10 1 * *` - First day of every month at 10 AM
- `0 9 * * 1-5` - Every weekday at 9 AM

### Add Notifications

The workflow includes optional Slack notifications:

1. Create a Slack webhook:
   - Go to https://api.slack.com/apps
   - Create an app
   - Add Incoming Webhooks feature
   - Copy webhook URL

2. Add to n8n environment variables:
   - Key: `SLACK_WEBHOOK_URL`
   - Value: Your webhook URL

3. Activate notification nodes in the workflow

### Modify Git Branch

Edit the "Git Commit & Push" node to change the target branch:

```bash
git push -u origin your-branch-name
```

## Troubleshooting

### Workflow not triggering

**Check:**
1. Workflow is activated (toggle in top right)
2. n8n is running (`n8n start`)
3. No errors in n8n logs

### Article generation fails

**Check:**
1. `ANTHROPIC_API_KEY` is set correctly
2. Python dependencies are installed
3. Run the script manually to see errors:
   ```bash
   python3 article_generator/generator.py
   ```

### Git push fails

**Check:**
1. Git credentials are configured
2. You have push access to the repository
3. The branch name is correct
4. Run git commands manually to test:
   ```bash
   git push -u origin branch-name
   ```

## Advanced Configuration

### Run n8n in Production

**Using PM2:**
```bash
npm install -g pm2
pm2 start n8n
pm2 startup
pm2 save
```

**Using systemd (Linux):**
```bash
sudo nano /etc/systemd/system/n8n.service
```

Add:
```ini
[Unit]
Description=n8n
After=network.target

[Service]
Type=simple
User=your_username
ExecStart=/usr/local/bin/n8n start
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable:
```bash
sudo systemctl enable n8n
sudo systemctl start n8n
```

### Secure n8n

For production deployments:

1. **Use HTTPS**: Set up reverse proxy (nginx/Apache)
2. **Authentication**: Configure n8n basic auth
3. **Firewall**: Restrict access to n8n port
4. **Environment Variables**: Use secure secret management

## Resources

- n8n Documentation: https://docs.n8n.io/
- n8n Community: https://community.n8n.io/
- Workflow Templates: https://n8n.io/workflows/

## Support

For issues specific to this workflow, check the main [SETUP_GUIDE.md](../SETUP_GUIDE.md) or open an issue on GitHub.
