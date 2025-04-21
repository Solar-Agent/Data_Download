# Data_Download

이 프로젝트는 ERA5 hourly data on single levels에서 태양광 발전량 예측에 중요한 일사량 데이터를 수집하고 전처리하는 기능을 제공합니다.

수집되는 데이터는 태양광 발전량에 영향을 주는 일사량 데이터입니다.
- SSR(surface_solar_radiation_downwards) : 실제 구름 조건에서 지표에 도달한 전체 일사량(직접 복사 + 간접 복사)
- SSRC(surface_solar_radiation_downward_clear_sky) : 구름이 없는 맑은 하늘을 가정한 일사량(직접 복사 + 간접 복사)

## 패키지 설치

```bash
uv pip install cdsapi xarray cfgrib
```

GRIB 파일 처리를 위한 라이브러리 설치 (운영체제에 따라):

```bash
sudo apt-get install libeccodes-dev  # Ubuntu
brew install eccodes  # macOS
```

## 사용 방법

```python
from Data_Download.merge_era5 import download_and_merge_era5_solar

# 2022년 12월부터 2023년 1월까지, 특정 위경도 지역에 대해 데이터 다운로드 및 병합
df = download_and_merge_era5_solar(
    start_date="2022-12",      # 시작 연월 (YYYY-MM)
    end_date="2023-01",        # 종료 연월 (YYYY-MM)
    lat=37.257,                # 위도 (예: 평택 지역)
    lon=126.983                # 경도
)

# 결과 저장
df.to_csv("data.csv", index=False)
```

## 함수 설명
- 위도, 경도는 내부적으로 소수점 둘째 자리 기준 올림/내림 처리하여 0.01° × 0.01° 범위에 대한 데이터를 수집합니다.
- 실제 ERA5 data의 해상도는 0.25° × 0.25°입니다.
- 수집된 .grib 파일은 내부에서 읽어서 pandas.DataFrame으로 정리되고, UTC 시간을 **KST(+9시간)**으로 변환한 컬럼(valid_time_kst)이 포함되어 있습니다.


## 결과 예시

ssr: 실제 구름 조건의 일사량 (J/m²)
ssrc: 맑은 하늘 기준 일사량 (J/m²)

```
 valid_time_kst        ssr          ssrc
5 2022-12-01 09:00:00+00:00   398369.0  3.945422e+05
6 2022-12-01 10:00:00+00:00   838895.0  8.996606e+05
7 2022-12-01 11:00:00+00:00  1168082.0  1.313346e+06
8 2022-12-01 12:00:00+00:00  1306724.0  1.564482e+06
9 2022-12-01 13:00:00+00:00  1298187.0  1.625028e+06
```

## 참고
- ERA5 데이터는 [**Copernicus Climate Data Store (CDS)**](https://cds.climate.copernicus.eu/profile?tab=profile)에서 제공되며,
계정 생성 후 CDS API 키 설정을 먼저 해야 합니다.

- `.cdsapirc` 설정은 사용자 홈 디렉터리에 있어야 합니다.
