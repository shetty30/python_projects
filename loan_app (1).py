import streamlit as st

# Configure page
st.set_page_config(page_title="Loan Eligibility Checker", page_icon="💸")

def main():
    st.title("🚀 Smart Loan Eligibility Checker")
    st.markdown("""
    *Banks use similar rules to assess applicants!*  
    *Fill your details below to check qualification.*
    """)
    
    with st.form("loan_form"):
        # Input widgets
        col1, col2 = st.columns(2)
        with col1:
            income = st.number_input("Monthly Income (₹)", min_value=0, value=30000)
            employment = st.selectbox("Employment Type", 
                                     ["Salaried", "Self-Employed", "Unemployed"])
        with col2:
            debt = st.number_input("Existing Debt (₹/month)", min_value=0, value=5000)
            credit_score = st.slider("Credit Score", 300, 900, 700)
        
        age = st.number_input("Age", min_value=18, max_value=70, value=25)
        
        # Submit button
        submitted = st.form_submit_button("Check Eligibility")
        
        if submitted:
            check_eligibility(income, debt, employment, credit_score, age)

def check_eligibility(income, debt, employment, credit_score, age):
    try:
        debt_ratio = debt / income if income > 0 else 1
        
        # Bank-like rules
        conditions = [
            income >= 25000,
            credit_score >= 700,
            employment != "Unemployed",
            debt_ratio < 0.4,
            21 <= age <= 65
        ]
        
        if all(conditions):
            st.success("### ✅ Approved! \nYou meet all eligibility criteria.")
            st.balloons()
        else:
            reasons = []
            if income < 25000: reasons.append("📉 Income below ₹25k")
            if credit_score < 700: reasons.append("💳 Credit score < 700")
            if employment == "Unemployed": reasons.append("👔 Unemployed status")
            if debt_ratio >= 0.4: reasons.append="🏦 High debt ratio (≥40%)"
            if age < 21 or age > 65: reasons.append="👶👴 Age outside 21-65 range"
            
            st.error(f"### ❌ Rejected \nReasons: {', '.join(reasons)}")
            
    except Exception as e:
        st.warning(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    main()