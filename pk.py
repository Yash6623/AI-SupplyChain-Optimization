# # ---------------- Streamlit UI for AI Optimization in Supply Chain ----------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.set_page_config(page_title="AI Supply Chain Dashboard", layout="wide")

# # ---------------- Load or Generate Data ----------------
# # Replace this with your actual full_metrics and df_pred CSV if needed
# num_items = 10
# num_stores = 3
# np.random.seed(42)

# full_metrics = pd.DataFrame({
#     'item_id': np.random.choice([f'item_{i}' for i in range(num_items)], size=100),
#     'store_id': np.random.choice([f'store_{i}' for i in range(num_stores)], size=100),
#     'MAPE': np.random.uniform(10, 200, size=100),
#     'Bias': np.random.randint(-50, 50, size=100),
#     'Stockout_rate': np.random.uniform(0, 1, size=100),
#     'Overstock_rate': np.random.uniform(0, 1, size=100),
#     'mean_demand': np.random.randint(10, 100, size=100),
#     'std_residual': np.random.uniform(5, 50, size=100),
#     'safety_stock': np.random.uniform(20, 200, size=100),
#     'reorder_point': np.random.uniform(50, 500, size=100)
# })

# df_pred = pd.DataFrame({
#     'item_id': full_metrics['item_id'],
#     'store_id': full_metrics['store_id'],
#     'actual': np.random.randint(0, 100, size=100),
#     'forecast': np.random.randint(0, 100, size=100)
# })

# # ---------------- AI Recommendation Engine ----------------
# def generate_recommendation(row):
#     rec = []
#     severity = "Low"

#     # Forecast accuracy
#     if row['MAPE'] > 100:
#         rec.append(f"High forecast error (MAPE {row['MAPE']:.2f})")
#         severity = "High"
#     elif row['MAPE'] > 50:
#         rec.append(f"Moderate forecast error (MAPE {row['MAPE']:.2f})")
#         severity = "Medium"

#     # Stockout risk
#     if row['Stockout_rate'] > 0.5:
#         rec.append("High stockout risk")
#         severity = "High"
#     elif row['Stockout_rate'] > 0.2:
#         rec.append("Moderate stockout risk")
#         severity = max(severity, "Medium", key=lambda x: ["Low","Medium","High"].index(x))

#     # Overstock risk
#     if row['Overstock_rate'] > 0.5:
#         rec.append("High overstock risk")
#         severity = max(severity, "Medium", key=lambda x: ["Low","Medium","High"].index(x))

#     if not rec:
#         rec.append("All metrics are normal")

#     return pd.Series({
#         "AI_Recommendation": " | ".join(rec),
#         "Recommendation_Severity": severity
#     })

# # Apply AI recommendation
# ai_rec_df = full_metrics.apply(generate_recommendation, axis=1)
# full_metrics = pd.concat([full_metrics, ai_rec_df], axis=1)

# # ---------------- Sidebar Filters ----------------
# st.sidebar.header("Filters")
# selected_store = st.sidebar.selectbox("Select Store", options=sorted(full_metrics['store_id'].unique()))
# selected_sku = st.sidebar.selectbox("Select SKU", options=sorted(full_metrics['item_id'].unique()))

# filtered_metrics = full_metrics[
#     (full_metrics['store_id'] == selected_store) &
#     (full_metrics['item_id'] == selected_sku)
# ]

# # ---------------- Dashboard Title ----------------
# st.title("AI Optimization in Supply Chain Dashboard")
# st.subheader(f"Metrics for {selected_sku} at {selected_store}")

# # ---------------- KPI Table ----------------
# st.markdown("### KPI Table")
# st.dataframe(filtered_metrics[['item_id','store_id','MAPE','Bias','Stockout_rate','Overstock_rate']])

# # ---------------- Inventory Metrics ----------------
# st.markdown("### Inventory Metrics")
# st.dataframe(filtered_metrics[['mean_demand','std_residual','safety_stock','reorder_point']])

# # ---------------- AI Recommendations ----------------
# st.markdown("### 🤖 AI Recommendations")
# if not filtered_metrics.empty:
#     recommendation_text = filtered_metrics['AI_Recommendation'].values[0]
#     severity_text = filtered_metrics['Recommendation_Severity'].values[0]
#     st.write("Recommendation:", recommendation_text)
#     st.write("Severity:", severity_text)
# else:
#     st.write("No data available for this selection.")

# # ---------------- Top 5 Plots ----------------
# st.markdown("### Top 5 SKUs by MAPE")
# top5_mape = full_metrics.sort_values('MAPE', ascending=False).head(5)
# fig, ax = plt.subplots(figsize=(10,5))
# sns.barplot(x='item_id', y='MAPE', hue='store_id', data=top5_mape, palette='Reds', dodge=True, ax=ax)
# ax.set_title("Top 5 SKUs by Forecast Error (MAPE)")
# st.pyplot(fig)

# st.markdown("### Top 5 SKUs by Stockout Risk")
# top5_stockout = full_metrics.sort_values('Stockout_rate', ascending=False).head(5)
# fig, ax = plt.subplots(figsize=(10,5))
# sns.barplot(x='item_id', y='Stockout_rate', hue='store_id', data=top5_stockout, palette='Blues', dodge=True, ax=ax)
# ax.set_title("Top 5 SKUs by Stockout Risk")
# st.pyplot(fig)

