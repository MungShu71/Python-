
import json
import csv
from re import T
import time
'''

A2 In this assignment we will read a CSV and a JSON file
and find the most pettable dogs in NYC

Some syntax you will need for this assignment
* Mapping one list to another with list comprehensions:
	[dog[INDEX_BREED_NAME] for dog in dogs]
* Filter one list to a smaller list with list comprehensions:
	[dog for dog in dogs if dog[INDEX_BREED_NAME] == "POODLE"]
* Checking if an element is already in a list: "if elem in my_list"
* Casting a CSVreader to a list
	list(csv.reader(f))

'''

INDEX_BREED_NAME = 0
INDEX_BREED_ALT_NAME = 1
INDEX_BREED_WEIGHT = 4
INDEX_BREED_TEMPERAMENT = 5
INDEX_BREED_PRICE = 6
INDEX_BREED_INTELLIGENCE = 7
INDEX_BREED_WATCHDOG = 8

INDEX_DOG_ID = 0
INDEX_DOG_NAME = 1
INDEX_DOG_SEX = 2
INDEX_DOG_BIRTHYEAR = 3
INDEX_DOG_BREED = 4
INDEX_DOG_ZIPCODE = 6


#---------------------------------
# Helper functions

def is_breed_match(name, query):
	'''
	Test if these breed names match.

		Parameters:
			name (str): a name of a breed
			query (str): a name of a breed
		Returns:
			(bool): True if the name matches or partially matches the query (ignoring case)
					False otherwise
	'''

	

	# Empty strings don't count as a match for this, 
	# because they would occur in *any* other string
	if name == "" or query == "":
		return False
	return  name.upper() in query.upper() or query.upper() in name.upper()

def dog_to_string(dog_data): 
	'''
	Turn a list of dog data into a string that is more human-readable

		Parameters:
			dog_data (list): a list of strings representing data of a single NYC dog
		Returns:
			(str): A string in the format "NAME (BREED) ZIPCODE ATTRIBUTES"
				e.g. "Rocko (CHIHUAHUA) 10035 Inquisitive, Alert, Friendly"
	'''

	try:
		breed = get_breed_data_for_dog(dog_data)
	except:
		breed = None
	attributes = f"({breed[INDEX_BREED_NAME]}:{breed[INDEX_BREED_TEMPERAMENT]})" if breed else ""
	return f"{dog_data[INDEX_DOG_NAME]} ({dog_data[INDEX_DOG_BREED]}) {dog_data[INDEX_DOG_ZIPCODE]} {attributes}"


