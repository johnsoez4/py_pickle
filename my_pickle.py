""" Module that provides serialization functions
    using the Python 'pickle' library.

    In a real application, the 'get' function would
    do something useful, but for now it only deserializes
    a Python object using the function 'from_pickle' to show
    how it's used.

    Classes:
        <None>

    Functions:
        get
        to_pickle
        from_pickle

    Misc Variables:
        <None>
"""

import pickle
from typing import Any


def get(py_object_hex: str) -> str:
    py_object = from_pickle(py_object_hex)

    print("get.object_hex =", py_object_hex)  # Debug
    print("get.py_object =", py_object)  # Debug

    '''
    Do something useful with the Python object here
    and return a string value.
    '''
    return "Some string"


def to_pickle(py_object: Any) -> str:
    '''Function to serialize a Python object.

        Args:
            py_object (object): A Python object

        Returns:
            str: The object's equivalent as a hexadecimal string value.
                Example (dict): "8004952e000000000000007d948c0d417574686f72697a6174696f6e948c17426561726572203031323334353637383941424344454694732e"
    '''
    return pickle.dumps(py_object).hex().__str__()


def from_pickle(py_object_hex: str) -> Any:
    '''Function to unserialize a Python object from it's string representation.

        Args:
            py_object_hex (str): A Python object serialized as a hexadecimal string.

        Returns:
            Any: A Python object.
                Example (dict): {'Authorization': 'Bearer 0123456789ABCDEF'}
    '''
    return pickle.loads(bytes.fromhex(py_object_hex))


if __name__ == "__main__":
    py_dict = {"Authorization": 'Bearer 0123456789ABCDEF'}

    print('py_dict = ', py_dict)
    py_object_hex = to_pickle(py_dict)
    print('py_object_hex = ', py_object_hex)
    py_object = from_pickle(py_object_hex)
    print('py_object = ', py_object)

    result = get(py_object_hex)
    print('main.result = ', result)
