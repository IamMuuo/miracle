import requests


def send_file_to_api(file_path):
    url = "http://localhost:8000/parser/"
    files = {"mir_file": open(file_path, "rb")}
    response = requests.post(url, files=files)
    return response
