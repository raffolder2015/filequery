### -------- FILEQUERY -------- ###
#                                 #
#   so. tool for... evaluating    #
#   file information? hell yea    #
#                                 #
### --------------------------- ###

import sys

try:
    if sys.argv[1] == "launch":
        print("\nFILEQUERY launched.")
except:
    print("ERROR: Invalid command")
    exit(1)

