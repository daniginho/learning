print("whats the weather like?")
weather=input()
if weather=="cloudy":
    advice="no sunglasses"
elif weather=="rainy":
    advice="get an unmbrella"
elif weather=="snowy":
    advice="mittens and earmuffs"
else:
    advice="no particular advice"
print(advice)