"""
Marketing Manager Dashboard
Displays marketing analytics, campaign performance, and social media insights
"""

import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Marketing Dashboard - StyleNest BI",
    page_icon="📱",
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
    data_path = Path(__file__).parent.parent / "data" / "marketing.json"
    with open(data_path, "r") as f:
        return json.load(f)

data = load_data()

# Header
st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 2rem;'>
        <h1 style='font-size: 2.5rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;'>
            📱 Marketing Manager Dashboard
        </h1>
        <p style='color: #94a3b8; font-size: 1rem;'>Digital Marketing Analytics & Campaign Performance</p>
    </div>
""", unsafe_allow_html=True)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Website Visits</div>
            <div class='kpi-value'>{data['website_visits']/1000:.0f}K</div>
            <div class='kpi-change positive'>↑ 15% vs last month</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Conversion Rate</div>
            <div class='kpi-value'>{data['conversion_rate']}%</div>
            <div class='kpi-change positive'>↑ 0.5% improvement</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Ad Spend</div>
            <div class='kpi-value'>${data['ad_spend']/1000:.1f}K</div>
            <div class='kpi-change'>Within budget</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>Best Campaign</div>
            <div class='kpi-value' style='font-size: 1.2rem;'>{data['best_campaign']}</div>
            <div class='kpi-change positive'>Top performer</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts Section
col1, col2 = st.columns(2)

# Social Media Engagement - Bar Chart
with col1:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Social Media Engagement</div>", unsafe_allow_html=True)
    
    social_df = pd.DataFrame(data['social_media_engagement'])
    fig = px.bar(
        social_df,
        x='platform',
        y='engagement',
        title="",
        labels={'engagement': 'Engagement', 'platform': 'Platform'},
        color='engagement',
        color_continuous_scale='plasma',
        text='engagement'
    )
    fig.update_traces(texttemplate='%{text:,}', textposition='outside')
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

# Campaign ROI - Line Chart
with col2:
    st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
    st.markdown("<div class='chart-title'>Campaign ROI</div>", unsafe_allow_html=True)
    
    campaign_df = pd.DataFrame(data['campaign_roi'])
    fig = px.line(
        campaign_df,
        x='campaign',
        y='roi',
        markers=True,
        title="",
        labels={'roi': 'ROI (%)', 'campaign': 'Campaign'},
        text='roi'
    )
    fig.update_traces(
        line_color='#8b5cf6',
        marker_color='#ec4899',
        line_width=3,
        texttemplate='%{text:.0f}%',
        textposition='top center'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#94a3b8',
        xaxis=dict(gridcolor='#334155', tickangle=-45),
        yaxis=dict(gridcolor='#334155'),
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Customer Demographics - Pie Chart (Full Width)
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Customer Demographics</div>", unsafe_allow_html=True)

demo_df = pd.DataFrame(data['customer_demographics'])
fig = px.pie(
    demo_df,
    values='percentage',
    names='age_group',
    title="",
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.Viridis
)
fig.update_traces(
    textposition='inside',
    textinfo='percent+label',
    hovertemplate='<b>%{label}</b><br>Percentage: %{percent}<br>Count: %{customdata}<extra></extra>',
    customdata=demo_df['count']
)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#94a3b8',
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Additional Metrics Table
st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
st.markdown("<div class='chart-title'>Campaign Performance Details</div>", unsafe_allow_html=True)

campaign_df = pd.DataFrame(data['campaign_roi'])
campaign_df['ROI %'] = campaign_df['roi']
campaign_df['Spend ($)'] = campaign_df['spend']
campaign_df['Revenue ($)'] = campaign_df['revenue']
display_df = campaign_df[['campaign', 'Spend ($)', 'Revenue ($)', 'ROI %']]
st.dataframe(display_df, use_container_width=True, hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

# Back to Home
st.sidebar.markdown("---")
if st.sidebar.button("🏠 Back to Home"):
    st.switch_page("app.py")

