# 📊 FINMATE Financial Calculation Formulas

## Overview
This document explains all the mathematical formulas and calculations used in the FINMATE dashboard to compute financial metrics and insights.

---

## 💰 Core Financial Metrics

### 1. Monthly Income Calculation
```python
Monthly Income = Sum of all income transactions for the month
```

**Formula in Code:**
```python
income_transactions = transactions.filter(
    transaction_type='income',
    date__year=year,
    date__month=month
)
monthly_income = income_transactions.aggregate(total=Sum('amount'))['total']
```

**Growth Calculation:**
```python
Growth % = ((Current Month Income - Previous Month Income) / Previous Month Income) × 100
```

---

### 2. Monthly Expenses Calculation
```python
Total Monthly Expenses = Sum of all expense transactions for the month
```

**Category Breakdown:**
- **Mandatory**: Rent, utilities, groceries, insurance, loan payments
- **Non-Mandatory**: Dining, shopping, entertainment, subscriptions  
- **Luxury**: Travel, luxury items, premium services
- **Investment**: Mutual funds, stocks, bonds, SIPs

**Percentage by Category:**
```python
Category % = (Category Amount / Total Expenses) × 100
```

---

### 3. Monthly Surplus Calculation
```python
Monthly Surplus = Monthly Income - Monthly Expenses
```

**Savings Rate:**
```python
Savings Rate % = (Monthly Surplus / Monthly Income) × 100
```

**Example:**
- Monthly Income: ₹75,000
- Monthly Expenses: ₹56,500
- Monthly Surplus: ₹18,500
- Savings Rate: (₹18,500 / ₹75,000) × 100 = 24.7%

---

### 4. Total Savings Calculation
```python
Total Savings = Sum of all savings and investment transactions
```

**Monthly Savings Growth:**
```python
Monthly Growth % = ((Current Month Savings - Previous Month Savings) / Previous Month Savings) × 100
```

---

### 5. Investment Goal Progress
```python
Progress % = (Current Investments / Target Investment Goal) × 100
```

**Example from your dashboard:**
- Current Investments: ₹36,000
- Target Goal: ₹50,000
- Progress: (₹36,000 / ₹50,000) × 100 = 72%

**Remaining Amount:**
```python
Remaining = Target Goal - Current Investments
Remaining = ₹50,000 - ₹36,000 = ₹14,000
```

---

## 📈 Growth Percentage Calculations

### Standard Growth Formula
```python
Growth % = ((New Value - Old Value) / Old Value) × 100
```

### Applied to Your Dashboard Metrics:

**1. Income Growth (5.2%):**
```python
Previous Month Income: ₹71,250
Current Month Income: ₹75,000
Growth = ((₹75,000 - ₹71,250) / ₹71,250) × 100 = 5.26% ≈ 5.2%
```

**2. Savings Growth (12.4%):**
```python
Previous Month Savings: ₹40,000
Current Month Savings: ₹45,000
Growth = ((₹45,000 - ₹40,000) / ₹40,000) × 100 = 12.5% ≈ 12.4%
```

**3. Surplus Growth (8.1%):**
```python
Previous Month Surplus: ₹17,100
Current Month Surplus: ₹18,500
Growth = ((₹18,500 - ₹17,100) / ₹17,100) × 100 = 8.19% ≈ 8.1%
```

---

## 📊 Chart Data Calculations

### 1. Spending Distribution (Pie Chart)
```python
for category in ['Mandatory', 'Non-Mandatory', 'Luxury', 'Investment', 'Others']:
    percentage = (category_amount / total_expenses) × 100
    chart_data.append({
        'name': category,
        'value': percentage,
        'amount': category_amount
    })
```

### 2. Savings Trend (Line Chart)
```python
for month in last_6_months:
    monthly_surplus = calculate_monthly_surplus(month)
    trend_data.append({
        'month': month_name,
        'savings': monthly_surplus
    })
```

---

## 🎯 Goal Timeline Calculations

### Simple Savings Goal
```python
Months to Goal = (Target Amount - Current Amount) / Monthly Contribution
```

### Investment Goal with Compound Interest
```python
# Monthly interest rate
monthly_rate = annual_rate / 12

# Future value of current amount
FV_current = current_amount × (1 + monthly_rate)^months

# Future value of monthly contributions (annuity)
FV_contributions = monthly_contribution × [((1 + monthly_rate)^months - 1) / monthly_rate]

# Total future value
Total_FV = FV_current + FV_contributions
```

