import pandas as pd
import os

# =====================================
# BASE DIRECTORY
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

print("BASE_DIR:")
print(BASE_DIR)

# =====================================
# CREATE ANALYSIS OUTPUT FOLDER
# =====================================

analysis_path = os.path.join(
    BASE_DIR,
    "data",
    "analysis"
)

os.makedirs(analysis_path, exist_ok=True)

# =====================================
# LOAD FEATURED DATASET
# =====================================

featured_file = os.path.join(
    BASE_DIR,
    "data",
    "final",
    "featured_dataset.csv"
)

print("Loading featured dataset...")
print(featured_file)

df = pd.read_csv(
    featured_file,
    low_memory=False
)

print("✅ Dataset loaded successfully")

# =====================================
# DELINQUENCY RATE
# =====================================

print("\n=========================")
print("DELINQUENCY RATE")
print("=========================")

delinquent = df[
    df["DAYS_PAST_DUE"] > 0
]

rate = len(delinquent) / len(df)

print(f"Delinquency Rate: {rate:.2%}")

# Save delinquency summary
delinquency_summary = pd.DataFrame({
    "Metric": ["Delinquency Rate"],
    "Value": [rate]
})

delinquency_file = os.path.join(
    analysis_path,
    "delinquency_rate.csv"
)

delinquency_summary.to_csv(
    delinquency_file,
    index=False
)

print("✅ Delinquency report saved")

# =====================================
# RISK DISTRIBUTION
# =====================================

print("\n=========================")
print("RISK DISTRIBUTION")
print("=========================")

risk_distribution = (
    df["RISK_CATEGORY"]
    .value_counts()
)

print(risk_distribution)

# Save risk distribution
risk_distribution_file = os.path.join(
    analysis_path,
    "risk_distribution.csv"
)

risk_distribution.to_csv(
    risk_distribution_file
)

print("✅ Risk distribution report saved")

# =====================================
# AGE SEGMENT ANALYSIS
# =====================================

print("\n=========================")
print("AGE SEGMENT ANALYSIS")
print("=========================")

age_segment_analysis = (
    df.groupby("AGE_BAND")["PAYMENT_RATIO"]
    .mean()
)

print(age_segment_analysis)

# Save age analysis
age_analysis_file = os.path.join(
    analysis_path,
    "age_segment_analysis.csv"
)

age_segment_analysis.to_csv(
    age_analysis_file
)

print("✅ Age segment analysis saved")

# =====================================
# PAYMENT ANALYSIS
# =====================================

print("\n=========================")
print("PAYMENT ANALYSIS")
print("=========================")

payment_summary = df[
    [
        "PAYMENT_AMOUNT",
        "EXPECTED_PAYMENT",
        "PAYMENT_RATIO"
    ]
].describe()

print(payment_summary)

payment_summary_file = os.path.join(
    analysis_path,
    "payment_summary.csv"
)

payment_summary.to_csv(
    payment_summary_file
)

print("✅ Payment summary saved")

# =====================================
# CUSTOMER RISK SUMMARY
# =====================================

print("\n=========================")
print("CUSTOMER RISK SUMMARY")
print("=========================")

customer_risk_summary = (
    df.groupby("RISK_CATEGORY")["CUSTOMER_AGE"]
    .agg(["count", "mean"])
)

print(customer_risk_summary)

customer_risk_file = os.path.join(
    analysis_path,
    "customer_risk_summary.csv"
)

customer_risk_summary.to_csv(
    customer_risk_file
)

print("✅ Customer risk summary saved")

# =====================================
# OVERALL ANALYSIS SUMMARY
# =====================================

summary = pd.DataFrame({

    "Metric": [
        "Total Records",
        "Delinquent Customers",
        "Delinquency Rate"
    ],

    "Value": [
        len(df),
        len(delinquent),
        f"{rate:.2%}"
    ]
})

summary_file = os.path.join(
    analysis_path,
    "analysis_summary.csv"
)

summary.to_csv(
    summary_file,
    index=False
)

print("✅ Analysis summary saved")

# =====================================
# FINISHED
# =====================================

print("\n🎉 Data analysis completed successfully")