# st.markdown("### Top 5 SKUs by Overstock Risk")
# top5_overstock = full_metrics.sort_values('Overstock_rate', ascending=False).head(5)
# fig, ax = plt.subplots(figsize=(10,5))
# sns.barplot(x='item_id', y='Overstock_rate', hue='store_id', data=top5_overstock, palette='Greens', dodge=True, ax=ax)
# ax.set_title("Top 5 SKUs by Overstock Risk")
# st.pyplot(fig)

# # ---------------- Forecast Error Histogram ----------------
# st.markdown("### Forecast Error Histogram")
# df_pred['error'] = df_pred['forecast'] - df_pred['actual']
# fig, ax = plt.subplots(figsize=(10,5))
# sns.histplot(df_pred['error'], bins=50, kde=True, color='skyblue', ax=ax)
# ax.set_title("Forecast Error Distribution")
# ax.set_xlabel("Forecast Error (Forecast - Actual)")
# ax.set_ylabel("Count")
# st.pyplot(fig)

# # ---------------- Export Option ----------------
# st.markdown("### Export Data")
# csv = full_metrics.to_csv(index=False)
# st.download_button("Download Metrics as CSV", data=csv, file_name="full_metrics.csv", mime="text/csv")
# ---------------- Streamlit UI for AI Optimization in Supply Chain ----------------


# 1.
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.set_page_config(page_title="AI Supply Chain Dashboard", layout="wide")

# # ---------------- Load or Generate Data ----------------
# # Replace with your actual data if you have full_metrics.csv
# num_items = 10
# num_stores = 3
# np.random.seed(42)

# full_metrics = pd.DataFrame({
#     'item_id': np.random.choice([f'item_{i}' for i in range(num_items)], size=100),
#     'store_id': np.random.choice([f'store_{i}' for i in range(num_stores)], size=100),
#     'MAPE': np.random.uniform(10, 200, size=100),
#     'Bias': np.random.randint(-50, 50, size=100),
#     'Stockout_rate': np.random.uniform(0, 1, size=100),
#     'Overstock_rate': np.random.uniform(0, 1, size=100),
#     'mean_demand': np.random.randint(10, 100, size=100),
#     'std_residual': np.random.uniform(5, 50, size=100),
#     'safety_stock': np.random.uniform(20, 200, size=100),
#     'reorder_point': np.random.uniform(50, 500, size=100)
# })

# df_pred = pd.DataFrame({
#     'item_id': full_metrics['item_id'],
#     'store_id': full_metrics['store_id'],
#     'actual': np.random.randint(0, 100, size=100),
#     'forecast': np.random.randint(0, 100, size=100)
# })

# # ---------------- AI Recommendation Engine ----------------
# def generate_recommendation(row):
#     rec = []
#     severity = "Low"

#     # Forecast accuracy
#     if row['MAPE'] > 100:
#         rec.append(f"High forecast error (MAPE {row['MAPE']:.2f})")
#         severity = "High"
#     elif row['MAPE'] > 50:
#         rec.append(f"Moderate forecast error (MAPE {row['MAPE']:.2f})")
#         severity = "Medium"

#     # Stockout risk
#     if row['Stockout_rate'] > 0.5:
#         rec.append("High stockout risk")
#         severity = "High"
#     elif row['Stockout_rate'] > 0.2:
#         rec.append("Moderate stockout risk")
#         severity = max(severity, "Medium", key=lambda x: ["Low","Medium","High"].index(x))

#     # Overstock risk
#     if row['Overstock_rate'] > 0.5:
#         rec.append("High overstock risk")
#         severity = max(severity, "Medium", key=lambda x: ["Low","Medium","High"].index(x))

#     if not rec:
#         rec.append("All metrics are normal")

#     return pd.Series({
#         "AI_Recommendation": " | ".join(rec),
#         "Recommendation_Severity": severity
#     })

# ai_rec_df = full_metrics.apply(generate_recommendation, axis=1)
# full_metrics = pd.concat([full_metrics, ai_rec_df], axis=1)

# # ---------------- Sidebar Filters ----------------
# st.sidebar.header("Filters")
# selected_store = st.sidebar.selectbox("Select Store", options=sorted(full_metrics['store_id'].unique()))
# selected_sku = st.sidebar.selectbox("Select SKU", options=sorted(full_metrics['item_id'].unique()))

# filtered_metrics = full_metrics[
#     (full_metrics['store_id'] == selected_store) &
#     (full_metrics['item_id'] == selected_sku)
# ]

# # ---------------- Dashboard Title ----------------
# st.title("AI Optimization in Supply Chain Dashboard")
# st.subheader(f"Metrics for {selected_sku} at {selected_store}")

# # ---------------- KPI Table ----------------
# st.markdown("### KPI Table")
# st.dataframe(filtered_metrics[['item_id','store_id','MAPE','Bias','Stockout_rate','Overstock_rate']])

# # ---------------- Inventory Metrics ----------------
# st.markdown("### Inventory Metrics")
# st.dataframe(filtered_metrics[['mean_demand','std_residual','safety_stock','reorder_point']])

# # ---------------- AI Recommendations ----------------
# st.markdown("### 🤖 AI Recommendations")
# if not filtered_metrics.empty:
#     recommendation_text = filtered_metrics['AI_Recommendation'].values[0]
#     severity_text = filtered_metrics['Recommendation_Severity'].values[0]
#     st.write("Recommendation:", recommendation_text)
#     st.write("Severity:", severity_text)
# else:
#     st.write("No data available for this selection.")

