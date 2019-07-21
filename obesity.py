import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile("Obes-phys-acti-diet-eng-2014-tab.xls")
# Define the columns to be read
columns1 = ["year", "total", "males", "females"]
data_gender = data.parse(u"7.1", skiprows=4, skipfooter=14, names=columns1)
# Remove the N/A from the data
data_gender.dropna(inplace=True)
data_gender.set_index("year", inplace=True)

# print(data_gender[["year"]])
# Plot all
data_gender.plot()
plt.show()
