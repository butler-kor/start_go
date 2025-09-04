import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

form_class = uic.loadUiType("weather.ui")[0]  #weather.ui 를 불러옵니다.


weather_apikey = "8aeac4a34033dddda3560c8df1873c4b"  #나의 API 키

class WeatherApp(QMainWindow, form_class):# 선생님께 물어 볼 것  밑에 DEF 를 왜 저렇게 써야 하는지 모르겟음
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_weather.clicked.connect(self.get_weather) #이것도 그냥 보고 쓴 것 왜 이렇게 써야 하는지 물어 볼 것

    def get_weather(self):
        city = self.city_input.text().strip()  # 도시명을 입력하는 것
        if not city: # 만약 도시 가 없다면
            QMessageBox.warning(self, "입력 오류", "도시 이름을 입력하세요.")
            return

        lang = "kr"       # 언어는 한국어로 함
        units = "metric"  # 온도는 섭씨로 함
        weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_apikey}&lang={lang}&units={units}"
#나의 api 주소를 이용하여 도시명 , 언어 / 온도를 구하는 방식
        try:
            response = requests.get(weather_api).json()

            if response.get("cod") != 200:
                self.result_label.setText("❌ 도시 정보를 불러올 수 없습니다.")
                return

            # 데이터 추출
            weather = response["weather"][0]["description"]
            temp = response["main"]["temp"]
            feels_like = response["main"]["feels_like"]
            humidity = response["main"]["humidity"]
            country = response["sys"]["country"]

            # 결과 문자열
            result_text = (
                f"📍 도시: {city}, {country}\n"
                f"🌤 날씨: {weather}\n"
                f"🌡 현재 온도: {temp}℃ (체감 {feels_like}℃)\n"
                f"💧 습도: {humidity}%"
            )
            self.result_label.setText(result_text)

        except Exception as e:
            QMessageBox.critical(self, "에러 발생", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WeatherApp()
    myWindow.show()
    sys.exit(app.exec_())
