import datetime

def main():
    time = datetime.datetime.now().strftime("%H:%M %d/%m/%Y")
    print(time)

if __name__ == '__main__':
    pass
else:
    main()