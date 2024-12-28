from pydantic import BaseModel

class WeatherResponse(BaseModel):
    temperature: float
    condition: str

class WeatherAPI:
    def get_weather(self, location: str, unit: str = "celsius") -> dict:
        # simulate weather API call
        weather = WeatherResponse(temperature=18, condition="cloudy")
        return weather.dict()