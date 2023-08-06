# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    sp = len((bin(number))[2:])
    
    for n in range(1,number+1):
        print(str(n).rjust(sp),
        oct(n)[2:].rjust(sp),
        hex(n)[2:].upper().rjust(sp),
        bin(n)[2:].rjust(sp))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
