import argparse

parser = argparse.ArgumentParser(description="Search for words including 'word'.")
parser.add_argument('snippet', help='partial / complete word to search for')

args = parser.parse_args()
snippet = args.snippet.lower()

with open(r'.\python3-scripting-for-sys-admin\intermediate-scripting/words.txt') as f:
    words = f.readlines()

# matches = []
#
# for word in words:
#     if snippet in word.lower():
#         matches.append(word)

print([word for word in words if snippet in word.lower()])