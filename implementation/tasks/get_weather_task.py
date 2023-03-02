from core.task_base import TaskBase
from implementation.api_weather.api_client import YandexWeatherAPI
from implementation.api_weather.data_classes import Forecast


class GetWeatherTask(TaskBase):
    """Класс получения прогноза погоды по Москвe."""

    def __init__(self, param: str):
        super().__init__(param)

    @property
    def name(self):
        return 'get weather'

    def execute(self) -> None:
        weather_dict = {}
        forecasts = Forecast.parse_obj(YandexWeatherAPI().get_forecasting())
        type(forecasts)
        weather = forecasts.forecasts
        for weather_day in weather:
            weather_dict[weather_day.date] = weather_day.hours
        with open(self.param, 'w') as f:
            f.write(f'{weather_dict}')
        print(f'Create file with weather: {self.param}')
