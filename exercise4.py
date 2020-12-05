from time import localtime
#min =localtime().tm_min
#print(min)



while True:
    a = localtime()
    print(str(a.tm_hour) + ":" + str(a.tm_min)+ ":" + str(a.tm_sec))
