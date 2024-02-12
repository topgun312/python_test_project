import csv
import os
import sys
from os.path import exists
from typing import Dict, List

phone_data = []
header_names = [
    "Фамилия",
    "Имя",
    "Отчество",
    "Название организации",
    "Телефон рабочий",
    "Телефон личный (сотовый)",
]


class PhoneBook:
    """
    Класс для работы с телефонным справочником.
    """

    def create_csv_file(self) -> None:
        """
        Метод класса для создания csv файла
        """

        path = "phonebook.csv"
        if exists(path):
            print('Телефонный справочник уже существует!')
        else:
            with open("phonebook.csv", "w", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",", lineterminator="\r")
                writer.writerow(header_names)
                print("Телефонный справочник создан.")

    def add_user_data(self) -> List[Dict]:
        """
        Метод класса для добавления данных пользователя.
        :return: список с данными в виде словаря
        """
        global work_phone_number, cell_phone_number

        while True:
            surname = input("Введите фамилию: ")
            if surname.isalpha():
                break
            else:
                print(
                    "В фамилии должны быть только буквы! Введите фамилию корректно пожалуйста!"
                )
                continue

        while True:
            name = input("Введите имя: ")
            if name.isalpha():
                break
            else:
                print(
                    "В имени должны быть только буквы! Введите имя корректно пожалуйста!"
                )
                continue

        while True:
            patronymic = input("Введите отчество: ")
            if patronymic.isalpha():
                break
            else:
                print(
                    "В отчестве должны быть только буквы! Введите отчество корректно пожалуйста!"
                )
                continue

        name_organization = input("Введите название организации: ")

        while True:
            try:
                work_phone_number = int(input("Введите рабочий телефон: "))
            except ValueError:
                print(
                    "В номере телефона должны быть только числа! Введите номер телефона корректно пожалуйста!"
                )
                continue
            if len(str(work_phone_number)) == 10:
                break
            else:
                print("В номере телефона должно быть 10 чисел")
                continue

        while True:
            try:
                cell_phone_number = int(input("Введите личный (сотовый) телефон: "))
            except ValueError:
                print(
                    "В номере телефона должны быть только числа! Введите номер телефона корректно пожалуйста!"
                )
                continue
            if len(str(cell_phone_number)) == 10:
                break
            else:
                print("В номере телефона должно быть 10 чисел")
                continue

        phone_data.append(
            {
                "surname": surname,
                "name": name,
                "patronymic": patronymic,
                "name_organization": name_organization,
                "work_phone_number": work_phone_number,
                "cell_phone_number": cell_phone_number,
            }
        )

        return phone_data

    def add_user(self) -> None:
        """
        Метод класса для добавления пользователя в телефонный справочник.
        """
        path = "phonebook.csv"
        if not exists(path):
            self.create_csv_file()
        else:
            phonebook_data = self.add_user_data()
            for phone_user in phonebook_data:
                with open("phonebook.csv", "a", encoding="utf-8") as file:
                    writer = csv.writer(file, delimiter=",", lineterminator="\r")
                    writer.writerow(
                        (
                            phone_user["surname"],
                            phone_user["name"],
                            phone_user["patronymic"],
                            phone_user["name_organization"],
                            phone_user["work_phone_number"],
                            phone_user["cell_phone_number"],
                        )
                    )
            phonebook_data.clear()
            print("Запись добавлена в телефонный справочник!")

    def read_phonebook_data(self) -> None:
        """
        Метод класса для вывода постранично записей из справочника на экран.
        """
        with open("phonebook.csv", "r", encoding="utf-8") as file:
            file_reader = csv.reader(file, delimiter=",")
            count = 0
            for row in file_reader:
                print(f"{row[0]}, {row[1]}, {row[2]}, " f"{row[3]}, {row[4]}, {row[5]}")
                count += 1
            print(f"Всего в телефонном справочнике {count - 1} записей.")

    def update_user_data(self) -> None:
        """
        Метод класса для редактирования записей в справочнике.
        """
        surname, name = input(
            "Введите фамилию и имя (через запятую без пробела), чьи данные хотите изменить: "
        ).split(",")
        fields_to_update = input(
            "Введите данные которые вы хотите изменить (через запятую без пробела): "
        ).split(",")
        data_to_update = {}
        for field in fields_to_update:
            data_to_update[field] = input(f"Введите {field}: ")

        with open("phonebook.csv", "r+", newline="", encoding="utf-8") as file:
            content = file.readlines()
            for num, row in enumerate(content):
                row = row.split(",")
                if row[0] == surname and row[1] == name:
                    for key, value in data_to_update.items():
                        index = header_names.index(key)
                        row[index] = value
                    qwerty = num
                    break
            new_text = ",".join([i for i in row])
            content.pop(qwerty)
            content.insert(qwerty, new_text)
            content = "".join(content)
            file.seek(0)
            file.write(content)

    def search_phonebook_data(self) -> None:
        """
        Метод класса для поиска записей по одной или нескольким характеристикам.
        """
        fields_to_search = input(
            "Введите характеристики по которым необходимо произвести поиск (через запятую без пробела): "
        ).split(",")
        data_to_search = {}
        for field in fields_to_search:
            data_to_search[field] = input(f"Введите {field}: ")

        with open("phonebook.csv", "r", newline="", encoding="utf-8") as file:
            file_reader = csv.reader(file, delimiter=",")
            for row in file_reader:
                if all([x in row for x in data_to_search.values()]):
                    print(", ".join(row))

    def delete_phonebook(self) -> None:
        """
        Функция для удаления телефонного справочника.
        """
        os.remove("phonebook.csv")
        print("Удалить телефонный справочник")

    def exit_phonebook(self) -> None:
        """
        Метод класса для остановки работы справочника.
        """
        print("Работа с телефонным справочником завершена!")
        sys.exit()


def create_tasks() -> None:
    """
    Основная функция для запуска работы всех возможностей телефонного справочника.
    """
    while True:
        try:
            a = PhoneBook()
            task = int(
                input(
                    "Введите номер задачи для работы с телефонным справочником: \n"
                    "1 - Создать телефонный справочник  \n"
                    "2 - Вывод постранично записей из справочника на экран \n"
                    "3 - Добавление новой записи в справочник \n"
                    "4 - Возможность редактирования записей в справочнике \n"
                    "5 - Поиск записей по одной или нескольким характеристикам \n"
                    "6 - Завершить работу с телефонным справочником \n"
                    "7 - Удалить телефонный справочник \n"
                )
            )
            if task == 1:
                a.create_csv_file()
            elif task == 2:
                a.read_phonebook_data()
            elif task == 3:
                a.add_user()
            elif task == 4:
                a.update_user_data()
            elif task == 5:
                a.search_phonebook_data()
            elif task == 6:
                a.exit_phonebook()
            elif task == 7:
                a.delete_phonebook()
            else:
                print("Введите число от 1 до 7 для корректной работы со справочником!")
                continue
        except Exception as ex:
            print("Ошибка!", str(ex))


if __name__ == "__main__":
    create_tasks()




