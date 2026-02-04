import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. Page Config for 2026 Standards
st.set_page_config(page_title="Ethiopia FI Dashboard", layout="wide")

# 2. Load Data
@st.cache_data
def load_data():
    # Historical data including channel breakdown
    hist_data = {
        'Year': [2011, 2014, 2017, 2022],
        'Access': [22.0, 22.0, 35.0, 46.1],
        'Digital_P2P': [5.1, 7.2, 12.4, 25.3],
        'ATM_Withdrawal': [10.5, 12.1, 18.3, 20.1]
    }
    df_hist = pd.DataFrame(hist_data)
    df_forecast = pd.read_csv('data/processed/forecast_results.csv')
    return df_hist, df_forecast

df_hist, df_forecast = load_data()

# 3. Navigation Sidebar
st.sidebar.title("📈 FI Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Channel Trends", "Forecasts"])

# --- PAGE 1: OVERVIEW ---
if page == "Overview":
    st.title("Strategic Overview: Ethiopia Financial Inclusion")
    
    # Key Metric Cards
    c1, c2, c3 = st.columns(3)
    c1.metric("Current Access", "46.1%", "Findex 2022")
    c2.metric("Target (2027)", "60.0%", "Consortium Goal")
    # P2P/ATM Crossover Ratio
    ratio = round(df_hist.iloc[-1]['Digital_P2P'] / df_hist.iloc[-1]['ATM_Withdrawal'], 2)
    c2.metric("P2P/ATM Ratio", f"{ratio}x", "Digital Dominance")

    # VISUAL 1: Progress Gauge (Requirement: Target Visual)
    st.subheader("Progress toward 60% Inclusion Target")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number", value = 46.1,
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "darkgreen"},
                 'threshold': {'line': {'color': "red", 'width': 4}, 'value': 60}}))
    st.plotly_chart(fig_gauge, width='stretch')

# --- PAGE 2: CHANNEL TRENDS ---
elif page == "Channel Trends":
    st.title("Historical Channel Trends")
    
    # VISUAL 2: Channel Comparison (Requirement: Channel Comparison)
    st.subheader("Digital P2P vs. ATM Cash Usage (%)")
    fig_trend = px.line(df_hist, x='Year', y=['Digital_P2P', 'ATM_Withdrawal'],
                        markers=True, title="The Digital Crossover (2011-2022)")
    st.plotly_chart(fig_trend, width='stretch')
    
    # VISUAL 3: Interactive Data Table (Requirement: Interactive Exploration)
    st.subheader("Raw Data Explorer")
    st.dataframe(df_hist, width='stretch')

# --- PAGE 3: FORECASTS ---
elif page == "Forecasts":
    st.title("🔮 2027 Scenarios & Projections")
    
    # Scenario Selector
    scenario = st.sidebar.selectbox("Select Model Scenario", df_forecast['Scenario'].unique())
    plot_df = df_forecast[df_forecast['Scenario'] == scenario]

    # VISUAL 4: Forecast with Confidence Intervals (Requirement: Forecast Visual)
    fig_fore = go.Figure()
    # Confidence Area
    fig_fore.add_trace(go.Scatter(x=plot_df['Year'].tolist() + plot_df['Year'].tolist()[::-1],
                                 y=plot_df['Upper_CI'].tolist() + plot_df['Lower_CI'].tolist()[::-1],
                                 fill='toself', fillcolor='rgba(0,100,0,0.2)', line_color='rgba(255,255,255,0)', name='95% CI'))
    # Forecast Line
    fig_fore.add_trace(go.Scatter(x=plot_df['Year'], y=plot_df['Access_Forecast'], line=dict(color='green', width=4), name='Forecast'))
    
    # FIX: Set Y-Axis range to 45-70 to see scenario differences clearly
    fig_fore.update_layout(yaxis_range=[45, 70], title=f"Access Projection: {scenario}")
    st.plotly_chart(fig_fore, width='stretch')

    # Data Download (Requirement: Download Functionality)
    csv = df_forecast.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Forecast Results (CSV)", data=csv, file_name="ethiopia_fi_forecast.csv")

    # Q&A (Requirement: Answer Consortium Questions)
    st.info("**Analysis:** Under the Base scenario, we reach **58.9%** by 2027. Reaching the 60% target requires an additional boost from Fayda ID adoption.")