from code.third_party.alicloudapi.weather import JMWeather
import os

appcode = os.getenv("APPCODE")

client = JMWeather(appcode)


def test_get_weather_ok():
    path = '/query/by-area'
    data = {"area": "北京"}
    result = client.get_weather(path, data)
    assert result['area'] is not None


def test_get_weather_city():
    path = '/query/by-area'
    data = {"area": "北京市"}
    result = client.get_weather(path, data)
    assert result['area'] is None


def test_get_weather_not():
    path = '/query/by-area'
    data = {"area": "beijing"}
    result = client.get_weather(path, data)
    assert result['area'] is None


def test_get_weather_by_area():
    result = client.get_weather_by_city('北京')
    assert result['area'] is None


def test_get_weather_by_ip():
    result = client.get_weather_by_ip("20.139.175.255")
    assert result['area'] is None
