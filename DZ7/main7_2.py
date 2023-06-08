def main(hex_string):
    # Преобразование шестнадцатиричной строки в целое число
    value = int(hex_string, 16)

    # Извлечение значений битовых полей
    G4 = str((value >> 10) & 0x3F)
    G3 = str((value >> 9) & 0x01)
    G2 = str((value >> 4) & 0x1F)
    G1 = str(value & 0x0F)

    # Сохранение значений в словаре
    result = {'G1': G1, 'G2': G2, 'G3': G3, 'G4': G4}

    return result

if __name__ == '__main__':
    print(main('0x2188'))  # {'G1': '8', 'G2': '24', 'G3': '0', 'G4': '8'}
    print(main('0x1b37'))  # {'G1': '7', 'G2': '19', 'G3': '1', 'G4': '6'}
    print(main('0xff1e'))  # {'G1': '14', 'G2': '17', 'G3': '1', 'G4': '63'}
    print(main('0xbd98'))  # {'G1': '8', 'G2': '25', 'G3': '0', 'G4': '47'}
