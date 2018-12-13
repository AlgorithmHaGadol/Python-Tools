def switch(x, cases):
    for i in range(len(cases)):
        if x == i:
            eval(cases[i])
        else:
            continue
      
# Usage Example

# int
age = 13

switch(age,
    cases = {
        13: "print('You Are 13')",
        14: "print('You Are 14')",
        15: "print('You Are 15')",
        16: "print('You Are 16')"
    }
)

# Bool
isSmart = True

switch(isSmart,
    cases = {
        True: "print('You Are Smart!')",
        False: "print('You Are Not Smart at all!')"
    }
)

# String
color = 'Blue'

switch(color,
    cases = {
        'Blue': "print('You like Blue')",
        'Green': "print('You like Green')",
        'Red': "print('You like Red')"
    }
)
