"""
MIRFile

author: Erick Muuo

A class that representing a MIR file and expose functionality
to parse a .MIR file
"""


class MIRFile:

    def __init__(self, path: str = "") -> None:
        self.path: str = path
        self.header: dict = dict()
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
