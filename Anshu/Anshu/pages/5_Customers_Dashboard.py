"""
Customers Dashboard - Customer Insights & Analytics
Displays customer metrics, segments, and product showcase
"""

import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Customers Dashboard - StyleNest BI",
    page_icon="👥",
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
    data_path = Path(__file__).parent.parent / "data" / "customers.json"
    with open(data_path, "r") as f:
        return json.load(f)

data = load_data()

# Header
st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 2rem;'>
        <h1 style='font-size: 2.5rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;'>
            👥 Customers Dashboard
        </h1>
        <p style='color: #94a3b8; font-size: 1rem;'>Customer Insights & Product Showcase</p>
    </div>
""", unsafe_allow_html=True)

# KPI Cards Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Total Customers</div>
            <div class='kpi-value'>{data['total_customers']/1000:.1f}K</div>
            <div class='kpi-change positive'>↑ 5% growth</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>New Customers Today</div>
            <div class='kpi-value'>{data['new_customers_today']}</div>
            <div class='kpi-change positive'>↑ 15% vs yesterday</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Avg Order Value</div>
            <div class='kpi-value'>${data['avg_order_value']}</div>
            <div class='kpi-change positive'>↑ $3 increase</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    # Calculate average satisfaction from trend
    avg_satisfaction = sum([item['score'] for item in data['customer_satisfaction_trend']]) / len(data['customer_satisfaction_trend'])
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Avg Satisfaction</div>
            <div class='kpi-value'>{avg_satisfaction:.1f}%</div>
            <div class='kpi-change positive'>↑ 2% improvement</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts Section
col1, col2 = st.columns(2)

# Customer Acquisition Trend - Line Chart
with col1:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Customer Acquisition Trend</div>", unsafe_allow_html=True)
    
    acquisition_df = pd.DataFrame(data['customer_acquisition'])
    fig = px.line(
        acquisition_df, 
        x='month', 
        y='new_customers',
        markers=True,
        title="",
        labels={'new_customers': 'New Customers', 'month': 'Month'}
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

# Customer Segments - Pie Chart
with col2:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Customer Segments Distribution</div>", unsafe_allow_html=True)
    
    segments_df = pd.DataFrame(data['customer_segments'])
    fig = px.pie(
        segments_df,
        values='count',
        names='segment',
        title="",
        color_discrete_sequence=['#6366f1', '#8b5cf6', '#ec4899']
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.1
        )
    )
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        textfont_size=12
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Customer Satisfaction Trend - Full Width
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Customer Satisfaction Trend</div>", unsafe_allow_html=True)

satisfaction_df = pd.DataFrame(data['customer_satisfaction_trend'])
fig = px.area(
    satisfaction_df,
    x='month',
    y='score',
    title="",
    labels={'score': 'Satisfaction Score (%)', 'month': 'Month'},
    color_discrete_sequence=['#10b981']
)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#94a3b8',
    xaxis=dict(gridcolor='#334155'),
    yaxis=dict(gridcolor='#334155', range=[80, 95]),
    hovermode='x unified'
)
fig.update_traces(
    fill='tonexty',
    line=dict(width=3)
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Clothes Showcase Section
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>🛍️ Featured Collection</div>", unsafe_allow_html=True)

# Clothes images - using Unsplash URLs for fashion/clothing
clothes_images = [
    {
        "name": "Classic White Shirt",
        "url": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400&h=500&fit=crop",
        "price": "$49.99"
    },
    {
        "name": "Denim Jacket",
        "url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=500&fit=crop",
        "price": "$79.99"
    },
    {
        "name": "Elegant Dress",
        "url": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=500&fit=crop",
        "price": "$89.99"
    },
    {
        "name": "Casual T-Shirt",
        "url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=500&fit=crop",
        "price": "$29.99"
    },
    {
        "name": "Formal Suit",
        "url": "https://images.unsplash.com/photo-1594938291221-94f18e0e0e6b?w=400&h=500&fit=crop",
        "price": "$199.99"
    },
    {
        "name": "Summer Shorts",
        "url": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400&h=500&fit=crop",
        "price": "$39.99"
    }
]

# Display clothes in a grid
cols = st.columns(3)
for idx, item in enumerate(clothes_images):
    with cols[idx % 3]:
        st.markdown(f"""
            <div style='background: rgba(30, 41, 59, 0.5); border-radius: 12px; padding: 1rem; 
                        margin-bottom: 1rem; border: 1px solid #334155; text-align: center;'>
                <img src='{item["url"]}' style='width: 100%; height: 300px; object-fit: cover; 
                     border-radius: 8px; margin-bottom: 0.5rem;' />
                <h4 style='color: #f1f5f9; margin: 0.5rem 0; font-size: 1rem;'>{item["name"]}</h4>
                <p style='color: #6366f1; font-size: 1.1rem; font-weight: 600; margin: 0;'>{item["price"]}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Back to Home
st.sidebar.markdown("---")
if st.sidebar.button("🏠 Back to Home"):
    st.switch_page("app.py")

