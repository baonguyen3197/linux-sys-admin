import os

stage = os.getenv("STAGE", default="dev").upper()

output = f"Running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER! " + output

print(output)