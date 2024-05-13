"""
MIRFile

author: Erick Muuo

A class that representing a MIR file and expose functionality
to parse a .MIR file
"""

from .MIRHeader import MIRHeader
import json


class MIRFile:

    def __init__(self, path: str = "") -> None:
        self.path: str = path
        self.header: MIRHeader = MIRHeader()
        self.body: dict = dict()

    def set_file_path(self, path: str):
        """
        Sets the path of the MIR file.
        """
        self.path = path

    def read_bytes(self) -> bytes | None:
        """
        Open the specified .MIR file and read its bytes

        Incase of any error expect the function to throw an exception and
        return None
        """
        if not self.path.endswith(".MIR"):
            raise Exception("The specified file is not of .MIR format")

        with open(self.path, "rb") as fobj:
            data: bytes = fobj.read(-1)

            if len(data) <= 0:
                raise Exception(
                    "The specified .MIR file was empty and cannot be parsed"
                )

            return data

    def parse(self, data: bytes):
        self.header.from_bytes(data[0:344])

        file_name = self.path.split("/")[-1]
        file_name = file_name.replace(".MIR", ".json")

        with open(file_name, "w") as fobj:
            json.dump(self.header.header_info, fobj, indent=4)
