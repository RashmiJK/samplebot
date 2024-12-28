from pydantic import BaseModel

class WeatherResponse(BaseModel):
    temperature: float
    condition: str

class WeatherAPI:
    def get_weather(self, location: str, unit: str = "celsius") -> WeatherResponse:
        # simulate weather API call
        return WeatherResponse(temperature=18, condition="cloudy")