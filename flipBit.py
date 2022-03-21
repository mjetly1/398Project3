import mraa

gpio23 = mraa.Gpio(23)
gpio23.dir(mraa.DIR_IN)

while(1):
    print(gpio23.read())


    
