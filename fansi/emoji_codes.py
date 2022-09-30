## @file emoji_codes.py
#  @author Zahid Mirza
#  @brief A module that takes an emoji code and forms an emoji from it
#  @details The emoji's and their codes are all pulled from the emojis.json file
#  @date April 4, 2022

import json
from os import path

#  @brief A module that takes an emoji code and forms an emoji from it
#  @details The emoji's and their codes are all pulled from the emojis.json file
class EmojiCodes:
    """
    Every Unicode emoji code.
    """

    emojipath = path.join(path.dirname(__file__), "emojis.json")
    with open(emojipath, "r", encoding="utf-8") as data:
        emojis = json.load(data)

    @classmethod
    ## @brief Returns an emoji based on the emoji code specified, if it exists
    #  @details If the emoji doesn't exist it returns an empty string
    #  @param code The emoji code
    #  @return An emoji
    def get_emoji(cls, code):
        # shortcode is ':shortcode:', our code is 'code', so add colons.
        code = ":" + code + ":"

        for emoji in cls.emojis["emojis"]:
            if emoji["shortname"] == code or emoji["name"] == code:
                return emoji["emoji"]

        return ""