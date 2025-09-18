import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory is already exists.")

receipts = glob.glob('./new/receipt-[0-9]*.json') # glob syntax [1-3]*
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # name = path.split("/")
    filename = os.path.basename(path)
    # destination = f"./processed/{filename}"
    destination = path.replace("/new/", "/processed/")
    shutil.move(path, destination)
    print(f"move '{path} to {destination}")

print(f"Receipt subtotal: ${subtotal}")

import math
print(f"Receipt subtotal: ${math.ceil(subtotal)}")
print(f"Receipt subtotal: ${math.floor(subtotal)}")
print(f"Receipt subtotal: ${round(subtotal, 2)}")