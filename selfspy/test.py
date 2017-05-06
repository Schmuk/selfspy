import re
import models
'''
string1 = "jhkjshgjkhfgjksfhgjk khfdjkhg fhb gjfg bsfdkjl <[Backspace]><[Tab]x2>jjdbclhiedbv<[Tab]x4>jjdbclh"
tabrex = re.compile("\<\[Tab\]x?(\d+)?\>", re.IGNORECASE)
tabmatches = tabrex.findall(string1)
sub = "/t"*int(tabmatches[0])
sub += " "
print string1
print re.sub("\<\[Tab\]x?(\d+)?\>", sub, string1)'''


def to_humanreadable(text):
    backspace_rex = re.compile("\<\[Backspace\]x?(\d+)?\>", re.IGNORECASE)  # creates regualer expression object
    tab_rex = re.compile("\<\[Tab\]x?(\d+)?\>", re.IGNORECASE)
    return_rex = re.compile("\<\[Return\]x?(\d+)?\>", re.IGNORECASE)
    up_rex = re.compile("\<\[Up\]x?(\d+)?\>", re.IGNORECASE)
    down_rex = re.compile("\<\[Down\]x?(\d+)?\>", re.IGNORECASE)
    left_rex = re.compile("\<\[Left\]x?(\d+)?\>", re.IGNORECASE)
    right_rex = re.compile("\<\[Right\]x?(\d+)?\>", re.IGNORECASE)

    backspace_matches = backspace_rex.search(text)
    tab_match = tab_rex.search(text)
    return_match = return_rex.search(text)
    up_match = up_rex.search(text)
    down_match = down_rex.search(text)
    left_match = left_rex.search(text)
    right_match = right_rex.search(text)

    while backspace_matches is not None:
        backspaces = backspace_matches.group(1)
        try:
            deletechars = int(backspaces)
        except TypeError:
            deletechars = 1

        newstart = backspace_matches.start() - deletechars
        if newstart < 0:
            newstart = 0

        text = (text[:newstart] + text[backspace_matches.end():])
        backspace_matches = backspace_rex.search(text)

    while tab_match is not None:

        try:
            tabs = r"\\t" * int(tab_match.group(1)) + " "
        except TypeError:
            tabs = r"\\t" + " "

        text = re.sub("\<\[Tab\]x?(\d+)?\>", tabs, text, 1)
        tab_match = tab_rex.search(text)

    while return_match is not None:

        try:
            returns = r"\\r" * int(return_match.group(1)) + " "
        except TypeError:
            returns = r"\\r" + " "

        text = re.sub("\<\[Return\]x?(\d+)?\>", returns, text, 1)
        return_match = return_rex.search(text)

    while up_match is not None:

        try:
            up_presses = "\up" * int(up_match.group(1)) + " "
        except TypeError:
            up_presses = "\up" + " "

        text = re.sub("\<\[Up\]x?(\d+)?\>", up_presses, text, 1)
        up_match = up_rex.search(text)

    while down_match is not None:

        try:
            down_button_presses = "\down" * int(down_match.group(1)) + " "
        except TypeError:
            down_button_presses = "\down" + " "

        text = re.sub("\<\[Down\]x?(\d+)?\>", down_button_presses, text, 1)
        down_match = down_rex.search(text)

    while left_match is not None:

        try:
            left_button_presses = "\<" * int(left_match.group(1)) + " "
        except TypeError:
            left_button_presses = "\<" + " "

        text = re.sub("\<\[Left\]x?(\d+)?\>", left_button_presses, text, 1)
        left_match = left_rex.search(text)

    while right_match is not None:

        try:
            right_button_presses = r"\>" * int(right_match.group(1)) + " "
        except TypeError:
            right_button_presses = r"\>" + " "

        text = re.sub("\<\[Right\]x?(\d+)?\>", right_button_presses, text, 1)
        right_match = right_rex.search(text)

    return text

print to_humanreadable("<[Tab]x3>Said someone had seem <[Tab]x2>n Jon on his bike")