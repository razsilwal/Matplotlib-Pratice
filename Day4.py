# import matplotlib.pyplot as plt
# import pandas as pd

# plt.style.use("fivethirtyeight")

# data = pd.read_csv("data2Day4.csv")

# ages = data['Age']
# dev_salaries = data['All_Devs']
# python_salaries = data['Python']
# javascript_salaries = data['JavaScript']

# plt.plot(ages, dev_salaries, linestyle = "--", label = "Full Stack Devs")

# plt.plot(ages, python_salaries, label = "Python Devs" )

# # plt.fill_between(ages, dev_salaries, interpolate = True, color = 'red', label = "Fill", alpha = 0.3)

# plt.fill_between(ages, python_salaries, dev_salaries, where = (python_salaries > dev_salaries), interpolate = True, color = 'blue', alpha = 0.25, label = "Above Full Stack")
# plt.fill_between(ages, python_salaries, dev_salaries, where = (python_salaries <= dev_salaries), interpolate = True, color = "red", alpha = 0.25, label = "Below Full Stack")

# plt.legend()
# plt.title("Median Salaries in USD by Age")
# plt.xlabel("Ages")
# plt.ylabel("Median Salaries in USD")

# plt.tight_layout()
# plt.show()


# --Dataset 1 Day 4--#
# -------------------#
 
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter 

plt.style.use("fivethirtyeight")

data = pd.read_csv("dataDay4.csv")
ids = data["Responder_id"]
lang_response = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_response:
    language_counter.update(response.split(";"))

# print(language_counter)

most_repeted = language_counter.most_common(10)
# print(most_repeted)

languages = []

popularity = []

for item in most_repeted:
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Top 10 most Popular languages")
plt.xlabel("No of people who uses")

plt.tight_layout()
plt.show()