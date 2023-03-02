import json
from http import HTTPStatus
from urllib.request import urlopen


URL_MOSCOW = 'https://code.s3.yandex.net/async-module/moscow-response.json'
ERR_MESSAGE_TEMPLATE = "Something wrong. Please contact with mentor."


class YandexWeatherAPI:
    """
    Base class for requests
    """

    @staticmethod
    def _do_req(url):
        """Base request method"""
        try:
            with urlopen(url) as req:
                resp = req.read().decode("utf-8")
                resp = json.loads(resp)
            if req.status != HTTPStatus.OK:
                raise Exception(
                    "Error during execute request. {}: {}".format(
                        resp.status, resp.reason
                    )
                )
            return resp
        except Exception:
            raise Exception(ERR_MESSAGE_TEMPLATE)

    def get_forecasting(self):
        """
        :return: response data as json
        """
        return self._do_req(URL_MOSCOW)
