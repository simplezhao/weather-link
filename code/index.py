import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import random
from third_party.alicloudapi.weather import JMWeather
from third_party.quotes.daodejing import dao
import arrow

appcode = os.getenv("APPCODE")

jm_client = JMWeather(appcode)
app = FastAPI()


@app.get('/weather')
async def weather(city: str = '北京'):

    weather_info = jm_client.get_weather_by_city(city)
    update_time = arrow.now(tz="Asia/Shanghai").format('hh:mm A')
    data = f"""
        <!doctype html>
        <html lang="zh" data-hairline="true" data-theme="light">
            <head>
                <meta charset="utf-8"/>
                <meta data-rh="true" property="og:title" content="{weather_info['temperature']}℃ | {update_time} | 
                我在{weather_info['city']} | {random.choice(dao)}"/> 
                <meta data-rh="true" property="og:url" content=""/>
                <meta data-rh="true" property="og:description" content="出自道德经"/>
                <meta data-rh="true" property="og:image" content="{weather_info['weather_pic']}"/>
                <meta data-rh="true" property="og:type" content="document"/>
                <meta data-rh="true" property="og:site_name" content="weather-info"/>
                <link crossorigin="" rel="shortcut icon" type="image/x-icon" href="{weather_info['weather_pic']}"/>
            </head>
            <body>
                
            </body>
        </html>

        """
    return HTMLResponse(data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
