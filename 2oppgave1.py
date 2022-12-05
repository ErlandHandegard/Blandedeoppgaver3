import matplotlib.pyplot as plt

yverdier = [5, 3, 6, 3, 5, 1, 2, 2, 2, 4, 2, 2, 5, 5, 6, 3, 5, 3, 5, 4, 2, 6,
            1, 4, 2, 3, 3, 3, 5, 5]

plt.hist(yverdier, [1,2,3,4,5,6], align = "left", rwidth=0.5)
plt.show()

sextimeteryverdier = [9.92, 8.46, 9.65, 7.74, 9.33, 8.58, 10.17, 8.03, 9.29, 9.55, 11.36, 9.77, 8.97, 9.68, 8.47, 8.29, 8.25, 9.12, 6.38, 7.94, 11.01, 8.34, 9.52, 7.75, 10.4, 9.9, 10.24, 7.94, 8.14, 9.05, 6.98, 9.08, 9.28, 6.89, 7.54, 8.86, 9.16, 8.32, 10.96, 10.43, 11.23, 10.21, 9.98, 9.96, 9.81, 10.12, 10.36, 9.41, 8.14, 7.91, 7.51, 10.28, 9.48, 9.62, 8.14, 10.49, 9.78, 9.39, 8.16, 8.07, 7.79, 7.39, 8.56, 9.15, 8.23, 9.36, 7.7, 8.21, 9.07, 8.5, 8.3, 9.9, 9.97, 8.82, 8.92, 9.13, 9.87, 9.88, 9.19, 9.45, 8.82, 9.49, 8.71, 9.16, 7.38, 7.05, 8.83, 9.63, 9.41, 9.0, 8.73, 9.13, 8.28, 10.64, 9.48, 8.95, 9.04, 8.81, 9.0, 8.86, 9.62, 8.98, 7.7, 9.32, 9.84, 7.29, 9.92, 10.89, 9.64, 9.74, 9.41, 10.83, 6.22, 9.71, 9.79, 9.75, 9.39, 7.78, 9.02, 9.09]

plt.hist(sextimeteryverdier, 10)
plt.show()

aarstall = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
eksportert = [325, 898, 1421, 2176, 907, 1859, 3174, 1569, 1644, 3373, 4767, 5259, 5607, 5703, 6877, 1570, 4250, 5493, 2501, 7154, 6704, 13847, 9130, 4627, 2180, 3320, 7355, 15166, 16241, 6049, 10109, 8486, 4968, 8962, 4236, 4874, 4412, 8776, 20529, 7162, 15002, 5587, 3842, 15695, 8947, 15320, 17291, 14633, 7123, 14329, 22006, 15140, 21932, 22038, 22151, 21276, 18489, 12309, 24968, 25819]
importert = [-34, -54, -116, -117, -631, -344, -179, -221, -808, -458, -120, -66, -63, -83, -240, -2653, -845, -842, -2039, -1925, -642, -431, -860, -4083, -4212, -2983, -1727, -314, -334, -3274, -1380, -587, -4836, -2300, -13212, -8692, -8046, -6857, -1474, -10760, -5329, -13472, -15334, -3653, -9802, -5284, -3414, -5650, -14673, -11255, -4190, -10135, -6347, -7411, -5741, -6112, -8340, -12353, -4496, -8235]
yverdier = []

for i in range(len(eksportert)):
    yverdier.append(eksportert[i]+importert[i])

plt.plot(aarstall, yverdier)
plt.show()