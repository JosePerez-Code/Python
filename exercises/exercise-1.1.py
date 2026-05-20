# Average duration
other_course_min = 2.5
other_course_max = 7
other_course_average = 4
dalto_course = 1.5

# Raw duration
raw_average = 5
raw_dalto = 3.5

# Difference with other courses 
difference_with_min = 100 - dalto_course / other_course_min * 100
difference_with_max = 100 - dalto_course / other_course_max * 100
difference_with_average = 100 - dalto_course / other_course_average * 100

# calculating the average amount of idle time
empty_time_average = 100 - other_course_average / raw_average * 100
empty_time_dalto = 100 - dalto_course / raw_dalto * 100

# Showing the difference in duration (exercise A)
print(f"The Dalto course takes {difference_with_min}% less time than the fastest one.")
print(f"The Dalto course takes {round(difference_with_max)}% less time than the slowest one.")
print(f"The Dalto course takes {difference_with_average}% less time than the average.")
print("-------------------------------------")

# Showing the amount of empty spaces that are removed (exercise B)
print(f"An average course eliminates {empty_time_average}% of idle time.")
print(f"The dalto course eliminates {round(empty_time_dalto)}% of idle time.")
print("-------------------------------------")

# showing the difference if the courses lasted 10 hours (exercise C)

print(f"Watching 10 hours of the Dalto course is equivalent to watching {other_course_average * 100 // dalto_course / 10} hours of these average course.")
print(f"Watching 10 hours of the Dalto course is equivalent to watching {other_course_min * 100 // dalto_course / 10} hours of these min course.")
print(f"Watching 10 hours of the Dalto course is equivalent to watching {other_course_max * 100 // dalto_course / 10} hours of these max course.")
