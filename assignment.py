#wap to create the favourite movie in the list and print it .then append new movie and print the it
favourite_movie=["3 idiots","john wick "," insterstellar"]
print(favourite_movie)
favourite_movie.append("spider-man")
print(favourite_movie)


#Create a list of integers from 1 to 10 and print it .calculate the sum of all numbers in list and print it 
nums=[]
for i in range(1,11):
    nums.append(i)
print(nums)
sum=0
for num in nums:
    sum+=num
print("the sum of all numbers in list is ",sum)


#to create a tuple of of the days of the week and print it and access the 3rd day of the week and print it
days_of_week=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(days_of_week)
print(days_of_week[2])


#tuples of favourite colors and print it . check if certain color is present in the tuple and print the result 
favourite_colors=("red","blue","green","black")
print(favourite_colors)
color_to_check="blue"
if color_to_check in favourite_colors:
    print(color_to_check,"is present in the tuple")
else:
    print(color_to_check,"is not present in the tuple")


#9 dictionary of books with keys title , author and year print it . update the year and print it 
books={
    "title":"the alchemist",
    "author":"paulo coelho",
    "year":1988

}
print(books)
books["year"]=1993
print(books)



#10 dictionary of fruits as keys and corresponding colors as values and print it .add new color pair to dictionary and print the updated dictionary 
fruits={"Mangoes":"yellow",
        "Apples":"red",
        "grapes":"green"
        

}
print(fruits)
fruits["Orange"]="orange"
print(fruits)

#11 cites name and population numbers and print and remove a city fom dict and print it
cities={"ktm":1100000,
        "POkhara":50000,
        "biratnagar":500670
        }
print(cities)
del cities["biratnagar"]
print(cities)
