"""
CEO Dashboard - Executive Overview
Displays high-level KPIs and strategic insights for C-level executives
"""

import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="CEO Dashboard - StyleNest BI",
    page_icon="👔",
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
    data_path = Path(__file__).parent.parent / "data" / "sales.json"
    with open(data_path, "r") as f:
        return json.load(f)

data = load_data()

# Header
st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 2rem;'>
        <h1 style='font-size: 2.5rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;'>
            👔 CEO Dashboard
        </h1>
        <p style='color: #94a3b8; font-size: 1rem;'>Executive Overview & Strategic Insights</p>
    </div>
""", unsafe_allow_html=True)

# KPI Cards Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Total Revenue</div>
            <div class='kpi-value'>${data['total_revenue']/1000:.1f}K</div>
            <div class='kpi-change positive'>↑ 12% vs last month</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Profit Margin</div>
            <div class='kpi-value'>{data['profit_margin']}%</div>
            <div class='kpi-change positive'>↑ 2.5% vs last quarter</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Total Orders</div>
            <div class='kpi-value'>{data['total_orders']/1000:.1f}K</div>
            <div class='kpi-change positive'>↑ 8% growth</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Customer Satisfaction</div>
            <div class='kpi-value'>{data['customer_satisfaction']}%</div>
            <div class='kpi-change positive'>↑ 3% improvement</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts Section
col1, col2 = st.columns(2)

# Monthly Sales Trend - Line Chart
with col1:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Monthly Sales Trend</div>", unsafe_allow_html=True)
    
    monthly_df = pd.DataFrame(data['monthly_sales'])
    fig = px.line(
        monthly_df, 
        x='month', 
        y='revenue',
        markers=True,
        title="",
        labels={'revenue': 'Revenue ($)', 'month': 'Month'}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155'),
        hovermode='x unified'
    )
    fig.update_traces(
        line_color='#6366f1',
        marker_color='#8b5cf6',
        line_width=3
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Category-wise Revenue - Bar Chart
with col2:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Category-wise Revenue</div>", unsafe_allow_html=True)
    
    category_df = pd.DataFrame(data['category_revenue'])
    fig = px.bar(
        category_df,
        x='category',
        y='revenue',
        title="",
        labels={'revenue': 'Revenue ($)', 'category': 'Category'},
        color='revenue',
        color_continuous_scale='viridis'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155'),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Regional Customer Growth - Full Width
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Regional Customer Growth</div>", unsafe_allow_html=True)

regional_df = pd.DataFrame(data['regional_growth'])
fig = go.Figure()

fig.add_trace(go.Bar(
    x=regional_df['region'],
    y=regional_df['customers'],
    name='Customers',
    marker_color='#6366f1',
    text=regional_df['customers'],
    textposition='outside'
))

fig.add_trace(go.Scatter(
    x=regional_df['region'],
    y=regional_df['growth'] * 100,
    name='Growth %',
    yaxis='y2',
    mode='lines+markers',
    line=dict(color='#ec4899', width=3),
    marker=dict(size=10)
))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#94a3b8',
    xaxis=dict(gridcolor='#334155'),
    yaxis=dict(
        title='Number of Customers',
        gridcolor='#334155',
        side='left'
    ),
    yaxis2=dict(
        title='Growth Percentage (%)',
        overlaying='y',
        side='right',
        gridcolor='#334155'
    ),
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

# Back to Home
st.sidebar.markdown("---")
if st.sidebar.button("🏠 Back to Home"):
    st.switch_page("app.py")

