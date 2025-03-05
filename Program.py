# This is enough code to load the json file into the variable data
import json
import time
import sys

f = open(sys.argv[1])
data = json.load(f)

from datetime import timedelta
start_time = time.monotonic()

# Insert your code below this point. Note: $data contains the loaded json as a JSON object
# ----------------------------------------------------------------------------------------

# WRITE YOUR CODE HERE
people = data['people']
items = data['items']
matches = []
matched_items = []
for person in people:
    match_items = [x for x in items if x['color'] == person['color'] and person['min'] <= x['size'] <= person['max']]
    matches.append(len(match_items))
    matched_items.extend(match_items)

print(f"Total items: {len(items)}")
print(f"Total unmatched items: {len([x for x in items if x not in matched_items])}")
for i in range(len(people)):
    print(f"Total items matched by {people[i]['name']}: {matches[i]}")

# ----------------------------------------------------------------------------------------
# Close file and output execution time

end_time = time.monotonic()
print("Time:", timedelta(seconds=end_time - start_time))

f.close()
