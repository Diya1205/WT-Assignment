import pandas as pd

# Load data
df = pd.read_csv("sample_data.csv")

# Add total and average columns
df["Total"] = df.iloc[:, 1:].sum(axis=1)
df["Average"] = df.iloc[:, 1:-1].mean(axis=1)

# Class average per subject
print("🔹 Class Average per Subject:")
print(df.iloc[:, 1:5].mean())

# Topper
topper = df.loc[df["Total"].idxmax()]
print(f"\n🏆 Topper: {topper['Name']} with {topper['Total']} marks")

# Subject-wise highest and lowest
print("\n📊 Subject-wise Highest and Lowest:")
for subject in df.columns[1:5]:
    highest = df.loc[df[subject].idxmax()]
    lowest = df.loc[df[subject].idxmin()]
    print(f"{subject} - Highest: {highest['Name']} ({highest[subject]}), Lowest: {lowest['Name']} ({lowest[subject]})")

# Pass/Fail count (Assuming pass if all subjects >= 40)
df["Status"] = df.iloc[:, 1:5].apply(lambda x: "Pass" if all(x >= 40) else "Fail", axis=1)
print("\n✅ Pass Count:", (df["Status"] == "Pass").sum())
print("❌ Fail Count:", (df["Status"] == "Fail").sum())
