import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Loan Calculator 💳")

# User input for loan details
st.header("Enter Loan Details")

# Loan amount input
loan_amount = st.slider("Loan Amount ($)", min_value=1000, max_value=100000, value=20000, step=1000)

# Interest rate input
interest_rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=20.0, value=5.0, step=0.1)

# Loan tenure input
loan_tenure = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=5)

# Calculate EMI
def calculate_emi(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    months = tenure * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return emi

# Calculate and display EMI
emi = calculate_emi(loan_amount, interest_rate, loan_tenure)
st.subheader(f"Your Monthly EMI: ${emi:.2f}")

# Generate amortization schedule
def generate_amortization_schedule(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)
    months = tenure * 12
    schedule = []
    for month in range(1, months + 1):
        interest_payment = principal * monthly_rate
        principal_payment = emi - interest_payment
        principal -= principal_payment
        schedule.append((month, interest_payment, principal_payment, principal))
    return pd.DataFrame(schedule, columns=["Month", "Interest Payment", "Principal Payment", "Remaining Balance"])

# Create amortization schedule
amortization_schedule = generate_amortization_schedule(loan_amount, interest_rate, loan_tenure)

# Display amortization schedule
st.header("Amortization Schedule")
st.write(amortization_schedule)

# Plotting the amortization schedule
st.subheader("Loan Repayment Schedule 📈")
plt.figure(figsize=(10, 5))
plt.plot(amortization_schedule["Month"], amortization_schedule["Remaining Balance"], marker='o')
plt.title("Remaining Loan Balance Over Time")
plt.xlabel("Months")
plt.ylabel("Remaining Balance ($)")
plt.grid()
st.pyplot(plt)

# Additional information
st.markdown("""
### How to Use:
1. Adjust the sliders to set your loan amount, interest rate, and tenure.
2. The app will calculate your monthly EMI and display the amortization schedule.
3. The graph shows how your remaining loan balance decreases over time.
""")