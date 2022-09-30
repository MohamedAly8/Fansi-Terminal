def commands():
    """Print all available commands"""
    print("""
    Invalid Command!
    Available commands:
    inpect
    latex
    simplemath
    emoji
    effects
    colour
    """)

def colour_help():
    """Print all available colours with hex values"""
    """Print all available effects with descriptions"""
    print("This is colours help")
    print("Execute the command fansi.say(text) to use the different colours")
    print("Ensure that the text is a string (i.e. text is in quotation marks)")
    print("To use the colours you must specify them in the following way (hexadecimal RGB format):")
    print("::<colour>:: this text has colour ::end::")
    print('''Example: "::#ff/00/00:: this text is red ::end::"''')
    print("You can put the ::<colour>:: and ::end:: anywhere, as long as ::<colour>:: is before ::end::")
    print("Additionally, there MUST be a space seperating the commands from your text")
    print("A list of all the available colours and their corresponding hexadecimal are down below")
    colored = [0] + [0x5f + 40 * n for n in range(0, 5)]
    # print("Colored palette below:")
    colored_palette = [
        "%02x/%02x/%02x" % (r, g, b) 
        for r in colored
        for g in colored
        for b in colored
    ]
    grayscale = [0x08 + 10 * n for n in range(0, 24)]
    grayscale_palette = [
        "%02x/%02x/%02x" % (a, a, a)
        for a in grayscale 
    ]
    normal = "\033[38;5;%sm" 
    bold = "\033[7;38;5;%sm"
    reset = "\033[0m"
    full_palette = colored_palette + grayscale_palette
    for (i, color) in enumerate(full_palette, 16):
        index = (bold + "%4s" + normal + reset) % (i, str(i) + ':', i)
        hex   = (normal + "%s" + reset) % (i, color)
        # text = (normal + "%s" + reset) % (i, "TEST TEXT") WORKS!!
        newline = '\n' if i % 6 == 3 else ''
        print(index, hex, newline) 
    print('''It's possible to combine styles with the different colours. For more information on how to do this, take a look at 
    ''')
    print("Additionally, you can also use a rainbow effect")
    print("However, you cannot use any other styles with the rainbow effect, and the effect is specified differently")
    print("It's usage is as follows:")
    print("::rb:: this text is rainbow")
    print("Notice how no ::end:: is specified. You MUST specify the rainbow text using ::rb::, as it's a special colour command")

def effects_help():
    """Print all available effects with descriptions"""
    print("This is text effects help")
    print("Execute the command fansi.say(text) to use the text styles")
    print("Ensure that the text is a string (i.e. text is in quotation marks)")
    print("To use the styles you must specify them in the following way:")
    print("::<text effect>:: this text has style ::end::")
    print('''Example: "::italics:: this text is italicized ::end::"''')
    print("You can put the ::<text effect>:: and ::end:: anywhere, as long as ::<text effect>:: is before ::end::")
    print("Additionally, there MUST be a space seperating the commands from your text")
    print("A list of all the available commands are down below")
    codes = {
        "reset": 0,
        "bold": 1,
        "italics": 3,
        "underline": 4,
        "blink": 5,
        "background": 7,
        "invisible": 8,}
    i = 0
    for key in codes.keys():
        print(str(i) + ": " + key)
        i += 1
    print("Note that it's possible to combine multiple styles, and additionally multiple colours as well")
    print("Some more examples: ")
    print("::italics bold:: this text is italicized and bolded ::end::")
    print("::italics bold background #ff/00/ff:: this text has a purple background, is italicized and bolded ::end::")
    print('''For more information on the available colours use "fansi.help_command("colour")"''')

def emoji_help():
    """Print all available emojis with descriptions"""

def latex_help():
    """Print latex instructions"""
    print("This is LaTeX help!")
    print("Execute the command fansi.latex(YOUR_LATEX) to show a visual of the desired LaTeX command")
    print("For saving the images, use fansi.latexSave(YOUR_LATEX)")
    print("_____________________________________________________________")
    print("Make sure you use double back slashes when writing your LaTeX!")
    print("_____________________________________________________________")
    print("Upon executing the command a pop-up window will appear with your LaTeX equation")
    print("If the pop-up is blank, your LaTeX equation has syntax errors")
    print("Usage examples:")
    print("fansi.latex('\\sqrt{x^2+1}')")
    print("fansi.latex('\\(x^2 + y^2 = z^2\\)'")
    print("fansi.latex('\\int^a_b \\frac{1}{3}x^3')")
    print("\n")
    print("Refer to: https://www.giss.nasa.gov/tools/latex/ltx-2.html for more LaTeX commands")

def simpleMath_help():
    """Print simpleEquation instructions"""

    print("This is simpleMath help!")
    print("Execute the command fansi.simpleMath(YOUR_EQUATION) to show a visual of the desired equation")
    print("Syntax:")
    print("""
    Add: x+y
    Subtract: x-y
    Multiplication: x*y
    Divide: x/y

    Sinusodal: sin(x), cos(x), tan(x)
    Exponent: x**y
    Integral: Integral(x)
    Derivative: Derivative(x)

    Gamma: Gamma(x)
    Binomial: Binomial(a,b,...)
    Order of Precedence: Follows BEDMAS

    Refer to: https://docs.sympy.org/latest for more commands
    """)

def inspect_help():
    """Print Python object inspection instructions"""
    for i in range(20):
        print("\n")
    print("This is Fansi Python object inspection help")
    print("Execute the command fansi.inspect(file_path) to inspect a custom Python object in the terminal")
    print("Ensure that file_path is the FULL path of the file you are trying to inspect")
    print("Also ensure the file path is enclosed in quotation marks")
    print("Upon executing the command, you should see a box breaking down the Python object")
    print("This includes the class name, class methods and functions with their inputs")
    print("To see descriptions of functions and methods as part of inspection, include description as a docstring in the object")

def help(input):
    input = input.lower()
    if(input == "inspect"):
        inspect_help()
    elif(input == "latex"):
        latex_help()
    elif input == "simplemath":
        simpleMath_help()
    elif(input == "emoji"):
        emoji_help()
    elif(input == "effects"):
        effects_help()
    elif(input == "colour"):
        colour_help()
    else:
        commands()
