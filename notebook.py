import pandas as pd

# -------------------------------
# 1. Check duplicates in RAW data
# -------------------------------
raw_df = pd.read_csv('data/train.csv')

raw_duplicates = raw_df.duplicated().sum()

print("\nRaw Data Duplicate Check")
print("Total duplicate rows:", raw_duplicates)


# -------------------------------
# 2. Check duplicates in CLEAN data
# -------------------------------
clean_df = pd.read_csv('sql/clean_data.csv')

clean_duplicates = clean_df.duplicated().sum()

print("\nClean Data Duplicate Check")
print("Total duplicate rows:", clean_duplicates)


# -------------------------------
# 3. Conclusion
# -------------------------------
if clean_duplicates == 0:
    print("\nData Cleaning Successful: No duplicates in cleaned dataset")
else:
    print("\nWarning: Duplicates still exist in cleaned dataset")