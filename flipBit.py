import mraa

def main():
    
    gpio23 = mraa.Gpio(23)
    gpio23.dir(mraa.DIR_OUT)
    gpio23.write(1)

    while(1):
        value = gpio23.read()
        if value == 1:
            print("1")
            gpio23.write(0)

        else:
            print("0")
            gpio23.write(1)

if __name__ == '__main__' :
    main()


    
