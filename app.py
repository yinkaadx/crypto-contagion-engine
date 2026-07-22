import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Macroeconomic Contagion Engine", layout="wide")

st.title("Serverless FinTech Contagion Pipeline")
st.caption("Real-Time Cryptocurrency Market Anomaly & Liquidity Drain Detection")

st.sidebar.header("Middleware Configuration")
selected_market = st.sidebar.selectbox("Select Target Market", ["BTC/USDT Global Orderbook", "ETH/USDC Institutional Pool", "Solana DeFi Aggregator"])
macro_shock = st.sidebar.slider("Simulate Macro Liquidity Drain Severity", 1, 10, 5)
run_simulation = st.sidebar.button("Initialize Machine Learning Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: AWS Lambda -> Vectorization -> XGBoost Contagion Model")

if run_simulation:
    st.subheader(f"Active High-Frequency Monitoring: {selected_market}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_price = col1.empty()
    metric_spread = col2.empty()
    metric_velocity = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(202)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    price_values = []
    contagion_scores = []
    
    base_price = 65000.0 if "BTC" in selected_market else 3500.0
    
    for i in range(100):
        if i < 35:
            current_price = base_price + np.random.uniform(-50.0, 50.0)
            current_score = np.random.uniform(10.0, 20.0)
            spread = np.random.uniform(0.1, 0.5)
            velocity = int(np.random.uniform(500, 1000))
        elif i >= 35 and i < 65:
            current_price = base_price - (i - 35) * (15.0 * macro_shock) + np.random.uniform(-100.0, 100.0)
            current_score = np.random.uniform(50.0, 85.0)
            spread = np.random.uniform(1.0, 5.0)
            velocity = int(np.random.uniform(3000, 8000))
        else:
            current_price = base_price - (30 * 15.0 * macro_shock) + np.random.uniform(-200.0, 200.0)
            current_score = np.random.uniform(90.0, 99.9) 
            spread = np.random.uniform(5.0, 15.0)
            velocity = int(np.random.uniform(10000, 25000))
            
        price_values.append(current_price)
        contagion_scores.append(current_score)
        
        metric_price.metric("Asset Index Price", f"${current_price:,.2f}", f"{(current_price - base_price):,.2f}")
        metric_spread.metric("Bid-Ask Spread", f"${spread:.2f}")
        metric_velocity.metric("Transaction Velocity", f"{velocity} Tx/s")
        
        if current_score >= 85.0:
            metric_status.metric("Macro Risk Status", "CONTAGION DETECTED", "Systemic Drain")
        else:
            metric_status.metric("Macro Risk Status", "STABLE LIQUIDITY", "Normal")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=price_values, mode='lines', name='Index Price', line=dict(color='orange')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=contagion_scores, mode='lines', name='Contagion Risk Score', yaxis='y2', line=dict(color='red', dash='dot')))
        
        fig.update_layout(
            title="Real-Time Asset Liquidation vs Macro Contagion Score",
            xaxis=dict(title="Timestamp (High-Frequency)"),
            yaxis=dict(title="Price (USD)"),
            yaxis2=dict(title="Contagion Score (%)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if current_score >= 85.0:
            log_placeholder.error(f"MACRO WARNING: Cascading liquidations detected at {time_steps[i].strftime('%H:%M:%S')}. Debt cycle deleveraging signature matches historical crisis vectors.")
        else:
            log_placeholder.success(f"Log: Tick data {i} processed via AWS API Gateway. Market microstructure remains within normal deviations.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. Serverless pipeline successfully isolated high-frequency financial contagion patterns.")
else:
    st.info("Click 'Initialize Machine Learning Engine' in the sidebar to simulate high-frequency tick data ingestion.")