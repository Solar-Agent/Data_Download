from Data_Download.merge_era5 import download_and_merge_era5_solar

df = download_and_merge_era5_solar(
    start_date="2014-12",
    end_date="2023-01",
    lat=37.257,
    lon=126.983
)
df.to_csv("data.csv", index=False)
print(df.head())