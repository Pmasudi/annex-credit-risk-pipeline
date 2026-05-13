import pandas as pd
import glob
import os

# =====================================
# BASE DIRECTORY
# =====================================

BASE_DIR = "/opt/airflow"

# =====================================
# CREATE OUTPUT FOLDER
# =====================================

processed_path = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

os.makedirs(processed_path, exist_ok=True)

# =====================================
# CREDIT DATA
# =====================================

credit_path = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "Credit Data"
)

print("Checking Credit Data folder:")
print(credit_path)

credit_files = glob.glob(
    os.path.join(credit_path, "*.csv")
)

print("Files found:")
print(credit_files)

if len(credit_files) == 0:
    raise FileNotFoundError(
        f"No CSV files found in {credit_path}"
    )

credit_dfs = []

for file in credit_files:

    print(f"Reading: {file}")

    df = pd.read_csv(file)

    # Add source filename
    df["SOURCE_FILE"] = os.path.basename(file)

    credit_dfs.append(df)

# =====================================
# COMBINE CREDIT FILES
# =====================================

credit_df = pd.concat(
    credit_dfs,
    ignore_index=True
)

print("Combined rows:", len(credit_df))

# =====================================
# SAVE CREDIT OUTPUT
# =====================================

credit_output = os.path.join(
    processed_path,
    "credit_combined.csv"
)

credit_df.to_csv(
    credit_output,
    index=False
)

print("✅ Credit data combined successfully")

# =====================================
# SALES DATA
# =====================================

sales_file = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "Sales and Customer Data",
    "Sales and Customer Data.xlsx"
)

print("Reading Sales file:")
print(sales_file)

sales_df = pd.read_excel(sales_file)

sales_output = os.path.join(
    processed_path,
    "raw_sales.csv"
)

sales_df.to_csv(
    sales_output,
    index=False
)

print("✅ Sales data ingested")

# =====================================
# NPS DATA
# =====================================

nps_file = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "NPS DATA",
    "NPS Data.xlsx"
)

print("Reading NPS file:")
print(nps_file)

nps_df = pd.read_excel(nps_file)

nps_output = os.path.join(
    processed_path,
    "raw_nps.csv"
)

nps_df.to_csv(
    nps_output,
    index=False
)

print("✅ NPS data ingested")

# =====================================
# FINISHED
# =====================================

print("🎉 All ingestion completed successfully")



