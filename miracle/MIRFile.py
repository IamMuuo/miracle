"""
MIRFile

author: Erick Muuo

A class that representing a MIR file and expose functionality
to parse a .MIR file
"""

import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from .MIRBody import MIRBody
from .MIRHeader import MIRHeader
import json


class MIRFile:

    def __init__(self, path: str = "") -> None:
        self.path: str = path
        self.header: MIRHeader = MIRHeader()
        self.body: MIRBody = MIRBody()

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
        print(self.path)
        if not self.path.endswith(".MIR"):
            raise Exception("The specified file is not of .MIR format")

        with open(self.path, "rb") as fobj:
            data: bytes = fobj.read(-1)

            if len(data) <= 0:
                raise Exception(
                    "The specified .MIR file was empty and cannot be parsed"
                )

            return data

    def read_in_memory_file_bytes(
        self, uploaded_file: InMemoryUploadedFile
    ) -> bytes | None:
        """

        Open the specified .MIR file and read its bytes

        Incase of any error expect the function to throw an exception and
        return None
        """

        file_extension = os.path.splitext(uploaded_file.name)
        extension_valid = ".MIR" in file_extension

        if extension_valid:
            data: bytes = bytes()
            for chunk in uploaded_file.chunks():
                data += chunk

            if len(data) <= 0:
                raise Exception(
                    "The specified .MIR file was empty and cannot be parsed"
                )

            return data

        raise Exception("The specified .MIR file cannot be parsed")

    def parse(self, data: bytes):
        self.header.from_bytes(data[0:344])
        self.body.parse(data[344:])

        return {
            "header": self.header.header_info,
            "body": self.body.to_serializable(),
        }
