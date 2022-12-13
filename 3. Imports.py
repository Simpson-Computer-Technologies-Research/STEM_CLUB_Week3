
# /////////////////
# //   Imports   //
# /////////////////

# //
# // You can install libraries using 'pip install {name}'
# // Libraries can be found easily on pypi.org
# //

# // The following libraries are python defaults
import string
import sys

# // Same line imports
import string, sys


# // Use the string library
letters = string.ascii_letters


# // Import function from a library
from random import choice

# // Use the random.choice function
rand_char = choice(letters)


# // Import library as a custom name
import datetime as dt

# // Get the current date
current_date = dt.datetime.now()
