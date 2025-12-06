# Multi-Horizon Forecasting (LSTM + KPI Analysis + AI Recommendations + Streamlit UI)

This project provides an end-to-end AI forecasting pipeline using:
- PyTorch LSTM multi-horizon forecasting
- Automated KPI evaluation (MAPE, Bias, Stockout, Overstock)
- Inventory analytics (Safety Stock, Reorder Point)
- Advanced AI Recommendation Engine
- Streamlit front-end dashboard

---

## 🚀 Features

### 1. **Deep Learning Time-Series Forecasting**
- Sequence generation for multivariate forecasting
- LSTM + MLP multi-horizon model (30-day prediction)
- Automatic train/validation split
- Saves best model weights based on MSE

### 2. **KPI & Inventory Analytics**
Scripts compute:
- MAPE
- Bias
- Stockout rate
- Overstock rate
- Safety stock
- Reorder point

### 3. **Advanced AI Recommendation Engine**
For every SKU + Store:
- Detect demand spikes
- Flag slow-moving inventory
- Suggest safety stock increases/decreases
- Warn about high variability
- Provide Critical / High / Medium / Low severity

### 4. **Streamlit Dashboard**
A UI for:
- Upload forecasts
- View KPIs
- Plot top 5 SKUs (MAPE / Stockout / Overstock)
- Export results with recommendations

---

## 📂 Project Structure

