#recursion Isko aap ek example se samajh sakte hain: Maan lijiye aap ek lambi line mein khade hain aur aapko pata karna hai ki aapka line mein kaunsa number hai. Aap apne aage wale person se puchte hain, woh uske aage wale se puchta hai, aur yeh tab tak chalta hai jab tak sabse aage wala (first person) na aa jaye. First person bolta hai "Main 1st hoon", aur phir yeh information peeche paas hoti hai jab tak aapko apna number pata nahi chal jata. Recursion bilkul aise hi kaam karta hai!
#factorial(5) = 5*4*3*2*1
#factorial(8) = 8*factorial(7)
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
# a = factorial(int(input("enter a number: ")))
print(factorial(int(input("enter a number: "))))
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0) = 1 + 0 = 1
# f(3) = f(2) + f(1) = 1 + 1 = 2
# f(4) = f(3) + f(2)  