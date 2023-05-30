from struct import unpack_from, calcsize


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_e(reader):
    e1 = reader.read(Types.float)
    e2 = reader.read(Types.int32)
    e3 = reader.read(Types.uint32)
    e4 = reader.read(Types.float)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4)


def read_d(reader):
    d1 = reader.read(Types.int64)
    d2 = reader.read(Types.int8)
    d3 = reader.read(Types.int32)
    d4 = reader.read(Types.int16)
    d5 = reader.read(Types.int32)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5)


def read_c(reader):
    c1 = reader.read(Types.double)
    c2 = reader.read(Types.uint32)
    return dict(C1=c1, C2=c2)


def read_b(reader):
    b1 = b''.join([reader.read(Types.char) for _ in range(6)]).decode('utf-8')

    b2_size = reader.read(Types.uint32)
    b2_offset = reader.read(Types.uint32)
    b2_reader = reader.jump(b2_offset)
    b2 = [read_c(reader.jump(b2_reader.
                             read(Types.uint16))) for _ in range(b2_size)]

    b3 = reader.read(Types.int64)

    b4_size = reader.read(Types.uint32)
    b4_offset = reader.read(Types.uint32)
    b4_reader = reader.jump(b4_offset)
    b4 = [b4_reader.read(Types.int64) for _ in range(b4_size)]

    b5_size = reader.read(Types.uint32)
    b5_offset = reader.read(Types.uint16)
    b5_reader = reader.jump(b5_offset)
    b5 = [b5_reader.read(Types.uint16) for _ in range(b5_size)]

    d_offset = reader.read(Types.uint32)
    d_reader = reader.jump(d_offset)
    b6 = read_d(d_reader)

    b7 = reader.read(Types.uint16)

    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)


def read_a(reader):
    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump(b_offset)
    a1 = read_b(b_reader)
    a2 = read_e(reader)
    a3 = reader.read(Types.uint64)
    a4 = reader.read(Types.int64)
    a5 = reader.read(Types.double)
    a6 = [reader.read(Types.int32) for _ in range(4)]
    a7 = reader.read(Types.uint16)
    a8 = reader.read(Types.int8)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(stream):
    return read_a(BinaryReader(stream, 5))

if __name__ == '__main__':
    print(main(b'WRCO\xf0\x89\x00\x00\x00I6V?p%\xf0\xcb\xd0\xf1^0\x04\xf25?\x1f\xc0\x08'
               b'\xbd\xfc\x80\x0e\x85\x88\xc8$\xabn\x06\xe3\x13@\xccnS\x18\xc7\xa7?\x08\xfeC'
               b'`p\x06\xc2V\xebP]\xd4\xda\xbd\x7f[\xcd\x9f\xa7\x1e\xc6\xfe\x8aM\xa5\xe9\xbf'
               b'\xa7>i\x82\xfe\xfcjL;}\xe6?\xdfK\xf4\x12D\x00P\x00\xfbzP\x98\x00\x91\x10\xeb'
               b'TK\x96\x8e\xfa\xb6\x00]\xa3\xd31\xe2\n\xff_\xb9Q\xf6\x99`\xeb\xb8?\xfceEGD'
               b'\xf5\xe5\xca\x9dBzvmzzr\x02\x00\x00\x00\\\x00\x00\x00\x14\x03\x1auU'
               b'\xa6Z\xaf\x02\x00\x00\x00`\x00\x00\x00\x03\x00\x00\x00p\x00v\x00\x00'
               b'\x00S\xc9'))
