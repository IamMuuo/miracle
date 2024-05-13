import os
from miracle import MIRFile
import sys

# Read the file
# mirFile: MIRFile = MIRFile("/home/erick/Desktop/your.MIR")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please call the program using program file.MIR")
        exit(1)

    mirFiles: list[MIRFile] = []

    for file in sys.argv[1:]:
        mirFiles.append(MIRFile(file))

    # Process the files
    for mirFile in mirFiles:
        data_bytes = mirFile.read_bytes()
        if data_bytes is not None:
            mirFile.parse(data_bytes)
