# dictionary  = {
#     "bug": "usually an error a human made"
# }


# dictionary["loop"] = "sth that keeps repeating by a constraint"
# print(dictionary)


# for key in dictionary:
#     print(key)
#     print(dictionary[key])
#Challenge 9.1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for student in student_scores:
  score = student_scores[student]
  # grade = student_grades[student]
  if score >= 91 and score <= 100:
    student_grades[student]= "Outstanding"
  elif score >=81 and score <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif score >= 71 and score <= 80:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
           
#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
# print(student_grades)

#challenge 2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, num_visits, cities):
  new_dict = {}
  new_dict["country"] = country
  new_dict['visits'] = num_visits
  new_dict['cities'] = cities
  travel_log.append(new_dict)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print(travel_log[1][1])