## @file ansi_codes.py
#  @author Zahid Mirza
#  @brief A module containing the codes used to change the text style, and colour and background colour
#  @date April 4, 2022

## @brief AnsiCodes is an ADT that stores all the ansi codes used to change the text's style and/or colour
#  @details 
class AnsiCodes:
    """
    Every Ansi Code for formatting text.
    """

    codes = {
        "reset": 0,
        "bold": 1,
        "italics": 3,
        "underline": 4,
        "blink": 5,
        "background": 7,
        "invisible": 8,
        # --- Foreground Colors ---
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
        # --- Background Colors ---
        "bg-black": 40,
        "bg-red": 41,
        "bg-green": 42,
        "bg-yellow": 43,
        "bg-blue": 44,
        "bg-magenta": 45,
        "bg-cyan": 46,
        "bg-white": 47,
    }

    colour_palette = []

    @classmethod
    ## @brief Sets the colour palette hexadecimal values
    def set_colour_palettes(cls):
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

        full_palette = colored_palette + grayscale_palette
        cls.colour_palette = full_palette

    @classmethod
    ## @brief Forms a code that modifies the style and/or colour of the text
    #  @details Code is checked with the colour_palette and the code variables
    #  @param options List of strings that contain all the various commands to take into account
    #  @return An ansi code
    def form_code(cls, options):
        cls.set_colour_palettes()
        options = set(options.strip().split(" "))
        curr_colour = "0"
        curr_style = []
        for option in options:
            try:
                curr_style.append(cls.codes[option])
            except KeyError:
                if '#' in option:
                    option = option[1:]
                    if option in cls.colour_palette:
                        ansi_colour = cls.colour_palette.index(option)+16
                        curr_colour = str(ansi_colour)
                    else:
                        print("Invalid Hexadecimal specified.")
                continue
        ansi_string = ""
        if curr_colour == "0":
                curr_colour = "255"
        
        if len(curr_style) != 0:
            for style in curr_style:
                ansi_string += "\033[%s;38;5;%sm" % (str(style), str(curr_colour))
        else:
            ansi_string = "\033[38;5;%sm" % str(curr_colour)
        return ansi_string

    @classmethod
    ## @brief Returns a reset code
    #  @details The reset code is important for resetting text back to normal after modifying it
    #  @return An ansi code that resets text back to normal
    def reset(cls, options=""):
        return "\033[0m"
