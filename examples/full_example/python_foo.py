from radiant import PythonHandler
import math

########################################################################


class MyClass(PythonHandler):
    """"""

    # ----------------------------------------------------------------------
    def local_python(self):
        """"""
        return "This file are running from Local Python environment"

    # ----------------------------------------------------------------------

    def pitagoras(self, a, b):
        """"""
        return math.sqrt(a**2 + b**2)
