"""
StyleNest BI Dashboard - Main Application
A comprehensive Business Intelligence dashboard for StyleNest company
"""

import streamlit as st
import json
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="StyleNest BI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    css_path = Path(__file__).parent / "styles.css"
    if css_path.exists():
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if 'selected_role' not in st.session_state:
    st.session_state.selected_role = "CEO"

# Load CSS
load_css()

# Header
st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='font-size: 3rem; font-weight: 700; background: linear-gradient(135deg, #6366f1, #ec4899); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;'>
            📊 StyleNest BI Dashboard
        </h1>
        <p style='color: #94a3b8; font-size: 1.1rem;'>Business Intelligence & Analytics Platform</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem 0; margin-bottom: 2rem;'>
        <h2 style='color: #6366f1; font-size: 1.5rem; font-weight: 700;'>StyleNest</h2>
        <p style='color: #94a3b8; font-size: 0.9rem;'>Business Intelligence</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Role Selection
st.sidebar.markdown("### 🎯 Select Your Role")
role = st.sidebar.radio(
    "Dashboard Access",
    ["CEO", "Marketing Manager", "Inventory Manager", "Sales Executive", "Customers"],
    index=0,
    label_visibility="collapsed"
)

# Store selected role in session state
st.session_state.selected_role = role

# Navigation buttons
st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 Navigate to Dashboard")

# Navigation based on role
if st.sidebar.button("Go to Dashboard", type="primary", use_container_width=True):
    if role == "CEO":
        st.switch_page("pages/1_CEO_Dashboard.py")
    elif role == "Marketing Manager":
        st.switch_page("pages/2_Marketing_Dashboard.py")
    elif role == "Inventory Manager":
        st.switch_page("pages/3_Inventory_Dashboard.py")
    elif role == "Sales Executive":
        st.switch_page("pages/4_Sales_Dashboard.py")
    elif role == "Customers":
        st.switch_page("pages/5_Customers_Dashboard.py")

# Home Page Content
st.markdown("""
    <div style='max-width: 800px; margin: 3rem auto; padding: 2rem; 
                background: rgba(30, 41, 59, 0.5); border-radius: 16px; border: 1px solid #334155;'>
        <h2 style='color: #f1f5f9; margin-bottom: 1rem;'>Welcome to StyleNest BI Dashboard</h2>
        <p style='color: #94a3b8; line-height: 1.8; margin-bottom: 1.5rem;'>
            This comprehensive Business Intelligence platform provides role-based insights 
            for different stakeholders in the organization. Select your role from the sidebar 
            to access your personalized dashboard.
        </p>
        <h3 style='color: #f1f5f9; margin-top: 2rem; margin-bottom: 1rem;'>Available Dashboards:</h3>
        <ul style='color: #94a3b8; line-height: 2;'>
            <li><strong style='color: #6366f1;'>CEO Dashboard:</strong> Executive overview with revenue, profit, orders, and customer satisfaction metrics</li>
            <li><strong style='color: #8b5cf6;'>Marketing Dashboard:</strong> Website analytics, campaign performance, and social media engagement</li>
            <li><strong style='color: #ec4899;'>Inventory Dashboard:</strong> Stock levels, turnover ratios, and supplier performance</li>
            <li><strong style='color: #10b981;'>Sales Dashboard:</strong> Daily sales trends, regional performance, and product analytics</li>
            <li><strong style='color: #f59e0b;'>Customers Dashboard:</strong> Customer insights, segments, satisfaction trends, and product showcase</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; margin-top: 3rem; border-top: 1px solid #334155;'>
        <p style='color: #94a3b8; font-size: 0.9rem;'>StyleNest Business Intelligence Platform © 2024</p>
    </div>
""", unsafe_allow_html=True)

