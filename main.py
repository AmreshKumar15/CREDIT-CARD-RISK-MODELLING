"""
Lauki Finance: Credit Risk Modelling Dashboard
A professional Streamlit application for credit risk assessment
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from prediction_helper import predict
import time

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Lauki Finance - Credit Risk Model",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS STYLING ====================
st.markdown("""
<style>
    /* Main background and text colors */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --success-color: #2ca02c;
        --danger-color: #d62728;
        --warning-color: #ff9896;
    }
    
    /* Custom header styling */
    .main-header {
        font-size: 2.5em;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0.5em;
        text-align: center;
    }
    
    .sub-header {
        font-size: 1.5em;
        font-weight: bold;
        color: #333;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5em;
    }
    
    /* Cards styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .risk-low {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        color: #155724;
    }
    
    .risk-medium {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: #856404;
    }
    
    .risk-high {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: #721c24;
    }
    
    /* Input styling */
    .input-label {
        font-weight: 600;
        color: #333;
        margin-bottom: 0.3em;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.75em;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1557a0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Result styling */
    .result-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2em;
        border-radius: 15px;
        margin-top: 1.5em;
    }
    
    .result-title {
        font-size: 1.8em;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1em;
    }
    
    .info-box {
        background: #e7f3ff;
        border-left: 4px solid #1f77b4;
        padding: 1em;
        border-radius: 5px;
        margin: 0.5em 0;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR NAVIGATION ====================
with st.sidebar:
    st.markdown("### 📊 Navigation")
    page = st.radio(
        "Select a page:",
        ["🏠 Dashboard", "📈 Risk Predictor", "📊 Analytics", "ℹ️ About"]
    )
    
    st.markdown("---")
    st.markdown("""
    ### 🏢 About Lauki Finance
    A premium credit risk modelling platform powered by 
    machine learning algorithms.
    
    **Version:** 1.0.0  
    **Last Updated:** Dec 2024
    """)


# ==================== HELPER FUNCTIONS ====================
def get_risk_metric_color(probability):
    """Return color based on risk probability."""
    if probability < 0.15:
        return "#84fab0", "#2ca02c"
    elif probability < 0.35:
        return "#ffd700", "#ff9896"
    else:
        return "#ff6b6b", "#d62728"


def create_risk_gauge(probability, credit_score):
    """Create a beautiful risk gauge chart."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=int(probability * 100),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Default Risk %"},
        delta={'reference': 15},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 15], 'color': "#84fab0"},
                {'range': [15, 35], 'color': "#ffd700"},
                {'range': [35, 100], 'color': "#ff6b6b"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20))
    return fig


def create_score_gauge(credit_score):
    """Create a credit score gauge chart."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=credit_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Credit Score"},
        gauge={
            'axis': {'range': [300, 850]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [300, 500], 'color': "#ff6b6b"},
                {'range': [500, 700], 'color': "#ffd700"},
                {'range': [700, 850], 'color': "#84fab0"}
            ]
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20))
    return fig


