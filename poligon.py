import requests

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        per= 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        fer= {'Authorization': 'OAuth ' + token}
        path={'path': file_path}
        res=requests.get(per, headers=fer, params=path)
        print(res.status_code)
        foto=res.json()
        print(foto)

        per=foto['href']
        with open(file_path, 'rb') as f:
             res_2=requests.post(per, files={'file':f})
             print(res_2.status_code)


        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'STK-20191221-WA0003.webp'
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)