"""
Visualization Generator for Articles
Creates illustrative graphs and charts based on article topic
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict
from pathlib import Path

from config import VISUALIZATION_CONFIG, ARTICLE_CONFIG


# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette(VISUALIZATION_CONFIG["color_palette"])


def create_article_visualizations(topic: Dict, content: str) -> List[str]:
    """
    Create visualizations based on article topic
    Returns list of image file paths
    """
    topic_title = topic["title"].lower()
    article_slug = topic["title"].lower().replace(" ", "-").replace(":", "")
    images = []

    # Determine which visualizations to create based on topic
    if "customer lifetime value" in topic_title or "cltv" in topic_title:
        images.extend(create_cltv_visualizations(article_slug))

    elif "lstm" in topic_title or "time series" in topic_title or "forecasting" in topic_title:
        images.extend(create_timeseries_visualizations(article_slug))

    elif "a/b test" in topic_title or "statistical significance" in topic_title:
        images.extend(create_ab_test_visualizations(article_slug))

    elif "clustering" in topic_title or "segmentation" in topic_title:
        images.extend(create_clustering_visualizations(article_slug))

    elif "feature engineering" in topic_title:
        images.extend(create_feature_importance_visualizations(article_slug))

    elif "recommendation" in topic_title:
        images.extend(create_recommendation_visualizations(article_slug))

    elif "nlp" in topic_title or "sentiment" in topic_title:
        images.extend(create_nlp_visualizations(article_slug))

    elif "gradient boosting" in topic_title or "xgboost" in topic_title:
        images.extend(create_boosting_visualizations(article_slug))

    elif "explainable ai" in topic_title or "shap" in topic_title:
        images.extend(create_explainability_visualizations(article_slug))

    else:
        # Generic data science visualizations
        images.extend(create_generic_visualizations(article_slug))

    return images


def save_figure(fig, filename: str) -> str:
    """Save figure and return path"""
    Path(ARTICLE_CONFIG["images_dir"]).mkdir(parents=True, exist_ok=True)

    filepath = f"{ARTICLE_CONFIG['images_dir']}{filename}.png"
    fig.savefig(filepath, dpi=VISUALIZATION_CONFIG["dpi"], bbox_inches='tight')
    plt.close(fig)

    return filepath


def create_cltv_visualizations(article_slug: str) -> List[str]:
    """Create CLTV-related visualizations"""
    images = []

    # 1. CLTV Distribution
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    np.random.seed(42)
    cltv_data = np.random.lognormal(mean=5, sigma=1.5, size=1000)
    ax.hist(cltv_data, bins=50, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Customer Lifetime Value ($)', fontsize=12)
    ax.set_ylabel('Number of Customers', fontsize=12)
    ax.set_title('Distribution of Customer Lifetime Value', fontsize=14, fontweight='bold')
    ax.axvline(np.median(cltv_data), color='red', linestyle='--', label=f'Median: ${np.median(cltv_data):.2f}')
    ax.legend()
    images.append(save_figure(fig, f"{article_slug}_cltv_distribution"))

    # 2. CLTV by Segment
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    segments = ['High Value', 'Medium Value', 'Low Value', 'New Customers']
    cltv_values = [450, 280, 120, 85]
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#95a5a6']
    bars = ax.bar(segments, cltv_values, color=colors, edgecolor='black')
    ax.set_ylabel('Average CLTV ($)', fontsize=12)
    ax.set_title('Customer Lifetime Value by Segment', fontsize=14, fontweight='bold')

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    images.append(save_figure(fig, f"{article_slug}_cltv_segments"))

    # 3. CLTV Trend over Time
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    months = pd.date_range(start='2023-01', end='2024-12', freq='M')
    base_cltv = 200
    trend = base_cltv + np.cumsum(np.random.randn(len(months)) * 10)

    ax.plot(months, trend, marker='o', linewidth=2, markersize=6)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Average CLTV ($)', fontsize=12)
    ax.set_title('Customer Lifetime Value Trend Over Time', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    images.append(save_figure(fig, f"{article_slug}_cltv_trend"))

    return images


def create_timeseries_visualizations(article_slug: str) -> List[str]:
    """Create time series and LSTM-related visualizations"""
    images = []

    # 1. Time Series with Trend and Seasonality
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    np.random.seed(42)
    time = np.arange(0, 365)
    trend = 0.1 * time
    seasonality = 10 * np.sin(2 * np.pi * time / 30)
    noise = np.random.randn(len(time)) * 2
    series = 50 + trend + seasonality + noise

    ax.plot(time, series, label='Observed Data', alpha=0.7)
    ax.plot(time, 50 + trend, label='Trend', linestyle='--', linewidth=2)
    ax.set_xlabel('Days', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('Time Series Decomposition', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    images.append(save_figure(fig, f"{article_slug}_timeseries"))

    # 2. LSTM Prediction vs Actual
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    test_time = np.arange(300, 365)
    actual = series[300:]
    predicted = actual + np.random.randn(len(actual)) * 3

    ax.plot(test_time, actual, label='Actual', marker='o', markersize=4)
    ax.plot(test_time, predicted, label='LSTM Prediction', marker='s', markersize=4, alpha=0.7)
    ax.set_xlabel('Days', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('LSTM Model: Predictions vs Actual Values', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    images.append(save_figure(fig, f"{article_slug}_lstm_prediction"))

    # 3. Model Performance Metrics
    fig, ax = plt.subplots(figsize=(8, 6))
    metrics = ['MAE', 'RMSE', 'MAPE']
    lstm_scores = [2.5, 3.2, 8.5]
    arima_scores = [3.8, 4.9, 12.3]

    x = np.arange(len(metrics))
    width = 0.35

    ax.bar(x - width/2, lstm_scores, width, label='LSTM', color='#3498db')
    ax.bar(x + width/2, arima_scores, width, label='ARIMA', color='#e74c3c')

    ax.set_ylabel('Error Value', fontsize=12)
    ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    images.append(save_figure(fig, f"{article_slug}_model_comparison"))

    return images


def create_ab_test_visualizations(article_slug: str) -> List[str]:
    """Create A/B testing visualizations"""
    images = []

    # 1. Conversion Rate Comparison
    fig, ax = plt.subplots(figsize=(8, 6))
    groups = ['Control (A)', 'Variant (B)']
    conversion_rates = [12.5, 15.8]
    colors = ['#95a5a6', '#2ecc71']

    bars = ax.bar(groups, conversion_rates, color=colors, edgecolor='black', linewidth=2)
    ax.set_ylabel('Conversion Rate (%)', fontsize=12)
    ax.set_title('A/B Test: Conversion Rate Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 20)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Add significance indicator
    ax.plot([0, 1], [18, 18], 'k-', linewidth=2)
    ax.text(0.5, 18.5, 'p < 0.05 *', ha='center', fontsize=10)

    images.append(save_figure(fig, f"{article_slug}_ab_test_results"))

    # 2. Statistical Power Analysis
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    sample_sizes = np.arange(100, 10000, 100)
    power = 1 - np.exp(-sample_sizes / 3000)

    ax.plot(sample_sizes, power, linewidth=2, color='#3498db')
    ax.axhline(y=0.8, color='red', linestyle='--', label='80% Power Threshold')
    ax.set_xlabel('Sample Size per Group', fontsize=12)
    ax.set_ylabel('Statistical Power', fontsize=12)
    ax.set_title('Statistical Power vs Sample Size', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    images.append(save_figure(fig, f"{article_slug}_power_analysis"))

    return images


def create_clustering_visualizations(article_slug: str) -> List[str]:
    """Create clustering visualizations"""
    images = []

    # 1. K-means Clustering
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    np.random.seed(42)

    # Generate synthetic clusters
    cluster1 = np.random.randn(100, 2) * 0.5 + np.array([2, 2])
    cluster2 = np.random.randn(100, 2) * 0.5 + np.array([6, 6])
    cluster3 = np.random.randn(100, 2) * 0.5 + np.array([6, 2])

    ax.scatter(cluster1[:, 0], cluster1[:, 1], c='#e74c3c', label='Segment 1', alpha=0.6, s=50)
    ax.scatter(cluster2[:, 0], cluster2[:, 1], c='#3498db', label='Segment 2', alpha=0.6, s=50)
    ax.scatter(cluster3[:, 0], cluster3[:, 1], c='#2ecc71', label='Segment 3', alpha=0.6, s=50)

    # Add centroids
    centroids = np.array([[2, 2], [6, 6], [6, 2]])
    ax.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=200,
               edgecolors='white', linewidths=2, label='Centroids')

    ax.set_xlabel('Feature 1 (e.g., Purchase Frequency)', fontsize=12)
    ax.set_ylabel('Feature 2 (e.g., Average Order Value)', fontsize=12)
    ax.set_title('Customer Segmentation using K-means Clustering', fontsize=14, fontweight='bold')
    ax.legend()
    images.append(save_figure(fig, f"{article_slug}_clustering"))

    # 2. Elbow Method
    fig, ax = plt.subplots(figsize=(8, 6))
    k_values = range(1, 11)
    inertia = [1000, 650, 400, 280, 220, 180, 160, 150, 142, 138]

    ax.plot(k_values, inertia, marker='o', linewidth=2, markersize=8)
    ax.axvline(x=3, color='red', linestyle='--', label='Optimal K=3')
    ax.set_xlabel('Number of Clusters (K)', fontsize=12)
    ax.set_ylabel('Within-Cluster Sum of Squares', fontsize=12)
    ax.set_title('Elbow Method for Optimal K', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    images.append(save_figure(fig, f"{article_slug}_elbow_method"))

    return images


def create_feature_importance_visualizations(article_slug: str) -> List[str]:
    """Create feature engineering visualizations"""
    images = []

    # Feature Importance
    fig, ax = plt.subplots(figsize=(10, 6))
    features = ['Purchase_Frequency', 'Avg_Order_Value', 'Days_Since_Last',
                'Total_Spent', 'Product_Diversity', 'Session_Duration',
                'Cart_Abandonment', 'Email_Engagement']
    importance = [0.25, 0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.04]

    colors = ['#2ecc71' if imp > 0.15 else '#3498db' if imp > 0.10 else '#95a5a6'
              for imp in importance]

    ax.barh(features, importance, color=colors, edgecolor='black')
    ax.set_xlabel('Feature Importance', fontsize=12)
    ax.set_title('Feature Importance for Customer Churn Prediction', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    images.append(save_figure(fig, f"{article_slug}_feature_importance"))

    return images


def create_recommendation_visualizations(article_slug: str) -> List[str]:
    """Create recommendation system visualizations"""
    images = []

    # Collaborative Filtering Matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    np.random.seed(42)
    ratings = np.random.randint(0, 6, size=(8, 10))
    ratings[ratings == 0] = np.nan  # Some missing ratings

    im = ax.imshow(ratings, cmap='YlOrRd', aspect='auto')
    ax.set_xticks(range(10))
    ax.set_yticks(range(8))
    ax.set_xticklabels([f'Item {i+1}' for i in range(10)], rotation=45)
    ax.set_yticklabels([f'User {i+1}' for i in range(8)])
    ax.set_title('User-Item Rating Matrix (Collaborative Filtering)', fontsize=14, fontweight='bold')

    plt.colorbar(im, ax=ax, label='Rating')
    images.append(save_figure(fig, f"{article_slug}_rating_matrix"))

    return images


def create_nlp_visualizations(article_slug: str) -> List[str]:
    """Create NLP and sentiment analysis visualizations"""
    images = []

    # Sentiment Distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    sentiments = ['Positive', 'Neutral', 'Negative']
    counts = [450, 280, 120]
    colors = ['#2ecc71', '#3498db', '#e74c3c']

    wedges, texts, autotexts = ax.pie(counts, labels=sentiments, colors=colors,
                                        autopct='%1.1f%%', startangle=90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)

    ax.set_title('Sentiment Distribution in Customer Reviews', fontsize=14, fontweight='bold')
    images.append(save_figure(fig, f"{article_slug}_sentiment_distribution"))

    return images


def create_boosting_visualizations(article_slug: str) -> List[str]:
    """Create gradient boosting comparison visualizations"""
    images = []

    # Model Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    models = ['XGBoost', 'LightGBM', 'CatBoost', 'Random\nForest']
    accuracy = [0.92, 0.93, 0.91, 0.88]
    training_time = [45, 28, 52, 60]

    # Accuracy comparison
    bars1 = ax1.bar(models, accuracy, color=['#e74c3c', '#3498db', '#2ecc71', '#95a5a6'],
                    edgecolor='black')
    ax1.set_ylabel('Accuracy', fontsize=12)
    ax1.set_title('Model Accuracy Comparison', fontsize=14, fontweight='bold')
    ax1.set_ylim(0.85, 0.95)

    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Training time comparison
    bars2 = ax2.bar(models, training_time, color=['#e74c3c', '#3498db', '#2ecc71', '#95a5a6'],
                    edgecolor='black')
    ax2.set_ylabel('Training Time (seconds)', fontsize=12)
    ax2.set_title('Training Time Comparison', fontsize=14, fontweight='bold')

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f}s', ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    images.append(save_figure(fig, f"{article_slug}_model_comparison"))

    return images


def create_explainability_visualizations(article_slug: str) -> List[str]:
    """Create XAI/SHAP visualizations"""
    images = []

    # SHAP Feature Importance
    fig, ax = plt.subplots(figsize=(10, 6))
    features = ['Income', 'Age', 'Credit_Score', 'Debt_Ratio',
                'Employment_Length', 'Num_Accounts', 'Recent_Inquiries']
    shap_values = [0.35, 0.28, 0.22, 0.18, 0.12, 0.08, 0.05]

    colors = ['#e74c3c' if sv > 0.2 else '#3498db' for sv in shap_values]

    ax.barh(features, shap_values, color=colors, edgecolor='black')
    ax.set_xlabel('Mean |SHAP Value|', fontsize=12)
    ax.set_title('SHAP Feature Importance (Loan Default Prediction)', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    images.append(save_figure(fig, f"{article_slug}_shap_importance"))

    return images


def create_generic_visualizations(article_slug: str) -> List[str]:
    """Create generic data science visualizations"""
    images = []

    # Model Performance
    fig, ax = plt.subplots(figsize=VISUALIZATION_CONFIG["figure_size"])
    epochs = range(1, 21)
    train_loss = [0.8 * np.exp(-x/5) + 0.1 for x in epochs]
    val_loss = [0.8 * np.exp(-x/5) + 0.15 + np.random.rand()*0.05 for x in epochs]

    ax.plot(epochs, train_loss, label='Training Loss', marker='o', linewidth=2)
    ax.plot(epochs, val_loss, label='Validation Loss', marker='s', linewidth=2)
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Loss', fontsize=12)
    ax.set_title('Model Training Progress', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    images.append(save_figure(fig, f"{article_slug}_training_progress"))

    return images
