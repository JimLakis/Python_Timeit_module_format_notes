'''
Created on May 2, 2022

@author: Jim Lakis
'''

import pandas as pd
import timeit


def main():
    
#    Single quotes, single statement with the string literal assigned to a variable

#        Format notes:

#            Every line ends with a forward slash and the entire string is enclosed in single quotes

#            Alignment within the assignment statement is irrelevant depicted by columns "Region" and "Team"

    s_ment ='df1 = pd.DataFrame({\
                "Region":["North","West","East","South","North","West","East","South"],\
                "Team":["One","One","One","One","Two","Two","Two","Two"],\
            "Squad":["A","B","C","D","E","F","G","H"],\
            "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],\
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]\
            })'

    my_setup = 'from __main__ import pd'
    print(timeit.timeit(setup = my_setup, stmt = s_ment, number = 100))


# ---


#    Single quotes, single statement with the string literal defined directly within the timeit() function

#        Format notes:

#            Every line ends with a forward slash

#            Alignment within the function is irrelevant depicted by columns "Region" and "Team"

    my_setup = 'from __main__ import pd'
    print(timeit.timeit(setup = my_setup, stmt = 'df1 = pd.DataFrame({\
                "Region":["North","West","East","South","North","West","East","South"],\
                "Team":["One","One","One","One","Two","Two","Two","Two"],\
            "Squad":["A","B","C","D","E","F","G","H"],\
            "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],\
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]\
            })', number = 100))


# ---


#    Single quotes, MULTIPLE statements with the string literal assigned to a variable

#        Format notes:

#            Every line statement ends with a semicolon and every line ends with a forward slash

#            Alignment within the function and other statements is irrelevant

    s_ment ='df1 = pd.DataFrame({\
                "Region":["North","West","East","South","North","West","East","South"],\
                "Team":["One","One","One","One","Two","Two","Two","Two"],\
            "Squad":["A","B","C","D","E","F","G","H"],\
            "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],\
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]\
            });    ### <-- statement concludes with a semicolon, the lines ends with a forward slash -->  \
        x = 2'
            
    my_setup = 'from __main__ import pd'
    print(timeit.timeit(setup = my_setup, stmt = s_ment, number = 100))


# -------------------------------------------------------------------


#    Triple quotes, single statement with the string literal assigned to a variable

#    Format notes:

#        No additional formatting; ie forward slashes

#        Alignment within the assignment statement is irrelevant depicted by columns "Region" and "Team"

    s_ment ='''df1 = pd.DataFrame({
                "Region":["North","West","East","South","North","West","East","South"],
                "Team":["One","One","One","One","Two","Two","Two","Two"],
            "Squad":["A","B","C","D","E","F","G","H"],
            "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]
            })'''
            
    my_setup = 'from __main__ import pd'
    print(timeit.timeit(setup = my_setup, stmt = s_ment, number = 100))


# ---


#    Triple quotes, single statement with the string literal defined directly within the timeit() function

#    Format notes:

#        No additional formatting; ie forward slashes

#        Alignment within the assignment statement is irrelevant depicted by columns "Region" and "Team"

    my_setup = 'from __main__ import pd'
    print(timeit.timeit(setup = my_setup, stmt = '''df1 = pd.DataFrame({
                "Region":["North","West","East","South","North","West","East","South"],
                "Team":["One","One","One","One","Two","Two","Two","Two"],
            "Squad":["A","B","C","D","E","F","G","H"],
            "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]
            })''', number = 100))


# ---


#    Triple quotes, MULTIPLE statements with the string literal assigned to a variable

#    Format notes:

#        Only the conclusion of a statement ends with a semicolon and a forward slash

#        Alignment within the function and other statements is irrelevant

    my_setup = 'from __main__ import pd'
    print(timeit.timeit(setup = my_setup, stmt = '''df1 = pd.DataFrame({
                        "Region":["North","West","East","South","North","West","East","South"],
                        "Team":["One","One","One","One","Two","Two","Two","Two"],
            "Squad":["A","B","C","D","E","F","G","H"],
            "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]
            });    ### <-- statement concludes with a semicolon, the lines ends with a forward slash -->    \
    x = 2''', number = 100))
    
    
if __name__ == '__main__':
    main()