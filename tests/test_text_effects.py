from src.fansi import text_effects

# Test if the italics and a specified hexadecimal colour work
# Should output light green italicized text that says " test"
def test_parse_inline_styles_one():
    print(text_effects.__parse_inline_styles__("::italics #af/d7/87:: test"))

# Test if just italics work
def test_parse_inline_styles_two():
    print(text_effects.__parse_inline_styles__("::italics:: test"))

# Test if just a valid hexadecimal works
def test_parse_inline_styles_three():
    print(text_effects.__parse_inline_styles__("::#ff/00/00:: test"))

# Test out italics and hexadecimal work for text with multiple words
# Outputs red italicized text that says "test all these words"
def test_parse_inline_styles_four():
    print(text_effects.__parse_inline_styles__("::#ff/00/d7 italics:: test all these words"))

# Test out italics and hexadecimal work for text with multiple words, with ::end:: at the end 
def test_parse_inline_styles_five():
    print(text_effects.__parse_inline_styles__("::#ff/d7/00 italics:: test all these words ::end::"))

# Test out italics and hexadecimal work for text with multiple words, with ::end:: at a position besides the end
def test_parse_inline_styles_six():
    print(text_effects.__parse_inline_styles__("::#ff/00/ff italics:: test all ::end:: these words"))

# Test if invalid hexadecimal works
# Should output "Invalid hexadecimal specified" with the text afterwards (other options should work)
def test_parse_inline_styles_seven():
    print(text_effects.__parse_inline_styles__("::#ff/00/gg italics:: test all ::end:: these words"))

# Test out if the bold works (option 1)
def test_parse_emphasis_one():
    print(text_effects.__parse_emphasis__("__test__"))

# Test out if the bold works (option 2)
def test_parse_emphasis_two():
    print(text_effects.__parse_emphasis__("**test**"))

# Test out if italics works (option 1)
def test_parse_emphasis_three():
    print(text_effects.__parse_emphasis__("*test*"))

# Test out if italics works (option 2)
def test_parse_emphasis_four():
    print(text_effects.__parse_emphasis__("_test_"))

# Test out if italics works with multiple words (option 1)
def test_parse_emphasis_five():
    print(text_effects.__parse_emphasis__("*test lol*"))

# Test out if italics works with multiple words (option 2)
def test_parse_emphasis_six():
    print(text_effects.__parse_emphasis__("_test lol_"))

# Test out if bold works with multiple words (option 1)
def test_parse_emphasis_seven():
    print(text_effects.__parse_emphasis__("**test lol**"))

# Test out if bold works with multiple words (option 2)
def test_parse_emphasis_eight():
    print(text_effects.__parse_emphasis__("__test lol__"))

# Test out if bold and italics works with multiple words (option 2)
def test_parse_emphasis_nine():
    print(text_effects.__parse_emphasis__("***testlol***"))

# Test out if bold and italics works with multiple words (option 2)
def test_parse_emphasis_ten():
    print(text_effects.__parse_emphasis__("___testlol___"))

# Test out if one emoji works
def test_parse_emojis_one():
    print(text_effects.__parse_emojis__(":poop: test"))

# Test out if two emojis work
def test_parse_emojis_two():
    print(text_effects.__parse_emojis__(":poop: test :rainbow:"))

# Test out invalid emoji
def test_parse_emojis_three():
    print(text_effects.__parse_emojis__(":poop: test :rain:"))

# Test out the rainbow text effect
def test_format_one():
    print(text_effects.format("::rb:: this text will be coloured"))

# Test out the rainbow text effect with emojis
def test_format_two():
    print(text_effects.format("::rb:: this text will be coloured :poop:"))

# Test out the rainbow text effect invalid format
def test_format_three():
    print(text_effects.format("::rb: this text will be coloured :poop:"))

# Test out both specifying hexadecimal and emojis
def test_format_four():
    print(text_effects.format("::#ff/00/00:: this text will be coloured :poop:"))

# Test out both specifying hexadecimal, and an inline style and emojis
def test_format_five():
    print(text_effects.format("::#ff/00/00:: this **text** will ___be___ coloured :poop:"))

# Overlapping styles
def test_format_six():
    print(text_effects.format("::#ff/00/00 italics:: this **text** will ___be___ coloured :poop:"))
