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
# FEATURE ENGINEERING FUNCTION
# =====================================

def feature_engineering():

    print("🚀 Starting feature engineering...")

    # =====================================
    # LOAD CLEAN DATA
    # =====================================

    credit_file = os.path.join(
        BASE_DIR,
        "data",
        "final",
        "cleaned_credit.csv"
    )

    sales_file = os.path.join(
        BASE_DIR,
        "data",
        "final",
        "cleaned_sales.csv"
    )

    nps_file = os.path.join(
        BASE_DIR,
        "data",
        "final",
        "cleaned_nps.csv"
    )

    print("Loading cleaned datasets...")

    credit_df = pd.read_csv(
        credit_file,
        low_memory=False,
        dtype={
            "LOAN_ID": str
        }
    )

    sales_df = pd.read_csv(
        sales_file,
        low_memory=False,
        dtype={
            "SALE_ID": str,
            "LOAN_ID": str
        }
    )

    nps_df = pd.read_csv(
        nps_file,
        low_memory=False,
        dtype={
            "LOAN_ID": str
        }
    )

    print("✅ Clean datasets loaded")

    # =====================================
    # PAYMENT RATIO
    # =====================================

    credit_df["PAYMENT_RATIO"] = (
        credit_df["PAYMENT_AMOUNT"] /
        credit_df["EXPECTED_PAYMENT"].replace(0, 1)
    )

    print("✅ PAYMENT_RATIO created")

    # =====================================
    # RISK CATEGORY
    # =====================================

    def risk_category(row):

        if row["DAYS_PAST_DUE"] > 90:
            return "Critical"

        elif row["DAYS_PAST_DUE"] > 30:
            return "High"

        elif row["PAYMENT_RATIO"] < 0.8:
            return "Medium"

        else:
            return "Low"

    credit_df["RISK_CATEGORY"] = credit_df.apply(
        risk_category,
        axis=1
    )

    print("✅ RISK_CATEGORY created")

    # =====================================
    # AGE BAND
    # =====================================

    def age_band(age):

        if age <= 25:
            return "18-25"

        elif age <= 35:
            return "26-35"

        elif age <= 45:
            return "36-45"

        elif age <= 55:
            return "46-55"

        else:
            return "55+"

    credit_df["AGE_BAND"] = (
        credit_df["CUSTOMER_AGE"]
        .apply(age_band)
    )

    print("✅ AGE_BAND created")

    # =====================================
    # MERGE SALES DATA
    # =====================================

    print("Merging sales data...")

    master_df = pd.merge(
        credit_df,
        sales_df,
        on="LOAN_ID",
        how="left"
    )

    print("✅ Sales data merged")

    # =====================================
    # MERGE NPS DATA
    # =====================================

    print("Merging NPS data...")

    master_df = pd.merge(
        master_df,
        nps_df,
        on="LOAN_ID",
        how="left"
    )

    print("✅ NPS data merged")

    # =====================================
    # SAVE FEATURED DATASET
    # =====================================

    output_file = os.path.join(
        BASE_DIR,
        "data",
        "final",
        "featured_dataset.csv"
    )

    master_df.to_csv(
        output_file,
        index=False
    )

    print("✅ Featured dataset saved")
    print("🎉 Feature engineering complete")


# =====================================
# RUN SCRIPT
# =====================================

if __name__ == "__main__":

    feature_engineering()