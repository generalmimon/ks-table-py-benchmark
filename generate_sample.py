import random
import struct

endian = 'little'

n_rows = 8192
n_columns = 4
column_types = [1, 2, 3, 4]

is_row_0_fixed = True

COL_U2 = 1
COL_U4 = 2
COL_F4 = 3
COL_F8 = 4

assert len(column_types) == n_columns, 'len(column_types) = {} must be equal to n_columns = {}'.format(
    len(column_types),
    n_columns
)

packer_f4le = struct.Struct('<f')
packer_f8le = struct.Struct('<d')

with open('./sample.bin', 'xb') as f:
    f.write(n_rows.to_bytes(4, endian))
    f.write(n_columns.to_bytes(1, endian))
    for t in column_types:
        f.write(t.to_bytes(2, endian))

    if is_row_0_fixed:
        assert column_types == [1, 2, 3, 4], 'column_types = {} does not match the row_0 format'.format(column_types)
        row_0 = [0x7a46, 0x86b97d9c, 0.842150092124939, 0.5340359913176319]

        f.write(b'\x00')
        f.write(row_0[0].to_bytes(2, endian))
        f.write(row_0[1].to_bytes(4, endian))
        f.write(packer_f4le.pack(row_0[2]))
        f.write(packer_f8le.pack(row_0[3]))

    for y in range(n_rows - 1):
        f.write(b'\x00')
        for t in column_types:
            if t == COL_U2:
                f.write((random.randrange(0, 0xffff)).to_bytes(2, endian))
            elif t == COL_U4:
                f.write((random.randrange(0, 0xffff_ffff)).to_bytes(4, endian))
            elif t == COL_F4:
                f.write(packer_f4le.pack(random.random()))
            elif t == COL_F8:
                f.write(packer_f8le.pack(random.random()))