# # ---------------- Summary Metrics ----------------
# st.markdown("### Summary Metrics")
# avg_mape = full_metrics['MAPE'].mean()
# avg_stockout = full_metrics['Stockout_rate'].mean()
# avg_overstock = full_metrics['Overstock_rate'].mean()
# st.write(f"Average MAPE: {avg_mape:.2f}")
# st.write(f"Average Stockout Rate: {avg_stockout:.2f}")
# st.write(f"Average Overstock Rate: {avg_overstock:.2f}")

# # ---------------- Top 5 Plots ----------------
# st.markdown("### Top 5 SKUs by MAPE")
# top5_mape = full_metrics.sort_values('MAPE', ascending=False).head(5)
# fig, ax = plt.subplots(figsize=(10,5))
# sns.barplot(x='item_id', y='MAPE', hue='store_id', data=top5_mape, palette='Reds', dodge=True, ax=ax)
# ax.set_title("Top 5 SKUs by Forecast Error (MAPE)")
# st.pyplot(fig)

# st.markdown("### Top 5 SKUs by Stockout Risk")
# top5_stockout = full_metrics.sort_values('Stockout_rate', ascending=False).head(5)
# fig, ax = plt.subplots(figsize=(10,5))
# sns.barplot(x='item_id', y='Stockout_rate', hue='store_id', data=top5_stockout, palette='Blues', dodge=True, ax=ax)
# ax.set_title("Top 5 SKUs by Stockout Risk")
# st.pyplot(fig)

# st.markdown("### Top 5 SKUs by Overstock Risk")
# top5_overstock = full_metrics.sort_values('Overstock_rate', ascending=False).head(5)
# fig, ax = plt.subplots(figsize=(10,5))
# sns.barplot(x='item_id', y='Overstock_rate', hue='store_id', data=top5_overstock, palette='Greens', dodge=True, ax=ax)
# ax.set_title("Top 5 SKUs by Overstock Risk")
# st.pyplot(fig)

# # ---------------- Forecast Error Histogram ----------------
# st.markdown("### Forecast Error Histogram")
# df_pred['error'] = df_pred['forecast'] - df_pred['actual']
# fig, ax = plt.subplots(figsize=(10,5))
# sns.histplot(df_pred['error'], bins=50, kde=True, color='skyblue', ax=ax)
# ax.set_title("Forecast Error Distribution")
# ax.set_xlabel("Forecast Error (Forecast - Actual)")
# ax.set_ylabel("Count")
# st.pyplot(fig)

# # ---------------- Export Option ----------------
# st.markdown("### Export Data")
# csv = full_metrics.to_csv(index=False)
# st.download_button("Download Metrics as CSV", data=csv, file_name="full_metrics.csv", mime="text/csv")


# 2.
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from io import StringIO
# from datetime import datetime

# st.set_page_config(page_title="AI Supply Chain Dashboard", layout="wide")

# # ---------------- Example / Load Data ----------------
# # Replace this block with loading your real `full_metrics` and `df_pred`
# num_items = 10
# num_stores = 3
# np.random.seed(42)

# full_metrics = pd.DataFrame({
#     'item_id': np.random.choice([f'item_{i}' for i in range(num_items)], size=100),
#     'store_id': np.random.choice([f'store_{i}' for i in range(num_stores)], size=100),
#     'MAPE': np.random.uniform(10, 200, size=100),
#     'Bias': np.random.randint(-50, 50, size=100),
#     'Stockout_rate': np.random.uniform(0, 1, size=100),
#     'Overstock_rate': np.random.uniform(0, 1, size=100),
#     'mean_demand': np.random.randint(10, 100, size=100),
#     'std_residual': np.random.uniform(5, 50, size=100),
#     'safety_stock': np.random.uniform(20, 200, size=100),
#     'reorder_point': np.random.uniform(50, 500, size=100)
# })

# df_pred = pd.DataFrame({
#     'item_id': full_metrics['item_id'],
#     'store_id': full_metrics['store_id'],
#     'actual': np.random.randint(0, 100, size=100),
#     'forecast': np.random.randint(0, 100, size=100)
# })

# # ---------------- Helper logic ----------------
# def compute_suggested_order(row, lookahead_days=7):
#     """
#     Simple suggested order formula:
#       target_stock = mean_daily_demand * (lead_time + lookahead_days) + safety_stock
#       suggested_order = max(0, target_stock - (mean_daily_demand * lead_time))
#     For MVP we assume lead_time = 7 days (you can add per-SKU lead_time later).
#     """
#     lead_time = 7
#     mean_daily = row['mean_demand']
#     safety = row['safety_stock']
#     target_stock = mean_daily * (lead_time + lookahead_days) + safety
#     current_proj = mean_daily * lead_time  # proxy for on-hand + incoming (replace with real data)
#     suggested = max(0, int(round(target_stock - current_proj)))
#     return suggested

# def compute_priority_score(row):
#     # Tunable weights: prioritize stockout risk and MAPE
#     return float(row['Stockout_rate'] * 0.6 + (row['MAPE'] / 100.0) * 0.4)

# def compute_severity(score):
#     if score >= 0.7:
#         return "High"
#     elif score >= 0.4:
#         return "Medium"
#     return "Low"