**Example:**
- Current Amount: ₹50,000
- Monthly SIP: ₹15,000
- Target: ₹5,00,000
- Annual Return: 12%

```python
monthly_rate = 12% / 12 = 1% = 0.01

# After 24 months:
FV_current = ₹50,000 × (1.01)^24 = ₹63,412
FV_contributions = ₹15,000 × [((1.01)^24 - 1) / 0.01] = ₹4,05,769
Total = ₹63,412 + ₹4,05,769 = ₹4,69,181
```

---

## 📋 Financial Ratios

### 1. Expense-to-Income Ratio
```python
Expense Ratio % = (Total Monthly Expenses / Monthly Income) × 100
```

### 2. Debt-to-Income Ratio
```python
Debt Ratio % = (Monthly Debt Payments / Monthly Income) × 100
```

### 3. Emergency Fund Coverage
```python
Emergency Fund Months = Total Savings / Monthly Expenses
```

---

## 🤖 Insight Generation Logic

### Savings Rate Analysis
```python
if savings_rate >= 50:
    insight = "Excellent Saving Rate"
elif savings_rate >= 20:
    insight = "Good Saving Habits"
else:
    insight = "Low Savings Rate - Need Improvement"
```

### Luxury Spending Alert
```python
luxury_percentage = (luxury_spending / total_expenses) × 100

if luxury_percentage > 15:
    alert = "Luxury Spending Alert - Consider reducing by 10%"
```

### Investment Recommendation
```python
if monthly_surplus > ₹10,000:
    recommendation = "Consider diversifying into equity funds or SIPs"
```

---

## 🔄 API Response Format

### Dashboard Metrics Response
```json
{
  "monthly_income": {
    "amount": 75000,
    "formatted": "₹75,000",
    "growth": {
      "value": "+5.2%",
      "is_positive": true
    }
  },
  "total_savings": {
    "amount": 45000,
    "formatted": "₹45,000",
    "growth": {
      "value": "+12.4%",
      "is_positive": true
    }
  },
  "monthly_surplus": {
    "amount": 18500,
    "formatted": "₹18,500",
    "growth": {
      "value": "+8.1%",
      "is_positive": true
    },
    "savings_rate": "24.7%"
  },
  "investment_goal": {
    "progress": "72%",
    "current_amount": 36000,
    "target_amount": 50000,
    "remaining": 14000
  }
}
```

---

## 🧮 Advanced Calculations

### Compound Interest Formula
```python
A = P(1 + r/n)^(nt)

Where:
A = Final amount
P = Principal amount
r = Annual interest rate
n = Number of times interest compounds per year
t = Time in years
```

### SIP Future Value Formula
```python
FV = PMT × [((1 + r)^n - 1) / r]

Where:
FV = Future Value
PMT = Monthly payment
r = Monthly interest rate
n = Number of payments
```

### Goal Achievement Timeline
```python
n = log(FV/PV) / log(1 + r)

Where:
n = Number of periods
FV = Future Value (goal amount)
PV = Present Value (current amount)
r = Interest rate per period
```

---

## 📱 Frontend Integration

### Fetching Dashboard Data
```javascript
const response = await fetch('/api/transactions/dashboard/metrics/');
const data = await response.json();

// Display formatted values
document.getElementById('monthly-income').textContent = data.monthly_income.formatted;
document.getElementById('income-growth').textContent = data.monthly_income.growth.value;
```

### Chart Data Processing
```javascript
// Pie chart data
const pieData = data.charts.spending_distribution.map(item => ({
  name: item.name,
  value: item.value,
  color: item.color
}));

// Line chart data
const lineData = data.charts.savings_trend.map(item => ({
  month: item.month,
  savings: item.savings
}));
```

---

## 🎯 Summary

All calculations in FINMATE follow standard financial formulas with real-time data processing:

1. **Income/Expense Tracking**: Direct sum aggregation from transaction data
2. **Growth Calculations**: Period-over-period percentage change
3. **Goal Progress**: Simple ratio calculations with timeline projections
4. **Investment Projections**: Compound interest with SIP calculations
5. **Insights**: Rule-based analysis of financial ratios and patterns

The system provides accurate, real-time financial insights based on actual transaction data, helping users make informed financial decisions.

---

*Last Updated: October 11, 2025*