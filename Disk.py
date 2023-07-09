import requests

with open('Token.txt', 'rt', encoding='utf-8') as f:
    line = f.readline()

#Папку не создает, просто кидает файл на диск
class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
                }


    def _link_load_file(self,disk_file_path):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(link_url, headers=headers, params=params)
        return response.json()


    def load_file(self,disk_file_path,file_name):
        result = self._link_load_file(disk_file_path=disk_file_path)
        url = result.get('href')
        response = requests.put(url, data=open(file_name,'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    #path_to_file = 'Succ_ess.txt'
    token = line
    uploader = YaUploader(token)
    uploader.load_file(disk_file_path='Succ_ess.txt',file_name='Succ_ess.txt')