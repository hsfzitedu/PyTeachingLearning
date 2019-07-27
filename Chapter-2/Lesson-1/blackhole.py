m = 5300
lightspeed = 300000
days_of_year = 365
hours_per_day = 24
seconds_per_hour = 60 * 60

ly = lightspeed * days_of_year * hours_per_day * seconds_per_hour


print("Distance of M87* = %d Km" %(ly * m))
print("Distance of M87* = {0:>50,} Km".format(ly * m))
print("Distance of M87* = {0:.5E} Km".format(ly * m))

data_of_photo = 4
KB = 2**10
MB = 2**10 * KB
GB = 2**10 * MB
TB = 2**10 * GB
PB = 2**10 * TB

print("Data of the photo = %d bytes" %(data_of_photo * PB))
print("Data of the photo = {0:,} bytes".format(data_of_photo * PB))



