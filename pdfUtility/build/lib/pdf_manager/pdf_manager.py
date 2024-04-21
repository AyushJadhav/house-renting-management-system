import requests

def download_pdf(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

def upload_pdf(file_path, upload_url):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(upload_url, files=files)
    return response.status_code
