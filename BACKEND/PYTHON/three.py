import re

patterns = ["term1","term2"]

text = "this is where only term1 lies theres no other term"

for pattern in patterns:
    print("i am sarching for {}".format(pattern))

    if re.search(pattern,text):
        print("match")
    else:
        print("no match found")
