def swap_case(s):
    s= list(s)
    swap = ''
    for i in range(len(s)):
        if s[i].islower():
            swap = swap + s[i].upper()
        else:
            swap = swap + s[i].lower()
    return swap
