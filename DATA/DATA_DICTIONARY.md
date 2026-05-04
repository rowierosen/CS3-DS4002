# Data Dictionary — Movie Poster Visual Features Dataset

## File: `sample_poster_features.csv`

This dataset contains pre-extracted visual features from the official movie posters of ~1,000 theatrical films, along with their worldwide box office revenue. Each row represents one film.

---

## Variables

| Variable | Type | Description |
|---|---|---|
| `tconst` | string | Unique IMDB identifier for the film (e.g., `tt1234567`) |
| `primaryTitle` | string | The primary title of the film |
| `startYear` | integer | The year the film was released |
| `worldwide` | float | Worldwide theatrical gross revenue in USD |
| `domestic` | float | Domestic (US/Canada) theatrical gross revenue in USD |
| `log_worldwide` | float | Natural log of worldwide revenue: `ln(worldwide)`. Used as the target variable for regression to normalize the heavily right-skewed revenue distribution. |
| `log_domestic` | float | Natural log of domestic revenue: `ln(domestic)` |
| `dom_r` | integer (0–255) | Red channel value of the poster's most dominant color (extracted via K-Means clustering, k=5) |
| `dom_g` | integer (0–255) | Green channel value of the poster's most dominant color |
| `dom_b` | integer (0–255) | Blue channel value of the poster's most dominant color |
| `avg_brightness` | float (0–255) | Mean pixel brightness of the poster image, computed by converting to HSV color space and averaging the V (value) channel |
| `avg_saturation` | float (0–255) | Mean pixel saturation of the poster image, computed by converting to HSV color space and averaging the S channel. Higher values indicate more vivid colors. |
| `orange_teal_score` | float (0–1) | Proportion of pixels in the poster that fall within the "orange" or "teal" hue ranges in HSV space. Captures the prevalence of the popular Hollywood color grading trend. |
| `face_count` | integer | Number of human faces detected in the poster using the RetinaFace deep learning model |
| `face_density` | float | Face density metric: `(face_count / total_pixels) × 10,000`. Normalizes face count by poster resolution to allow cross-poster comparison. |
| `release_month` | integer (1–12) | The month the film was theatrically released |
| `release_window` | string | Categorical release window derived from `release_month`: `"Summer"` (May–Jul), `"Holiday"` (Nov–Dec), `"Spring"` (Mar–Apr), or `"Other"` |

---

## Notes

- **Revenue values** are nominal (not inflation-adjusted). Films with missing or zero revenue have been excluded.
- **Log-transformed revenue** (`log_worldwide`) is the recommended target variable for regression, as raw revenue is heavily right-skewed.
- **Dominant color** is the centroid of the largest K-Means cluster (k=5) fitted to all pixels in the poster. It represents the single most prevalent color.
- **Orange-teal score** uses the following HSV hue ranges: Orange ≈ 10–25°, Teal ≈ 80–100° (on 0–180 OpenCV scale).
- **Face detection** uses the RetinaFace model, a deep-learning-based face detector that is robust to occlusion, varied angles, and small faces. Face density normalizes for poster resolution.
