running = True
while running:
    entry = input("enter your age: ")
    try:
        age = int(entry)
    except ValueError:
        print("please entry number of age")
    except KeyboardInterrupt:
        print("oke... you surrender")
    print("your age is..", age)
    assert age <= 100
    print("are you kidding me")
