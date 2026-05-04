# 🎬 Can You Judge a Movie's Success by Its Poster?
### DS 4002 Case Study by Rowan Rosenblum

![Movie Poster Analysis](SUPPLEMENTAL_MATERIALS/poster_collage.png)

## Overview

This case study challenges you to investigate whether the visual characteristics of a movie poster — its color palette, brightness, saturation, and number of faces — can predict worldwide box office revenue. Using a dataset of ~1,000 films with pre-extracted poster features, you will perform exploratory data analysis, build regression models, and evaluate predictive performance.

---

## Repository Structure

```
CS3-DS4002/
├── README.md
├── LICENSE
├── CS3-Movie-Poster-Hook.md          # Hook document (1-page mission brief)
├── CS3Rubric.md                       # Rubric with deliverable specs
├── DATA/
│   ├── sample_poster_features.csv     # Pre-extracted features for ~1,000 films
│   ├── DATA_DICTIONARY.md             # Variable definitions
│   └── DATA_PREPARATION.md            # How to obtain/expand the dataset
├── SCRIPTS/
│   ├── helper_functions.py            # Utility functions for feature extraction
│   └── starter_analysis.ipynb         # Starter notebook with TODOs
└── SUPPLEMENTAL_MATERIALS/
    ├── blog_explainer.md              # Motivational explainer article
    └── poster_collage.png             # Header image
```

---

## Getting Started

1. **Read the Hook** — `CS3-Movie-Poster-Hook.md` sets the scene and your mission.
2. **Read the Rubric** — `CS3Rubric.md` details exactly what to produce and how you'll be evaluated.
3. **Explore the Data** — Start with `DATA/sample_poster_features.csv` and review the `DATA_DICTIONARY.md`.
4. **Open the Starter Notebook** — `SCRIPTS/starter_analysis.ipynb` has a structured template with TODOs.
5. **Use the Helper Functions** — `SCRIPTS/helper_functions.py` provides utilities for feature extraction if you want to expand the dataset.

---

## Data

The `DATA/` folder contains:
- **sample_poster_features.csv** — Pre-extracted visual features for ~1,000 films including dominant colors (RGB), average brightness, average saturation, orange-teal score, face density, and worldwide box office revenue.
- **DATA_DICTIONARY.md** — Complete variable definitions for every column.
- **DATA_PREPARATION.md** — Step-by-step instructions for downloading poster images from TMDB and extracting features yourself if you want to scale up.

---

## Reference Materials

**Brochado, F., et al.** (2021). Can a Movie Trailer Tell Us Enough? The Effectiveness of Online Movie Trailer Metrics. *Journal of Advertising Research*. [https://doi.org/10.2501/JAR-2021-002](https://doi.org/10.2501/JAR-2021-002)

**TMDB.** (2024). The Movie Database API Documentation. [https://developer.themoviedb.org/docs](https://developer.themoviedb.org/docs)

**Scikit-learn.** (2024). Random Forest Regressor Documentation. [https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

Additional reference materials including a blog-style explainer are available in the `SUPPLEMENTAL_MATERIALS/` folder.
