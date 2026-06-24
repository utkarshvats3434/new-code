# try:
#     # Wo code jahan galti ho sakti hai
#     num1 = int(input("Pehla number daalo: "))
#     num2 = int(input("Dusra number daalo: "))
    
#     result = num1 / num2

# except ZeroDivisionError:
#     # Agar 0 se divide kiya toh ye chalega
#     print("Arre bhai! Kisi bhi number ko 0 se divide nahi kar sakte.")

# except ValueError:
#     # Agar number ki jagah text daala toh ye chalega
#     print("Galti kar di! Sirf numbers (0-9) hi daalo.")

# except Exception as e:
#     # Agar koi aur anjaan error aaya toh ye sab sambhal lega
#     print(f"Kuch toh gadbad hai: {e}")

# else:
#     # Agar sab sahi raha aur koi error nahi aaya
#     print(f"Sahi jawab hai: {result}")

# finally:
#     # Ye toh chalega hi chalega, chahe jo ho jaye
#     print("Danyavaad! Calculator program khatam.")

###day38
from itertools import count

# 1. Custom Exception Class
class InsufficientBalanceError(Exception):
    def __init__(self, message="Aapke account me itne paise nahi hain!"):
        self.message = message
        super().__init__(self.message)

# 2. Main Program Logic
account_balance = 50009090090909787

print(f"--- Welcome to Bank ---")
print(f"Aapka current balance hai: ₹{account_balance}")

try:
    withdraw_amount = int(input("Kitne paise nikalne hain? "))
    
    if withdraw_amount > account_balance:
        # Custom error raise kar rahe hain
        raise InsufficientBalanceError()
    else:
        account_balance -= withdraw_amount
        print(f"Success! ₹{withdraw_amount} nikal gaye.")
        print(f"Bacha hua balance: ₹{account_balance}")

except InsufficientBalanceError as e:
    # Custom error catch hoga yahan
    print(f"Transaction Failed: {e}")
except ValueError:
    # Agar user ne number ki jagah text daal diya
    print("Error: Kripya sirf numbers hi enter karein!")
  