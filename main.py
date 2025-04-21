from Data_Download.merge_era5 import download_and_merge_era5_solar
from Data_Download.utility import find_missing_dates

# 전체 프로세스
df = download_and_merge_era5_solar(
    start_date="2014-12",
    end_date="2023-01",
    lat=37.257,
    lon=126.983
)

# 중간에 빠진 시간 데이터가 있는지 확인
find_missing_dates(df, "valid_time_kst", freq='h')

# 저장
df.to_csv("data.csv", index=False)
print(df.head())