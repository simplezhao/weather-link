import requests
from loguru import logger
import json


class JMWeather:
    def __init__(self, appcode):
        self.appcode = appcode
        self.baseurl = 'https://jmweather.market.alicloudapi.com/weather'

    def get_weather(self, path, data):
        """
        获取天气信息
        :param path: 获取方式的地址
        :param data: 查询数据
        :return: 天气数据字典
        """
        resp = requests.post(
            url=self.baseurl + path,
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Authorization": f"APPCODE {self.appcode}",
            },
            data=data

        )
        weather_info = {}
        content = resp.content.decode('utf8')
        code = resp.status_code
        if code == 200:
            content = json.loads(content)
            province = content['data']['province']
            area = content['data']['area']
            city = content['data']['city']
            temperature = content['data']['now']['temperature']
            weather = content['data']['now']['weather']
            weather_pic = content['data']['now']['weather_pic']

            weather_info.update(
                area=area,
                city=city,
                province=province,
                temperature=temperature,
                weather=weather,
                weather_pic=weather_pic
            )
            return weather_info

        elif code == 400:
            content = json.loads(content)
            city = content['msg']
            area = None
            weather_info.update(
                city=city,
                area=area
            )

        else:
            logger.error(f'get error with code: {code}, with reason: {content}')
            weather_info.update(
                city=None,
                area=None
            )
        return weather_info

    def get_weather_by_ip(self, ip: str):
        weather_info = self.get_weather('/query/by-area', data={"ip": ip})
        return weather_info

    def get_weather_by_city(self, city: str):

        if city[-1] in ["市", "区"] and len(city) > 2:
            city = city[:-1]

        weather_info = self.get_weather('/query/by-area', data={"area": city})
        return weather_info












