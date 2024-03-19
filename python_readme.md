## Welcome to my python cleaning tool

To all the python doubters, ha.

# To Use
To prepare the program: 
- Make sure python is installed (probably version 3.6 or later)
- Make sure pandas is installed (install with `pip install pandas`)
- Ensure all wanted csv files are in the same directory as `main.py`, or a subdirectory
# To use
run the following command
> `python main.py CSV_FILE`
> Feel free to use `DIRECTORY/CSV_FILE`
> Or even use `*.csv` to target all csv files
> Or use `DIRECTORY/*.csv` to target all csv files within a directory

# Note
Note that the output files will be labed `cooked_NAME.csv` as they were raw data, and now the data's been cooked.
Additionally, they will all be outputted to the same directory as main, because I'm lazy and didn't change that. If you want, in `main.py`, change `cooked_...` to `./DIRECTORY/cooked_...` to put the output files into a different subdirectory


# End
This program and its readme were written by Max Wanger, but its simple code so really doesn't matter.
