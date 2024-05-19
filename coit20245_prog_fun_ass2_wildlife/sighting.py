# wildlife.py
import requests

def get_species_list(coordinate, radius):

    # Unpack coordinates
    latitude, longitude = coordinate

    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={latitude},{longitude},{100000}"

    response = requests.get(url)

    data = response.json()

    species_list = []
    for species in data['SpeciesSightingSummariesContainer']['SpeciesSightingSummary']:
        species_data= species['Species']
        species_list.append(species_data)
        
    return species_list

def get_surveys_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&&circle={coordinate},{radius}"
    response = requests.get(url)
    data = response.json()
    return data



# assert get_surveys_by_species("-16.92,145.777", 100000, "860")


# Testing the function get_surveys_by_species
if __name__ == "__main__":
     # Test case: Retrieving species list for a coordinate and radius
     coordinate = (-16.92, 145.777)
     radius = 100000
     result = get_species_list(coordinate, radius,)
     print(f"Species list for coordinate {coordinate} and radius {radius}: {result}")

    # Additional test cases can be added as needed
