# 🚀 Quick Start Guide

## 💻 Running Locally (5 Minutes)

### Windows Users

1. **Open Command Prompt** in the project directory
2. **Run the setup script**:
   ```bash
   setup.bat
   ```
3. **Start the app**:
   ```bash
   streamlit run main.py
   ```
4. **Open in browser**: http://localhost:8501

### Mac/Linux Users

1. **Open Terminal** in the project directory
2. **Run the setup script**:
   ```bash
   bash setup.sh
   ```
3. **Start the app**:
   ```bash
   streamlit run main.py
   ```
4. **Open in browser**: http://localhost:8501

### Manual Setup (All Platforms)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
```

---

## ☁️ Deploying to Streamlit Cloud (5 Minutes)

### Step 1: Push Code to GitHub
```bash
git add .
git commit -m "Deploy Lauki Finance to Streamlit Cloud"
git push origin main
```

### Step 2: Go to Streamlit Cloud
1. Visit https://streamlit.io/cloud
2. Click "New app"
3. Connect your GitHub repository
4. Select `AmreshKumar15/CREDIT-CARD-RISK-MODELLING`
5. Leave default settings and click "Deploy"

### Step 3: Share Your Live App
Your app will be live at:
```
https://<your-github-username>-creditcardriskmodelingapp.streamlit.app
```

---

## 📚 Navigation Guide

### 🏠 Dashboard
- Overview of platform capabilities
- Key statistics and metrics
- Quick start instructions

### 📈 Risk Predictor
- **Main Feature**: Calculate credit risk
- Enter customer information (age, income, residence)
- Enter loan details (amount, tenure, purpose)
- Enter credit profile data
- Click "Calculate Risk" button
- Get detailed results with:
  - Default probability gauge
  - Credit score gauge
  - Risk rating (Low/Medium/High)
  - Detailed risk analysis
  - Recommendations

### 📊 Analytics
- System-wide statistics
- Risk distribution charts
- Model performance metrics
- System health indicators

### ℹ️ About
- Information about Lauki Finance
- Technology stack
- Model details and performance
- Contact information

---

## 🎯 Example Prediction

### Input:
- Age: 35
- Income: ₹1,200,000
- Residence: Owned
- Loan Amount: ₹2,560,000
- Loan Tenure: 36 months
- Credit Utilization: 30%
- Delinquency Ratio: 10%
- Open Accounts: 2

### Output:
- 🟢 Low Risk (28%)
- Credit Score: 698
- ✅ APPROVED

---

## ❓ Common Questions

**Q: Can I run this on Windows?**
A: Yes! Use `setup.bat` script

**Q: What if port 8501 is already in use?**
A: Run `streamlit run main.py --server.port 8502`

**Q: How do I update my deployed app?**
A: Just push to GitHub, it auto-deploys!

**Q: Can I customize the colors?**
A: Yes! Edit `.streamlit/config.toml`

**Q: Is my data secure?**
A: Yes! Data is processed locally, not stored.

---

## 🔧 Troubleshooting

### App doesn't start
```bash
pip install --upgrade streamlit
streamlit run main.py
```

### Import errors
```bash
pip install -r requirements.txt --force-reinstall
```

### Clear Streamlit cache
```bash
streamlit cache clear
```

---

## 📞 Need Help?

- **Documentation**: Read README.md and DEPLOYMENT_GUIDE.md
- **Streamlit Docs**: https://docs.streamlit.io
- **GitHub Issues**: Check project GitHub issues
- **Community**: https://discuss.streamlit.io

---

## ✅ Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] App runs locally
- [ ] Code pushed to GitHub
- [ ] App deployed on Streamlit Cloud
- [ ] Live URL tested and working

---

**You're all set! 🎉 Enjoy your credit risk modelling application!**
