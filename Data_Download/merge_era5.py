import pandas as pd

from Data_Download.utility import generate_month_list
from Data_Download.cds_api import download_era5_solar
from Data_Download.extracting_grib import read_era5_solar_grib

def download_and_merge_era5_solar(
    start_date: str,
    end_date: str,
    lat: float,
    lon: float
) -> pd.DataFrame:
    """
    다운로드 및 병합 함수: ERA5 데이터를 특정 범위의 연/월에 따라 다운로드하고 병합합니다.
    
    Args:
        start_date (str): 시작 날짜 ("YYYY-MM" 형식)
        end_date (str): 끝 날짜 ("YYYY-MM" 형식)
        lat (float): 위도
        lon (float): 경도
    
    Returns:
        pd.DataFrame: 병합된 데이터프레임
    """

    df = None  # 초기 데이터프레임 설정

    month_list = generate_month_list(start_date, end_date)

    # 반복적으로 데이터 다운로드 및 병합
    for year_month in month_list:
        print(f"=============={year_month}===============")

        year = int(year_month.split("-")[0])
        month = int(year_month.split("-")[1])

        # 파일명 지정
        file_name = "solar_data.grib"
        
        # 데이터 다운로드
        download_era5_solar(
            year=year,
            month=month,
            lat=lat,
            lon=lon,
            file_name=file_name
        )
        
        # 다운로드된 데이터를 로드
        df_new = read_era5_solar_grib(grib_file=file_name)

        # 데이터 병합
        if df is None:
            df = df_new
        else:
            df = pd.concat([df, df_new])

    return df  # 병합된 데이터프레임 반환