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

## ⚖️ Task 3: Event Impact Quantification
**Objective:** Translate qualitative events (Policy shifts, Market entry) into quantitative "growth boosts."
- **Key Deliverable:** `event_indicator_matrix.csv`
- **Logic:** - Analyzed the correlation between major milestones (e.g., Safaricom Launch) and specific FI indicators.
    - Assigned impact scores (0.1 to 1.0) based on historical sensitivity.
    - Calculated a **Mean Event Boost** (0.33) used to adjust the baseline growth rates in the forecast.

## 🔮 Task 4: Scenario-Based Forecasting (2025-2027)
**Objective:** Predict the trajectory of Ethiopia’s financial inclusion under different policy environments.
- **Scenarios Modeled:**
    - **Optimistic:** Rapid Fayda ID adoption + full interoperability (Target: ~62%).
    - **Base:** Steady execution of the National Financial Inclusion Strategy II (Target: 58.7%).
    - **Pessimistic:** Infrastructure bottlenecks and slow behavior change (Target: ~52%).
- **Key Metric:** Quantified **Uncertainty** using 95% Confidence Intervals (The "Fan Chart").
- **Goal Alignment:** Measured progress against the National Bank of Ethiopia's **60% Inclusion Target**.

## 🖥️ Task 5: Interactive Dashboard
**Objective:** Provide an interactive interface for stakeholders to explore projections and trends.
- **Technology Stack:** Streamlit, Plotly, Pandas.
- **Interactive Features:**
    - **Overview Page:** Key metrics summary (Access rate, P2P/ATM Ratio).
    - **Trends Page:** Interactive line charts comparing Digital P2P vs. Cash Withdrawal channels.
    - **Forecasts Page:** Scenario selector and dynamic "Fan Chart" visualizations.
    - **Target Tracking:** A real-time gauge showing progress toward the 60% national goal.
- **Data Export:** Built-in functionality to download forecast results as CSV.

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10+ (Developed using Python 3.13.5)
- Virtual Environment (Recommended)

### 2. Installation
Clone the repository and install the required packages:
```bash
git clone https://github.com/AstraMeron/ethiopia-fi-forecast
```
```bash
cd ethiopia-fi-forecast
```
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### Running the Dashboard
```bash
streamlit run dashboard/app.py