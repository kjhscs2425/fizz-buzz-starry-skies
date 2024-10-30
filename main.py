# print out every single number if it is a multiple of 3 and npt 5, print fizz
# if multiple of 5 but not 3, print buzz
# if multiple of 3 and 5, print fizz buzz
# if not multiple of 3 and 5, print number

def print_fizz_buzz(n):
    if n%3==0 and n%5!=0:
        print("fizz")
    elif n%3!=0 and n%5==0:
        print("buzz")
    elif n%3==0 and n%5==0:
        print("fizzbuzz")
    else: 
        print(n)
print_fizz_buzz(15)