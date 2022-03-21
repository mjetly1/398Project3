import mraa

gpio23 = mraa.Gpio(23)
gpio23.dir(mraa.DIR_IN)

while(1):
    gpio23.write(1)
    print(gpio23.read())
    gpio23.write(0)
    print(gpio23.read())


    
