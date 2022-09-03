import streamlit as st
def calculate_emi(p, n, r):
    num = ((1 + (r/100)) ** n)
    den = num - 1
    return p * (r/100) * (num/den)
st.title("EMI Calculator")
principal = st.slider("Principal Amount: ", 0, 100000, step = 100)
tenure = st.slider("Tenure of the loan : ", 0, 3, step = 1) * 12
roi = st.slider("Rate of Interest ", 0.0, 15.0, step = 0.01) / 12
if st.button("Calculate EMI"):
    st.write(round(calculate_emi(principal, tenure, roi), 3))

import streamlit as st
def calculate_emi(p, n, r):
    num = ((1 + (r/100)) ** n)
    den = num - 1
    return p * (r/100) * (num/den)
def calculate_outstanding_loan_balance(p, n, r, m):
    num_t1 = ((1 + (r/100)) ** n)
    num_t2 = ((1 + (r/100)) ** m)
    den_t1 = ((1 + (r/100)) ** n)
    return p * ((num_t1 - num_t2) / (den_t1 - 1))
st.title("Improvised EMI Calculator")
principal_2 = st.slider("Principal Amount : ", 0, 100000, step = 100)
tenure_2 = st.slider("Tenure of the loan: ", 0, 3, step = 1) * 12
roi_2 = st.slider("Rate of Interest", 0.0, 15.0, step = 0.01) / 12
m_2 = st.slider("Period after which the Outstanding Loan Balance is calculated (in months)",
                1.0, float(tenure_2), step = 1.0)
if st.button("Calculate EMI "):
    st.write(round(calculate_emi(principal_2, tenure_2, roi_2), 3))
if st.button("Calculate Outstanding Loan Balance"):
    st.write(round(calculate_outstanding_loan_balance(principal_2, tenure_2, roi_2, m_2), 2))