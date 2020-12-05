
while True:
    print("Guess my lucky number.")
    lucky=int(input())
    if lucky==13:
        print("Wow you guessed it!")
        break
    else:
        print("Sorry its not",lucky)


