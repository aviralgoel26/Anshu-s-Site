"""
Sales Executive Dashboard
Displays daily sales trends, regional performance, and product analytics
"""

import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Sales Dashboard - StyleNest BI",
    page_icon="💰",
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
    sales_path = Path(__file__).parent.parent / "data" / "sales.json"
    customers_path = Path(__file__).parent.parent / "data" / "customers.json"
    
    with open(sales_path, "r") as f:
        sales_data = json.load(f)
    with open(customers_path, "r") as f:
        customers_data = json.load(f)
    
    return sales_data, customers_data

sales_data, customers_data = load_data()

# Header
st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 2rem;'>
        <h1 style='font-size: 2.5rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;'>
            💰 Sales Executive Dashboard
        </h1>
        <p style='color: #94a3b8; font-size: 1rem;'>Sales Performance & Regional Analytics</p>
    </div>
""", unsafe_allow_html=True)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

# Calculate daily sales average
daily_avg = sum([d['sales'] for d in sales_data['daily_sales']]) / len(sales_data['daily_sales'])
daily_units = sum([d['units'] for d in sales_data['daily_sales']]) / len(sales_data['daily_sales'])

with col1:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Daily Sales</div>
            <div class='kpi-value'>${daily_avg/1000:.1f}K</div>
            <div class='kpi-change positive'>↑ 5% vs yesterday</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Units Sold</div>
            <div class='kpi-value'>{int(daily_units)}</div>
            <div class='kpi-change positive'>↑ 8% growth</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>New Customers</div>
            <div class='kpi-value'>{customers_data['new_customers_today']}</div>
            <div class='kpi-change positive'>↑ Today</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Avg Order Value</div>
            <div class='kpi-value'>${customers_data['avg_order_value']}</div>
            <div class='kpi-change positive'>↑ $2 increase</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts Section
col1, col2 = st.columns(2)

# Daily/Weekly Sales Trend - Line Chart
with col1:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Daily Sales Trend (Last 7 Days)</div>", unsafe_allow_html=True)
    
    daily_df = pd.DataFrame(sales_data['daily_sales'])
    daily_df['date'] = pd.to_datetime(daily_df['date'])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=daily_df['date'],
        y=daily_df['sales'],
        name='Sales ($)',
        mode='lines+markers',
        line=dict(color='#6366f1', width=3),
        marker=dict(size=10, color='#8b5cf6'),
        yaxis='y'
    ))
    
    fig.add_trace(go.Bar(
        x=daily_df['date'],
        y=daily_df['units'],
        name='Units Sold',
        marker_color='#ec4899',
        opacity=0.6,
        yaxis='y2'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(
            title='Sales ($)',
            gridcolor='#334155',
            side='left'
        ),
        yaxis2=dict(
            title='Units Sold',
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

# Region-wise Sales - Bar Chart
with col2:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Region-wise Sales Performance</div>", unsafe_allow_html=True)
    
    region_df = pd.DataFrame(sales_data['region_sales'])
    fig = px.bar(
        region_df,
        x='region',
        y='sales',
        title="",
        labels={'sales': 'Sales ($)', 'region': 'Region'},
        color='sales',
        color_continuous_scale='plasma',
        text='sales'
    )
    fig.update_traces(
        texttemplate='$%{text:,.0f}',
        textposition='outside'
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

# Product Performance - Full Width
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Top Product Performance</div>", unsafe_allow_html=True)

product_df = pd.DataFrame(sales_data['product_performance'])
fig = go.Figure()

fig.add_trace(go.Bar(
    x=product_df['product'],
    y=product_df['sales'],
    name='Sales ($)',
    marker_color='#6366f1',
    text=product_df['sales'],
    texttemplate='$%{text:,.0f}',
    textposition='outside',
    yaxis='y'
))

fig.add_trace(go.Scatter(
    x=product_df['product'],
    y=product_df['units'],
    name='Units Sold',
    mode='lines+markers',
    line=dict(color='#ec4899', width=3),
    marker=dict(size=12),
    yaxis='y2'
))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#94a3b8',
    xaxis=dict(gridcolor='#334155', tickangle=-45),
    yaxis=dict(
        title='Sales ($)',
        gridcolor='#334155',
        side='left'
    ),
    yaxis2=dict(
        title='Units Sold',
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

# Product Performance Table
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Product Sales Details</div>", unsafe_allow_html=True)

product_df['Sales ($)'] = product_df['sales']
product_df['Units Sold'] = product_df['units']
display_df = product_df[['product', 'Sales ($)', 'Units Sold']]
display_df['Sales ($)'] = display_df['Sales ($)'].apply(lambda x: f"${x:,.0f}")
st.dataframe(display_df, use_container_width=True, hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

# Back to Home
st.sidebar.markdown("---")
if st.sidebar.button("🏠 Back to Home"):
    st.switch_page("app.py")

