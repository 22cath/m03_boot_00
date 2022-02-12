def countdown(e):
    print("{},".format(e), end="")
    if e>0:
        countdown(e-1)
    
countdown(10)
