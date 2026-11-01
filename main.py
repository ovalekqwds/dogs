import requests
import os
from pathlib import Path
import shutil


def download_picture(folder, filename, picture_link):
    file_path=os.path.join(folder, filename)
    response = requests.get(picture_link)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def main():
    folder="dogs"
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder,exist_ok=True)
    for number in range(50):
        url = 'https://random.dog/woof.json'
        params = {"filter":"mp4,webm"}
        response = requests.get(url,params=params)
        response.raise_for_status()
        picture_link=response.json()["url"]
        print(picture_link)
        picture_extension=Path(picture_link).suffix
        print(picture_extension)
        filename=f"dog_{number}{picture_extension}"
        download_picture(folder,filename,picture_link)


if __name__ == '__main__':
    main()
