def gps(city):
    # Stub implementation, always returning Brisbane's coordinates
    brisbane_coordinates = { "latitude": -27.4689682, "longitude": 153.0234991 }
    return brisbane_coordinates

def search_species(city):
    # Stub im
    #plementation, returning a list of species dictionary
    species_list = [
        {"name": "Koala", "population": 5000},
        {"name": "Kangaroo", "population": 3000},
        {"name": "Platypus", "population": 100},
        {"name": "Shark", "population": 500},
        {"name": "Dolphine", "population": 3500},
        {"name": "Cat", "population": 1200},
    ]
    print (" Here the Brisbane all species:---------- \n",species_list)

# Assert statements to check if Brisbane's coordinates are returned correctly
brisbane_coordinates = gps("Brisbane")
assert brisbane_coordinates == { "latitude": -27.4689682, "longitude": 153.0234991 }


# Test the search_species function
city_species = search_species("Brisbane")
print(city_species)  # Output will be a list of species dictionaries
