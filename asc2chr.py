# Helpers
def longestString(strs):
    longest = strs[0]
    for str in strs:
        curLen, lonLen = len(str), len(longest)
        if curLen > lonLen:
            longest = str
    return longest

class CharNumber:
    def __init__(self, lines):
        self.lines = lines
        self.cols = longestString(lines)
        self.rows = len(lines)

# Main Process
gimmePath = "data/nums-hor.asc"
with open(gimmePath, "r") as f:
    lines = f.read().split("\n")
