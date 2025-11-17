"""
Inventory Manager Dashboard
Displays stock levels, inventory turnover, and supplier performance metrics
"""

import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Inventory Dashboard - StyleNest BI",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    css_path = Path(__file__).parent.parent / "styles.css"
    if css_path.exists():
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Load data
@st.cache_data
def load_data():
    data_path = Path(__file__).parent.parent / "data" / "inventory.json"
    with open(data_path, "r") as f:
        return json.load(f)

data = load_data()

# Header
st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 2rem;'>
        <h1 style='font-size: 2.5rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;'>
            📦 Inventory Manager Dashboard
        </h1>
        <p style='color: #94a3b8; font-size: 1rem;'>Stock Management & Supplier Analytics</p>
    </div>
""", unsafe_allow_html=True)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Stock Available</div>
            <div class='kpi-value'>{data['stock_available']/1000:.0f}K</div>
            <div class='kpi-change'>units</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Out of Stock Items</div>
            <div class='kpi-value'>{data['out_of_stock_items']}</div>
            <div class='kpi-change negative'>⚠️ Needs attention</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Inventory Turnover</div>
            <div class='kpi-value'>{data['inventory_turnover_ratio']}</div>
            <div class='kpi-change positive'>↑ Healthy ratio</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Supplier Score</div>
            <div class='kpi-value'>{data['supplier_performance_score']}/100</div>
            <div class='kpi-change'>Good performance</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts Section
col1, col2 = st.columns(2)

# Category-wise Stock Levels - Bar Chart
with col1:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Category-wise Stock Levels</div>", unsafe_allow_html=True)
    
    category_df = pd.DataFrame(data['category_stock'])
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=category_df['category'],
        y=category_df['stock'],
        name='Current Stock',
        marker_color='#6366f1',
        text=category_df['stock'],
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        x=category_df['category'],
        y=category_df['threshold'],
        name='Reorder Threshold',
        marker_color='#ef4444',
        opacity=0.6,
        text=category_df['threshold'],
        textposition='outside'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155', title='Units'),
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Supplier Comparison - Bar Chart
with col2:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Supplier Performance Comparison</div>", unsafe_allow_html=True)
    
    supplier_df = pd.DataFrame(data['supplier_comparison'])
    fig = px.bar(
        supplier_df,
        x='supplier',
        y='total_score',
        title="",
        labels={'total_score': 'Performance Score', 'supplier': 'Supplier'},
        color='total_score',
        color_continuous_scale='viridis',
        text='total_score'
    )
    fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        xaxis=dict(gridcolor='#334155', tickangle=-45),
        yaxis=dict(gridcolor='#334155', range=[0, 100]),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Top 10 Selling Products - Table (Full Width)
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Top 10 Selling Products</div>", unsafe_allow_html=True)

products_df = pd.DataFrame(data['top_selling_products'])
products_df['Units Sold'] = products_df['units_sold']
products_df['Current Stock'] = products_df['stock']
products_df['Status'] = products_df['status']
display_df = products_df[['product', 'Units Sold', 'Current Stock', 'Status']]

# Style the dataframe
def style_status(val):
    if val == 'Out of Stock':
        return 'background-color: rgba(239, 68, 68, 0.2); color: #ef4444;'
    elif val == 'Low Stock':
        return 'background-color: rgba(245, 158, 11, 0.2); color: #f59e0b;'
    else:
        return 'background-color: rgba(16, 185, 129, 0.2); color: #10b981;'

styled_df = display_df.style.applymap(style_status, subset=['Status'])
st.dataframe(styled_df, use_container_width=True, hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

# Low Stock Alert Section
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>⚠️ Low Stock Alerts</div>", unsafe_allow_html=True)

low_stock_df = pd.DataFrame(data['low_stock_items'])
st.dataframe(low_stock_df, use_container_width=True, hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

# Back to Home
st.sidebar.markdown("---")
if st.sidebar.button("🏠 Back to Home"):
    st.switch_page("app.py")