def read_breed_data(path_to_csv): 
	'''
	Open a CSV file at the given path, read in the lines, and return a list of lists
	representing a  

		Parameters:
			path_to_csv (str): a relative path to the breed information csv file
		Returns:
			(list): a list of lists of str [["Affenpinscher","","Toy"], ...[more breed data]]
	'''

	# TASK 0: load all breed data
	# Given a path to a CSV file
	# Open the file with "open(some_path)" 
	# (you can use the "with" syntax or not)
	# Use the CSV module to create a CSV reader (don't use readlines)
	# Cast it to a list before returning, as CSV reader objects aren't lists yet

	# ** DON'T change the path! **

	# More information here
	a = []
	# (https://realpython.com/python-csv/) 
	with open('dog_breed_characteristics.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		label = True
		
			
		for row in csv_reader:
			a.append([i for i in row])
		
				
	return a


def read_dog_data(path_to_json): 
	'''
	Open a JSON file of dog data at the given path, 
	read in the lines, and return a list of lists representing the dogs of NYC 

		Parameters:
			path_to_json (str): a relative path to the nyc dog json file
		Returns:
			(list): a list of lists of str [[Rocko, Chihuahua,...],...[some dog data]]
	'''
	f = open('nyc_dogs.json')
	data = json.load(f)
	a = []
	for i in data:
		a.append([c for c in i])
	# TASK 1: load all dog data
	# Given a path to a JSON file
	# Open the file 
	# Use the JSON module load the files contents into data (in this case, a list)
	# Return the list 

	# More on how to use Python's json library
	# https://www.geeksforgeeks.org/json-load-in-python/


	return a


	
def get_breed_data_by_name(breeds, query_name):
	'''
	Get the first list of breed information e.g. ["Corgi","","Herding"...] in breeds
		that has  a name that matches or partially matches query_name, 
		(** use the "is_breed_match" helper function **)
		or returns None, if the query isn't found
		e.g. "poodle" => ['Poodle', '', 'Non Sporting', 'Gun', '26', 'Active, Alert, Faithful, Instinctual, Intelligent, Trainable', '1250', '2', '4', '', '', '1', '7']
	

		Parameters:
			query_name (str): a name of a breed ("CHIHUAHUA", "Welsh corgi")
		Returns:
			(list): a list of str ["Corgi","","Herding"...] with a breed name that matches the query
			None: if no match is found
	'''
	
	for i in breeds[1::]:
		if i[0].upper() == query_name.upper() or i[1].upper() == query_name.upper():
			return i
		

	# This is an assert that will fail if something unexpected is passed as an argument to this function
	# Asserts like these will inform you if a user calls this function incorrectly
	assert isinstance(query_name, str), f"expected 'query_name' to be str, got {type(query_name)}{query_name}"
	
	# TASK 2: get breed data by breed name
	# Look at each breed in breeds 
	# Use the "is_breed_match" helper function above 
	#   to compare this breed's name agains the query name
	# When you find a breed who's name matches the query, return the breed's data (a list)
	# (breeds and dogs are in the "global scope" so you can access them from any code)
	return None
	

def get_breed_data_for_dog(breeds, dog_data):
	'''
	Get the first list of breed information e.g. ["Corgi","","Herding"...] in breeds
		that represents the 

		Parameters:
			dog_data (str): a list representing a single dog: ["Rocko", "Chihuahua",...]
		Returns:
			(list): a list of str ["Chihuahua","","Toy","Companion"...] 
			with a breed name that matches the breed name in the dog_data
			None: if no match is found
	'''
	for i in breeds[1::]:
		if i[0].upper() in dog_data[INDEX_DOG_BREED].upper():
			return i

	assert isinstance(dog_data, list), f"expected 'dog_data' to be list, got {type(dog_data)}{dog_data}"
	assert len(dog_data) == 10, f"expected 'dog_data' to have 10 elements (thats the format of the nyc data)"


	# TASK 3: get breed data by individual dog
	# You just wrote a "get_breed_data_by_name" function that gets breed data if you have a breed name
	# Now we have dog_data that contains a lot of data about a dog, including its breed.
	# Can you combine this information with the previous function to solve this in one or two lines?
	
	return None
	

def get_missing_breeds(dogs, breeds):
	'''
	Returns a list of breeds that are listed in the dogs, 
		but do not have breed data in breeds

		Parameters:
			None
		Returns:
			(list): a list of str ["Pitbull","Zoodle","PIT AMERICAN","UNKNOWN"...] 
			of all dogs in dogs that don't have breed-data matches on breeds
	'''

	"""
	EXAMPLE: An example of a simple list comprehension that gets each dog's breed that doesn't appear in the 
	list of dog breeds

	You can see how an existing function can be used to filter a list of dogs
		into just the dogs we care about, and can them map that filter into 
		just the data (breed names) that we care about
	"""
	
	return [dog[INDEX_DOG_BREED] for dog in dogs if not get_breed_data_for_dog(dog)]

def get_dogs_by_breed(dogs, breed_name):
	'''
	Returns a list of all dogs that have a breed listed that is
		a match for this breed name (using is_breed_match)

		Parameters:
			breed_name (str): a name of a breed ("Pitbull","Zoodle")
		Returns:
			(list): a list of lists of str, (e.g. a list of all dog-data records)
				that are all dogs in dogs who have a match for that breed
	'''

	assert isinstance(breed_name, str), f"expected 'breed_name' to be str, got {type(breed_name)}{breed_name}"

	# TASK 4: get dogs by breed name
	# Return a list of all dog-records (ie, a list of lists) 
	# containing each dog whose breed matches this query (use "is_breed_match")
	# Hint: the next two tasks can be done in a single-line list comprehension
	# a = []
	# [a.append(i) for i in dogs if is_breed_match(i[INDEX_DOG_BREED], breed_name)]
	return [i for i in dogs if is_breed_match(i[INDEX_DOG_BREED], breed_name)]

def get_names_by_breed(dogs, breed_name):
	'''
	Returns a SORTED list of all dogs names that have a breed listed that is
		a match for this breed name (using is_breed_match)

		Parameters:
			breed_name (str): a name of a breed (e.g. "Pitbull")
		Returns:
			(list): a SORTED list of strings of the names 
			of dogs with that breed["Alphonso", "Butter", "Cordelia"....]
	'''

	assert isinstance(breed_name, str), f"expected 'breed_name' to be str, got {type(breed_name)}{breed_name}"

	# TASK 5: for a given breed, return a sorted list of all dog' names with that breed
	# Return an alphabetically sorted list of all the individual dog's names for this breed (use "is_breed_match")
	# Hint: sorted(some_list) will return a sorted copy of a list (if strings, this will sort them alphabetically)

	return sorted([i[INDEX_DOG_NAME] for i in dogs if is_breed_match(i[INDEX_DOG_BREED], breed_name)])

def has_temperament(breed_data, adjective):
	'''
	Returns if list representing a breed's data contains a particular adjective (case-sensitive)
		
		ie ["Chihuahua",...,"Courageous, Devoted, Lively, Intelligent, Quick",...], "Quick" => True
		   ["Chihuahua",...,"Courageous, Devoted, Lively, Intelligent, Quick",...], "Silly" => False


		Parameters:
			breed_data (list or None): a list of str representing a breed
			adjective (str): an adjective "Devoted", "Quick", etc
		Returns:
			(bool)
				False if the breed_data is None
				True if that breed's temperament contains that adjective
				False if the breed's temperament doesn't contain that adjective
	'''


	assert isinstance(breed_data, list) or breed_data == None, f"expected 'breed_data' to be list or None, got {type(breed_data)}: {breed_data}"
	assert isinstance(adjective, str), f"expected 'adjective' to be str, got {type(adjective)}: {adjective}"
	
	# TASK 6: return True/False if a breed has a particular personality trait
	# Hint: "some_value in some_string" will return True if that value can be found in the string
	# This function will also be a useful helper function in Task 7 and Task 10
	# return (adjective in  breed_data[5] )
	if breed_data is None: return False
	return True if adjective in breed_data[5] else False
	

def get_breeds_by_temperament(breeds, adjective):
	'''
	Returns of list of all breeds in breeds that have this adjective in their temperament 
		(breeds are lists of str, ie ["Chihuahua",...,"Courageous, Devoted, Lively, Intelligent, Quick",...])
		
		Parameters:
			adjective (str): an adjective "Devoted", "Quick", etc
		Returns:
			(list) a list of breeds
	'''
	assert isinstance(adjective, str), f"expected 'adjective' to be str, got {type(adjective)}: {adjective}"
	
	# Task 7: Use another list comprehension to get a list of all breeds that have a given temperament
	# You can do this in just one line!
	# a = []
	# [a.append(i[0]) for i in breeds[1::] if has_temperament(i, adjective) == True]
	return [i for i in breeds[1::] if has_temperament(i, adjective) == True]

def list_all_zip_codes(dogs):
	'''
	Returns a sorted list of all unique (no duplicates) zip codes in the list of NYC dogs
		
		Parameters:
			None
		Returns:
			(list): a list of str e.g.["10001", "10012", "100022"...] 
			of each zip code in the dogs dataset
	'''

	# Task 8: return a list of all zip codes in the dogs database, sorted.  
	# Keep a list of zipcodes
	# For each dog in all dogs, get its zip code
	# If that zip code *doesn't* already exist in the list, add it 
	#   (so each zip code will only be in the list once)
	# Return a sorted version of the list ("sorted(some_list)" => a sorted copy of the list!)

	# Hint: "some_value in some_string" will return True if that value can be found in the list, 
	#  just like using it for strings in has_attribute()
	s = set()
	for i in dogs:
		s.add(i[6])
		
	return sorted(list(s))
	# a = []
	# for i in dogs:
	# 	a.append(i[6])
	# return a


def list_breeds(dogs):
	'''
	Returns a sorted list of all unique (no duplicates) dog breeds in the list of NYC dogs
		
		Parameters:
			None
		Returns:
			(list): a SORTED list of str e.g.["Australian Cattledog", "Beagle", "Bloodhound", Corgi"...] 
			of each unique breed in the dogs dataset
	'''

	assert isinstance(dogs, list), f"expected 'dogs' to be list, got {type(dogs)}: {dogs}"
	
	# Task 9: return a list of all unique breed nams in this list of dogs, sorted alphabetically
	# Very similar to Task 8!
	s = set()
	for i in dogs:
		s.add(i[INDEX_DOG_BREED])
	return sorted(list(s))

	return []

def search_dogs(dogs, breeds, zip_code=None,positive_traits=[],negative_traits=[],name=None,breed=None):
	'''
	Returns a sorted list of all dogs in the dogs set that pass the provided filters
		
		Parameters:
			zip_code (str): if provided, the zipcode the dog must have
			positive_traits (list): the dog's breed temperament must contain ALL of these
			negative_traits (list): the dog's breed temperament must contain NONE of these
			name (str): if provided, the dog's name must match this (case insensitive)
			breed (str): if provided, the dog's name must match this (using is_breed_match)
		Returns:
			(list): a list of dogs (each dog is a list of str) that match the filters
	'''
	
	# Task 10: the big one!
	# Implement the "dog_is_match" helper function. 
	# This function will check a *single dog* against all of the tests in the optional parameters
	# Then we can use that function in a single list comprehension to return all the dogs that match it

	# This is our most advanced function. It has *optional* parameters, 
	# which means that any of these parameters may be provided by the function call:
	# Dogs named charlie: search_dogs(name="charlie") 
	# Dogs named peaches who are boxers search_dogs(breed="boxer", name="peaches") 
	# Dogs named peaches in zip code 11219 search_dogs(name="peaches", zip="11219")
	# Dogs with breeds that have the properties friendly and curious search_dogs(positive_traits=["curious", "friendly"])
	# Dogs with breeds that are friendly and curious but not energetic or clownish
	# 	 search_dogs(positive_traits=["curious", "friendly"], negative_trait=["energetic", "clownish"])

	def dog_is_match(dog):
		
		if name:
			if dog[1].upper() != name.upper():
				return False
		if breed:
			if not is_breed_match(dog[4], breed):
				return False
		if zip_code:
			if dog[6] != zip_code:
				return False

		if positive_traits:
			x = get_breed_data_for_dog(breeds,dog)
			for i in positive_traits:
				if not has_temperament(x,i):
					return False
		if negative_traits:
			c = get_breed_data_for_dog(breeds,dog)
			# print(c)
			for i in negative_traits:
				if has_temperament(c,i):
					return False
					
		
			
		return True
		# Check this dog against all of the tests. 
		# If the dog fails any test, return False
		# If you get to the end of the function and the dog has passed all tests
		#  return True
		# If the value of name, zip_code, or breed is None, you can skip those tests
		# For the positive and negative tests, 
		#	look at each adjective in the given list
		# 	for the positive traits, return False if any adjective *isn't* in the breed's temperament
		# 	for the negative traits, return False if any adjective *is* in the breed's temperament
		# (Note that this means that "unknown" breeds can pass negative traits)
	

	return [dog for dog in dogs if dog_is_match(dog)]
	

if __name__ == "__main__":

	"""
	As with A1, __main__ is your scratchpad and testing place.
	You can run functions, print the output, write asserts 
	and comment-out things that you are not currently working on
	"""

	path_to_breed_characteristics = "dog_breed_characteristics.csv"
	path_to_nyc_dogs = "nyc_dogs.json"

	breeds = read_breed_data(path_to_breed_characteristics)
	# print(breeds)
	dogs = read_dog_data(path_to_nyc_dogs)
	
	print("\n--------------------\nLoading data")


	assert isinstance(breeds,list), "breeds should be a list"
	assert len(breeds)>0, "breeds should have at least one entry, are you loading the data yet?"
	assert isinstance(breeds[0],list), "breeds should be a list of lists"
	assert isinstance(breeds[0][1],str), "breeds should be a list of lists of strings"
	assert len(dogs)>0, "breeds should have at least one entry"
	assert isinstance(dogs[0],list), "dogs should be a list of lists"
	assert isinstance(dogs[0][1],str), "dogs should be a list of lists of strings"


	# The labels
	print("\nLabels for the breeds\n", breeds[0])
	# The first line of data
	print("\nFirst breed\n", breeds[1])

	# The first line of data (the dog data doesnt have labels)
	print("\nFirst dog\n", dogs[0])
	
	# Test TASK 1 and TASK 2
	print(f"\nThere are {len(breeds)} breeds and {len(dogs)} dogs in this dataset")

	print("\n--------------------\nGetting data about breeds")
	print("\nPoodle breed data:", get_breed_data_by_name(breeds, "POODLE"))
	print("\nWire Haired Fox Terrier:", get_breed_data_by_name(breeds, "Wire Haired Fox Terrier"))
	print("\nZoodle data:", get_breed_data_by_name(breeds, "ZOODLE"))
	assert isinstance(get_breed_data_by_name(breeds, "POODLE"), list), "getting the breed of POODLE should return a list"
	assert get_breed_data_by_name(breeds, "ZOODLE") == None, "getting the breed of ZOODLE should return None"

	print("\n--------------------\nGetting data about dogs")
	# # Test TASK 3
	rocko = dogs[1]
	print("\nThe second dog in the dataset is Rocko:\n", rocko)
	rocko_breed_data = get_breed_data_for_dog(breeds, rocko)
	print("\nRocko's breed info:", rocko_breed_data)
	assert rocko_breed_data[INDEX_BREED_NAME] == 'Chihuahua', "Rocko's breed data should list him as a 'Chihuahua' breed"

	# Test TASK 4
	mastiffs_found = get_dogs_by_breed(dogs, "mastiff")
	print(f"\nMastiffs found {len(mastiffs_found)}: ")
	assert isinstance(mastiffs_found, list), "Get dogs by breed should return a list"
	assert len(mastiffs_found) == 5, "There are 5 mastiffs (Kevin, Alfonso, Princess, Butter, Massimo)"
	for dog in mastiffs_found:
		print(f"{dog[INDEX_DOG_NAME]} ({dog[INDEX_DOG_BREED]}) is a mastiff")

	zoodles_found = get_dogs_by_breed(dogs, "zoodle")
	assert len(zoodles_found) == 0, f"There should be no zoodles in the data, found {len(zoodles_found)}"
	
	# # Test TASK 5
	corgi_names = get_names_by_breed(dogs, "corgi")
	print("\nCorgi names: ", corgi_names)
	assert len(corgi_names) == 15, f"There should be 15 corgis, you found {len(corgi_names)}"
	assert corgi_names[0] == "BADGER", f"If sorted, the first corgi should be 'BADGER', not {corgi_names[0]}"
	

	print("\n--------------------\nGetting data about breed tempraments")
	# # Test TASK 6
	affenpinscher = breeds[1]
	print(has_temperament(None, "Friendly"))
	print(has_temperament(affenpinscher, "Curious"))
	assert has_temperament(affenpinscher, "Curious"), f"Affenpinscher should have temperament Curious"
	assert not has_temperament(affenpinscher, "Friendly"), f"Affenpinscher should not have temperament Friendly"
	assert not has_temperament(None, "Friendly"), f"None should not have temperament Friendly"
	
	# # Test TASK 7
	clown_breeds = get_breeds_by_temperament(breeds, "Clownish")
	print(f"\nClownish breeds:")
	for breed in clown_breeds:
		# print(breed)
		print(f"\t{breed[INDEX_BREED_NAME]} ({breed[INDEX_BREED_TEMPERAMENT]})")
	assert len(clown_breeds) == 4, f"There should be 4 clownish breeds in this dataset"	

	psychic_breeds = get_breeds_by_temperament(breeds, "Psychic")
	print(f"\nPsychic breeds:", psychic_breeds)
	assert len(psychic_breeds) == 0, f"There should be 0 psychic breeds in this dataset"	

	# # Test TASK 8
	zipcodes = list_all_zip_codes(dogs)
	print(f"{len(zipcodes)} zip codes found {zipcodes[0]}-{zipcodes[-1]}", )
	
	assert len(zipcodes) == 188, f"there are 188 zipcodes in this dataset, you found {len(zipcodes)}"
	assert "10035" in zipcodes, "10035 should be in the zipcodes"
	assert zipcodes[-1]=="7733", f"7733 is the last zipcode, you found {zipcodes[-1]}"

	# Test TASK 9
	# Take a *small slice* of all the dog data
	# Use this for the next few tasks, to avoid dealing with ALL the dog data
	print("\n--------------------\nPracticing queries on smaller datasets\n")
	
	test_dogs = dogs[0:10]
	test_dog_breeds = list_breeds(test_dogs)
	print(f"{len(test_dog_breeds)} breeds in this dataset\n", test_dog_breeds)
	print('----------------')
	assert "Pug" in test_dog_breeds, "Pug should be in list of breeds found in this test data"
	assert len(test_dog_breeds) == 8, "8 different breeds should have been found in this test data"

	# Test TASK 10
	print([dog_to_string(dog) for dog in search_dogs(test_dogs,  breeds, zip_code="10007")])
	

	
	print([dog_to_string(dog) for dog in search_dogs(test_dogs,  breeds, positive_traits=["Devoted", "Intelligent", "Gentle", "Reserved"])])
	print([dog_to_string(dog) for dog in search_dogs(test_dogs,  breeds, positive_traits=["Devoted", "Gentle"], negative_traits=["Intelligent"])])
	
	# Task 10

	# Finds only chihuahuas
	print(search_dogs(test_dogs, breeds, breed="chihuahua"))

	print('----------------')
	
	# # Finds two unknown and two Labradors
	print(search_dogs(test_dogs, breeds,negative_traits=["Courageous", "Calm", "Faithful"])) 
	print('----------------')
	
	# Finds Rocko
	print(search_dogs(test_dogs, breeds, name="Rocko"))
	print(search_dogs(test_dogs, breeds, zip_code="10035"))


	print("\n--------------------\nSearching on the full datasets\n")
	
	# Spaniels in Forest Park, Queens
	spaniels_of_queens = search_dogs(dogs, breeds, breed="spaniel", zip_code="11375")
	print("\nSpaniels of Queens:\n", spaniels_of_queens)
	assert len(spaniels_of_queens) == 3, f"There should be 3 spaniels in 11375"	

	# # Loving dogs named "baby"
	baby_dogs = search_dogs(dogs, breeds, name="baby", positive_traits=["Loving"])
		
	print("\nLoving babies:\n", [dog_to_string(dog) for dog in baby_dogs])
	print([dog_to_string(dog) for dog in baby_dogs])
	assert len(baby_dogs) == 2, f"There should be 2 loving dogs named Baby"	

	# # Tiny dogs who can chill
	tiny_dogs = search_dogs(dogs, breeds, name="tiny", negative_traits=["Active"])
	print("\nTiny chill dogs:\n", tiny_dogs)
	assert len(tiny_dogs) == 2, f"There should be 2 non-active dogs named Tiny"	
	
	


	
	# 