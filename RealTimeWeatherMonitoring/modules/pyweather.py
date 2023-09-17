import python_weather

import asyncio

""" _summary_:
        This function returns the weather of a city.
    _parameters_:
        city: str
            The city to get the weather of.
    _returns_:
        weather: python_weather.Weather
            The weather of the city.                
"""

async def get_weather(city):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city)
    
    print(weather) 
    return weather

if __name__ == "__main__":
    asyncio.run(get_weather("New York"))