"""
consider a string that will have digits in that, we need to remove all the not digits and replace the digits with #
"""

def replace_digits(s):
    s1 = ""
    for i in s:
        if i.isdigit():
            s1 += i

    return(re.sub('[0-9]','#',s1)) # modified string which is after replacing the # with digits

replace_digits("#2a$#b%c%561#")
