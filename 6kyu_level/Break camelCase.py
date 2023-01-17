""" Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  "" """


#def solution(s):
s="camelLow"
list = ""
for letter in s:
    if letter.lower() == letter :
        list += str(letter)
    else :
        list += str(" ")
        list += str(letter)
print(list)
#    pass