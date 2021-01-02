import os
import sys
__all__ = [
    "load_module",
    "mytest_the_file",
]


def load_module(file_path, module_name=None):
    """
    Load a module by name and search path

    This function should work with python 2.7 and 3.x

    Returns None if Module could not be loaded.
    """
    if module_name is None:
        module_name = os.path.basename(os.path.splitext(file_path)[0])
    if sys.version_info >= (3, 5,):
        import importlib.util

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if not spec:
            return

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    else:
        import imp
        mod = imp.load_source(module_name, file_path)
        return mod


def mytest_the_file(filename):
    file_dir, file_name = os.path.split(filename)
    module_test = load_module(file_path=filename)
    if "_t" in file_name:
        filename_val = os.path.join(file_dir, f"{file_name.split('_t')[0]}.py")
        module_val = load_module(file_path=filename_val)
    else:
        module_val = module_test
    module_val.Solution.check_class(module_test.Solution)
    return True, file_name


