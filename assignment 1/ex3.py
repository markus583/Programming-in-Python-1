"""ex3.py
Author: Markus Frohmann
Matr.Nr.: K12005604
Exercise 3
"""

#
# Start of code block that should not be modified.
#

# The next 3 lines will ask the user for input through the console and set the variables var1 and var2
# to the corresponding input values. The variables will be initially of datatype string, so if you want to do
# numerical computations  with them you will need to convert them to datatype int or float. See the assignment
# sheet for more details.
var1 = input('Enter var1:')
var2 = input('Enter var2:')
result = None  # This variable should be overwritten with the result of your operation later.

#
# End of code block that should not be modified.
#

# Place your code here. Store the result in the variable "result".
int_var1 = int(var1)
float_var2 = float(var2)
result = int_var1 * float_var2

#
# Do not modify the code below this line.
#

# This will print the result to the console.
print(f"Result: {result}")
