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

    c_offset = reader.read(Types.uint16)
    c_reader = reader.jump(c_offset)
    address_c_uint16 = read_c(c_reader)

    b2_size = reader.read(Types.uint16)
    b2_offset = reader.read(Types.uint16)
    b2_reader = reader.jump(b2_offset)
    b2 = [b2_reader.read(address_c_uint16) for _ in range(b2_size)] #бляяяяяяя

    b3 = reader.read(Types.int64)

    b4_size = reader.read(Types.uint32)
    b4_offset = reader.read(Types.uint32)
    b4_reader = reader.jump(b4_offset)
    b4 = [b4_reader.read(Types.int64) for _ in range(b4_size)]

    b5_size = reader.read(Types.uint32)
    b5_offset = reader.read(Types.uint16)
    b5_reader = reader.jump(b5_offset)
    b5 = [b5_reader.read(Types.uint16) for _ in range(b5_size)]

    d_offset = reader.read(Types.uint32) # может быть uint16
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
    print(main(b'WRCO\xf0\x8d\x00\x00\x00\x9e\xd9\x1c?\x05\x7f\xab\xb9\xa4\xeb\xa4'
               b'\xe9\xe6\x83\x95=\xc5\xe9\xe2\xb7h2\x18P\xf3\tL\x05\t>\xd1\xf9<~\xcf'
               b'Tm\x08\xe8\xbf\xae\xf6\xdf\xbd\xad\x91\xd9\xf7\x8fG\x0e\xc6\x7fF\xe7'
               b'\x7f\xb2\x96\x13\xa0\x93U\xdb\xd5t\xa8?8\xcc\x81\xa5\xcc\xa5\xf1+'
               b'\x13\xf0\xef?}.\x97\rD\x00P\x00\xbf\x131\xfe\rP+\xefFXhMk\xef\x83\x02'
               b'\x0e\x9f\xd8\x9b\x1ctV\x86\x8d^\xef\x1e~D\xaf]<\x94\xc1}\xcc\xb8\xa9\xc3'
               b"\xb5'\x1b\xc3\x97wzjgjj\x02\x00\x00\x00\\\x00\x00\x00\xed0\xce\x86\x17"
               b'"B\xaa\x02\x00\x00\x00`\x00\x00\x00\x05\x00\x00\x00p\x00z\x00\x00\x00\x97p'))
