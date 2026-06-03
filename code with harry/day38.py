#raising custom errors kyu karege kyunki program ruk jaye aur age kuch extra na kare
a = int(input("enters any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("value should between 5 and  9")

