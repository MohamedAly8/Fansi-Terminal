# Fansi
Fansi is a Python library that makes formatting, colouring and adding emojis to terminal printouts easy.

![fansi demo](https://i.postimg.cc/zGcL6MhG/Screenshot-2018-10-26-at-13-40-19.png)

# Installation

`pip install fansi`

To uninstall: `pip uninstall fansi`

# Usage
## First steps
First, include fansi in your script: 

> `from fansi import fansi`

Then, instead of `print()` statements, use `fansi.say()`.

> `fansi.say("This string can have fansi formatting!")`

If you want to generate a formatted string without printing it, use `fansi.format()`.

> `a = fansi.format("Here's a string ::blue:: formatted with Ansi characters! ::end:: It's partly blue!")`

## Basic formatting

To add italics, use `_tags_` or `*tags*`. To add bolding, use `__tags__` or `**tags**`. To add bolding and italics, use `___tags___` or `***tags***`.

For example:
> `fansi.say("This _text will be italicised_. This text will be **bolded**. ___This text will be both___.")`

## Inline tagging

You can add Ansi formatting characters inline, affecting the colour or emphasis of your text, using `::tags::` To reset the formatting, use the `::end::` tag.

For example: 
> `fansi.say("This text will be normal. ::green bold italics:: This text will be green, bold and italicised. ::end:: This text will be back to normal.")`

## Global tags

Fansi tags can also be added to the entire string.

For example: `fansi.say("This text will be magenta on a blue background.", "magenta bg-blue")`

## Emojis

You can also add any emoji, using `:tags:`. Long and shortnames work.

For example: 
> `fansi.say("Here are some :poop: emojis! :panda_face::tiger::cat:")`'

That's it!

## Latex

**LaTeX**

Generate an image of Latex input using the `latex` command.

Example: `fansi.latex("hello")` displays an visualization of the LaTeX command

Examples: 

`fansi.latex('\\int \\sqrt{\\frac{1}{x}}\\, dx')`

`fansi.latex('\\[E=mc^2\\]')`

`fansi.latex('\\sqrt{x^2+1}')`

`fansi.latex('\\int^a_b \\frac{1}{3}x^3')`

Refer to: https://www.giss.nasa.gov/tools/latex/ltx-2.html for more LaTeX commands

**SimpleEquation**

An alternative to users inexperienced with LaTeX but still want a display of equations in terminal.
 
Example:

`fansi.simpleEquation("Integral(sin(x)/2))")` 

Usage:

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


# Appendix: Fansi tags

| Tag          | Description           |
|--------------|-----------------------|
| `bold`       | Bold text             |
| `italics`    | Italicised text       |
| `underline`  | Underlined text       |
| `blink`      | Blinking text (don't) |
| `invisible`  | Invisible text        |
|--------------|-----------------------|
| `black`      | Black text            |
| `red`        | Red text              |
| `green`      | Green text            |
| `yellow`     | Yellow text           |
| `blue`       | Blue text             |
| `magenta`    | Magenta text          |
| `cyan`       | Cyan text             |
| `white`      | White text            |
|--------------|-----------------------|
| `bg-black`   | Black background      |
| `bg-red`     | Red background        |
| `bg-green`   | Green background      |
| `bg-yellow`  | Yellow background     |
| `bg-blue`    | Blue background       |
| `bg-magenta` | Magenta background    |
| `bg-cyan`    | Cyan background       |
| `bg-white`   | White background      |
