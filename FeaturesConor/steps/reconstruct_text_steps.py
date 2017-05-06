# -*- coding: utf-8 -*-
from lettuce import step, world
import re

@step(u'Given the user has the text "([^"]*)"')
def given_the_user_has_the_text_group1(step, user_text):
    world.user_text = user_text
@step(u'When the to_humanreadable method is called on the text')
def when_the_to_humanreadable_method_is_called_on_the_text(step):
    world.user_text = to_humanreadable(world.user_text)
@step(u'Then the output text should be "([^"]*)"')
def then_the_output_text_should_be_group1(step, reconstruct_text):
    if world.user_text == reconstruct_text:
        assert True
    else:
        assert False


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
            tabs = r"\\t"

        text = re.sub("\<\[Tab\]x?(\d+)?\>", tabs, text, 1)
        tab_match = tab_rex.search(text)

    while return_match is not None:

        try:
            returns = r"\\r" * int(return_match.group(1))
        except TypeError:
            returns = r"\\r"

        text = re.sub("\<\[Return\]x?(\d+)?\>", returns, text, 1)
        return_match = return_rex.search(text)

    while up_match is not None:

        try:
            up_presses = "\u" * int(up_match.group(1))
        except TypeError:
            up_presses = "\u"

        text = re.sub("\<\[Up\]x?(\d+)?\>", up_presses, text, 1)
        up_match = up_rex.search(text)

    while down_match is not None:

        try:
            down_button_presses = "\d" * int(down_match.group(1))
        except TypeError:
            down_button_presses = "\d"

        text = re.sub("\<\[Down\]x?(\d+)?\>", down_button_presses, text, 1)
        down_match = down_rex.search(text)

    while left_match is not None:

        try:
            left_button_presses = "\<" * int(left_match.group(1))
        except TypeError:
            left_button_presses = "\<"

        text = re.sub("\<\[Left\]x?(\d+)?\>", left_button_presses, text, 1)
        left_match = left_rex.search(text)

    while right_match is not None:

        try:
            right_button_presses = "\>" * int(right_match.group(1))
        except TypeError:
            right_button_presses = "\>"

        text = re.sub("\<\[Right\]x?(\d+)?\>", right_button_presses, text, 1)
        right_match = right_rex.search(text)

    return text



