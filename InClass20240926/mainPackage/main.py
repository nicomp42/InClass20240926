#main.py 
from nicholdwPackage.nicholdw import *
from team1.team1 import *                  # Nonconforming
from team2Package.team2 import *           # Nonconforming
from Group3.Group3 import *                # Nonconforming
from team04Package.team04 import *         # Nonconforming
from Team5Package.Team5 import *           # Nonconforming
from team07Package.team07 import *         # Nonconforming
from team8Package.Team8 import *           # Nonconforming
from team10Package.team10 import *         # Nonconforming
from team12Package.team12 import *         # Nonconforming
from team13Package.team13 import *         # Nonconforming
from Group14Package.Group14 import *         
from team15Package.team15 import *         # Nonconforming
from team17Package.team17 import *         # Nonconforming
from Team19.Team19 import *                # Nonconforming
from Team20package1.Team20 import *        # Nonconforming

# Do not edit this module at all.
# Create some new artifacts in the project...
# Name your package {team}Package
# Name your module {team}.py
# Name your function {team}
# The {} are for clarity and are not part of any name
# Your function should return a list of dictionaries, just a few rows.


if __name__ == "__main__":
    print("testing your code...")
    print("nicholdw")
    data = nicholdw()
    for item in data:
        print(item)
        
    group_names = ["team1",   "team2",  "Group3", "team04",  "Team5", "group6",  "group7", "team8",   "group9",  "team10",
                   "group11", "team12", "team13", "Group14", "team15", "group16", "team17", "group18", "Team19",  "Team20"]

    for group_name in group_names:
        print(group_name, " ****************************************************************************************************")
        try:
            function_name = group_name
            items = eval(function_name)()
            for item in items:
                print(item)
        except Exception as e:
            print("Error in ", group_name, ":", e)
