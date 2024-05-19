# This is all about Task 7
import requests

def gps_coordinate(city):

    base_url = f"https://us1.locationiq.com/v1/search?key=pk.37e94aa3017ca984d06aff04b69037ef&q={city}&format=json&"
    
    response = requests.get(base_url)
    # response.raise_for_status()
    data = response.json()
    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return {'latitude': latitude, 'longitude': longitude}
    else:
        return None
# Uncomment the following lines for testing

# Testing the gps_coordinate function
# assert gps_coordinate("Cairns") == {'latitude': -16.9206657, 'longitude': 145.7721854}
# assert gps_coordinate("Queensland") == {'latitude': -17.1022281, 'longitude': 145.7650465401662}

user_input=input("enter the city name:")
city=user_input
print(gps_coordinate(city))
