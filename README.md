# ethiopia-fi-forecast
# Ethiopia Financial Inclusion Forecasting (2026-2027)
**Author:** Meron Tilahun (Mary) | 10 Academy KAIM Training

## Project Overview
This project leverages the Unified Schema to forecast financial inclusion indicators in Ethiopia. It bridges historical data (Findex, NBE) with recent 2025/2026 market developments like Telebirr and Safaricom's entry.

## Key Insights (Task 2)
1. **The Registration Paradox:** Mobile money accounts grew 1,200%, but formal ownership only grew +3pp (2021-2024).
2. **Infrastructure Lag:** 4G expansion leads usage growth by approximately 12 months.
3. **KYC Barriers:** Stagnation is primarily driven by lack of formal ID; Fayda ID is the predicted catalyst for 2026 growth.

## Dataset & Enrichment
- **Source:** `ethiopia_fi_unified_data.csv`
- **Enrichments:** Added 2025 Telebirr user growth (58.6M) and Fayda Digital ID policy milestones.

## How to Run
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`
3. Run `notebooks/02_exploratory_data_analysis.ipynb`.