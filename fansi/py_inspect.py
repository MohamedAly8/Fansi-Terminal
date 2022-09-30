from ast import arg
import inspect
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.console import Group, group

@group()
def get_groups(list):
    for i in list:
        yield(i)

def render(object_to_render):
    p = Panel.fit(
    Group(Group("Methods:", get_groups(object_to_render["methods"])), "\n", Group("Functions:", get_groups(object_to_render["functions"]))),
    title=object_to_render["title"],
    padding=1,
    )

    return p

def print_box(object_to_render):
    c = Console()

    panel = render(object_to_render)

    return [c, panel]

def extract_class(file_name):
    if ".py" in file_name:
        exploded_path = file_name.split(".py")[0].split(os.sep)
        module_name = exploded_path[-1]
        package = os.sep.join(exploded_path[:-1])

        if package not in sys.path:
            sys.path.append(package)
        return __import__(module_name)

def get_signature(callables, arguments, descriptions):
    signatures = []

    for i in range(len(callables)):
        signature = callables[i][0] + "(" + ", ".join(arguments[i]) + "): " + str(descriptions[i])
        signatures.append(signature)
    
    return signatures

def build_object(to_render):
    functions = to_render[4]
    function_args = to_render[5]
    function_docs = to_render[6]

    methods = to_render[1]
    method_args = to_render[2]
    method_docs = to_render[3]

    function_signatures = get_signature(functions, function_args, function_docs)
    method_signatures = get_signature(methods, method_args, method_docs)

    object_to_render = {
        "title": to_render[0],
        "methods": method_signatures,
        "functions": function_signatures
    }

    return print_box(object_to_render)

def py_inspect(file_name):
    modules = [extract_class(file_name)]
    functions = inspect.getmembers(modules[0], inspect.isfunction)
    class_name = inspect.getmembers(modules[0], inspect.isclass)[0][0]
    methods = inspect.getmembers(getattr(modules[0], class_name), inspect.isfunction)

    function_args = []
    method_args = []

    for func in functions:
        args = inspect.getfullargspec(func[1]).args
        function_args.append(args)

    for method in methods:
        args = inspect.getfullargspec(method[1]).args
        method_args.append(args)

    function_docs = []
    method_docs = []
    for func in functions:
        docs = inspect.getdoc(func[1])
        function_docs.append(docs)
    

    for method in methods:
        docs = inspect.getdoc(method[1])
        method_docs.append(docs)

    to_render = [class_name, methods, method_args, method_docs, functions, function_args, function_docs]
    return build_object(to_render)