# # ---------------- Add derived columns ----------------
# full_metrics = full_metrics.copy()
# full_metrics['suggested_order_qty'] = full_metrics.apply(lambda r: compute_suggested_order(r, lookahead_days=28), axis=1)
# full_metrics['priority_score'] = full_metrics.apply(compute_priority_score, axis=1)
# full_metrics['alert'] = full_metrics['priority_score'].apply(lambda s: "⚠ High Priority" if s >= 0.7 else ("! Medium" if s >= 0.4 else "Normal"))
# full_metrics['priority_severity'] = full_metrics['priority_score'].apply(compute_severity)

# # ---------------- Session state for confirmed orders ----------------
# if 'confirmed_orders' not in st.session_state:
#     st.session_state.confirmed_orders = []  # list of dicts

# def confirm_order(item_id, store_id, qty, user_note=""):
#     st.session_state.confirmed_orders.append({
#         'timestamp': datetime.utcnow().isoformat(),
#         'item_id': item_id,
#         'store_id': store_id,
#         'confirmed_qty': int(qty),
#         'user_note': user_note
#     })
#     st.success(f"Order confirmed: {item_id} @ {store_id} — Qty {qty}")

# # ---------------- Sidebar filters ----------------
# st.sidebar.header("Filters & Settings")
# selected_store = st.sidebar.selectbox("Select Store", options=["All"] + sorted(full_metrics['store_id'].unique().tolist()))
# selected_sku = st.sidebar.selectbox("Select SKU", options=["All"] + sorted(full_metrics['item_id'].unique().tolist()))
# top_n_alerts = st.sidebar.slider("Top N priority alerts", min_value=3, max_value=20, value=5)
# lookahead_days = st.sidebar.number_input("Lookahead days for suggested order", min_value=7, max_value=90, value=28)
# # If user changes lookahead, recompute suggestions (simple approach: rerun)
# if lookahead_days != 28:
#     full_metrics['suggested_order_qty'] = full_metrics.apply(lambda r: compute_suggested_order(r, lookahead_days=lookahead_days), axis=1)

# # ---------------- Filtering ----------------
# filtered = full_metrics.copy()
# if selected_store != "All":
#     filtered = filtered[filtered['store_id'] == selected_store]
# if selected_sku != "All":
#     filtered = filtered[filtered['item_id'] == selected_sku]

# # ---------------- Layout ----------------
# st.title("AI Supply Chain Operations — Agentic Dashboard")
# st.markdown("Monitor KPIs, view AI recommendations, adjust and confirm suggested orders.")

# # Top-level summary metrics
# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Average MAPE", f"{full_metrics['MAPE'].mean():.2f}")
# col2.metric("Avg Stockout Rate", f"{full_metrics['Stockout_rate'].mean():.2f}")
# col3.metric("Avg Overstock Rate", f"{full_metrics['Overstock_rate'].mean():.2f}")
# col4.metric("Open Confirmed Orders", len(st.session_state.confirmed_orders))

# # ---------------- Main: KPI Table & Inventory Metrics ----------------
# with st.expander("KPI Table"):
#     st.dataframe(filtered[['item_id','store_id','MAPE','Bias','Stockout_rate','Overstock_rate','priority_score','priority_severity','alert']].sort_values('priority_score', ascending=False).reset_index(drop=True), height=300)

# with st.expander("Inventory Metrics & Suggested Orders"):
#     display_cols = ['item_id','store_id','mean_demand','std_residual','safety_stock','reorder_point','suggested_order_qty','priority_score','priority_severity']
#     st.dataframe(filtered[display_cols].sort_values('priority_score', ascending=False).reset_index(drop=True), height=300)

# # ---------------- AI Recommendation Box for selected SKU/store ----------------
# st.markdown("### 🤖 AI Recommendation & Action")
# if filtered.empty:
#     st.info("No data for the selected filter combination.")
# else:
#     # Use the first matching row as the detailed view (for simplicity)
#     detail = filtered.iloc[0]
#     st.subheader(f"{detail['item_id']} @ {detail['store_id']}")
#     st.write("**Recommendation:**", detail.get('AI_Recommendation', "Use suggested order below"))
#     st.write("**Priority Severity:**", detail['priority_severity'])
#     st.write(f"**Suggested Order Qty (lookahead={lookahead_days}d):** {int(detail['suggested_order_qty'])}")
#     # Interactive adjustment
#     adjusted_qty = st.number_input("Adjust order quantity", min_value=0, max_value=100000, value=int(detail['suggested_order_qty']), step=1, key=f"adj_{detail['item_id']}_{detail['store_id']}")
#     user_note = st.text_input("Optional note for this order", key=f"note_{detail['item_id']}_{detail['store_id']}")
#     if st.button("Confirm Order", key=f"confirm_{detail['item_id']}_{detail['store_id']}"):
#         confirm_order(detail['item_id'], detail['store_id'], adjusted_qty, user_note)

# # ---------------- Top Alerts Panel ----------------
# st.markdown("### ⚠ Top Priority Alerts")
# top_priority = full_metrics.sort_values('priority_score', ascending=False).head(top_n_alerts)
# st.dataframe(top_priority[['item_id','store_id','priority_score','priority_severity','suggested_order_qty']].reset_index(drop=True), height=300)

# # ---------------- Charts: Top 5 by metrics ----------------
# st.markdown("### Visuals")
# left_col, right_col = st.columns(2)

