import os, sys

# Helpers
def longest_string(strs):
    longest = strs[0]
    for str in strs:
        cur_len, lon_len = len(str), len(longest)
        if cur_len > lon_len:
            longest = str
    return len(longest)

class Char_Numbers:

    def __init__(self, lines, rows=0):
        self.rows = rows
        self.lines = lines
        self.cols = longest_string(lines)

    def summarize(self):
        message = ("Each line is {} character(s) wide.\n").format(self.cols)
        message += ("There are {} line(s) in total.").format(len(self.lines))
        if self.rows:
            total_characters = len(self.lines) / self.rows
            message += ("\nEach character has {} row(s).\n").format(self.rows)
            message += ("There are {} character(s) in total.\n").format(total_characters)
            message += ("Each character is {}x{}.").format(self.cols, self.rows)
        return message

    def to_string(self):
        result = ""
        for line in self.lines:
            for i, char in enumerate(line):
                result += str(ord(char)) + "\n"
            if len(line) < self.cols:
                result += "32\n" * (self.cols - len(line))
        return result

# Main Process
# test cmd: py asc2chr.py "data/asc/nums-hor.asc" "3"
try: rows = int(sys.argv[2])
except: rows = 0
try: gimme_path = sys.argv[1]
except:
    print("Need a path to a .asc file, bud.")
    exit()
save_path = gimme_path.replace("/asc/", "/chr/", 1).replace(".asc", ".chr", 1)
success_message = ("/-\\|" * 20) + "\n"
success_message += ("Saved {} with chr translation as {}.\n").format(gimme_path, save_path)
success_message += "Courtesy of @EthanThatOneKid <3"
with open(gimme_path, "r") as asc_file:
    lines = asc_file.read().split("\n")
    char_nums = Char_Numbers(lines, rows)
    print(char_nums.summarize())
    with open(save_path, "w") as chr_file:
        result = char_nums.to_string()
        chr_file.write(result)
        print(success_message)
exit()
