""" Mojo module that depends on a Python module which
    provides serialization functions using the Python 'pickle' library.

    Structs:
        MyStruct

    Functions:
        <None>

    Misc Variables:
        <None>
"""

from python import Python

alias LF: String = "\n"
alias KEY = "Authorization"
alias VALUE = "Bearer 0123456789ABCDEF"
alias PY_OBJECT_HEX = "8004952e000000000000007d948c0d417574686f72697a6174696f6e948c17426561726572203031323334353637383941424344454694732e"


struct MyStruct:
    fn __init__(inout self) raises:
        pass

    fn getResponse(inout self) raises -> String:
        Python.add_to_path("./")

        var py_module = Python.import_module("my_pickle")

        var py_dict = Python.dict()
        py_dict[KEY] = VALUE
        print("getResponse.py_dict[" + KEY + "]   =", py_dict[KEY])

        """
        to_pickle:
            The following line returns a valid pickled value, prints it, then crashes.
            ...
            Segmentation fault (core dumped)
        """
        var py_object_hex: String = py_module.to_pickle(py_dict.py_object)
        # var py_object_hex: String = PY_OBJECT_HEX  # Debug, uncomment if pickling is disabled above
        print("getResponse.py_object_hex =", py_object_hex + LF)

        """ 
        from_pickle:
            Comment out the preceding call 'to_pickle', then
            inject a pickled value (PY_OBJECT_HEX),and the
            unpickling works.
        """
        var py_object = py_module.from_pickle(py_object_hex)
        print("getResponse.py_object[" + KEY + "] =", py_object[KEY])

        var response = py_module.get(py_object_hex)
        return response


fn main() raises:
    var my_struct = MyStruct()
    var response: String = my_struct.getResponse()
    print("main.response =", response)
