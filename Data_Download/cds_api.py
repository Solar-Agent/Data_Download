import cdsapi
import calendar
import math

def download_era5_solar(
    year: int, month: int,
    lat: float, lon: float,
    file_name: str="solar_data.grib"
) -> None:
    """
    ERA5에서 surface solar radiation 데이터를 다운로드합니다.

    Parameters:
    - year (int): 연도 (예: 2022)
    - month (int): 월 (1~12)
    - lat (float): 위도 (예: 37.255)
    - lon (float): 경도 (예: 126.985)
    - file_name (str): 저장할 파일 이름 (예: "output.grib")
    """

    # 해당 월의 전체 날짜 리스트 생성
    num_days = calendar.monthrange(year, month)[1]
    days = [f"{day:02d}" for day in range(1, num_days + 1)]
    year_str = str(year)
    month_str = f"{month:02d}"

    # 모든 시간 리스트
    hours = [f"{h:02d}:00" for h in range(24)]

    # 좌표 소수점 둘째자리 기준으로 내림/올림 처리
    north = math.ceil(lat * 100) / 100  # 위도 올림
    south = math.floor(lat * 100) / 100  # 위도 내림
    west = math.floor(lon * 100) / 100  # 경도 내림
    east = math.ceil(lon * 100) / 100  # 경도 올림

    area = [north, west, south, east]

    # CDS 요청
    client = cdsapi.Client()
    client.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": [
                "surface_net_solar_radiation",
                "surface_net_solar_radiation_clear_sky"
            ],
            "year": year_str,
            "month": month_str,
            "day": days,
            "time": hours,
            "data_format": "grib",
            "download_format": "unarchived",
            "area": area
        },
        file_name
    )

if __name__ == "__main__":
    download_era5_solar(year=2022, month=2, lat=37.257, lon=126.983, file_name="solar_data.grib")
