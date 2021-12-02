import sys
# lib to work with json
import json
# lib to draw the table
from prettytable import PrettyTable


# custom function to read two inputs from CMD. First param is the json file path, second is the .txt file path
# json file path is the path from where the json file needs to be picked and read
# .txt file path is the path where tabular flattened json needs to be saved as text file
def jasontotab(first, second):
    t = PrettyTable(["Id", "Type", "Name", "Batter", "Topping"])
    with open(first, 'r') as f:
        data = json.load(f)
    # will come back to this to optimize it further
    for d in data["items"]["item"]:
        for b in d["batters"]["batter"]:
            for c in d["topping"]:
                t.add_row([d.get("id"), d.get("type"), d.get("name"), b.get("type"), c.get("type")])
    # writing the tabular content to a file
    with open(second, 'w') as r:
        r.write(t.get_string())

# this is main function which gets called first
if __name__ == "__main__":
    jasontotab((sys.argv[1]), (sys.argv[2]))

# Execution Remarks:

# to run in normal CMD - install PrettyTable by using pip install and then run the below python command
# pip install PrettyTable
# for windows
# python jsontotable.py "C:\\Users\\rahul\\Desktop\\assignment\\Sample.json" "C:\\Users\\rahul\\Desktop\\assignment\\rahul123.txt"