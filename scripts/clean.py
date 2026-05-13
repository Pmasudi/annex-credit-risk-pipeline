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
# CREATE FINAL FOLDER
# =====================================

final_path = os.path.join(
    BASE_DIR,
    "data",
    "final"
)

os.makedirs(final_path, exist_ok=True)

# =====================================
# LOAD DATA
# =====================================

credit_file = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "credit_combined.csv"
)

sales_file = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "raw_sales.csv"
)

nps_file = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "raw_nps.csv"
)

print("Loading files...")

credit_df = pd.read_csv(
    credit_file,
    low_memory=False
)

sales_df = pd.read_csv(
    sales_file,
    low_memory=False
)

nps_df = pd.read_csv(
    nps_file,
    low_memory=False
)

print("✅ Files loaded successfully")

# =====================================
# CLEAN COLUMN NAMES
# =====================================

for df in [credit_df, sales_df, nps_df]:

    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .str.replace(" ", "_")
    )

print("✅ Column names cleaned")

# =====================================
# HANDLE NULLS
# =====================================

credit_df["PAYMENT_AMOUNT"] = (
    credit_df["PAYMENT_AMOUNT"]
    .fillna(0)
)

credit_df["EXPECTED_PAYMENT"] = (
    credit_df["EXPECTED_PAYMENT"]
    .fillna(0)
)

credit_df["DAYS_PAST_DUE"] = (
    credit_df["DAYS_PAST_DUE"]
    .fillna(0)
)

print("✅ Null values handled")

# =====================================
# REMOVE DUPLICATES
# =====================================

credit_df = credit_df.drop_duplicates()

sales_df = sales_df.drop_duplicates()

nps_df = nps_df.drop_duplicates()

print("✅ Duplicates removed")

# =====================================
# FIX DATES
# =====================================

date_columns = [
    "DATE",
    "SALE_DATE",
    "RETURN_DATE"
]

for col in date_columns:

    if col in credit_df.columns:

        credit_df[col] = pd.to_datetime(
            credit_df[col],
            errors="coerce"
        )

print("✅ Date columns cleaned")

# =====================================
# RENAME NPS COLUMNS
# =====================================

nps_df = nps_df.rename(columns={

    'USING_A_SCALE_FROM_0_(NOT_LIKELY)_TO_10_(VERY_LIKELY),_HOW_LIKELY_ARE_YOU_TO_RECOMMEND_MOPHONES_TO_FRIENDS_OR_FAMILY?':
    'NPS_SCORE',

    'WHAT_IS_THE_MAIN_REASON_FOR_YOUR_SCORE?':
    'NPS_REASON',

    'WHAT_IS_ONE_THING_WE_COULD_DO_TO_IMPROVE_YOUR_EXPERIENCE_WITH_US?':
    'IMPROVEMENT_FEEDBACK',

    'ARE_YOU_HAPPY_WITH_THE_QUALITY_AND_PERFORMANCE_OF_YOUR_MOPHONES_DEVICE?':
    'DEVICE_SATISFACTION',

    'ARE_YOU_HAPPY_WITH_THE_SERVICE_AND_SUPPORT_PROVIDED_BY_MOPHONES?':
    'SERVICE_SATISFACTION',

    'HAVE_YOU_EVER_EXPERIENCED_A_DELAY_IN_YOUR_PAYMENT_REFLECTING_IN_YOUR_MOPHONES_ACCOUNT?':
    'PAYMENT_DELAY_EXPERIENCE',

    'HAVE_YOU_EVER_HAD_DIFFICULTY_GETTING_ASSISTANCE_FROM_MOPHONES_CUSTOMER_SUPPORT_WHEN_NEEDED?':
    'SUPPORT_DIFFICULTY',

    '(IF_YES)_–_PLEASE_DESCRIBE_THE_CHALLENGE_YOU_FACED_AND_HOW_WE_CAN_IMPROVE_YOUR_EXPERIENCE.':
    'SUPPORT_FEEDBACK',

    'HAVE_YOU_EXPERIENCED_ANY_BATTERY-RELATED_ISSUES_WITH_YOUR_MOPHONES_DEVICE?':
    'BATTERY_ISSUES',

    'HAVE_YOU_USED_THE_MOPHONES_APP_(MOAPP)_TO_MANAGE_YOUR_ACCOUNT_OR_MAKE_PAYMENTS?':
    'MOAPP_USAGE',

    'WHICH_COMMUNICATION_CHANNEL_DO_YOU_PREFER_WHEN_CONTACTING_MOPHONES_FOR_INQUIRIES_OR_SUPPORT?':
    'PREFERRED_CHANNEL',

    'HAVE_YOU_EVER_HAD_YOUR_PHONE_LOCK_DESPITE_MAKING_A_PAYMENT_ON_TIME?':
    'PHONE_LOCK_ISSUE',

    'ANY_OTHER_FEEDBACK?':
    'OTHER_FEEDBACK'
})

print("✅ NPS columns renamed")

# =====================================
# SAVE CLEAN DATA
# =====================================

credit_output = os.path.join(
    final_path,
    "cleaned_credit.csv"
)

sales_output = os.path.join(
    final_path,
    "cleaned_sales.csv"
)

nps_output = os.path.join(
    final_path,
    "cleaned_nps.csv"
)

credit_df.to_csv(
    credit_output,
    index=False
)

sales_df.to_csv(
    sales_output,
    index=False
)

nps_df.to_csv(
    nps_output,
    index=False
)

print("✅ Clean files saved successfully")

# =====================================
# FINISHED
# =====================================

print("🎉 Cleaning complete")