# with left_col:
#     st.markdown("Top 5 SKUs by MAPE")
#     top5_mape = full_metrics.sort_values('MAPE', ascending=False).head(5)
#     fig1, ax1 = plt.subplots(figsize=(8,4))
#     sns.barplot(x='item_id', y='MAPE', hue='store_id', data=top5_mape, dodge=True, ax=ax1)
#     ax1.set_title("Top 5 SKUs by Forecast Error (MAPE)")
#     st.pyplot(fig1)

#     st.markdown("Forecast Error Distribution")
#     df_pred['error'] = df_pred['forecast'] - df_pred['actual']
#     fig_err, ax_err = plt.subplots(figsize=(8,4))
#     sns.histplot(df_pred['error'], bins=40, kde=True, ax=ax_err)
#     ax_err.set_xlabel("Forecast Error (Forecast - Actual)")
#     st.pyplot(fig_err)

# with right_col:
#     st.markdown("Top 5 SKUs by Stockout Risk")
#     top5_stockout = full_metrics.sort_values('Stockout_rate', ascending=False).head(5)
#     fig2, ax2 = plt.subplots(figsize=(8,4))
#     sns.barplot(x='item_id', y='Stockout_rate', hue='store_id', data=top5_stockout, dodge=True, ax=ax2)
#     ax2.set_title("Top 5 SKUs by Stockout Risk")
#     st.pyplot(fig2)

#     st.markdown("Top 5 SKUs by Overstock Risk")
#     top5_overstock = full_metrics.sort_values('Overstock_rate', ascending=False).head(5)
#     fig3, ax3 = plt.subplots(figsize=(8,4))
#     sns.barplot(x='item_id', y='Overstock_rate', hue='store_id', data=top5_overstock, dodge=True, ax=ax3)
#     ax3.set_title("Top 5 SKUs by Overstock Risk")
#     st.pyplot(fig3)

# # ---------------- Confirmed Orders Table & Download ----------------
# st.markdown("### ✅ Confirmed Orders")
# if st.session_state.confirmed_orders:
#     confirmed_df = pd.DataFrame(st.session_state.confirmed_orders)
#     st.dataframe(confirmed_df, height=250)
#     csv = confirmed_df.to_csv(index=False)
#     st.download_button("Download Confirmed Orders CSV", data=csv, file_name="confirmed_orders.csv", mime="text/csv")
#     if st.button("Clear Confirmed Orders"):
#         st.session_state.confirmed_orders = []
#         st.experimental_rerun()
# else:
#     st.write("No orders confirmed yet.")

# # ---------------- Footer / Next steps ----------------
# st.markdown("---")
# st.markdown("**Next steps you can enable:**")
# st.markdown("- Hook `suggested_order_qty` to real `on_hand` and `incoming` columns (replace mean_daily proxy).")
# st.markdown("- Store confirmed orders to DB or create draft POs in ERP (requires API integration).")
# st.markdown("- Add scheduling (Prefect / cron) to refresh forecasts daily and trigger alerts automatically.")
# st.markdown("- Add per-item `lead_time` column to make order quantities more accurate.")


# 3...4


# app.py (UPDATED)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="AI Supply Chain Control Tower", layout="wide", initial_sidebar_state="expanded")

# ------------------------ SESSION STATE INIT ------------------------
if "confirmed_local" not in st.session_state:
    st.session_state.confirmed_local = []   # local, immediate UI feedback
if "db_persistence" not in st.session_state:
    st.session_state.db_persistence = False

# ------------------------ CONFIG / FILE PATHS ------------------------
DATA_DIR = Path(".")
FULL_METRICS_PATH = DATA_DIR / "full_metrics.csv"
DF_PRED_PATH = DATA_DIR / "df_pred.csv"
DB_PATH = DATA_DIR / "confirmed_orders.db"
# screenshot path you supplied (will display if exists)
SCREENSHOT_PATH = Path("/mnt/data/Screenshot 2025-11-25 021708.png")

# ------------------------ UTILITIES / AI RECOMMENDATION LOGIC ------------------------
def load_or_create_demo():
    """Load real CSVs if they exist, otherwise generate synthetic demo data."""
    if FULL_METRICS_PATH.exists() and DF_PRED_PATH.exists():
        full_metrics = pd.read_csv(FULL_METRICS_PATH, parse_dates=True)
        df_pred = pd.read_csv(DF_PRED_PATH, parse_dates=True)
        return full_metrics, df_pred

    # synthetic demo
    np.random.seed(42)
    num_items = 20
    num_stores = 6
    items = [f"item_{i}" for i in range(num_items)]
    stores = [f"store_{i}" for i in range(num_stores)]

    full_metrics = pd.DataFrame({
        "item_id": np.random.choice(items, size=300),
        "store_id": np.random.choice(stores, size=300),
        "MAPE": np.random.uniform(5, 200, size=300),
        "Bias": np.random.uniform(-50,50,size=300),
        "Stockout_rate": np.random.uniform(0,1,size=300),
        "Overstock_rate": np.random.uniform(0,1,size=300),
        "mean_demand": np.random.randint(1,200,size=300),
        "std_residual": np.random.uniform(1,50,size=300),
        # optional columns you can add later: on_hand, incoming, lead_time_days
    })
    full_metrics["safety_stock"] = 1.65 * full_metrics["std_residual"]
    full_metrics["reorder_point"] = full_metrics["mean_demand"] * 7 + full_metrics["safety_stock"]  # default lead_time=7

    df_pred = pd.DataFrame({
        "item_id": full_metrics["item_id"].values,
        "store_id": full_metrics["store_id"].values,
        "actual": np.random.randint(0,150,size=len(full_metrics)),
        "forecast": np.random.randint(0,150,size=len(full_metrics))
    })
    return full_metrics, df_pred

