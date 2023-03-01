from core.task_base import TaskBase
from implementation.api_weather.api_client import YandexWeatherAPI
from scheduler_config import get_logger
from implementation.api_weather.data_classes import Forecast

logger = get_logger()


class GetWeatherTask(TaskBase):
    def __init__(self, param=None):
        super().__init__(param)

    @property
    def name(self):
        return 'get weather'

    def execute(self):
        weather_dict = {}
        forecasts = Forecast.parse_obj(YandexWeatherAPI().get_forecasting())
        type(forecasts)
        weather = forecasts.forecasts
        for weather_day in weather:
            weather_dict[weather_day.date] = weather_day.hours
        with open(f'{self.param}', 'w') as f:
            f.write(f'{weather_dict}')
        print(f'Create file with weather: {self.param}')
        logger.info('Finished getting weather forecast.')
