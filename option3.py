from prettytable import PrettyTable

title = ['ПІП', "Вік", 'Категорія']
students_list = ['Іванов Іван Іванович', '23 роки', 'Студент 3 курсу', 
'Петров Семен Ігорович', '22 роки', 'Студент 2 курсу',
'Іванов Семен Ігорович', '22 роки', 'Студент 2 курсу',
'Акібов Ярослав Наумович', '23 роки', 'Студент 3 курсу',
'Борков Станіслав Максимович', '21 рік', 'Студент 1 курсу',
'Петров Семен Семенович', '21 рік', 'Студент 1 курсу',
'Романов Станіслав Андрійович', '23 роки', 'Студент 3 курсу ',
'Петров Всеволод Борисович', '21 рік', 'Студент 2 курсу']

def print_table():
    columns = len(title)  
    table = PrettyTable(title)  
    table_data = students_list[:]

    while table_data:
        table.add_row(table_data[:columns])
        table_data = table_data[columns:]
    print(table)

    