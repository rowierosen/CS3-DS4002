# CS3 Rubric — Movie Poster Visual Features & Box Office Revenue

**DS 4002 Case Study**

---

## General Description

Using a provided dataset of ~1,000 films with pre-extracted visual features from their official movie posters, you will investigate whether quantitative poster characteristics — such as color composition, brightness, saturation, and face density — are statistically significant predictors of worldwide theatrical box office revenue. You will produce a short analytical report (3–5 pages, PDF) with reproducible code.

---

## Why Am I Doing This?

Movie studios invest heavily in poster design as a key marketing tool. This case study asks you to apply the data science pipeline — from exploratory analysis through statistical modeling and predictive evaluation — to a creative, real-world question. You will practice working with image-derived features, interpreting regression output, and communicating a data-driven conclusion to a non-technical audience.

---

## Spec Category & Details

| Category | Details |
|---|---|
| **Data** | Use the provided `sample_poster_features.csv` dataset (~1,000 films) located in the `DATA/` folder. See `DATA_DICTIONARY.md` for variable definitions. If you wish to expand the dataset, follow `DATA_PREPARATION.md`. |
| **Exploratory Data Analysis** | Produce a correlation heatmap of all numeric visual features against log-transformed worldwide revenue (`log_worldwide`). Include at least one additional bivariate visualization (e.g., box plot by release window). Report exact correlation coefficients. |
| **Statistical Modeling** | Fit a Multiple Linear Regression (OLS) model predicting `log_worldwide` from the visual features and release window controls. Report R-squared, p-values, and interpret which predictors (if any) are statistically significant at α = 0.05. |
| **Predictive Evaluation** | Train a machine learning model (e.g., Random Forest) using an 80/20 train/test split. Report MAE, RMSE, and R-squared on the test set. Compare its performance to the linear model. Include a feature importance visualization. |
| **Report** | 3–5 page PDF. Must include: (1) an introduction framing the research question, (2) a methods section describing feature extraction and modeling, (3) results with at least 3 figures/tables, and (4) a conclusion addressing whether visual features predict box office success and what factors might be missing. |
| **Code** | All analysis code must be in a Jupyter Notebook (`.ipynb`) or Python script. It should be runnable by the grader with the provided data. Use the `SCRIPTS/` folder. A `starter_analysis.ipynb` is provided to get you started. |
| **Repository** | Submit a link to a GitHub repository containing your report (PDF), code, and any additional materials. |

---

## How Will I Know I Have Succeeded?

| Component | Meets Expectations | Does Not Meet Expectations |
|---|---|---|
| **EDA** | Correlation heatmap with all numeric features. At least one other visualization. Exact coefficients reported. | Missing heatmap, no additional visualization, or coefficients not reported. |
| **OLS Regression** | Model is fitted with visual + release window features. R-squared, p-values, and coefficients are reported and interpreted correctly. | Model is missing, uses wrong target variable, or output is not interpreted. |
| **Predictive Model** | ML model trained on 80/20 split. MAE, RMSE, and R² reported on test set. Feature importance plot included. Performance compared to OLS. | No ML model, or metrics not reported, or no comparison to OLS. |
| **Report Quality** | Clear writing. Research question stated. Methods described. Results supported by figures. Conclusion addresses the core question. | Unclear writing, missing sections, figures without interpretation, or no conclusion. |
| **Reproducibility** | Code runs without errors on the provided dataset. Notebook or script is well-organized with comments. | Code crashes, relies on unavailable files, or is disorganized. |

---

## References

See the `SUPPLEMENTAL_MATERIALS/` folder for:
- A blog-style explainer article motivating the project and introducing key concepts
- Links to technical documentation for the tools and APIs used

## Acknowledgements

This case study is based on a DS 4002 project by Rowan Rosenblum (Spring 2025). The analysis examined 21,000+ films to test whether poster visual features predict global box office revenue. The provided sample dataset is a curated subset for instructional use.
