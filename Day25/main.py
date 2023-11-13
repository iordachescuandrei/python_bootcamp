#goal of the project is to count how many squirrels with a specific color are int 2018_Central_Park... file
#once the count is done, build another csv file as a summary report.
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data['Primary Fur Color']=="Gray"])
red = len(data[data['Primary Fur Color']=="Cinnamon"])
black = len(data[data['Primary Fur Color']=="Black"])


print (gray)
print (red)
print (black)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirel_count.csv")