def compute_suggested_order(row, lead_time_days=7, lookahead_days=28, on_hand=None, incoming=None):
    """
    Use same logic you had:
    target_stock = mean_daily * (lead_time + lookahead_days) + safety_stock
    suggested = max(0, target_stock - current_proj)
    """
    mean_daily = float(row.get("mean_demand", 0.0))
    safety = float(row.get("safety_stock", 0.0))
    lt = float(row.get("lead_time_days", lead_time_days)) if row.get("lead_time_days") is not None else lead_time_days
    target_stock = mean_daily * (lt + lookahead_days) + safety

    if on_hand is None:
        current_proj = mean_daily * lt  # proxy
    else:
        current_proj = float(on_hand) + float(incoming or 0)

    suggested = max(0, int(round(target_stock - current_proj)))
    return suggested

def compute_priority_score(row, w_stockout=0.6, w_mape=0.4):
    mape_norm = min(float(row.get("MAPE", 0.0)) / 100.0, 2.0)
    stockout = float(row.get("Stockout_rate", 0.0))
    score = stockout * w_stockout + mape_norm * w_mape
    return float(np.clip(score, 0.0, 1.0))

def severity_from_score(score):
    if score >= 0.75: return "High"
    if score >= 0.45: return "Medium"
    return "Low"

# The AI Recommendation function you used earlier (copied/adapted)
def generate_ai_recommendation(row):
    rec = []
    severity = "Low"
    mape = float(row.get("MAPE", 0.0))
    stockout_rate = float(row.get("Stockout_rate", 0.0))
    overstock_rate = float(row.get("Overstock_rate", 0.0))

    # Forecast accuracy
    if mape > 100:
        rec.append(f"High forecast error (MAPE {mape:.2f})")
        severity = "High"
    elif mape > 50:
        rec.append(f"Moderate forecast error (MAPE {mape:.2f})")
        severity = "Medium"

    # Stockout risk
    if stockout_rate > 0.5:
        rec.append("High stockout risk")
        severity = "High"
    elif stockout_rate > 0.2:
        rec.append("Moderate stockout risk")
        if severity != "High":
            severity = "Medium"

    # Overstock risk
    if overstock_rate > 0.5:
        rec.append("High overstock risk")
        if severity != "High":
            severity = "Medium"

    if not rec:
        rec.append("All metrics are normal")

    return {"AI_Recommendation": " | ".join(rec), "Recommendation_Severity": severity}

