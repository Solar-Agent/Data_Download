import pandas as pd

def generate_month_list(start_date: str, end_date: str) -> list:
    """
    시작 날짜와 끝 날짜를 기준으로 월 리스트를 생성합니다.

    Args:
        start_date (str): 시작 날짜 ("YYYY-MM" 형식)
        end_date (str): 끝 날짜 ("YYYY-MM" 형식)

    Returns:
        list: 월 범위를 나타내는 문자열 리스트 ("YYYY-MM" 형식)
    """
    # 월 범위 생성
    date_range = pd.date_range(start=start_date, end=end_date, freq='MS')  # 'MS'는 월의 시작일을 의미

    # 문자열 포맷으로 변환
    date_list = date_range.strftime('%Y-%m').tolist()

    return date_list

def find_missing_dates(
    df: pd.DataFrame,
    date_column: str,
    freq: str='h',
    verbose: bool=True
) -> list:
    """
    특정 시간 범위 내에서 누락된 날짜/시간을 찾는 함수.

    Args:
        df (pd.DataFrame): 날짜/시간 데이터가 있는 DataFrame
        date_column (str): 날짜/시간 데이터가 있는 컬럼 이름
        freq (str): 시간 간격 ('h' - 1시간, 'D' - 1일 등)

    Returns:
        list: 누락된 날짜/시간 리스트
    """
    # 문자열 형식의 날짜를 datetime 형식으로 변환
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(by=date_column)

    full_range = pd.date_range(start=df[date_column].min(), end=df[date_column].max(), freq=freq)
    missing_dates = full_range.difference(df[date_column]).tolist()

    if verbose:
        print(f"missing dates: {missing_dates}")
        print(f"Total missing dates: {len(missing_dates)}")

    return missing_dates


if __name__ == "__main__":
    print(generate_month_list("2022-10", "2023-02"))
    # 사용 예시:
    data = {'dates': ['2022-01-01 01:00:00', '2022-01-03 03:00:00']}
    df = pd.DataFrame(data)
    # 1시간 단위로 누락된 시간 찾기
    missing_hourly = find_missing_dates(df, 'dates', freq='h')

