import pytest
# Path hack.
import sympy
from src.fansi import latex


def test_makeLatex():
    assert (latex.makeLatex(latex.sympify("x/2")) == "\\frac{x}{2}")
#
def test_makeLatex2():
    assert (latex.makeLatex(latex.sympify("Integral(sin(x)/2)")) ==
            "\\int \\frac{\\sin{\\left(x \\right)}}{2}\\, dx")

def test_makeLatex3():
    assert (latex.makeLatex(latex.sympify("x**(5/4) + 3*x**2 - sin(x) + 2")) ==
            "x^{\\frac{5}{4}} + 3 x^{2} - \\sin{\\left(x \\right)} + 2")

def test_type_sympify():
    type_latex = latex.sympify_("Integral(sin(x)/2)")
    assert isinstance(type_latex, sympy.integrals.integrals.Integral)

def test_type_sympify2():
    type_latex = latex.sympify_("Derivative(Gamma(x/3))")
    assert isinstance(type_latex, sympy.core.function.Derivative)

def test_type_sympify3():
    type_latex = latex.sympify_("x**5 + 3*x**2 - sin(x) + 2")
    assert isinstance(type_latex, sympy.core.add.Add)

def test_simpleOutput():
    assert(latex.simpleOutput("Integral((x**2)/sin(x))") ==
           "\\int \\frac{x^{2}}{\\sin{\\left(x \\right)}}\\, dx")

def test_simpleOutput2():
    assert(latex.simpleOutput("Derivate(x**2 / tan(x)**(1/2))") ==
           "\\operatorname{Derivate}{\\left(\\frac{x^{2}}{\\sqrt{\\tan{\\left(x \\right)}}} \\right)}")

def test_simpleOutput3():
    assert(latex.simpleOutput("Integral((1/2)*(x**(5/4) + 3*x**2 - sin(x) + 2))") ==
           "\\int \\left(\\frac{x^{\\frac{5}{4}}}{2} + \\frac{3 x^{2}}{2} - \\frac{\sin{\\left(x \\right)}}{2} + 1\\right)\\, dx")






