# Convert to dict for quick lookup
lookup = {row[0]: row[1] for row in quadstxt}
data=[]
for s, val in quadstxt:
    rev = s[::-1]  # reverse the string
    if rev in lookup and lookup[rev] == "" and lookup[s] != "" and lookup[rev] != "-"and lookup[s] != "-":
        #print(f"'{s}' has reverse '{rev}' with blank second column: {lookup[rev]}")
        data.append(rev)