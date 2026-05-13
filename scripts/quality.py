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
# CREATE QUALITY OUTPUT FOLDER
# =====================================

quality_path = os.path.join(
    BASE_DIR,
    "data",
    "quality"
)

os.makedirs(quality_path, exist_ok=True)

# =====================================
# NULL CHECK
# =====================================

print("\n=========================")
print("NULL VALUE CHECK")
print("=========================")

nulls = df.isnull().sum()

print(nulls)

# Save null report
null_report_file = os.path.join(
    quality_path,
    "null_report.csv"
)

nulls.to_csv(null_report_file)

print("✅ Null report saved")

# =====================================
# DUPLICATE CHECK
# =====================================

print("\n=========================")
print("DUPLICATE CHECK")
print("=========================")

duplicates = df.duplicated().sum()

print(f"Duplicates found: {duplicates}")

# Save duplicate rows if they exist
duplicate_rows = df[df.duplicated()]

duplicate_report_file = os.path.join(
    quality_path,
    "duplicate_records.csv"
)

duplicate_rows.to_csv(
    duplicate_report_file,
    index=False
)

print("✅ Duplicate report saved")

# =====================================
# AGE VALIDATION
# =====================================

print("\n=========================")
print("AGE VALIDATION")
print("=========================")

invalid_age = df[
    (df["CUSTOMER_AGE"] < 18) |
    (df["CUSTOMER_AGE"] > 120)
]

print(f"Invalid ages found: {len(invalid_age)}")

# Save invalid ages
invalid_age_file = os.path.join(
    quality_path,
    "invalid_age_records.csv"
)

invalid_age.to_csv(
    invalid_age_file,
    index=False
)

print("✅ Invalid age report saved")

# =====================================
# PAYMENT VALIDATION
# =====================================

print("\n=========================")
print("PAYMENT VALIDATION")
print("=========================")

negative_payments = df[
    df["PAYMENT_AMOUNT"] < 0
]

print(f"Negative payments found: {len(negative_payments)}")

negative_payment_file = os.path.join(
    quality_path,
    "negative_payment_records.csv"
)

negative_payments.to_csv(
    negative_payment_file,
    index=False
)

print("✅ Negative payment report saved")

# =====================================
# RISK CATEGORY VALIDATION
# =====================================

print("\n=========================")
print("RISK CATEGORY VALIDATION")
print("=========================")

valid_categories = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

invalid_risk = df[
    ~df["RISK_CATEGORY"].isin(valid_categories)
]

print(f"Invalid risk categories found: {len(invalid_risk)}")

invalid_risk_file = os.path.join(
    quality_path,
    "invalid_risk_categories.csv"
)

invalid_risk.to_csv(
    invalid_risk_file,
    index=False
)

print("✅ Risk category validation saved")

# =====================================
# SUMMARY REPORT
# =====================================

summary = pd.DataFrame({

    "Metric": [
        "Total Rows",
        "Total Columns",
        "Duplicate Rows",
        "Invalid Ages",
        "Negative Payments"
    ],

    "Value": [
        len(df),
        len(df.columns),
        duplicates,
        len(invalid_age),
        len(negative_payments)
    ]
})

summary_file = os.path.join(
    quality_path,
    "quality_summary.csv"
)

summary.to_csv(
    summary_file,
    index=False
)

print("✅ Quality summary saved")

# =====================================
# FINISHED
# =====================================

print("\n🎉 Data quality checks completed successfully")