# ========================= Returning first 20 Fibonacci numbers ====================================
# declaring a function
def fibnum(i):
        # checking if i is greater or equals to 1 , thenit should return 1
        if i<= 1:
           return i
        else:
            #  Recursion for adding the two first numbers before the current number
            return fibnum(i-2) + fibnum(i-1)

#  using a for loop to add a value to the parameter of the function
for i in range(20):
    print(fibnum(i), end=",")



