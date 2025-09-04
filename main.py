import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("17-googleplaystore.csv")
print(df.columns)
print(df.shape)
print(df.info(max_cols=None))
print(df.describe())

# missing data

print(df.isnull().sum())
# df["Reviews"]=df["Reviews"].astype(int)
print(df["Reviews"].str.isnumeric().sum())
print(df[~df["Reviews"].str.isnumeric()].to_string())

df_clean = df.copy()
df_clean = df_clean.drop(df_clean.index[10472])
print(df_clean["Reviews"].str.isnumeric().sum())
print(df_clean.info(max_cols=None))

df_clean["Reviews"] = df_clean["Reviews"].astype(int)
print(df_clean.info(max_cols=None))
print(df_clean.describe())

print(df_clean["Size"].value_counts())
print(df_clean["Size"].unique())

df_clean["Size"] = df_clean["Size"].str.replace("M", "000")
df_clean["Size"] = df_clean["Size"].str.replace("k", "")
print(df_clean["Size"].unique())
df_clean["Size"] = df_clean["Size"].replace("Varies with device", np.nan)
print(df_clean["Size"].unique())
df_clean["Size"] = df_clean["Size"].astype(float)
print(df_clean.info(max_cols=None))

print(df_clean.tail().to_string())

print(df_clean["Installs"].unique())
print(df_clean["Price"].unique())

chars_to_remove = ["+", ",", "$"]
cols_to_clean = ["Installs", "Price"]

for item in chars_to_remove:
    for cols in cols_to_clean:
        df_clean[cols] = df_clean[cols].str.replace(item, "")

print(df_clean["Price"].unique())

df_clean["Price"] = df_clean["Price"].astype(float)
df_clean["Installs"] = df_clean["Installs"].astype(int)
print(df_clean.info(max_cols=None))
print(df_clean["Price"].unique())
print(df_clean["Installs"].unique())

print(df_clean.describe())

print(df_clean.info(max_cols=None))
print(df_clean.isnull().sum())
print(df_clean["Last Updated"].unique())

df_clean["Last Updated"] = pd.to_datetime(df_clean["Last Updated"])
print(df_clean.head().to_string())
print(df_clean.info(max_cols=None))

# df_clean["Day"]=df_clean["Last Updated"].dt.day
# df_clean["Month"]=df_clean["Last Updated"].dt.month
# df_clean["Year"]=df_clean["Last Updated"].dt.year

print(df_clean.describe().to_string())

print(df_clean[df_clean.duplicated("App")])

df_clean = df_clean.drop_duplicates(subset=["App"], keep="first")
print(df_clean[df_clean.duplicated("App")])
print(df_clean.info(max_cols=None))

numeric_features = [feature for feature in df_clean.columns if df_clean[feature].dtype != "O"]
categorical_features = [feature for feature in df_clean.columns if df_clean[feature].dtype == "O"]

print(numeric_features)
print(categorical_features)

plt.figure(figsize=(15, 10))
for i in range(0, len(numeric_features)):
    plt.subplot(5, 3, i + 1)
    sns.kdeplot(x=df_clean[numeric_features[i]], color="b", fill=True)
    plt.xlabel(numeric_features[i])
    plt.tight_layout()
plt.show()

plt.figure(figsize=(16, 7))

category = ["Type", "Content Rating"]

for i in range(0, len(category)):
    plt.subplot(1, 2, i + 1)
    sns.countplot(x=df_clean[category[i]], color="b", fill=True)
    plt.xlabel(category[i])
    plt.tight_layout()
plt.show()

print(df_clean["Category"].value_counts())

df_cat_installs = df_clean.groupby(["Category"])["Installs"].sum().sort_values(ascending=False).reset_index()
df_cat_installs["Installs"] = df_cat_installs["Installs"] / 1000000000
print(df_cat_installs)

df_2 = df_cat_installs.head(10)
plt.figure(figsize=(18, 8))
sns.barplot(x="Installs", y="Category", data=df_2)
plt.xlabel("Installs in billion")
plt.ylabel("Categories")
plt.show()

# TOP 5 APPS İN CATEGORİES

apps = ["GAME", "COMMUNICATION", "TOOLS", "PRODUCTIVITY", "SOCIAL"]

df_cat_app_installs = df_clean.groupby(["Category", "App"])["Installs"].sum().sort_values(ascending=False).reset_index()

print(df_cat_app_installs)

plt.figure(figsize=(20, 10))
for i, app in enumerate(apps):
    df_3 = df_cat_app_installs[df_cat_app_installs["Category"] == app]
    df_3 = df_3.head(5)
    plt.subplot(3, 2, i + 1)
    sns.barplot(data=df_3, x="Installs", y="App")
    plt.title(app, size=20)
plt.tight_layout()
plt.show()

# 5 rating apps

rating_df = df_clean.groupby(["Category", "App"])["Rating"].sum().sort_values(ascending=False).reset_index()

top_rated_apps = rating_df[rating_df["Rating"] == 5.0]

df_clean["Android Ver"] = df_clean["Android Ver"].replace("Varies with device", np.nan, regex=True)
df_clean["Android Ver"] = df_clean["Android Ver"].replace("and up", "", regex=True)
df_clean["Android Ver"] = df_clean["Android Ver"].replace("W", "", regex=True)
df_clean["Android Ver"] = df_clean["Android Ver"].replace("-", "", regex=True)
df_clean["Android Ver"] = df_clean["Android Ver"].replace("", np.nan, regex=True)
print(df_clean["Android Ver"].unique())

# TARGET ENCODİNG

mean_genres_installs = df_clean.groupby(["Genres"])["Installs"].mean() / 1000000
mean_genres_installs = mean_genres_installs.to_dict()
print(mean_genres_installs)

df_clean["Genres Encoded"] = df_clean["Genres"].map(mean_genres_installs)
print(df_clean.head().to_string())