# ------------------------ DB persistence helpers ------------------------
def init_db(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS confirmed_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        item_id TEXT,
        store_id TEXT,
        confirmed_qty INTEGER,
        user_note TEXT
    );
    """)
    conn.commit()

def save_confirmed_order(conn, item_id, store_id, qty, note=""):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO confirmed_orders (timestamp, item_id, store_id, confirmed_qty, user_note) VALUES (?, ?, ?, ?, ?)",
        (datetime.utcnow().isoformat(), item_id, store_id, int(qty), note)
    )
    conn.commit()

def load_confirmed_orders(conn):
    cur = conn.cursor()
    cur.execute("SELECT timestamp, item_id, store_id, confirmed_qty, user_note FROM confirmed_orders ORDER BY id DESC")
    rows = cur.fetchall()
    return pd.DataFrame(rows, columns=["timestamp","item_id","store_id","confirmed_qty","user_note"])

# ------------------------ LOAD DATA ------------------------
full_metrics, df_pred = load_or_create_demo()

# Ensure lead_time exists
if "lead_time_days" not in full_metrics.columns:
    full_metrics["lead_time_days"] = 7

# Derived / AI columns (initial)
full_metrics = full_metrics.copy()
full_metrics["suggested_order_qty"] = full_metrics.apply(lambda r: compute_suggested_order(r, lookahead_days=28), axis=1)
full_metrics["priority_score"] = full_metrics.apply(compute_priority_score, axis=1)
full_metrics["priority_severity"] = full_metrics["priority_score"].apply(severity_from_score)

# Attach AI recommendation text & severity from your generate_ai_recommendation
ai_recs = full_metrics.apply(lambda r: pd.Series(generate_ai_recommendation(r)), axis=1)
full_metrics = pd.concat([full_metrics.reset_index(drop=True), ai_recs.reset_index(drop=True)], axis=1)

# ------------------------ DB init (if enabled) ------------------------
conn = None
if st.session_state.db_persistence:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    init_db(conn)

# ------------------------ SIDEBAR ------------------------
st.sidebar.header("Filters & Settings")
store_options = ["All"] + sorted(full_metrics["store_id"].unique().tolist())
sku_options = ["All"] + sorted(full_metrics["item_id"].unique().tolist())

selected_store = st.sidebar.selectbox("Store", options=store_options, index=0)
selected_sku = st.sidebar.selectbox("SKU / Item", options=sku_options, index=0)
lookahead_days = st.sidebar.slider("Lookahead days for suggested order", min_value=7, max_value=90, value=28)
recompute_btn = st.sidebar.button("Recompute suggestions (lookahead)")

# toggle DB persistence
persist_checkbox = st.sidebar.checkbox("Persist confirmed orders to local DB", value=st.session_state.db_persistence)
st.session_state.db_persistence = persist_checkbox
if st.session_state.db_persistence and conn is None:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    init_db(conn)

# ------------------------ FILTER DATA ------------------------
filtered = full_metrics.copy()
if selected_store != "All":
    filtered = filtered[filtered["store_id"] == selected_store]
if selected_sku != "All":
    filtered = filtered[filtered["item_id"] == selected_sku]

# recompute suggested qtys if requested
if recompute_btn:
    full_metrics["suggested_order_qty"] = full_metrics.apply(lambda r: compute_suggested_order(r, lead_time_days=r["lead_time_days"], lookahead_days=lookahead_days), axis=1)
    full_metrics["priority_score"] = full_metrics.apply(compute_priority_score, axis=1)
    full_metrics["priority_severity"] = full_metrics["priority_score"].apply(severity_from_score)
    # recompute AI recs
    ai_recs = full_metrics.apply(lambda r: pd.Series(generate_ai_recommendation(r)), axis=1)
    full_metrics[["AI_Recommendation", "Recommendation_Severity"]] = ai_recs[["AI_Recommendation","Recommendation_Severity"]]
    # re-filter
    filtered = full_metrics.copy()
    if selected_store != "All":
        filtered = filtered[filtered["store_id"] == selected_store]
    if selected_sku != "All":
        filtered = filtered[filtered["item_id"] == selected_sku]

# ------------------------ HEADER / KPI CARDS ------------------------
st.title("AI Supply Chain Control Tower — Enterprise View")
st.markdown("Monitor KPIs, review AI recommendations, and confirm suggested orders (local DB optional).")

c1, c2, c3, c4 = st.columns([1.2,1.2,1.2,1.0])
if filtered.empty:
    c1.metric("Average MAPE", "—")
    c2.metric("Avg Stockout Rate", "—")
    c3.metric("Avg Overstock Rate", "—")
else:
    c1.metric("Average MAPE", f"{filtered['MAPE'].mean():.2f}")
    c2.metric("Avg Stockout Rate", f"{filtered['Stockout_rate'].mean():.2f}")
    c3.metric("Avg Overstock Rate", f"{filtered['Overstock_rate'].mean():.2f}")

# confirmed orders count (session + DB)
def get_confirmed_count():
    local = len(st.session_state.confirmed_local)
    db_count = 0
    if st.session_state.db_persistence and conn is not None:
        try:
            db_df = load_confirmed_orders(conn)
            db_count = len(db_df)
        except Exception:
            db_count = 0
    return local + db_count

c4.metric("Open Confirmed Orders", f"{get_confirmed_count()}")

# ------------------------ TABS / MAIN LAYOUT ------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Demand", "Inventory", "AI Recommendations", "Confirmed Orders"])

# Optional: show uploaded screenshot (for your reference). Path from earlier: /mnt/data/...
if SCREENSHOT_PATH.exists():
    with st.container():
        st.markdown("#### (Debug) Top Alerts screenshot")
        st.image(str(SCREENSHOT_PATH), width=700)

# ------------------------ TAB: Demand ------------------------
with tab1:
    st.subheader("Demand Overview")
    left, right = st.columns(2)
    with left:
        st.markdown("Top SKUs by Mean Demand")
        top_demand = full_metrics.groupby("item_id")["mean_demand"].mean().sort_values(ascending=False).head(10).reset_index()
        fig, ax = plt.subplots(figsize=(8,4))
        sns.barplot(data=top_demand, x="item_id", y="mean_demand", ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)
    with right:
        st.markdown("MAPE Distribution")
        fig2, ax2 = plt.subplots(figsize=(8,4))
        sns.histplot(full_metrics["MAPE"], bins=40, kde=True, ax=ax2)
        ax2.set_xlabel("MAPE")
        st.pyplot(fig2)

# ------------------------ TAB: Inventory ------------------------
with tab2:
    st.subheader("Inventory Metrics & Suggested Orders")
    st.markdown(f"**Filters:** Store = **{selected_store}**, SKU = **{selected_sku}**, Lookahead = **{lookahead_days} days**")
    if filtered.empty:
        st.info("No data for the selected filters.")
    else:
        display_cols = ["item_id","store_id","mean_demand","std_residual","safety_stock","reorder_point","suggested_order_qty","priority_score","priority_severity"]
        df_show = filtered[display_cols].sort_values("priority_score", ascending=False).reset_index(drop=True)
        st.dataframe(df_show, height=350)

        # Action panel: select row from df_show
        st.markdown("#### Action Panel (Select a row index to confirm order)")
        max_idx = max(len(df_show)-1, 0)
        sel_idx = st.number_input("Select row index (0 = top row)", min_value=0, max_value=max_idx, value=0, step=1)
        sel_idx = int(sel_idx)
        if len(df_show) > 0:
            sel_row = df_show.iloc[sel_idx]
            st.write(f"**Selected:** {sel_row['item_id']} @ {sel_row['store_id']}")
            suggested_val = int(sel_row["suggested_order_qty"])
            adj_qty = st.number_input("Adjusted order qty", min_value=0, max_value=1_000_000, value=suggested_val, step=1, key=f"adj_{sel_row['item_id']}_{sel_row['store_id']}")
            note = st.text_input("Optional note for this order", key=f"note_{sel_row['item_id']}_{sel_row['store_id']}")
            if st.button("Confirm Order", key=f"confirm_{sel_row['item_id']}_{sel_row['store_id']}"):
                entry = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "item_id": sel_row["item_id"],
                    "store_id": sel_row["store_id"],
                    "confirmed_qty": int(adj_qty),
                    "user_note": note
                }
                # save locally for immediate UI
                st.session_state.confirmed_local.insert(0, entry)
                # optionally persist to local sqlite
                if st.session_state.db_persistence and conn is not None:
                    try:
                        save_confirmed_order(conn, sel_row["item_id"], sel_row["store_id"], int(adj_qty), note)
                    except Exception as e:
                        st.error(f"Unable to save to DB: {e}")
                st.success(f"Confirmed order: {sel_row['item_id']} @ {sel_row['store_id']} — Qty {adj_qty}")
                st.experimental_rerun()

# ------------------------ TAB: AI Recommendations ------------------------
with tab3:
    st.subheader("AI Recommendations & Alerts")
    if filtered.empty:
        st.info("No data available for this filter.")
    else:
        top_n = 12
        top_alerts = filtered.sort_values("priority_score", ascending=False).head(top_n).reset_index(drop=True)

        st.markdown("### ⚠ Top Alerts")
        # show table of alerts
        st.dataframe(top_alerts[["item_id","store_id","priority_score","priority_severity","suggested_order_qty","MAPE","Stockout_rate"]], height=300)

        # priority histogram
        figp, axp = plt.subplots(figsize=(8,3))
        sns.histplot(filtered["priority_score"], bins=30, kde=True, ax=axp)
        axp.set_title("Priority Score Distribution")
        st.pyplot(figp)

        # Detailed top recommendation and quick confirm (works with proper indexing)
        if not top_alerts.empty:
            st.markdown("#### Top Recommendation Details")
            sel_top_index = st.number_input("Select top-alert index", min_value=0, max_value=len(top_alerts)-1, value=0, step=1, key="top_alert_index")
            sel_top_index = int(sel_top_index)
            top = top_alerts.iloc[sel_top_index]
            st.write(f"**{top['item_id']} @ {top['store_id']}**")
            st.write(f"- Priority score: {top['priority_score']:.3f} ({top['priority_severity']})")
            st.write(f"- Suggested order qty: {int(top['suggested_order_qty'])}")
            st.write(f"- Mean daily demand: {top['mean_demand']:.2f}")
            st.write(f"- Safety stock: {top['safety_stock']:.2f}")
            if st.button(f"Confirm top order: {top['item_id']} @ {top['store_id']}", key=f"confirm_top_{top['item_id']}_{top['store_id']}"):
                entry = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "item_id": top["item_id"],
                    "store_id": top["store_id"],
                    "confirmed_qty": int(top["suggested_order_qty"]),
                    "user_note": "Confirmed from top alert"
                }
                st.session_state.confirmed_local.insert(0, entry)
                if st.session_state.db_persistence and conn is not None:
                    save_confirmed_order(conn, top["item_id"], top["store_id"], int(top["suggested_order_qty"]), "Confirmed from top alert")
                st.success("Top alert order confirmed.")
                st.experimental_rerun()

# ------------------------ TAB: Confirmed Orders ------------------------
with tab4:
    st.subheader("Confirmed Orders")
    st.markdown("Local (session) + persisted (DB) confirmed orders. Download or clear.")

    local_df = pd.DataFrame(st.session_state.confirmed_local)
    db_df = pd.DataFrame()
    if st.session_state.db_persistence and conn is not None:
        try:
            db_df = load_confirmed_orders(conn)
        except Exception:
            db_df = pd.DataFrame()

    if not local_df.empty:
        st.markdown("**Local (session)**")
        st.dataframe(local_df, height=200)
    else:
        st.write("No local confirmed orders in this session.")

    if not db_df.empty:
        st.markdown("**Persisted (DB)**")
        st.dataframe(db_df, height=300)
    else:
        st.write("No persisted confirmed orders (DB is empty).")

    combined = pd.concat([local_df, db_df], ignore_index=True, sort=False) if (not local_df.empty or not db_df.empty) else pd.DataFrame()
    if not combined.empty:
        csv = combined.to_csv(index=False)
        st.download_button("Download All Confirmed Orders (CSV)", data=csv, file_name="confirmed_orders_all.csv", mime="text/csv")
        if st.button("Clear Local Confirmed Orders"):
            st.session_state.confirmed_local = []
            st.experimental_rerun()
        if st.session_state.db_persistence and conn is not None:
            if st.button("Clear Persisted DB Orders (DROP)"):
                cur = conn.cursor()
                cur.execute("DELETE FROM confirmed_orders")
                conn.commit()
                st.success("Cleared persisted orders.")
                st.experimental_rerun()
    else:
        st.info("No confirmed orders to download.")

# ------------------------ FOOTER / NEXT STEPS ------------------------
st.markdown("---")
st.markdown("**Next steps & tips**")
st.markdown("- Replace synthetic demo loader with your real `full_metrics.csv` and `df_pred.csv` files (place them in the project folder).")
st.markdown("- Hook `suggested_order_qty` to real `on_hand` and `incoming` columns for accuracy.")
st.markdown("- Add model versioning / forecast timestamp to the UI (store with each forecast run).")
st.markdown("- Integrate with ERP / PO system if you want confirmed orders to create draft POs (requires API keys).")

# Close DB connection (safe)
try:
    if conn is not None:
        conn.close()
except Exception:
    pass













