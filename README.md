
# Miracle

Miracle is a Python library designed to parse `.MIR` files from TravelPort systems and output them in JSON format. This tool simplifies the extraction and manipulation of travel-related data, making it accessible for further analysis or integration into larger systems.

## Features

- Parses `.MIR` files into structured JSON.
- Supports various data fields within `.MIR` files.
- Easily integrates into Python applications.

## Installation
Clone the Repo

First, clone the repository to your local machine:

```bash
git clone https://github.com/IamMuuo/miracle.git
```
Navigate into the Repo

Change directory to the repository folder:

```bash
cd miracle
```
Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```
Activate the Virtual Environment

Activate the virtual environment. The command differs based on your operating system:

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

Install the Project Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```
Run the Server

Finally, run the Django development server:

```bash
python manage.py runserver
```

Your server should now be running, and you can access it at http://127.0.0.1:8000/.


This creates a JSON file corresponding to your filename

## Usage

After the server is running, you can use Postman to send a file. Use the form-data option with the file field named mir_file to send a request to /parser/. This will return a neatly formatted parsed JSON from the file.


## Contributing
Contributions are welcome

## Licencing
Licensed under the GNU license
