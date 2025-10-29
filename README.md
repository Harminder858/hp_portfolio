# Harminder Puri - Portfolio & Automated Article Generator

Personal portfolio website with automated data science article generation system.

🌐 **Live Site**: https://harminder858.github.io/hp_portfolio/

---

## 🚀 Features

### Portfolio Website
- Responsive single-page application
- Services showcase
- Project highlights
- Technical expertise display
- Insights & Articles section (auto-updated)
- Contact information

### Automated Article Generator
- **AI-Powered**: Uses Claude API to generate high-quality data science articles
- **Visual Content**: Automatically creates relevant graphs and visualizations
- **10+ Topics**: Rotating pool of data science topics
- **Smart Scheduling**: n8n workflow automation
- **GitHub Integration**: Auto-commit and push to GitHub Pages
- **Professional Styling**: Beautiful HTML rendering with code highlighting

---

## 📚 Article Topics

The system rotates through various data science topics:
- Customer Lifetime Value Analysis
- Time Series Forecasting with LSTM
- A/B Testing & Statistical Significance
- Feature Engineering Best Practices
- Clustering & Customer Segmentation
- Recommendation Systems
- Natural Language Processing
- Gradient Boosting Algorithms
- Data Quality Management
- Explainable AI & Model Interpretability

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5
- Tailwind CSS
- Font Awesome Icons

**Backend/Automation:**
- Python 3.8+
- Anthropic Claude API
- n8n Workflow Automation
- Git/GitHub Actions

**Libraries:**
- matplotlib, seaborn, plotly (visualizations)
- pandas, numpy (data processing)
- markdown, Pygments (content rendering)

---

## 📦 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+ (for n8n)
- Anthropic API key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harminder858/hp_portfolio.git
   cd hp_portfolio
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

3. **Install Python dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r article_generator/requirements.txt
   ```

4. **Run the article generator**
   ```bash
   # Easy way - use the run script
   chmod +x run_generator.sh
   ./run_generator.sh

   # Or run directly
   python3 article_generator/generator.py
   ```

5. **Set up n8n automation (optional)**
   ```bash
   npm install -g n8n
   n8n start
   # Import workflow from n8n_workflows/article_automation_workflow.json
   ```

📖 **Detailed Setup Guide**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## 📁 Project Structure

```
hp_portfolio/
├── article_generator/          # Article generation system
│   ├── config.py              # Configuration & topics
│   ├── generator.py           # Main generator script
│   ├── visualizations.py      # Chart/graph creator
│   ├── html_builder.py        # HTML converter
│   └── requirements.txt       # Python dependencies
├── n8n_workflows/             # Automation workflows
│   └── article_automation_workflow.json
├── articles/                  # Generated content
│   ├── *.md                   # Markdown articles
│   ├── *.html                 # HTML articles
│   ├── images/                # Visualizations
│   └── articles_data.json     # Article metadata
├── index.html                 # Portfolio homepage
├── run_generator.sh           # Quick run script
├── .env.example               # Environment template
├── SETUP_GUIDE.md            # Detailed setup instructions
└── README.md                  # This file
```

---

## 🎯 Usage

### Generate a Single Article

```bash
# Activate virtual environment
source venv/bin/activate

# Run generator
python3 article_generator/generator.py

# Commit and push
git add articles/ index.html
git commit -m "New article: $(date +%Y-%m-%d)"
git push
```

### Automate with n8n

1. Start n8n: `n8n start`
2. Import workflow from `n8n_workflows/`
3. Configure schedule (default: Monday 9 AM)
4. Articles generate and publish automatically!

### Manual Trigger via Webhook

```bash
curl -X POST http://localhost:5678/webhook/generate-article
```

---

## 🎨 Customization

### Add New Topics

Edit `article_generator/config.py`:

```python
ARTICLE_TOPICS = [
    {
        "title": "Your Topic Title",
        "keywords": ["keyword1", "keyword2"],
        "focus": "topic focus"
    },
    # ... more topics
]
```

### Modify Writing Style

Adjust the `WRITING_STYLE` dictionary in `config.py` to match your preferences.

### Change Schedule

Edit the cron expression in the n8n workflow:
- `0 9 * * 1` = Every Monday at 9 AM
- `0 14 * * 3` = Every Wednesday at 2 PM

---

## 📊 Generated Content Examples

Each article includes:
- ✍️ AI-generated content (1500-2500 words)
- 📊 Custom visualizations (2-4 graphs per article)
- 💻 Code examples with syntax highlighting
- 🏷️ Keyword tags and metadata
- ⏱️ Reading time estimation
- 📱 Responsive HTML design

---

## 🔧 Development

### Run Tests

```bash
# Test article generation
python3 article_generator/generator.py

# Test visualizations only
python3 article_generator/visualizations.py

# Test HTML builder
python3 article_generator/html_builder.py
```

### Debug Mode

Set environment variable for verbose output:
```bash
export DEBUG=1
python3 article_generator/generator.py
```

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Harminder Puri**

- Website: https://harminder858.github.io/hp_portfolio/
- LinkedIn: https://www.linkedin.com/in/harminderpuri/
- GitHub: https://github.com/Harminder858
- Medium: https://medium.com/@harminderpuri

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙏 Acknowledgments

- Built with [Claude](https://www.anthropic.com/claude) by Anthropic
- Workflow automation by [n8n](https://n8n.io/)
- Styling with [Tailwind CSS](https://tailwindcss.com/)
- Icons from [Font Awesome](https://fontawesome.com/)

---

## 📞 Support

If you encounter any issues:
1. Check the [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Review the troubleshooting section
3. Open an issue on GitHub

---

**Last Updated**: January 2025

Made with ❤️ and ☕ by Harminder Puri
