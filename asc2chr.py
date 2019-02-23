import sys

# Helpers
def longest_string(strs):
    longest = strs[0]
    for str in strs:
        cur_len, lon_len = len(str), len(longest)
        if cur_len > lon_len:
            longest = str
    return len(longest)

class Char_Numbers:

    def __init__(self, lines):
        self.lines = lines
        self.cols = longest_string(lines)

    def to_string(self):
        result = ""
        for line in self.lines:
            for i, char in enumerate(line):
                result += str(ord(char)) + "\n"
            if len(line) < self.cols:
                result += "32\n" * (self.cols - len(line))
        return result

# Main Process
gimme_path = sys.argv[1]
save_path = ""
with open(gimme_path, "r") as f:
    lines = f.read().split("\n")
    char_nums = Char_Numbers(lines)
