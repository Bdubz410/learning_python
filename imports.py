# Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
import import_tshirt

import_tshirt.make_shirt('small', 'We are importing now!')

from import_tshirt import make_shirt

make_shirt('large', 'New to Importing!')

from import_tshirt import make_shirt as ms

ms('medium', 'Import with an alias!')

import import_tshirt as it

it.make_shirt('small', 'This is my favorite import!')

from import_tshirt import *

make_shirt('extra large', 'This is NOT the best approach for importing!')