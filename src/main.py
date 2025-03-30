from src.vacancies import Vacancy
from src.filehandler import JSONFileHandler
from src.api_interactions import hh_API


def user_interaction():
    hh_api = hh_API()
    file_handler = JSONFileHandler()

    while True:
        print("\nДобро пожаловать в систему поиска вакансий!")
        print("Выберите действие:")
        print("1. Найти вакансии по ключевому слову")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в названии")
        print("4. Сохранить вакансии в файл")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            cantidad = int(input("Введите количество вакансий для получения: "))
            try:
                vacancies_data = hh_api.get_vacancies(keyword, cantidad)
                vacancies = [
                    Vacancy(
                        name=vacancy['name'],
                        company=vacancy['employer']['name'],
                        url=vacancy['alternate_url'],
                        salary=vacancy.get('salary')
                    )
                    for vacancy in vacancies_data
                ]
                if vacancies:
                    print(f"\nНайдено {len(vacancies)} вакансий по запросу '{keyword}':")
                    for vacancy in vacancies:
                        print(
                            f"- {vacancy.name} в компании {vacancy.company}, зарплата: {vacancy.salary}, "
                            f"ссылка: {vacancy.url}")
                else:
                    print("Вакансии не найдены.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == '2':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            cantidad = int(input("Введите количество вакансий для получения: "))
            try:
                vacancies_data = hh_api.get_vacancies(keyword, cantidad)
                vacancies = [
                    Vacancy(
                        name=vacancy['name'],
                        company=vacancy['employer']['name'],
                        url=vacancy['alternate_url'],
                        salary=vacancy.get('salary')
                    )
                    for vacancy in vacancies_data
                ]
                top_vacancies = sorted(vacancies, key=lambda x: x.salary['to'] if x.salary else 0, reverse=True)[
                                :cantidad]
                if top_vacancies:
                    print(f"\nТоп {cantidad} вакансий по зарплате по запросу '{keyword}':")
                    for vacancy in top_vacancies:
                        print(
                            f"- {vacancy.name} в компании {vacancy.company}, зарплата: {vacancy.salary}, "
                            f"ссылка: {vacancy.url}")
                else:
                    print("Вакансии не найдены.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == '3':
            keyword = input("Введите ключевое слово для поиска в названии вакансий: ")
            cantidad = int(input("Введите количество вакансий для получения: "))
            try:
                vacancies_data = hh_api.get_vacancies(keyword, cantidad)
                vacancies = [
                    Vacancy(
                        name=vacancy['name'],
                        company=vacancy['employer']['name'],
                        url=vacancy['alternate_url'],
                        salary=vacancy.get('salary')
                    )
                    for vacancy in vacancies_data
                ]
                filtered_vacancies = [vacancy for vacancy in vacancies if keyword.lower() in vacancy.name.lower()]
                if filtered_vacancies:
                    print(f"\nВакансии с ключевым словом '{keyword}' в названии:")
                    for vacancy in filtered_vacancies:
                        print(
                            f"- {vacancy.name} в компании {vacancy.company}, зарплата: {vacancy.salary}, "
                            f"ссылка: {vacancy.url}")
                else:
                    print("Вакансии не найдены.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == '4':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            cantidad = int(input("Введите количество вакансий для получения: "))
            try:
                vacancies_data = hh_api.get_vacancies(keyword, cantidad)
                vacancies = [
                    {
                        'name': vacancy['name'],
                        'company': vacancy['employer']['name'],
                        'url': vacancy['alternate_url'],
                        'salary': vacancy.get('salary'),
                        'id': vacancy.get('id')  # Предполагается, что у вакансии есть уникальный идентификатор
                    }
                    for vacancy in vacancies_data
                ]
                if vacancies:
                    for vacancy in vacancies:
                        file_handler.add_vacancy(vacancy)
                    print(f"Вакансии успешно сохранены в файл '{file_handler._FileHandler__filename}'.")
                else:
                    print("Вакансии не найдены.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 5.")
