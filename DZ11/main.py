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
    e1 = [reader.read(Types.uint64) for _ in range(2)]
    e2_size = reader.read(Types.uint16)
    e2_offset = reader.read(Types.uint16)
    e2_reader = reader.jump(e2_offset)
    e2 = [e2_reader.read(Types.uint64) for _ in range(e2_size)]
    e3 = reader.read(Types.int8)
    e4 = reader.read(Types.uint64)
    e5 = reader.read(Types.uint32)
    e6 = reader.read(Types.float)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6)


def read_d(reader):
    d1 = reader.read(Types.int8)
    d2 = reader.read(Types.uint16)
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.double)
    c2 = [read_d(reader) for _ in range(3)]
    e_offset = reader.read(Types.uint16)
    e_reader = reader.jump(e_offset)
    c3 = read_e(e_reader)
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = b''.join([reader.read(Types.char) for _ in range(6)]).decode('utf-8')
    b2_size = reader.read(Types.uint16)
    b2_offset = reader.read(Types.uint16)
    b2_reader = reader.jump(e2_offset)
    b2 = [e2_reader.read(Types.uint64) for _ in range(e2_size)]
    b3 = reader.read(Types.int64)
    b4 = reader.read(Types.int64)
    b5 = reader.read(Types.int64)
    b6 = reader.read(Types.int64)
    b7 = reader.read(Types.uint16)
    return dict(B1=b1, B2=b2)


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
    print(main(b'UYKD\xed\x81q\xa6\x9b\xb9w\x9b\x01\xd1\x1cn"\xe8\xd9\xd2\xdc\xd6\x9b\xf4'
               b'ge3\x00q\xbb\x98\x8e\xf72M\xd7\xea?\xe8\x9e\x00]\xc2\xc5\xab\xdaon'
               b'\x00\x00\x00\x8a\xe9\xe6+=\x9a\xfd-\x13(\xee#\xee\x98&/X@\x12E\x87{\xd9{^'
               b'\x8d\xc6\xc9\xef\xf7\xbf\xfcX\x1c\x13\xc7\xb2B\xb5\xdb\xc4\xf6>p\x1f'
               b'R\xc5\xb3\x84\x06u\xb94\x88\x1e\x7f\xc9ax\x9b\x1a\xc2fQ\xc7l \x102\xc3\xa36`'
               b'$\xeb\x07\x006\x00\x1b\x11\xba\x15\x9e\x1c\x85\xf7t\xa3\x1f| O\n\xe7<'))