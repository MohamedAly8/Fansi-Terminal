from subprocess import call
import pytest
from src.fansi.py_inspect import build_object, get_signature, print_box, py_inspect, render, extract_class
from rich.console import Console
from rich.panel import Panel
from rich.console import Group

# print_box tests
def test_print_box():
    object_to_render = {
        "title": "test_title",
        "methods": "test_methods",
        "functions": "test_functions"
    }
    box = print_box(object_to_render)

    assert(len(box) == 2)
    assert type(box[0]) is Console 
    assert type(box[1]) is Panel

# render tests
def test_render():
    object_to_render = {
        "title": "test_title",
        "methods": ["test_methods"],
        "functions": ["test_functions"]
    }

    rendered_object = render(object_to_render)

    assert type(rendered_object) is Panel
    assert rendered_object.padding == 1
    assert rendered_object.title == object_to_render["title"]
    assert type(rendered_object.renderable) is Group
    assert type(rendered_object.renderable.renderables[0]) is Group
    assert rendered_object.renderable.renderables[0].renderables[0] == "Methods:"
    assert rendered_object.renderable.renderables[0].renderables[1].renderables == object_to_render["methods"]
    assert rendered_object.renderable.renderables[1] == "\n"
    assert rendered_object.renderable.renderables[2].renderables[0] == "Functions:"
    assert rendered_object.renderable.renderables[2].renderables[1].renderables == object_to_render["functions"]

# extract_class tests
def test_extract_class():
    test_file_path = "tests/Person.py"

    assert extract_class(test_file_path) == __import__("Person")

    incorrect_file_path = "/test/Test.py"
    
    with pytest.raises(ModuleNotFoundError):
        extract_class(incorrect_file_path)

# get_signature tests
def test_get_signature():
    test_callables = [["test1"], ["test2"]]
    test_args = [["arg1"], ["arg2", "arg3"]]
    test_descriptions = ["test_1_desc", "test_2_desc"]

    signatures = get_signature(test_callables, test_args, test_descriptions)

    assert len(signatures) == 2
    assert signatures[0] == "test1(arg1): test_1_desc"
    assert signatures[1] == "test2(arg2, arg3): test_2_desc"

# build_object tests
def test_build_object(mocker):
    mocked_get_signature_func = mocker.patch('src.fansi.py_inspect.get_signature')

    to_render = ["test_class_name", ["test_methods"], ["test_method_args"], ["test_method_docs"], ["test_functions"], ["test_function_args"], ["test_function_docs"]]

    object = build_object(to_render)

    assert mocked_get_signature_func.call_count == 2    
    mocked_get_signature_func.assert_any_call(["test_methods"], ["test_method_args"], ["test_method_docs"])    
    mocked_get_signature_func.assert_any_call(["test_functions"], ["test_function_args"], ["test_function_docs"])    
    assert(len(object) == 2)
    assert type(object[0]) is Console 
    assert type(object[1]) is Panel

# py_inspect tests
def test_py_inspect(mocker):
    mocked_extract_class = mocker.patch('src.fansi.py_inspect.extract_class', return_value=__import__("Person"))

    mocked_build_object = mocker.patch('src.fansi.py_inspect.build_object', return_value='test')
    
    file_name = 'test'

    object = py_inspect(file_name)

    assert mocked_extract_class.call_count == 1
    mocked_extract_class.assert_called_with(file_name)
    assert mocked_build_object.call_count == 1
    assert object == "test"