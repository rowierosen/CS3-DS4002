# Can a Movie Poster Predict Box Office Success? A Data Science Approach

*A motivational explainer for the DS 4002 Movie Poster Case Study*

---

## The Question That Started It All

Think about the last movie poster you noticed — maybe it was plastered on the side of a bus, pinned to a theater wall, or floating through your social media feed. It probably caught your eye for a reason. Maybe it was the vivid colors, the dramatic lighting, or the cluster of famous faces staring back at you.

Now here's a wilder question: **Could the look of that poster actually predict how much money the movie will make?**

This isn't as far-fetched as it sounds. Studios spend millions on marketing, and the poster is one of the first visual touchpoints between a film and its audience. Entire industries exist around color psychology, visual marketing, and first impressions. There's even a well-documented phenomenon in Hollywood called the **"orange and teal" look** — a specific color grading style that has dominated blockbuster posters for years. If you've ever noticed that action movie posters tend to feature warm-toned actors against cool blue/teal backgrounds, you've spotted it.

But do these visual choices actually *matter* at the box office?

---

## What We're Doing (And Why It's Cool)

In this case study, you'll become a **data-driven visual analyst**. You'll work with a real dataset of ~1,000 films with pre-extracted visual features from their official posters, including:

- **Dominant color palette** — What's the primary color of the poster? Extracted using K-Means clustering.
- **Brightness & Saturation** — Is the poster dark and moody or bright and vivid?
- **Orange-Teal Score** — How much of the poster uses that classic Hollywood color grading?
- **Face Density** — How many faces are on the poster, normalized by poster size?

Your job is to use these features to build statistical models that predict **worldwide theatrical revenue**. You'll start with exploratory analysis, move to regression modeling, and finish with a machine learning evaluation.

---

## The Key Techniques You'll Use

### 1. K-Means Clustering for Color Extraction
K-Means is an unsupervised machine learning algorithm that groups data points into clusters. When applied to the pixels of an image, it finds the *k* most representative colors. For this project, we use k=5 clusters and take the largest cluster as the "dominant color." This gives us a quantitative way to describe what a poster *looks like*.

### 2. Multiple Linear Regression (OLS)
OLS regression lets you model the relationship between multiple independent variables (your visual features) and a continuous outcome (box office revenue). You'll learn to read a regression summary table, interpret p-values, and understand R-squared — the proportion of variance your model explains.

### 3. Random Forest Regression
A Random Forest is an ensemble machine learning method that builds many decision trees and averages their predictions. It can capture non-linear relationships that OLS might miss. You'll compare its performance against the linear model to see if visual features have hidden predictive power.

### 4. Log Transformation
Movie revenue is heavily right-skewed — a few blockbusters earn billions while most films earn modest amounts. Taking the natural log of revenue produces a more normal distribution, making it suitable for regression analysis. This is a fundamental data transformation technique in data science.

---

## Why This Matters

Even if visual features turn out to be weak predictors (spoiler: the original analysis found that they explain less than 10% of revenue variance), the process of *testing that hypothesis* is exactly how real data science works. You formulate a question, gather data, build models, and draw conclusions — even when the conclusion is "the thing I tested doesn't work."

In fact, **a well-reasoned negative result is just as valuable as a positive one.** If poster visuals don't predict revenue, that tells us something important: commercial success is driven by factors we can't see on a poster — things like marketing budgets, franchise recognition, star power, and release strategy.

---

## Getting Started

1. Open the **starter notebook** (`SCRIPTS/starter_analysis.ipynb`) — it has structured sections with TODOs
2. Load the dataset (`DATA/sample_poster_features.csv`) — features are already extracted for you
3. Follow the rubric for specific deliverable requirements
4. Don't forget to check the **data dictionary** (`DATA/DATA_DICTIONARY.md`) to understand every variable

---

## Further Reading

- **Color in Film: A Visual History** — An exploration of how color palettes in cinema have evolved over decades and what drives aesthetic trends. [https://filmschoolrejects.com/color-in-film/](https://filmschoolrejects.com/color-in-film/)
- **TMDB API Docs** — If you want to download posters yourself. [https://developer.themoviedb.org/docs](https://developer.themoviedb.org/docs)
- **scikit-learn User Guide: Random Forests** — Technical reference for the ML model you'll use. [https://scikit-learn.org/stable/modules/ensemble.html#random-forests](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)
- **statsmodels OLS Documentation** — Reference for interpreting regression output. [https://www.statsmodels.org/stable/regression.html](https://www.statsmodels.org/stable/regression.html)

---

*This case study was developed by Rowan Rosenblum as part of DS 4002 (Spring 2025) at the University of Virginia.*
