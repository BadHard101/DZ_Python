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
    e_offset = reader.read(Types.uint32)
    e_reader = reader.jump(e_offset)
    c3 = read_e(e_reader)
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = reader.read(Types.uint8)
    b2 = reader.read(Types.uint16)
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.uint64)
    a2 = reader.read(Types.int32)
    a3 = reader.read(Types.uint64)
    a4 = b''.join([reader.read(Types.char) for _ in range(2)]).decode('utf-8')
    b_offset = reader.read(Types.uint16)
    b_reader = reader.jump(b_offset)
    a5 = read_b(b_reader)
    a6 = reader.read(Types.int16)
    a7 = read_c(reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(stream):
    return read_a(BinaryReader(stream, 4))

if __name__ == '__main__':
    print(main(b'UYKDL\x90\r\x10\xe0ZM\xd8<\xcd\xdaj\xef\xd0n\x9b/`\xc6\xa4nf3\x00'
               b'Z\x85\x18\xe1I\x03\x08\xfe\xef?D\xccV\x050\x03IhHN\x00\x00\x00e\x9e$\xd0\xa1'
               b"-%\xe0d\xccU,\xc9Xo\xf6\xab\x06M\x12]\xc6\xbc~\xa2'\xcc6\xa9a\xdf\x8e5"
               b'A\xd9g\xf3H\xa8E^W\x81\x03\x006\x00q\x9a$h\xf5Q\x96\x804%\xef\xad\x16gB;?'))