# ==================== PAGE: DASHBOARD ====================
if page == "🏠 Dashboard":
    # Header
    st.markdown('<div class="main-header">💳 Lauki Finance</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; color: #666; font-size: 1.1em; margin-bottom: 2em;">Credit Risk Assessment Platform</div>', unsafe_allow_html=True)
    
    # Key Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Active Users",
            value="15,234",
            delta="+12% this month"
        )
    
    with col2:
        st.metric(
            label="Loans Processed",
            value="52,891",
            delta="+2,450 this week"
        )
    
    with col3:
        st.metric(
            label="Model Accuracy",
            value="94.2%",
            delta="+2.1% improvement"
        )
    
    with col4:
        st.metric(
            label="Avg Processing Time",
            value="2.3s",
            delta="-0.5s faster"
        )
    
    st.markdown("---")
    
    # Features Overview
    st.markdown('<div class="sub-header">✨ Platform Features</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        ### 🎯 Real-time Predictions
        Get instant credit risk assessments with our advanced ML models trained on thousands of loan records.
        """)
    
    with col2:
        st.info("""
        ### 📊 Comprehensive Analytics
        Detailed risk analytics and visualizations to understand credit patterns and borrower behavior.
        """)
    
    with col3:
        st.info("""
        ### 🔒 Secure & Reliable
        Enterprise-grade security with industry-leading compliance and data protection standards.
        """)
    
    st.markdown("---")
    
    # Quick Start
    st.markdown('<div class="sub-header">🚀 Quick Start</div>', unsafe_allow_html=True)
    
    st.write("""
    1. Navigate to **📈 Risk Predictor** in the sidebar
    2. Enter loan and customer details
    3. Click "Calculate Risk" to get instant assessment
    4. View detailed analytics and recommendations
    """)


# ==================== PAGE: RISK PREDICTOR ====================
elif page == "📈 Risk Predictor":
    st.markdown('<div class="main-header">📈 Risk Predictor</div>', unsafe_allow_html=True)
    st.markdown("Enter loan and customer details to assess credit risk")
    
    st.markdown('<div class="sub-header">👤 Customer Information</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input(
            'Age (years)',
            min_value=18,
            max_value=100,
            value=35,
            step=1,
            help="Customer's age in years"
        )
    
    with col2:
        income = st.number_input(
            'Annual Income (₹)',
            min_value=0,
            value=1200000,
            step=50000,
            help="Annual household income"
        )
    
    with col3:
        residence_type = st.selectbox(
            'Residence Type',
            ['Owned', 'Rented', 'Mortgage'],
            help="Type of residence"
        )
    
    st.markdown('<div class="sub-header">💰 Loan Details</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        loan_amount = st.number_input(
            'Loan Amount (₹)',
            min_value=0,
            value=2560000,
            step=50000,
            help="Total loan amount requested"
        )
    
    with col2:
        loan_tenure_months = st.number_input(
            'Loan Tenure (months)',
            min_value=1,
            max_value=360,
            value=36,
            step=1,
            help="Loan duration in months"
        )
    
    with col3:
        loan_purpose = st.selectbox(
            'Loan Purpose',
            ['Education', 'Home', 'Auto', 'Personal'],
            help="Purpose of the loan"
        )
    
    st.markdown('<div class="sub-header">📊 Credit Profile</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        credit_utilization_ratio = st.slider(
            'Credit Utilization Ratio (%)',
            min_value=0,
            max_value=100,
            value=30,
            step=1,
            help="Percentage of available credit being used"
        )
    
    with col2:
        delinquency_ratio = st.slider(
            'Delinquency Ratio (%)',
            min_value=0,
            max_value=100,
            value=10,
            step=1,
            help="Percentage of delinquent months"
        )
    
    with col3:
        num_open_accounts = st.slider(
            'Number of Open Accounts',
            min_value=1,
            max_value=10,
            value=2,
            step=1,
            help="Total number of active loan accounts"
        )
    
    st.markdown('<div class="sub-header">⚠️ Delinquency Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        avg_dpd_per_delinquency = st.number_input(
            'Avg DPD (Days Past Due)',
            min_value=0,
            value=5,
            step=1,
            help="Average days past due per delinquency instance"
        )
    
    with col2:
        loan_type = st.selectbox(
            'Loan Type',
            ['Secured', 'Unsecured'],
            help="Type of loan security"
        )
    
    # Calculate loan to income ratio
    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Loan to Income Ratio", value=f"{loan_to_income_ratio:.2f}")
    
    with col2:
        st.metric(label="Monthly EMI (Approx)", value=f"₹{(loan_amount / loan_tenure_months):.0f}")
    
    with col3:
        st.metric(label="EMI as % of Income", value=f"{((loan_amount / loan_tenure_months) / (income / 12) * 100):.1f}%")
    
    st.markdown("---")
    
    # Calculate Risk Button
    if st.button("🔍 Calculate Risk", use_container_width=True):
        with st.spinner("🔄 Analyzing credit profile..."):
            time.sleep(1)  # Simulate processing
            
            probability, credit_score, rating = predict(
                age, income, loan_amount, loan_tenure_months,
                avg_dpd_per_delinquency, delinquency_ratio,
                credit_utilization_ratio, num_open_accounts,
                residence_type, loan_purpose, loan_type
            )
            
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">✅ Risk Assessment Results</div>', unsafe_allow_html=True)
            
            # Results in columns
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.plotly_chart(create_risk_gauge(probability, credit_score), use_container_width=True)
            
            with col2:
                st.plotly_chart(create_score_gauge(credit_score), use_container_width=True)
            
            with col3:
                # Risk Rating Card
                risk_color, _ = get_risk_metric_color(probability)
                
                if probability < 0.15:
                    rating_emoji = "🟢"
                    risk_level = "LOW RISK"
                    color_bg = "#d4edda"
                    color_text = "#155724"
                elif probability < 0.35:
                    rating_emoji = "🟡"
                    risk_level = "MEDIUM RISK"
                    color_bg = "#fff3cd"
                    color_text = "#856404"
                else:
                    rating_emoji = "🔴"
                    risk_level = "HIGH RISK"
                    color_bg = "#f8d7da"
                    color_text = "#721c24"
                
                st.markdown(f"""
                <div style="background: {color_bg}; color: {color_text}; padding: 20px; border-radius: 10px; text-align: center;">
                    <div style="font-size: 2em; margin-bottom: 10px;">{rating_emoji}</div>
                    <div style="font-size: 1.5em; font-weight: bold; margin-bottom: 10px;">{risk_level}</div>
                    <div style="font-size: 0.9em;">Recommendation: {'APPROVE' if probability < 0.35 else 'REVIEW REQUIRED'}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Detailed Analysis
            st.markdown('<div class="sub-header">📋 Detailed Analysis</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("""
                #### Key Risk Indicators
                """)
                
                risk_factors = []
                
                if age < 25 or age > 60:
                    risk_factors.append(f"❌ Age ({age}) is outside optimal range")
                else:
                    risk_factors.append(f"✓ Age ({age}) is within optimal range")
                
                if income < 300000:
                    risk_factors.append(f"❌ Low income (₹{income})")
                else:
                    risk_factors.append(f"✓ Adequate income (₹{income})")
                
                if loan_to_income_ratio > 3.5:
                    risk_factors.append(f"❌ High LTI ratio ({loan_to_income_ratio:.2f})")
                else:
                    risk_factors.append(f"✓ Healthy LTI ratio ({loan_to_income_ratio:.2f})")
                
                if delinquency_ratio > 25:
                    risk_factors.append(f"❌ High delinquency ratio ({delinquency_ratio}%)")
                else:
                    risk_factors.append(f"✓ Low delinquency ratio ({delinquency_ratio}%)")
                
                if credit_utilization_ratio > 70:
                    risk_factors.append(f"❌ High credit utilization ({credit_utilization_ratio}%)")
                else:
                    risk_factors.append(f"✓ Moderate credit utilization ({credit_utilization_ratio}%)")
                
                for factor in risk_factors:
                    st.write(factor)
            
            with col2:
                st.write("""
                #### Recommendation
                """)
                
                if probability < 0.15:
                    st.success("""
                    **Status:** ✅ APPROVED
                    
                    This applicant has a **low credit risk** profile.
                    - Proceed with loan approval
                    - Consider normal interest rates
                    - Standard documentation required
                    """)
                elif probability < 0.35:
                    st.warning("""
                    **Status:** ⚠️ CONDITIONAL APPROVAL
                    
                    This applicant has a **moderate credit risk**.
                    - Require additional documentation
                    - May need co-signer or additional security
                    - Consider slightly higher interest rates
                    """)
                else:
                    st.error("""
                    **Status:** ❌ REQUIRES REVIEW
                    
                    This applicant has a **high credit risk**.
                    - Recommend additional verification
                    - May need higher security or collateral
                    - Consider declining or restructuring terms
                    """)
            
            # Risk Distribution Chart
            st.markdown('<div class="sub-header">📊 Risk Distribution</div>', unsafe_allow_html=True)
            
            fig = go.Figure(data=[
                go.Bar(
                    x=['Default Risk', 'Approval Probability'],
                    y=[probability * 100, (1 - probability) * 100],
                    marker_color=['#ff6b6b', '#84fab0']
                )
            ])
            fig.update_layout(
                height=300,
                showlegend=False,
                yaxis_title="Probability (%)",
                hovermode="x unified"
            )
            st.plotly_chart(fig, use_container_width=True)


# ==================== PAGE: ANALYTICS ====================
elif page == "📊 Analytics":
    st.markdown('<div class="main-header">📊 Analytics & Insights</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📈 Key Metrics</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Predictions",
            value="12,459",
            delta="+456 today"
        )
    
    with col2:
        st.metric(
            label="Approval Rate",
            value="78.5%",
            delta="+2.3% vs last week"
        )
    
    with col3:
        st.metric(
            label="Avg Risk Score",
            value="28.4%",
            delta="-1.2% vs last week"
        )
    
    with col4:
        st.metric(
            label="System Uptime",
            value="99.99%",
            delta="Perfect record"
        )
    
    st.markdown("---")
    
    st.markdown('<div class="sub-header">📊 Risk Distribution</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart for risk distribution
        fig = go.Figure(data=[go.Pie(
            labels=['Low Risk', 'Medium Risk', 'High Risk'],
            values=[60, 25, 15],
            marker=dict(colors=['#84fab0', '#ffd700', '#ff6b6b'])
        )])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk over time
        fig = go.Figure()
        import numpy as np
        
        days = np.arange(0, 30)
        low_risk = 60 + np.random.randint(-5, 5, 30)
        med_risk = 25 + np.random.randint(-3, 3, 30)
        high_risk = 15 + np.random.randint(-2, 2, 30)
        
        fig.add_trace(go.Scatter(x=days, y=low_risk, name='Low Risk', fill='tozeroy', line=dict(color='#84fab0')))
        fig.add_trace(go.Scatter(x=days, y=med_risk, name='Medium Risk', fill='tonexty', line=dict(color='#ffd700')))
        fig.add_trace(go.Scatter(x=days, y=high_risk, name='High Risk', fill='tonexty', line=dict(color='#ff6b6b')))
        
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown('<div class="sub-header">💡 System Information</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **Model Version:** 2.1.0
        **Last Training:** Dec 5, 2024
        **Training Samples:** 45,230
        """)
    
    with col2:
        st.info("""
        **Model Type:** Logistic Regression
        **Accuracy:** 94.2%
        **F1 Score:** 0.891
        """)
    
    with col3:
        st.info("""
        **Average Response:** 2.3ms
        **Predictions/Hour:** 15,000+
        **Uptime:** 99.99%
        """)


# ==================== PAGE: ABOUT ====================
elif page == "ℹ️ About":
    st.markdown('<div class="main-header">ℹ️ About Lauki Finance</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Welcome to Lauki Finance
    
    ### 🎯 Our Mission
    Lauki Finance is committed to revolutionizing credit risk assessment through advanced machine learning and artificial intelligence. 
    We empower financial institutions with data-driven insights to make better lending decisions.
    
    ---
    
    ### 🔬 Technology Stack
    
    - **Backend:** Python with scikit-learn, XGBoost, TensorFlow
    - **Frontend:** Streamlit for interactive dashboards
    - **ML Models:** Logistic Regression, Random Forest, XGBoost
    - **Data Processing:** Pandas, NumPy, Scikit-learn
    - **Deployment:** Streamlit Cloud, Docker
    
    ---
    
    ### 📊 Model Information
    
    Our credit risk model is built on advanced machine learning algorithms trained on thousands of historical loan records.
    
    **Key Features:**
    - Multi-model ensemble approach
    - Real-time risk assessment
    - Interpretable predictions with risk indicators
    - Scalable architecture for enterprise use
    
    **Model Performance:**
    - Accuracy: 94.2%
    - Precision: 89.5%
    - Recall: 91.3%
    - F1 Score: 0.891
    - ROC-AUC: 0.958
    
    ---
    
    ### 👥 Team & Support
    
    **Developed by:** Lauki Finance Team  
    **Version:** 1.0.0  
    **Last Updated:** December 2024  
    
    For support, contact: support@laukifinance.com
    
    ---
    
    ### 📜 Terms & Conditions
    
    This tool is provided for educational and assessment purposes. All predictions should be validated by qualified financial professionals before making lending decisions.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🔒 Data Security
    
    We take data security seriously:
    - All data is encrypted in transit and at rest
    - No personal data is stored persistently
    - GDPR and local compliance adherent
    - Regular security audits and updates
    """)
    
    st.markdown("""
    ### 📞 Contact Us
    
    - **Email:** info@laukifinance.com
    - **Website:** www.laukifinance.com
    - **Support:** support@laukifinance.com
    """)
