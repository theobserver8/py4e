fname = input("Enter the file name: ")

if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")

else:
    count = 0
    try:
        fhand = open(fname)

    except:
        print("No se encuentra el archivo: ", fname)
        exit()

    for line in fhand:
        count = count + 1

    print("There were %d subject lines in %s" % (count, fname))