## @file text_effects.py
#  @author Zahid Mirza
#  @brief A module containing all the commands used to parse the various text effects, colours, and emojis
#  @date April 4, 2022

from .emoji_codes import EmojiCodes
from .ansi_codes import AnsiCodes
import re

def __parse_emphasis__(body, resetcode=AnsiCodes.reset()):
    """
    Italics with _tags_ or *tags*.
    Bold with __tags__ or **tags**.
    Bold and italic with ___tags___ or ***tags***
    """

    strong_emphasis = re.compile(r"(?<!\w)(_{3}|\*{3})(?!_)(.+?)(?<!_)\1(?!\w)")
    body = strong_emphasis.sub(
        AnsiCodes.form_code("bold italics") + r"\2" + AnsiCodes.reset() + resetcode,
        body,
    )

    strong = re.compile(r"(?<!\w)(_{2}|\*{2})(?!_)(.+?)(?<!_)\1(?!\w)")
    body = strong.sub(
        AnsiCodes.form_code("bold") + r"\2" + AnsiCodes.reset() + resetcode, body
    )

    emphasis = re.compile(r"(?<!\w)(_{1}|\*{1})(?!_)(.+?)(?<!_)\1(?!\w)")

    body = emphasis.sub(
        AnsiCodes.form_code("italics") + r"\2" + AnsiCodes.reset() + resetcode, body
    )

    return body


def __parse_inline_styles__(body, resetcode=AnsiCodes.reset()):
    """
    ::red bg-blue bold:: This text is affected ::end:: This code is not.
    """

    tag_re = re.compile(r"(^| )(?<!\w)(:{2})(?!:)(.+?)(?<!:)\2(?!\w)")
    body = tag_re.sub(lambda match: __check_for_end__(match.group(3), resetcode), body)
    return body

def __check_for_end__(body, resetcode):
    if body == "end":
        return AnsiCodes.reset() + resetcode
    else:
        return AnsiCodes.form_code(body)

def __parse_emojis__(body):
    """
    Parse emojis in the text.
    Syntax :poo: :lion: :multiple::emojis::together:
    """
    emoji_re = re.compile(r"(?<!\w)(:{1})(?!:)(.+?)(?<!:)\1(?!\w)")
    body = emoji_re.sub(lambda match: EmojiCodes.get_emoji(match.group(2)), body)
    return body

## @brief Formats the user's text
#  @details Parses the user's text by replacing the commands specified by them with codes that actually change the text's style, colour
#  and adds emojis as well. Additionally, converts the user's text to rainbow if ::rb:: is specified.
#  @param body String of the user's text
#  @return The modified version of body
def format(body, codes=None):
    if codes is not None:
        reset = AnsiCodes.form_code(codes)
        body = __parse_emphasis__(body, reset)
        body = __parse_inline_styles__(body, reset)
        body = __parse_emojis__(body)
        body = AnsiCodes.form_code(codes) + body + AnsiCodes.reset()
    elif "::rb::" in body:
        body = body.replace("::rb::", "")
        body = __parse_emojis__(body)
        body = __change_to_rainbow__(body)
        body = __parse_emphasis__(body)
        body = __parse_inline_styles__(body)
    else:
        body = __parse_emphasis__(body)
        body = __parse_inline_styles__(body)
        body = __parse_emojis__(body)
        body = AnsiCodes.reset() + body + AnsiCodes.reset()
    return body

def __change_to_rainbow__(body):
    hex_dict = {
        "red": "#ff/00/00",
        "orange": "#d7/5f/00",
        "yellow" : "#ff/ff/00",
        "green" : "#00/ff/00",
        "blue" : "#00/87/ff",
        "purple" : "#5f/00/ff",
        "pink" : "#af/00/af"
    }
    colours_to_cycle = []
    for key in hex_dict.keys():
        colours_to_cycle.append(key)
    new_body = ""
    current_colour_index = 0
    for c in body:
        if current_colour_index >= len(colours_to_cycle):
            current_colour_index = 0
        if c == " ":
            new_body += " "
            continue
        new_c = __parse_inline_styles__("::" + hex_dict[colours_to_cycle[current_colour_index]] + ":: " + c + " ::end::")
        new_c = new_c.replace(" ", "")
        new_body += new_c
        current_colour_index += 1
    return new_body + "\033[0m"
