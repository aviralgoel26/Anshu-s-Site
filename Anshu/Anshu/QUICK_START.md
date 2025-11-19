# Quick Start Guide - StyleNest BI Dashboard

## 🚀 Running the Application

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

### Step 3: Access Dashboard
- The app will open automatically in your browser
- Default URL: `http://localhost:8501`

## 📋 Using the Dashboard

1. **Home Page**: Select your role from the sidebar
2. **Navigate**: Click "Go to Dashboard" button to view your role-specific dashboard
3. **Explore**: Interact with charts by hovering over data points
4. **Return**: Use "Back to Home" button in any dashboard to return

## 📊 Dashboard Access

- **CEO**: Select "CEO" → Click "Go to Dashboard"
- **Marketing Manager**: Select "Marketing Manager" → Click "Go to Dashboard"
- **Inventory Manager**: Select "Inventory Manager" → Click "Go to Dashboard"
- **Sales Executive**: Select "Sales Executive" → Click "Go to Dashboard"

## ✅ Verification Checklist

- [x] All dependencies installed
- [x] JSON data files present in `data/` folder
- [x] CSS file (`styles.css`) in root directory
- [x] All dashboard pages in `pages/` folder
- [x] Application runs without errors

## 🐛 Common Issues

**Issue**: ModuleNotFoundError
- **Fix**: Run `pip install streamlit pandas plotly`

**Issue**: FileNotFoundError for JSON files
- **Fix**: Ensure `data/` folder contains all 4 JSON files

**Issue**: CSS not loading
- **Fix**: Ensure `styles.css` is in the same directory as `app.py`

## 📚 Documentation

- Full documentation: `documentation.md`
- Wireframes: `wireframes.md`
- README: `README.md`

---

**Happy Analyzing! 📊**


