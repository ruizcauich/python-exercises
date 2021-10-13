"""The test module contains basic custom functionality
to create test cases.
"""

import functools

def mock_print(func):
    """The mock_print decorator allows mocking the print
    builtin function, using an io.StringIO object.

    A test fuction must define a parameter at the end
    of its positional parameter list in order to access to
    the output value through the mock object: 

    @mock_print
    def test(param1, param2, mock, *args, **kwargs):
        ...
        output = mock.getvalue()
        ...

    NOTE:
    By default, the output obtained from the mock object
    will have a \\n at the end, unless the 'end' parameter is
    provided to the print function
    """
    @functools.wraps(func)
    def test_function(*args, **kwargs):
        import io
        import sys
        
        print(f'Running {func.__name__}')
        stdoutput = io.StringIO()
        sys.stdout = stdoutput
        
        args += (stdoutput,)

        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        print(f'Test output: \n{stdoutput.getvalue()}')
        return stdoutput.getvalue()
    return test_function
