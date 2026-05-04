# Data Preparation Guide

## For the Provided Sample Dataset

The `sample_poster_features.csv` file in this folder is **ready to use** — no additional preparation is needed. It contains pre-extracted visual features for ~1,000 films. Simply load it with:

```python
import pandas as pd
df = pd.read_csv("DATA/sample_poster_features.csv")
```

---

## If You Want to Expand the Dataset

The original analysis used 21,000+ films. If you want to extract features from additional movie posters, follow these steps:

### Step 1: Obtain a TMDB API Key

1. Create a free account at [https://www.themoviedb.org/](https://www.themoviedb.org/)
2. Navigate to **Settings → API** and request an API key (select "Developer" usage)
3. Save your API key — you'll need it for poster downloads

### Step 2: Get a Film List with IMDB IDs

You need a list of films with their IMDB `tconst` identifiers. Sources include:
- **IMDB Non-Commercial Datasets**: [https://datasets.imdbws.com/](https://datasets.imdbws.com/) — download `title.basics.tsv.gz` and filter to `titleType == "movie"`
- **The provided sample dataset**: Use the `tconst` column as a starting reference

### Step 3: Download Poster Images

Use the TMDB API to download official poster images. The helper function in `SCRIPTS/helper_functions.py` provides a `download_poster()` function:

```python
from helper_functions import download_poster

# Download a single poster
download_poster("tt1234567", api_key="YOUR_API_KEY", save_dir="posters/")
```

The TMDB API has a rate limit of ~40 requests per 10 seconds. The helper function includes built-in rate limiting.

### Step 4: Extract Visual Features

Use the feature extraction functions in `SCRIPTS/helper_functions.py`:

```python
from helper_functions import extract_all_features

# Extract features from a single poster image
features = extract_all_features("posters/tt1234567.jpg")
# Returns: dict with dom_r, dom_g, dom_b, avg_brightness, avg_saturation,
#          orange_teal_score, face_count, face_density
```

### Step 5: Get Box Office Revenue

Worldwide revenue can be obtained from:
- **TMDB API**: `GET /movie/{movie_id}` returns `revenue` field
- **Box Office Mojo**: Manual lookup at [https://www.boxofficemojo.com/](https://www.boxofficemojo.com/)

### Required Python Packages

```
pandas
numpy
matplotlib
seaborn
scikit-learn
opencv-python (cv2)
Pillow (PIL)
requests
statsmodels
retinaface
tensorflow  # required by retinaface
```

Install with:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn opencv-python Pillow requests statsmodels retinaface tensorflow
```

> **Note:** For RetinaFace face detection, you may need to set the environment variable `TF_USE_LEGACY_KERAS=1` if using TensorFlow 2.16+.
