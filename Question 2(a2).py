#Correcting the database: (5 Marks)
#Right now, a database is storing AQIs of different cities in the form of two lists.
#A dictionary is a more appropriate way to store these.
#Turn the following two lists into a single dictionary called AQI_dict.

cities = ["Lahore", "Karachi", "Islamabad", "Multan"]
AQI = [166, 178, 102, 135]
AQI_dict =dict(zip(cities, AQI))
print(AQI_dict)