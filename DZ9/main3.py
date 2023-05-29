def swap_name(full_name):
    full_name = full_name.split(" ")
    full_name = full_name[1] + " " + full_name[0]
    return full_name


def clear_number(number):
    number = number.replace("+7 (", "").replace(") ", "-")
    number = number[:10] + number[11:]
    return number


def change_bool(letter):
    if letter == 'Y':
        return 'true'
    else:
        return 'false'


def main(input_table):
    table = input_table

    result_table = []

    for row in table:
        new_row = []
        new_row.append(swap_name(row[0]))
        new_row.append(clear_number(row[2]))
        new_row.append(change_bool(row[4]))
        result_table.append(new_row)

    return result_table


if __name__ == '__main__':
    # Пример 1
    input_table_1 = [
        ["Ноласянц Анатолий", None, "+7 (887) 726-13-76", None, "N"],
        ["Сошук Юрий", None, "+7 (128) 319-98-20", None, "Y"],
        ["Сочегин Артемий", None, "+7 (722) 550-27-25", None, "Y"]
    ]
    print(main(input_table_1))


    # Ожидаемый результат:
    # Анатолий Ноласянц 887-726-1376	false
    # Юрий Сошук	128-319-9820	true
    # Артемий Сочегин	722-550-2725	true

