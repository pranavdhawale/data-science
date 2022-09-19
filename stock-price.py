import cv2
import matplotlib.pyplot as plt

apl_price = [93.96, 112.5, 104.72, 143.63, 169.6, 102.12]
ms_price = [39.05, 50.26, 120.72, 69.98, 53.2, 75.2]
year = [2010, 2011, 2012, 2013, 2014, 2015]

# Line Plotting

# Two different lines to show graph in one plotting
# plt.plot(year,apl_price)
# plt.plot(year,ms_price)

# One single line to show graph in one plotting
plt.plot(year,apl_price,
        year, ms_price)

# Scatter Plotting

plt.scatter(year,apl_price)
plt.scatter(year,ms_price)

# Label the X and Y axis
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()


'''
Addition Tips

We can customize the color or pattern of plotting by adding parameters in ' ' while giving parameters

'''