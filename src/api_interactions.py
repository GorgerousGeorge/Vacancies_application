import abc
import requests


class JobAPI(abc.ABC):
    @abc.abstractmethod
    def _connect(self):
        """Метод для подключения к API"""
        pass

    @abc.abstractmethod
    def get_vacancies(self, keyword: str):
        """Метод для получения вакансий по ключевому слову"""
        pass


class hh_API(JobAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = None

    def _connect(self):
        """Метод для подключения к API"""
        self.__session = requests.Session()
        response = self.__session.get(self.BASE_URL)
        response.raise_for_status()
        return response

    def get_vacancies(self, keyword: str, cantidad: int):
        """Метод для получения вакансий по ключевому слову"""
        self._connect()

        params = {
            'text': keyword,
            'per_page': cantidad
        }

        response = self.__session.get(self.BASE_URL, params=params)
        response.raise_for_status()

        vacancies = response.json().get('items', [])
        return [
            {
                'name': vacancy['name'],
                'url': vacancy['alternate_url'],
                'salary': vacancy.get('salary')
            }
            for vacancy in vacancies
        ]


if __name__ == "__main__":
    hh_api = hh_API()
    try:
        vacancies = hh_api.get_vacancies("Python", 10)
        for vacancy in vacancies:
            print(f"Название: {vacancy['name']}, Ссылка: {vacancy['url']}, Зарплата: {vacancy['salary']}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
