# Comprehensive Data Analysis of Superstore Sales
### Integrated Data Cleaning, Visualization, Statistical Analysis, and Predictive Modeling Using R

[![R Version](https://img.shields.io/badge/R-v4.6.1-blue.svg)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed%20%26%20Verified-brightgreen.svg)]()
[![Model Accuracy](https://img.shields.io/badge/Random%20Forest%20R²-78.45%25-success.svg)]()
[![Execution Time](https://img.shields.io/badge/Pipeline%20Runtime-44.35s-blue.svg)]()

---

## 1. Executive Summary & Project Purpose

This repository delivers the **Final Capstone Project** for the Yuva Intern Data Analytics Internship. The investigation synthesizes the analytical methodologies developed across Weeks 1, 2, and 3 into one comprehensive, publication-grade, evidence-based research investigation using the **Tableau / Kaggle Sample Superstore Sales Dataset**.

Rather than treating weekly assignments as fragmented exercises, this capstone unites the full data science lifecycle:
$$\text{Data Ingestion} \longrightarrow \text{Quality Auditing} \longrightarrow \text{Feature Engineering} \longrightarrow \text{Exploratory Visualization} \longrightarrow \text{Inferential Hypothesis Testing} \longrightarrow \text{Cross-Validated Machine Learning} \longrightarrow \text{Strategic Corporate Intelligence}$$

The enterprise investigation examines **9,994 line-item transactions** spanning January 4, 2011, through December 31, 2014, across 49 US states, representing **$2,297,200.86 in gross revenue** and **$286,397.02 in operating profit** (12.47% overall margin).

---

## 2. Enterprise Performance Scorecard (2011 - 2014)

| Key Metric | Value | Business Context & Performance Implications |
| :--- | :--- | :--- |
| **Total Commercial Revenue** | **$2,297,200.86** | 9,994 line-item orders across 5,009 unique customer transactions |
| **Cumulative Operating Profit** | **$286,397.02** | Net profitability across 793 enterprise & consumer accounts |
| **Enterprise Profit Margin** | **12.47%** | Top-line return on commercial sales |
| **Loss-Making Transactions** | **1,871 (18.72%)** | Line items resulting in negative net margins |
| **Top Performing Division** | **Technology ($145,454.95)** | 17.39% margin led by Copiers ($55.6k) and Phones ($44.5k) |
| **Severe Capital Drag Sector** | **Tables (-$17,725.48)** | Chronic line-item losses across 319 furniture transactions |
| **Top Regional Territory** | **West ($108,418.45)** | 14.95% profit margin with the lowest loss rate (9.93%) |
| **Vulnerable Regional Territory** | **Central (31.90% Loss Rate)** | Generates $501.2k sales but only $39.7k profit (7.92% margin) |
| **Promotional Cliff Threshold** | **Discount > 20%** | Profit collapses to -$62.58 median profit and -41.8% margin |
| **Champion Model Performance** | **Random Forest (R² = 78.45%)** | Test RMSE = $119.16, Test MAE = $26.66 (53.59% error cut) |

---

## 3. Core Analytical Questions Addressed

1. **Temporal Dynamics**: How do sales and profit evolve longitudinally, and what seasonal surges characterize the retail calendar?
2. **Category Revenue**: Which merchandise categories and sub-categories generate the greatest top-line commercial revenue?
3. **Category Profitability**: Which sectors yield the highest net margins, and which sub-categories destroy enterprise capital?
4. **Regional Matrix**: How do geographic territories diverge in sales volume, operating margin, and operational loss incidence?
5. **Customer Segmentation**: How do purchasing behavior, basket size, and fulfillment class differ across Consumer, Corporate, and Home Office clients?
6. **Promotional Discount Elasticity**: How does promotional discounting relate empirically to line-item profit and gross margin sustainability?
7. **Extreme Line-Item Losses**: Which specific products contribute disproportionately to enterprise capital destruction?
8. **Inferential Group Differences**: Are observed differences in profit across discount tiers and merchandise categories statistically significant?
9. **Regional Loss Dependence**: Is the probability of incurring a transaction loss statistically dependent on geographic sales territory?
10. **Predictive Modeling**: Can future transaction profitability be predicted out-of-sample using accessible operational predictors, and what model architecture best resolves non-linear retail dynamics?

---

## 4. Formal Inferential Hypothesis Testing Results

All inferential hypothesis tests were executed at $\alpha = 0.05$ with complete assumption verification (Levene's tests, normality diagnostics, and effect sizes):

| Test ID | Statistical Method | Null Hypothesis ($H_0$) | Test Statistic & Parameters | p-Value | Effect Size | Decision | Empirical Business Finding |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **HT-01** | Welch's Two-Sample t-Test | $\mu_{\text{No Disc}} = \mu_{\text{Discounted}}$ | $t(9162.2) = 15.74$ | $< 0.0001$ | Cohen's $d = 0.318$ | **Reject $H_0$** | Non-discounted orders average $66.90 profit vs -$6.66 for discounted; markdowns destroy gross margin. |
| **HT-02** | One-Way ANOVA & Tukey HSD | $\mu_{\text{Furn}} = \mu_{\text{Office}} = \mu_{\text{Tech}}$ | $F(2, 9991) = 54.31$ | $< 0.0001$ | $\eta^2 = 0.0108$ | **Reject $H_0$** | Technology ($78.75) significantly outperforms Office ($20.33) and Furniture ($8.40); Furniture bleeds capital. |
| **HT-03** | Pearson Chi-Square ($\chi^2$) | Region and Loss Status are Independent | $\chi^2(3) = 436.70$ | $< 0.0001$ | Cramer's $V = 0.2090$ | **Reject $H_0$** | Loss incidence is geographically clustered: Central suffers a 31.90% loss rate vs 9.93% in the West. |
| **HT-04** | Spearman Rank Correlation | Rank Correlation $\rho = 0$ | $S = 2.57 \times 10^{11}$ | $< 0.0001$ | Spearman $\rho = -0.5434$ | **Reject $H_0$** | Powerful monotonic inverse relationship proves volume gained from heavy discounting fails to offset margin loss. |

---

## 5. Predictive Machine Learning Benchmark

Models were trained on an **80% Training Partition** ($n = 7,995$) and evaluated across **5-Fold Cross-Validation** and an untouched **20% Holdout Test Partition** ($n = 1,999$) under a zero-leakage protocol:

| Model Architecture | CV RMSE | CV MAE | CV $R^2$ | Test RMSE | Test MAE | Test $R^2$ | Error Reduction | Model Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Naive Baseline (Mean)** | $226.15 | $61.14 | 0.0000 | $256.79 | $69.21 | 0.0000 | Baseline | Benchmark |
| **2. Multiple Linear (OLS)** | $196.50 | $58.28 | 0.2635 | $195.71 | $64.07 | 0.4186 | 23.78% | Underfitting |
| **3. Elastic Net ($\alpha=0.5$)** | $204.79 | $54.36 | 0.0410 | $197.74 | $61.57 | 0.4065 | 23.00% | Constrained |
| **4. Random Forest Regressor** | **$138.09** | **$23.74** | **0.6340** | **$119.16** | **$26.66** | **0.7845** | **53.59%** | **Champion (Selected)** |

### Top Permutation Features (%IncMSE)
1. **Sales**: 25.66% increase in MSE if permuted
2. **Discount**: 25.61% increase in MSE if permuted
3. **Sub_Category**: 6.83% increase in MSE if permuted
4. **Category**: 5.19% increase in MSE if permuted

---

## 6. Strategic Business Recommendations

1. **Implement Automated 20% Hard Discount Cap**: Establish software gates in POS and ERP systems requiring executive VP override for markdowns exceeding 20%, recovering $45,000 - $60,000 annually.
2. **Rationalize Furniture Catalog (Tables & Bookcases)**: Renegotiate supplier pricing or drop-ship unprofitable Table SKUs to eliminate $21,000+ in chronic capital drag.
3. **Centralize Central Region Discount Authority**: Standardize discount rules in Texas and Illinois to align with West regional protocols, elevating operating margins toward the 12.5% corporate benchmark.
4. **Deploy Real-Time Deal Margin Scoring API**: Integrate the trained Random Forest model artifact (`models/random_forest_model.rds`) into sales workflows for instant pre-quote margin scoring.
5. **Pre-Q4 Logistical Buffer Stocking**: Pre-stock inventory in high-margin Technology hardware (Copiers, Phones) 60 days ahead of the annual October-December commercial surge.

---

## 7. Project Directory Structure

```text
Week4_Superstore_Final/
├── R/
│   ├── 01_data_import.R                  # Ingestion, schema audit & cell completeness profiling
│   ├── 02_data_cleaning.R                # Type harmonization, postal padding, feature engineering
│   ├── 03_exploratory_analysis.R         # Moments, skewness, kurtosis, category & regional profiling
│   ├── 04_visualizations.R               # 7 publication ggplot2 charts (distributions, trends, cliffs)
│   ├── 05_statistical_analysis.R         # Welch's t-test, ANOVA, Chi-Square, Spearman tests & panels
│   ├── 06_predictive_modeling.R          # 80/20 split, 5-fold CV, OLS, Elastic Net, Random Forest
│   ├── 07_model_diagnostics.R            # 4-panel regression plots, holdout parity, error audit
│   └── 08_final_analysis.R               # Executive dashboard graphic, code cards & manifest
├── data/
│   ├── raw/
│   │   └── superstore_raw.csv            # Original raw benchmark dataset (9,994 rows x 21 cols)
│   └── processed/
│       ├── superstore_clean.csv          # Cleaned, standardized transactional dataset
│       ├── superstore_clean.rds          # Serialized R binary data frame
│       ├── train_set.csv                 # 80% Training partition (n = 7,995)
│       └── test_set.csv                  # 20% Holdout test partition (n = 1,999)
├── figures/
│   ├── exploratory/                      # 7 publication-grade 300 DPI exploratory figures
│   ├── statistical/                      # Composite 4-panel hypothesis testing evidence figure
│   ├── modeling/                         # Cross-validation, feature importance, parity scatter, diagnostics
│   └── executive_summary/                # 1-page master executive KPI dashboard graphic
├── models/
│   ├── baseline_model.rds                # Serialized naive mean benchmark object
│   ├── ols_model.rds                     # Serialized multiple linear regression model
│   ├── elastic_net_model.rds             # Serialized regularized glmnet model
│   └── random_forest_model.rds           # Serialized champion Random Forest ensemble model
├── outputs/
│   ├── tables/                           # 10 CSV tables (schema, cleaning, moments, categories, regions)
│   ├── statistics/                       # 5 CSV tables (hypotheses, contingency, Tukey HSD, correlations)
│   ├── model_results/                    # 5 CSV tables (master comparison, feature importance, error audits)
│   └── execution_manifest.csv            # End-to-end stage verification manifest
├── report/
│   └── Week4_Superstore_Comprehensive_Data_Analysis_Final_Report.docx # Complete 55-page Word Report
├── screenshots/
│   ├── outputs/                          # High-resolution terminal execution capture cards
│   └── diagnostics/                      # Residual diagnostic console cards
├── scripts/
│   └── run_all.R                         # Master orchestrator executing entire pipeline in 44.35s
├── generate_week4_report.py              # Automated Word document compilation engine
├── submission_description.txt            # Formatted 360-word portal submission description
└── Week4_Superstore_Final.Rproj          # RStudio project configuration
```

---

## 8. How to Reproduce

Clone the repository and execute the master pipeline:

```bash
git clone https://github.com/248r1a6767-byte/yuvainternweek4.git
cd yuvainternweek4
```

Execute the full automated R analytical pipeline:

```bash
Rscript scripts/run_all.R
```

Compile the final Microsoft Word report (.docx):

```bash
python generate_week4_report.py
```

*Execution runtime: ~45 seconds on standard x64 hardware with 0 fatal errors.*
