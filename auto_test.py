import contextlib, io
import fizz_buzz

f = io.StringIO()
with contextlib.redirect_stdout(f):
    fizz_buzz.fizz_buzz(10)

output = f.getvalue()


expected_output = \
    """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
"""

assert output == expected_output, f"Expected output: {expected_output}"
