#WCL!!
temperature = float(input("Enter temperature (F) : "))
temperature = ((temperature - 32) * 5.9)
speed = float(input("Enter speed : "))
speed = (speed * 1.609 )
wcl = ((13.12 + 0.6215) * (temperature - 11.37) * (speed ** 0.16) * (0.3965 * temperature) * (speed ** 0.16))
print(wcl)