## @file latex.py
#  @author Mohamed Aly
#  @brief A module containing all the commands used to visualize LaTeX commands in terminal
#  @date April 4, 2022
from collections import defaultdict
import matplotlib.pyplot as plt
from sympy import *
import sys

sys.tracebacklimit = 0

'''
Sympy commands:
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
'''

## @brief Shows a visual representation of equation
#  @details Using the string input, converts the string into LaTeX syntax and visualizes the equation on a
#  pop-up window
#  @param inputEquation String of the equation to be visualized in SymPy format
#  @return Visual display of the equation
def simpleEquation(inputEquation):
    # Sample input equation
    # y = Integral(sqrt(1 / x), x)

    inputEquation = sympify_(inputEquation)
    lat = makeLatex(inputEquation)

    # add text
    plt.text(.5, 0.6, r"$%s$" % lat, fontsize=30, ha='center', va='center')
    plt.title("Fansi LaTeX", fontsize=20)
    # hide axes
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    plt.draw()  # or savefig
    plt.show()

## @brief Change object type of input 
#  @details Changes input object type from String to SymPy Object
#  @param inputEquation String to be converted to SymPy format
#  @return The input string, inputEquation as a SymPy object
def sympify_(inputEquation):
    return sympify(inputEquation)

## @brief SymPy object to LaTeX Syntax 
#  @details Converts a given SymPy object to a String in LaTeX syntax
#  @param Equation SymPy Object to be converted to String LaTeX format
#  @return Equation in LaTeX syntax as a String.
def makeLatex(Equation):
    return latex(Equation)

## @brief String to LaTeX Syntax 
#  @details Converts a given Equation String to a String in LaTeX syntax
#  @param Equation String to be converted to String LaTeX format
#  @return Equation in LaTeX syntax as a String.
def simpleOutput(Equation):
    return latex(sympify_(Equation))

'''
Make sure you use double back slashes when writing your LaTeX!

Example LaTex Equations:
\\[E=mc^2\\]
\\sqrt{x^2+1}
\\(x^2 + y^2 = z^2\\)
\\int^a_b \\frac{1}{3}x^3

Refer to: https://www.giss.nasa.gov/tools/latex/ltx-2.html for more LaTeX commands
'''

## @brief Shows a visual representation of equation
#  @details Using the string input, converts the string into LaTeX syntax and visualizes the equation on a
#  pop-up window
#  @param inputEquation String of the equation to be visualized in LaTeX syntax
#  @return Visual display of the equation
def latexEquation(input):
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "Helvetica"
    })

    # sampleInput = '\\int \\sqrt{\\frac{1}{x}}\\, dx'

    # Add text to plot
    
    plt.text(.5, 0.6, r"%s" % "$" + input + "$", fontsize=30, ha='center', va='center')
    # hide axes
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    # Draw equation

    plt.title("Fansi LaTeX", fontsize=20)
    plt.draw()
    plt.show()

    for i in range(20):
        print("\n")
    print("If you did not get your desired output :(")
    print("*** Make sure to use double backslashes in your command ***")
    print("Your LaTeX input was \n" + input)
    print("You can also try simpleMath command if you are unfamiliar with LaTeX :)")


## @brief Saves a visual representation of equation
#  @details Using the string input, converts the string into LaTeX syntax and saves an image
#  of the equation on the user's desktop
#  @param inputEquation String of the equation to be saved in LaTeX syntax
#  @return Saved equation image in user's desktop
def latexEquation_save(input):
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "Helvetica"
    })

    # sampleInput = '\\int \\sqrt{\\frac{1}{x}}\\, dx'

    # Add text to plot
  
    plt.text(.5, 0.6, r"%s" % "$" + input + "$", fontsize=30, ha='center', va='center')
    # hide axes
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    # Draw equation

    plt.title("Fansi LaTeX", fontsize=20)
    plt.draw()
    plt.savefig('../../fansiLatex.png', bbox_inches='tight')

    for i in range(20):
        print("\n")

    print("If you did not get your desired output :(")
    print("*** Make sure to use double backslashes in your command ***")
    print("Your LaTeX input was \n" + input)
    print("You can also try simpleMath command if you are unfamiliar with LaTeX :)")