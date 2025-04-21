import xarray as xr
import pandas as pd

def read_era5_solar_grib(grib_file: str="solar_data.grib") -> pd.DataFrame:
    """
    ERA5 .grib 파일에서 표면 순 태양복사량(ssr)과 맑은 하늘 조건의 복사량(ssrc)을 추출하여
    KST 기준 시간으로 변환한 DataFrame을 반환합니다.

    Parameters:
    - grib_file (str): GRIB 파일 경로 (예: "solar_data.grib")

    Returns:
    - pd.DataFrame: [valid_time_kst, ssr, ssrc] 컬럼을 가진 DataFrame
    """
    # cfgrib로 데이터셋 열기
    ds = xr.open_dataset(grib_file, engine="cfgrib", decode_timedelta=True)
    
    # 데이터프레임으로 변환 및 인덱스 초기화
    df = ds.to_dataframe().reset_index()
    
    # 필요한 변수만 추출하고 ssr이 결측치인 행 제거
    df = df[['valid_time', 'ssr', 'ssrc']]
    df = df.dropna(subset=['ssr'])

    # 시간대를 KST로 변환
    df['valid_time'] = pd.to_datetime(df['valid_time'], utc=True)
    df['valid_time_kst'] = df['valid_time'] + pd.Timedelta(hours=9)

    # 최종 컬럼 순서
    return df[['valid_time_kst', 'ssr', 'ssrc']]


if __name__ == "__main__":
    grib_file = "solar_data.grib"
    df = read_era5_solar_grib(grib_file)
    print(df.head())
