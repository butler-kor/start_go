import requests

# OpenWeatherMap API 키
weather_apikey = '8aeac4a34033dddda3560c8df1873c4b'

# 사용자 입력
city = input("도시 이름을 입력하세요 (예: Seoul, London, Tokyo): ")
lang = "kr"   # 한국어로 결과 보기
units = "metric"  # 섭씨(℃)로 변환

# API 요청 URL 생성
weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_apikey}&lang={lang}&units={units}"

# API 요청
response = requests.get(weather_api).json()

# 오류 처리
if response.get("cod") != 200:
    print("❌ 도시 정보를 불러올 수 없습니다. 도시 이름을 확인하세요.")
else:
    # 필요한 정보 꺼내기
    weather = response["weather"][0]["description"]  # 날씨 설명
    temp = response["main"]["temp"]                 # 현재 온도
    humidity = response["main"]["humidity"]         # 습도
    feels_like = response["main"]["feels_like"]     # 체감 온도
    country = response["sys"]["country"]            # 나라 코드

    # 출력
    print(f"📍 도시: {city}, {country}")
    print(f"🌤 날씨: {weather}")
    print(f"🌡 현재 온도: {temp}℃ (체감 {feels_like}℃)")
    print(f"💧 습도: {humidity}%")
