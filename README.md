# О проекте
Реализовать телефонный справочник со следующими возможностями:
1. Вывод постранично записей из справочника на экран
2. Добавление новой записи в справочник
3. Возможность редактирования записей в справочнике
4. Поиск записей по одной или нескольким характеристикам

Требования к программе:
1. Реализация интерфейса через консоль (без веб- или графического интерфейса)
2. Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3. В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

Плюсом будет:
1. Аннотирование функций и переменных
2. Документирование функций
3. Подробно описанный функционал программы
4. Размещение готовой программы и примера файла с данными на github


## Разворачивание проекта

Необходимые компоненты
1. Python >=3.9

## Описание функциональности команд для терминала

После запуска скрипта в консоли
- `python main.py` - запускает основную функцию справочника для работы.

Далее вводим число определенной задачи:
- `1` - Создать телефонный справочник  
- `2` - Вывод постранично записей из справочника на экран 
- `3` - Добавление новой записи в справочник 
- `4` - Возможность редактирования записей в справочнике 
- `5` - Поиск записей по одной или нескольким характеристикам 
- `6` - Завершить работу с телефонным справочником
- `7` - Удалить телефонный справочник 

Создать телефонный справочник:
- Телефонный справочник создается автоматически если его не существует при введении числа 1

Вывод постранично записей из справочника на экран:
- Телефонный справочник выводит записи на экран автоматически при введении числа 2

Добавление новой записи в справочник:
- Вводим фамилию (только буквы)
- Вводим имя  (только буквы)
- Вводим отечество (только буквы)
- Вводим название организации (любые символы)
- Вводим номер рабочего телефона (только 10 цифр)
- Вводим номер (личного) сотового телефона (только 10 цифр)

Возможность редактирования записей в справочнике:
- Вводим фамилию и имя (через запятую без пробела), чьи данные хотите изменить
- Вводим характеристики которые вы хотите изменить (через запятую без пробела)
- Вводим новые данные

Поиск записей по одной или нескольким характеристикам:
- Вводим характеристики по которым необходимо произвести поиск (через запятую без пробела)
- Вводим новые данные

Завершить работу с телефонным справочником:
- Телефонный справочник завершает работу автоматически при введении числа 6

Удалить телефонный справочник:
- Телефонный справочник удаляется автоматически при введении числа 7

