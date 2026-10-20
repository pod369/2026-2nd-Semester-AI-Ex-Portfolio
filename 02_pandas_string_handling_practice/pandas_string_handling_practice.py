
import pandas as pd
import numpy as np


print("49p ------------------------------")
print("pandas import 완료\n")



df = pd.DataFrame(
    {
        "a": [4, 5, 6],
        "b": [7, 8, 9],
        "c": [10, 11, 12]
    },
    index=[1, 2, 3]
)
print("50p ------------------------------")
print(df, "\n")


print("51p ------------------------------")
print(df["a"], "\n")
print(df[["a", "b"]], "\n")
print(df.loc[3], "\n")


df = pd.DataFrame(
    {
        "a": [4, 5, 6, 6, np.nan],
        "b": [7, 8, np.nan, 9, 9],
        "c": [10, 11, 12, np.nan, 12]
    },
    index=pd.MultiIndex.from_tuples(
        [('d', 1), ('d', 2), ('e', 2), ('e', 3), ('e', 4)],
        names=['n', 'v']
    )
)
print("52p ------------------------------")
print(df, "\n")


print("53p ------------------------------")
print(df[df.a < 6], "\n")
print(df.a.isin([5]), "\n")


df = df.drop_duplicates(subset="a", keep="last")
print("54p ------------------------------")
print(df, "\n")


print("55p ------------------------------")
print(df.head(2), "\n")
print(df.tail(2), "\n")


document = [
    "코로나 상생지원금 문의입니다.",
    "지하철 운행시간 문의입니다.",
    "버스 운행시간 문의입니다.",
    "사회적 거리두기로 인한 영업시간 안내입니다.",
    "Bus 운행시간 문의입니다.",
    "Taxi 승강장 문의입니다."
]
print("56p ------------------------------")
print(document, "\n")


df_doc = pd.DataFrame(document, columns=["문서"])
print("57p ------------------------------")
print(df_doc, "\n")


print("58p ------------------------------")
print(df_doc["문서"].astype("string"), "\n")


print("59p ------------------------------")
print(df_doc["문서"].str.upper(), "\n")
print(df_doc["문서"].str.lower(), "\n")


print("60p ------------------------------")
print(df_doc["문서"].str.strip(), "\n")


print("61p ------------------------------")
print(df_doc["문서"].str.split(), "\n")
print(df_doc["문서"].str.split(expand=True), "\n")


print("62p ------------------------------")
print(df_doc["문서"].str.contains("버스"), "\n")
print(df_doc[df_doc["문서"].str.contains("버스")], "\n")


print("63p ------------------------------")
print(df_doc["문서"].str.replace("운행", "영업", regex=False), "\n")
print(df_doc["문서"].str.replace("버스|지하철", "대중교통", regex=True), "\n")


print("64p ------------------------------")
print(df_doc.replace("지하철", "교통", regex=True), "\n")
print(df_doc.replace({"문의": "질문"}, regex=True), "\n")


print("65~66p ------------------------------")
print(df_doc.replace({"문의": "질문"}, regex=True))
print(df_doc["문서"].str.split("문의"), "\n")
