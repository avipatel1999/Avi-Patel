# sighting.py
from wildlife import  get_species_list ,get_surveys_by_species
from nominatim import gps_coordinate


# Define constant radius
RADIUS = 100000  # 100 km

def gps(city):
    # Call the gps_coordinate function
    return gps_coordinate(city)

""" 8.1 This is for task 8 only to run this task you want to uncommant this part start """
user_input=input("enter the city name:")
city=user_input
""" 8.1 This is for task 8 only to run this task you want to uncommant this part end """


""" 9.1 This is for task 9 and also you have to uncommant 8.1 """
user_input_taxonid=input("Enter the taxonid of species:")
taxonid=user_input_taxonid
""" 9.1 part end"""

coordinate = gps(city)
# print(coordinate)

# print(species_list)


""" 8.2 This is for task 8 only to run this task you want to uncommant this part start"""
if __name__ == "__main__":
    # Test case: Retrieving species list for a coordinate and radius
    coordinate = (coordinate['latitude'],coordinate['longitude'])
    result = get_species_list(coordinate, RADIUS)

    for entry in result:
        if "AcceptedCommonName" in entry:
            print (
                "Taxon ID : "+ str(entry["TaxonID"]) + "\n"
                "name of species : "+ str(entry["AcceptedCommonName"]) + "\n"
                "Pest status : "+ str(entry["PestStatus"]) + "\n")
            
""" 8.2 This is for task 8 only to run this task you want to uncommant this part end"""


    # print(f"\n Species list for coordinate {coordinate} and radius {RADIUS}: {result}")

""" 9.2 This is for task 9 only to run this task you want to uncommant this part start"""
# if __name__ == "__main__":
#     # Test case: Retrieving species list for a coordinate and radius
#     coordinate = (coordinate['latitude'],coordinate['longitude'])
#     result = get_surveys_by_species(coordinate,RADIUS,taxonid)
    
#     # print(f"Species survey for coordinate {coordinate} radius {RADIUS} and taxonid {taxonid}: {result}")

#     survey = []
#     for entry in result["features"]:
#         species_details = entry["properties"]
#         survey.append(species_details)
    
#     for i in survey:
#         locality_details = i["LocalityDetails"]
#         start_date = i["StartDate"]
#         print(f"Animal was sighted in {locality_details} on {start_date}\n")

""" 9.2 This is for task 9 only to run this task you want to uncommant this part end"""
"""And also Task 10 Include in this file"""