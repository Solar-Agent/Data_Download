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

if __name__ == "__main__":
    print(generate_month_list("2022-10", "2023-02"))
