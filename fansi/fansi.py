# Fansi.py
"""
A library for easily adding colour, emphasis
and emojis to your terminal printouts.

By Daniel Rivas, 2018.
"""

"""
Modified by Areez Visram, Zahid Mirza, Mohamed Aly, 2022
as part of SFWRENG 3XA3 Winter 2022 class at McMaster University
"""

from .latex import latexEquation, simpleEquation, latexEquation_save
from .help import help
from .text_effects import format
from .py_inspect import py_inspect


def say(body, codes=None):
    body = format(body, codes)
    print(body)

# --- Premade formats ---


def danger(body, emoji=True):
    """
    For urgent messages, e.g. error printouts.
    """
    say(body, "bold red")


def latex(body, emoji=False):
    latexEquation(body)


def latexsave(body, emoji=False):
    latexEquation_save(body)


def simpleMath(body, emoji=False):
    simpleEquation(body)

def inspect(file_name):
    inspection_obj = py_inspect(file_name)

    console = inspection_obj[0]
    panel = inspection_obj[1]

    console.print(panel)

def help_command(body):
    help(input=body)
