import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 500)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

df = pd.read_csv(r"C:\Users\erenk\Desktop\amazon_review_veri220805073812-221026-191659\amazon_review.csv")
df.head()
df.shape

# reviewerID Kullanıcı ID’si
# asin Ürün ID’si
# reviewerName Kullanıcı Adı
# helpful Faydalı değerlendirme derecesi
# reviewText Değerlendirme
# overall Ürün rating’i
# summary Değerlendirme özeti
# unixReviewTime Değerlendirme zamanı
# reviewTime Değerlendirme zamanı Raw
# day_diff Değerlendirmeden itibaren geçen gün sayısı
# helpful_yes Değerlendirmenin faydalı bulunma sayısı
# total_vote Değerlendirmeye verilen oy sayısı

# rating dagilimi

df["overall"].value_counts()

df["helpful"].value_counts()

df.groupby("helpful").agg({"helpful": "count",
                           "overall": "mean"})

# Ortalama -------------------------------------------------------

df["overall"].mean()

# Zaman ----------------------------------------------------------

df["reviewTime"] = pd.to_datetime(df["reviewTime"])

df["unixReviewTime"] = pd.to_datetime(df["unixReviewTime"])

df.info()

df["reviewTime"].max()

current_date = pd.to_datetime('2014-12-07 0:0:0')

df["days"] = (current_date - df["reviewTime"]).dt.days

df.head()

df["days"].quantile([.25, .50, .75])

# df['comment_days_quantile'] = pd.qcut(df['days'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

print(df.loc[(df["days"] <= 280), "overall"].mean())
print(df.loc[(df["days"] > 280) & (df["days"] <= 430), "overall"].mean())
print(df.loc[(df["days"] > 430) & (df["days"] <= 600), "overall"].mean())
print(df.loc[(df["days"] > 600), "overall"].mean())

# df.loc[df["comment_days_quantile"]== "Q1"]["overall"].mean()0.35+df.loc[df["comment_days_quantile"]== "Q2"]["overall"].mean()0.30+df.loc[df["comment_days_quantile"]== "Q3"]["overall"].mean()0.20+df.loc[df["comment_days_quantile"]== "Q4"]["overall"].mean()0.15

def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[df["days"] <= 280, "overall"].mean() * 28 / 100 + \
            dataframe.loc[(df["days"] > 280) & (df["days"] <= 430), "overall"].mean() * 26 / 100 + \
            dataframe.loc[(df["days"] > 430) & (df["days"] <= 600), "overall"].mean() * 24 / 100 + \
            dataframe.loc[(df["days"] > 600), "overall"].mean() * 22 / 100
time_based_weighted_average(df)

time_based_weighted_average(df, 30, 26, 22, 22)

# Quantiles_=["Q1" , "Q2", "Q3", "Q4"]
#    for i in Quantiles_:
#        print(f"{i}" nin ortalaması: " {df.loc[df["comment_days_quantile"]== i]["overall"].mean()}")

################################# Gorev 2 ######################################

df["helpful_no"] = df["total_vote"] - df["helpful_yes"]

df["helpful_no"].sum()

def score_pos_neg_diff(pos, neg):
    return pos - neg

df["score_pos_neg_diff"] = df.apply(lambda x: score_pos_neg_diff(x["helpful_yes"],
                                                                 x["helpful_no"]), axis=1)

def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up +down)

df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"],
                                                                     x["helpful_no"]), axis=1)

def wilson_lower_bound(up, down, confidence=0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) /  ( 1 + z * z / n)

df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"],
                                                                 x["helpful_no"]), axis=1)


df.sort_values("wilson_lower_bound", ascending=False).head()

