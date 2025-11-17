# StyleNest Business Intelligence Dashboard
## Complete Documentation

---

## Cover Page

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    STYLENEST BUSINESS INTELLIGENCE                        ║
║                         DASHBOARD SYSTEM                                  ║
║                                                                           ║
║                    A Comprehensive BI Platform for                        ║
║                    Role-Based Analytics & Insights                        ║
║                                                                           ║
║                                                                           ║
║                              CA2 Project                                  ║
║                                                                           ║
║                         Python + Streamlit                                ║
║                                                                           ║
║                                                                           ║
║                             2024                                          ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Technology Stack](#3-technology-stack)
4. [System Architecture](#4-system-architecture)
5. [Role-Based Dashboards](#5-role-based-dashboards)
6. [BI Feature–Role Mapping](#6-bi-featurerole-mapping)
7. [Data Structure](#7-data-structure)
8. [User Interface Design](#8-user-interface-design)
9. [Installation & Setup](#9-installation--setup)
10. [How to Run the Project](#10-how-to-run-the-project)
11. [Screenshots](#11-screenshots)
12. [Conclusion](#12-conclusion)
13. [References](#13-references)

---

## 1. Introduction

### 1.1 Purpose

The StyleNest Business Intelligence Dashboard is a comprehensive web-based analytics platform designed to provide role-based insights and real-time business metrics for different stakeholders within the StyleNest organization. This application enables executives, managers, and sales teams to make data-driven decisions through interactive dashboards, visualizations, and KPI tracking.

### 1.2 Objectives

- **Centralized Analytics**: Provide a single platform for all business intelligence needs
- **Role-Based Access**: Deliver customized dashboards for different organizational roles
- **Real-Time Insights**: Display up-to-date metrics and trends
- **User-Friendly Interface**: Create an intuitive and visually appealing UI/UX
- **Scalable Architecture**: Design a modular system that can be extended easily

### 1.3 Scope

This project includes:
- Four role-specific dashboards (CEO, Marketing Manager, Inventory Manager, Sales Executive)
- Interactive data visualizations using Plotly
- Mock data stored in JSON format
- Custom CSS styling for modern UI
- Complete documentation and wireframes

---

## 2. Project Overview

### 2.1 Company Background

StyleNest is a modern e-commerce company specializing in electronics, clothing, home & living products, and accessories. The company operates across multiple regions and requires comprehensive business intelligence tools to track performance, optimize operations, and drive growth.

### 2.2 Project Goals

1. **Executive Visibility**: Provide C-level executives with high-level strategic metrics
2. **Marketing Optimization**: Enable marketing teams to track campaign performance and ROI
3. **Inventory Management**: Help inventory managers monitor stock levels and supplier performance
4. **Sales Analytics**: Empower sales teams with regional and product performance data

### 2.3 Key Features

- **Interactive Dashboards**: Real-time data visualization with Plotly charts
- **KPI Tracking**: Key performance indicators for each role
- **Multi-Chart Support**: Line charts, bar charts, pie charts, and combined visualizations
- **Responsive Design**: Works on desktop and tablet devices
- **Dark Theme UI**: Modern, professional appearance with neon accents

---

## 3. Technology Stack

### 3.1 Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.x | Backend programming language |
| Streamlit | Latest | Web framework for dashboard UI |
| Pandas | Latest | Data manipulation and analysis |
| Plotly | Latest | Interactive chart generation |
| JSON | Built-in | Data storage format |

### 3.2 Development Tools

- **IDE**: Any Python-compatible IDE (VS Code, PyCharm, etc.)
- **Version Control**: Git (optional)
- **Package Manager**: pip

### 3.3 Dependencies

```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
```

---

## 4. System Architecture

### 4.1 Project Structure

```
StyleNest_BI/
│
├── app.py                          # Main application entry point
│
├── pages/                          # Dashboard pages
│   ├── 1_CEO_Dashboard.py         # CEO executive dashboard
│   ├── 2_Marketing_Dashboard.py    # Marketing analytics dashboard
│   ├── 3_Inventory_Dashboard.py   # Inventory management dashboard
│   └── 4_Sales_Dashboard.py       # Sales performance dashboard
│
├── data/                           # Mock data storage
│   ├── sales.json                  # Sales and revenue data
│   ├── marketing.json              # Marketing and campaign data
│   ├── inventory.json              # Inventory and stock data
│   └── customers.json              # Customer analytics data
│
├── assets/                         # Static assets
│   └── logo.png                    # Company logo (placeholder)
│
├── styles.css                      # Custom CSS styling
│
├── wireframes.md                   # ASCII wireframe designs
│
├── documentation.md                # This documentation file
│
└── README.md                       # Quick start guide
```

### 4.2 Data Flow

```
JSON Data Files → Pandas DataFrame → Plotly Charts → Streamlit UI
```

### 4.3 Component Architecture

1. **Main App (app.py)**: Entry point with role selection
2. **Dashboard Pages**: Individual pages for each role
3. **Data Layer**: JSON files containing mock business data
4. **Presentation Layer**: Streamlit UI with custom CSS
5. **Visualization Layer**: Plotly charts for data representation

---

## 5. Role-Based Dashboards

### 5.1 CEO Dashboard

**Purpose**: Provide executive-level overview of business performance

**Key Metrics**:
- **Total Revenue**: $1.2M (with 12% growth indicator)
- **Profit Margin**: 18% (with 2.5% improvement)
- **Total Orders**: 24K (with 8% growth)
- **Customer Satisfaction**: 88% (with 3% improvement)

**Visualizations**:
1. **Monthly Sales Trend**: Line chart showing revenue progression over 12 months
2. **Category-wise Revenue**: Bar chart displaying revenue by product category
3. **Regional Customer Growth**: Combined bar and line chart showing customer base and growth percentage by region

**Use Cases**:
- Strategic planning and decision-making
- Board meeting presentations
- Performance reviews
- Market expansion analysis

---

### 5.2 Marketing Manager Dashboard

**Purpose**: Track digital marketing performance and campaign effectiveness

**Key Metrics**:
- **Website Visits**: 150K (with 15% increase)
- **Conversion Rate**: 3.5% (with 0.5% improvement)
- **Ad Spend**: $8K (within budget)
- **Best Campaign**: "Discount July" (top performer)

**Visualizations**:
1. **Social Media Engagement**: Bar chart comparing engagement across platforms (Facebook, Instagram, Twitter, LinkedIn, TikTok)
2. **Campaign ROI**: Line chart showing return on investment for different marketing campaigns
3. **Customer Demographics**: Pie chart displaying age group distribution

**Additional Features**:
- Campaign performance details table
- Monthly website visits trend

**Use Cases**:
- Campaign optimization
- Budget allocation
- Social media strategy
- Target audience analysis

---

### 5.3 Inventory Manager Dashboard

**Purpose**: Monitor stock levels, turnover, and supplier performance

**Key Metrics**:
- **Stock Available**: 30K units
- **Out of Stock Items**: 15 (needs attention)
- **Inventory Turnover Ratio**: 5.2 (healthy ratio)
- **Supplier Performance Score**: 78/100 (good performance)

**Visualizations**:
1. **Category-wise Stock Levels**: Grouped bar chart showing current stock vs. reorder thresholds
2. **Supplier Performance Comparison**: Bar chart ranking suppliers by total performance score
3. **Top 10 Selling Products**: Data table with stock status indicators

**Additional Features**:
- Low stock alerts table
- Product status indicators (In Stock, Low Stock, Out of Stock)

**Use Cases**:
- Stock replenishment planning
- Supplier relationship management
- Inventory optimization
- Demand forecasting

---

### 5.4 Sales Executive Dashboard

**Purpose**: Track daily sales performance and regional/product analytics

**Key Metrics**:
- **Daily Sales**: $2.3K (with 5% increase)
- **Units Sold**: 150 (with 8% growth)
- **New Customers**: 12 (today's acquisition)
- **Average Order Value**: $47 (with $2 increase)

**Visualizations**:
1. **Daily Sales Trend**: Combined line and bar chart showing sales and units sold over 7 days
2. **Region-wise Sales**: Bar chart comparing sales performance across regions
3. **Product Performance**: Combined bar and line chart showing top products by sales and units

**Additional Features**:
- Product sales details table
- Weekly/monthly trend analysis

**Use Cases**:
- Sales target tracking
- Regional performance analysis
- Product mix optimization
- Customer acquisition monitoring

---

## 6. BI Feature–Role Mapping

| BI Feature | CEO | Marketing Manager | Inventory Manager | Sales Executive |
|------------|-----|-------------------|-------------------|-----------------|
| **Revenue Metrics** | ✅ | ❌ | ❌ | ✅ |
| **Profit Analysis** | ✅ | ❌ | ❌ | ❌ |
| **Order Tracking** | ✅ | ❌ | ❌ | ✅ |
| **Customer Satisfaction** | ✅ | ✅ | ❌ | ✅ |
| **Website Analytics** | ❌ | ✅ | ❌ | ❌ |
| **Conversion Rate** | ❌ | ✅ | ❌ | ❌ |
| **Campaign Performance** | ❌ | ✅ | ❌ | ❌ |
| **Social Media Metrics** | ❌ | ✅ | ❌ | ❌ |
| **Stock Levels** | ❌ | ❌ | ✅ | ❌ |
| **Inventory Turnover** | ❌ | ❌ | ✅ | ❌ |
| **Supplier Performance** | ❌ | ❌ | ✅ | ❌ |
| **Product Stock Status** | ❌ | ❌ | ✅ | ❌ |
| **Daily Sales Trends** | ❌ | ❌ | ❌ | ✅ |
| **Regional Sales** | ✅ | ❌ | ❌ | ✅ |
| **Product Performance** | ✅ | ❌ | ✅ | ✅ |
| **Customer Demographics** | ❌ | ✅ | ❌ | ❌ |
| **Customer Acquisition** | ❌ | ❌ | ❌ | ✅ |

**Legend**:
- ✅ = Feature Available
- ❌ = Feature Not Available

---

## 7. Data Structure

### 7.1 Sales Data (sales.json)

```json
{
  "total_revenue": 1200000,
  "profit_margin": 18,
  "total_orders": 24000,
  "customer_satisfaction": 88,
  "monthly_sales": [...],
  "category_revenue": [...],
  "regional_growth": [...],
  "daily_sales": [...],
  "region_sales": [...],
  "product_performance": [...]
}
```

### 7.2 Marketing Data (marketing.json)

```json
{
  "website_visits": 150000,
  "conversion_rate": 3.5,
  "ad_spend": 8000,
  "best_campaign": "Discount July",
  "social_media_engagement": [...],
  "campaign_roi": [...],
  "customer_demographics": [...],
  "monthly_visits": [...]
}
```

### 7.3 Inventory Data (inventory.json)

```json
{
  "stock_available": 30000,
  "out_of_stock_items": 15,
  "inventory_turnover_ratio": 5.2,
  "supplier_performance_score": 78,
  "category_stock": [...],
  "top_selling_products": [...],
  "supplier_comparison": [...],
  "low_stock_items": [...]
}
```

### 7.4 Customer Data (customers.json)

```json
{
  "total_customers": 24000,
  "new_customers_today": 12,
  "avg_order_value": 47,
  "customer_segments": [...],
  "customer_acquisition": [...],
  "customer_satisfaction_trend": [...]
}
```

---

## 8. User Interface Design

### 8.1 Design Principles

1. **Dark Theme**: Modern dark background (#0f172a) for reduced eye strain
2. **Neon Accents**: Purple (#6366f1), pink (#ec4899) for visual appeal
3. **Card-Based Layout**: KPI cards with soft shadows and rounded corners
4. **Responsive Grid**: 4-column layout for KPIs, 2-column for charts
5. **Typography**: Inter font family for clean, modern look
6. **Interactive Elements**: Hover effects and smooth transitions

### 8.2 Color Palette

- **Primary**: #6366f1 (Indigo)
- **Secondary**: #8b5cf6 (Purple)
- **Accent**: #ec4899 (Pink)
- **Success**: #10b981 (Green)
- **Warning**: #f59e0b (Amber)
- **Danger**: #ef4444 (Red)
- **Background**: #0f172a (Dark Slate)
- **Card Background**: #1e293b (Slate)
- **Text Primary**: #f1f5f9 (Slate Light)
- **Text Secondary**: #94a3b8 (Slate)

### 8.3 UI Components

1. **KPI Cards**: Gradient borders, neon glow effects, trend indicators
2. **Chart Containers**: Rounded corners, subtle borders, dark theme
3. **Navigation Sidebar**: Role selection with radio buttons
4. **Data Tables**: Styled with status indicators and color coding

---

## 9. Installation & Setup

### 9.1 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for initial package installation)

### 9.2 Installation Steps

1. **Clone or Download the Project**
   ```bash
   # Navigate to project directory
   cd StyleNest_BI
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install streamlit pandas plotly
   ```

   Or create a `requirements.txt` file:
   ```
   streamlit>=1.28.0
   pandas>=2.0.0
   plotly>=5.17.0
   ```
   
   Then install:
   ```bash
   pip install -r requirements.txt
   ```

---

## 10. How to Run the Project

### 10.1 Running the Application

1. **Navigate to Project Directory**
   ```bash
   cd StyleNest_BI
   ```

2. **Start Streamlit Server**
   ```bash
   streamlit run app.py
   ```

3. **Access the Dashboard**
   - The application will automatically open in your default web browser
   - Default URL: `http://localhost:8501`
   - If it doesn't open automatically, copy the URL from the terminal

### 10.2 Using the Dashboard

1. **Select Your Role**: Use the sidebar radio buttons to choose your role
2. **Navigate Dashboards**: The app will automatically switch to the selected dashboard
3. **Interact with Charts**: Hover over charts for detailed information
4. **View Metrics**: KPI cards display key metrics with trend indicators
5. **Back to Home**: Use the "Back to Home" button in the sidebar

### 10.3 Troubleshooting

**Issue**: Module not found error
- **Solution**: Ensure all dependencies are installed: `pip install streamlit pandas plotly`

**Issue**: Port already in use
- **Solution**: Streamlit will automatically use the next available port, or specify: `streamlit run app.py --server.port 8502`

**Issue**: JSON file not found
- **Solution**: Ensure all JSON files are in the `data/` folder and the folder structure matches the project structure

**Issue**: CSS not loading
- **Solution**: Ensure `styles.css` is in the root directory alongside `app.py`

---

## 11. Screenshots

### 11.1 Screenshot Placeholders

*Note: In a real deployment, actual screenshots would be inserted here*

#### 11.1.1 Homepage
```
[Screenshot: Homepage with role selection sidebar and welcome message]
- Location: app.py
- Description: Main entry point with role selection interface
```

#### 11.1.2 CEO Dashboard
```
[Screenshot: CEO Dashboard showing 4 KPI cards and 3 charts]
- Location: pages/1_CEO_Dashboard.py
- Description: Executive overview with revenue, profit, orders, and customer metrics
```

#### 11.1.3 Marketing Dashboard
```
[Screenshot: Marketing Dashboard with website visits, conversion rate, and campaign analytics]
- Location: pages/2_Marketing_Dashboard.py
- Description: Marketing metrics, social media engagement, and campaign ROI
```

#### 11.1.4 Inventory Dashboard
```
[Screenshot: Inventory Dashboard displaying stock levels, supplier performance, and product status]
- Location: pages/3_Inventory_Dashboard.py
- Description: Inventory management with stock alerts and supplier analytics
```

#### 11.1.5 Sales Dashboard
```
[Screenshot: Sales Dashboard showing daily sales, regional performance, and product analytics]
- Location: pages/4_Sales_Dashboard.py
- Description: Sales executive view with trends and regional breakdowns
```

---

## 12. Conclusion

### 12.1 Project Summary

The StyleNest Business Intelligence Dashboard successfully delivers a comprehensive analytics platform that addresses the diverse needs of different organizational roles. The application provides:

- **Executive Visibility**: High-level strategic metrics for C-level decision-making
- **Marketing Insights**: Campaign performance and digital marketing analytics
- **Inventory Control**: Stock management and supplier performance tracking
- **Sales Analytics**: Regional and product performance monitoring

### 12.2 Key Achievements

1. ✅ **Complete Role-Based Dashboards**: Four fully functional dashboards with role-specific metrics
2. ✅ **Interactive Visualizations**: Plotly charts with hover effects and dynamic data
3. ✅ **Modern UI/UX**: Dark theme with neon accents and professional styling
4. ✅ **Modular Architecture**: Easy to extend and maintain
5. ✅ **Comprehensive Documentation**: Complete documentation and wireframes

### 12.3 Future Enhancements

Potential improvements for future iterations:

1. **Database Integration**: Replace JSON files with a real database (PostgreSQL, MySQL)
2. **User Authentication**: Add login system with role-based access control
3. **Real-Time Data**: Connect to live APIs or data streams
4. **Export Functionality**: Allow users to export reports as PDF or Excel
5. **Advanced Filtering**: Date range selectors and custom filters
6. **Alerts & Notifications**: Automated alerts for critical metrics
7. **Mobile Responsiveness**: Optimize for mobile devices
8. **Data Refresh**: Automatic data refresh at intervals
9. **Custom Dashboards**: Allow users to create custom dashboard layouts
10. **Historical Comparisons**: Year-over-year and period-over-period comparisons

### 12.4 Learning Outcomes

This project demonstrates:

- **Streamlit Proficiency**: Building multi-page web applications
- **Data Visualization**: Creating interactive charts with Plotly
- **UI/UX Design**: Implementing modern, professional interfaces
- **Data Management**: Working with JSON data structures
- **Python Programming**: Modular code organization and best practices
- **Documentation**: Creating comprehensive technical documentation

---

## 13. References

### 13.1 Technologies

- **Streamlit Documentation**: https://docs.streamlit.io/
- **Plotly Documentation**: https://plotly.com/python/
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Python Documentation**: https://docs.python.org/3/

### 13.2 Design Resources

- **Color Palette**: Tailwind CSS color system
- **Typography**: Google Fonts - Inter
- **Icons**: Emoji icons (native support)

### 13.3 Best Practices

- **Streamlit Best Practices**: https://docs.streamlit.io/library/advanced-features
- **Python PEP 8**: Code style guidelines
- **Data Visualization Best Practices**: Tufte's principles of information design

---

## Appendix A: File Structure Details

### A.1 Main Application Files

- **app.py**: Main entry point, handles routing and role selection
- **styles.css**: Custom CSS for UI styling

### A.2 Dashboard Pages

- **1_CEO_Dashboard.py**: CEO executive dashboard
- **2_Marketing_Dashboard.py**: Marketing analytics dashboard
- **3_Inventory_Dashboard.py**: Inventory management dashboard
- **4_Sales_Dashboard.py**: Sales performance dashboard

### A.3 Data Files

- **sales.json**: Sales, revenue, and order data
- **marketing.json**: Marketing and campaign data
- **inventory.json**: Inventory and supplier data
- **customers.json**: Customer analytics data

---

## Appendix B: Code Examples

### B.1 Loading Data

```python
@st.cache_data
def load_data():
    data_path = Path(__file__).parent.parent / "data" / "sales.json"
    with open(data_path, "r") as f:
        return json.load(f)
```

### B.2 Creating a KPI Card

```python
st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-label'>Total Revenue</div>
        <div class='kpi-value'>${data['total_revenue']/1000:.1f}K</div>
        <div class='kpi-change positive'>↑ 12% vs last month</div>
    </div>
""", unsafe_allow_html=True)
```

### B.3 Creating a Plotly Chart

```python
fig = px.line(
    monthly_df, 
    x='month', 
    y='revenue',
    markers=True
)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#94a3b8'
)
st.plotly_chart(fig, use_container_width=True)
```

---

**End of Documentation**

*StyleNest BI Dashboard - Complete Documentation v1.0*

