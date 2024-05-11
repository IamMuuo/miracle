from miracle import MIRFile

# Read the file
mirFile: MIRFile = MIRFile("/home/erick/Desktop/your.MIR")


# get the bytes
data_bytes = mirFile.read_bytes()

if data_bytes is not None:
    print(data_bytes)
