import pandas as pd

df = pd.read_csv("anime_cleaned.csv")

print("\nTOP 10 MOST POPULAR ANIME\n")

top10 = df.nlargest(10, "members")[["name", "members"]]

print(top10.to_string(index=False))


print("\nAVERAGE RATING BY TYPE\n")

avg_rating = (
    df.groupby("type")["rating"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_rating)


print("\nTOP 10 GENRES\n")

genres = (
    df["genre"]
    .str.split(", ")
    .explode()
)

top_genres = genres.value_counts().head(10)

print(top_genres)