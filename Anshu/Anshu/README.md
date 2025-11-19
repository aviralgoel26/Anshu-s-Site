# StyleNest Business Intelligence Dashboard

A comprehensive Python + Streamlit web application for Business Intelligence dashboards with role-based insights for StyleNest company.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd StyleNest_BI
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas plotly
   ```

   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 📊 Features

- **4 Role-Based Dashboards**:
  - 👔 CEO Dashboard - Executive overview
  - 📱 Marketing Dashboard - Campaign analytics
  - 📦 Inventory Dashboard - Stock management
  - 💰 Sales Dashboard - Sales performance

- **Interactive Visualizations**: Plotly charts with hover effects
- **Modern UI**: Dark theme with neon accents
- **Real-Time KPIs**: Key performance indicators for each role
- **Responsive Design**: Works on desktop and tablet

## 📁 Project Structure

```
StyleNest_BI/
├── app.py                          # Main application
├── pages/                          # Dashboard pages
│   ├── 1_CEO_Dashboard.py
│   ├── 2_Marketing_Dashboard.py
│   ├── 3_Inventory_Dashboard.py
│   └── 4_Sales_Dashboard.py
├── data/                           # Mock JSON data
│   ├── sales.json
│   ├── marketing.json
│   ├── inventory.json
│   └── customers.json
├── assets/                         # Static assets
├── styles.css                      # Custom CSS
├── wireframes.md                   # ASCII wireframes
├── documentation.md                # Full documentation
└── README.md                       # This file
```

## 🎯 Usage

1. **Select Your Role**: Use the sidebar to choose your role (CEO, Marketing Manager, Inventory Manager, or Sales Executive)
2. **View Dashboard**: The app automatically navigates to your role-specific dashboard
3. **Interact with Charts**: Hover over charts for detailed information
4. **Navigate**: Use the "Back to Home" button to return to the main page

## 📈 Dashboard Metrics

### CEO Dashboard
- Total Revenue: $1.2M
- Profit Margin: 18%
- Total Orders: 24K
- Customer Satisfaction: 88%

### Marketing Dashboard
- Website Visits: 150K
- Conversion Rate: 3.5%
- Ad Spend: $8K
- Best Campaign: "Discount July"

### Inventory Dashboard
- Stock Available: 30K units
- Out of Stock Items: 15
- Inventory Turnover Ratio: 5.2
- Supplier Performance Score: 78/100

### Sales Dashboard
- Daily Sales: $2.3K
- Units Sold: 150
- New Customers: 12
- Avg Order Value: $47

## 🛠️ Technology Stack

- **Python 3.x**: Backend programming
- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive charts
- **JSON**: Data storage

## 📚 Documentation

- **Full Documentation**: See `documentation.md` for complete project documentation
- **Wireframes**: See `wireframes.md` for ASCII-based design wireframes

## 🐛 Troubleshooting

**Module not found error**: 
```bash
pip install streamlit pandas plotly
```

**Port already in use**: 
Streamlit will automatically use the next available port, or specify:
```bash
streamlit run app.py --server.port 8502
```

**JSON file not found**: 
Ensure all JSON files are in the `data/` folder

## 📝 License

This project is created for educational purposes (CA2 Assignment).

## 👨‍💻 Author

StyleNest BI Development Team

---

**For detailed documentation, please refer to `documentation.md`**


