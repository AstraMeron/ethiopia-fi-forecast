# Ethiopia Financial Inclusion Forecasting (2026-2027)
**Author:** Meron Tilahun (Mary) | 5th Year CSE, ASTU
**Training:** 10 Academy KAIM (Batch 2026)

## 📌 Project Overview
This project focuses on modeling and forecasting financial inclusion (FI) indicators in Ethiopia. It utilizes a **Unified Schema** to combine historical survey data with real-time market milestones (Telebirr, Safaricom, Fayda ID).

---

## 🛠 Task 1: Data Enrichment & Schema Mapping
**Objective:** Enhance the raw dataset with recent market observations to improve forecast accuracy.
- **Key Additions:**
    - Updated **Telebirr** usage data to EOY 2025 (58.6M users).
    - Integrated **Fayda Digital ID** mandatory policy as a key institutional event.
- **Unified Schema:** All data was mapped to a standardized format involving `pillars`, `indicators`, and `impact_links`.

## 📊 Task 2: Exploratory Data Analysis (EDA)
**Objective:** Analyze patterns and identify drivers of financial inclusion.
- **Key Insights:**
    1. **The +3pp Stagnation:** Account ownership grew only 3% (2021-2024) despite massive mobile money expansion, likely due to KYC barriers and dormancy.
    2. **Infrastructure Lead:** 4G coverage growth consistently leads usage growth by 12–18 months.
    3. **The ID Catalyst:** Analysis suggests the Digital ID rollout is the most significant non-market driver for 2026 growth.

## 🧪 Robustness & Reproducibility
- **Error Handling:** Notebooks include `try-except` blocks for data loading and path validation.
- **Data Validation:** Automated assertions check for duplicate record IDs and critical null values.
- **Processed Output:** The final enriched dataset is available in `data/processed/ethiopia_fi_final_enriched.csv`.

## ⚠️ Limitations
- **Data Sparsity:** Relying on 3-year Findex cycles creates temporal gaps.
- **Proxy Use:** Operator data (registered accounts) may overrepresent unique users due to multi-SIM cards.