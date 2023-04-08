def main(fields):
    # Создаем маску для всех битовых полей
    mask = 0
    for bit_range in [(0, 4), (9, 15), (16, 21), (22, 25)]:
        start, end = bit_range
        for i in range(start, end+1):
            mask |= (1 << i)

    # Получаем значения битовых полей и применяем маску
    n1 = (int(fields.get('N1', '0'), 16) << 0) & mask
    n3 = (int(fields.get('N3', '0'), 16) << 9) & mask
    n4 = (int(fields.get('N4', '0'), 16) << 16) & mask
    n5 = (int(fields.get('N5', '0'), 16) << 22) & mask

    # Собираем все биты вместе
    value = n1 | n3 | n4 | n5

    return value


if __name__ == '__main__':
    print(main({'N1': '0xf', 'N3': '0x68', 'N4': '0x17', 'N5': '0x6'})) # 26726415
    print(main({'N1': '0xf', 'N3': '0x39', 'N4': '0xa', 'N5': '0x2'})) # 9073167
    print(main({'N1': '0x7', 'N3': '0x18', 'N4': '0x26', 'N5': '0x7'})) # 31862791
    print(main({'N1': '0x1c', 'N3': '0x4e', 'N4': '0x17', 'N5': '0x7'})) # 30907420
