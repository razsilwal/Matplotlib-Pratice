import matplotlib.pyplot as plt 
# from matplotlib import pyplot as plt # this is same as above 

## Bar Graph

# department = ["Computer Science","Electrical", "Civil", "Mechanical", "Aerospace", "Eomputer Engineering", "AI/ML", "Physics", "Economics"]

# no_of_students = [120, 60, 90, 80, 40, 50, 30, 60, 5]

# plt.style.use("fivethirtyeight")

# plt.bar(department, no_of_students, edgecolor = "black")

# for i, value in enumerate(no_of_students):
#     plt.text(i, value + 1, str(value), ha = "center")

# plt.xlabel("Departments")
# plt.ylabel("No of Students")
# plt.title("No of Students in each department")
# plt.tight_layout()

# plt.show()

# ----------------#
# --- Histogram --#

ages = [18, 19, 20, 21, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32]

plt.style.use("fivethirtyeight")

plt.hist(ages, bins=7, edgecolor = "black")

plt.xlabel("Age Range")
plt.ylabel("Number of Students")
plt.title("Age Distribution of Students")

plt.tight_layout()
plt.show()

## tommorrow study 
## Horizontal bar charts, Fill between, Stack plots 
# plots on real world data

