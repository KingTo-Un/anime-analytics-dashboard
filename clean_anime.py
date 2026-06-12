import pandas as pd

# Load dataset
df = pd.read_csv("anime.csv")

print("Original Rows:", len(df))

# -------------------------
# Handle Missing Values
# -------------------------

df["genre"] = df["genre"].fillna("Unknown")
df["type"] = df["type"].fillna("Unknown")

# Remove rows with missing ratings
df = df.dropna(subset=["rating"])

# -------------------------
# Convert Episodes to Numeric
# -------------------------

df["episodes"] = pd.to_numeric(
    df["episodes"],
    errors="coerce"
)

df["episodes"] = df["episodes"].fillna(0)

# -------------------------
# Normalize Ratings
# -------------------------

df["rating_normalized"] = (
    (df["rating"] - df["rating"].min())
    /
    (df["rating"].max() - df["rating"].min())
)

# -------------------------
# Remove Outliers using IQR
# -------------------------

Q1 = df["rating"].quantile(0.25)
Q3 = df["rating"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)

df = df[
    (df["rating"] >= lower)
    &
    (df["rating"] <= upper)
]

print("Cleaned Rows:", len(df))

# Export cleaned dataset
df.to_csv(
    "anime_cleaned.csv",
    index=False
)

print("Cleaning Complete")