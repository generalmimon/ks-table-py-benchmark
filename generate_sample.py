from kaitaistruct import KaitaiStream
import random

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

pk_u1 = KaitaiStream.packer_u1
pk_u2le = KaitaiStream.packer_u2le
pk_u4le = KaitaiStream.packer_u4le
pk_f4le = KaitaiStream.packer_f4le
pk_f8le = KaitaiStream.packer_f8le

with open('./sample.bin', 'wb') as f:
    f.write(pk_u4le.pack(n_rows))
    f.write(pk_u1.pack(n_columns))
    for t in column_types:
        f.write(pk_u2le.pack(t))

    if is_row_0_fixed:
        assert column_types == [1, 2, 3, 4], 'column_types = {} does not match the row_0 format'.format(column_types)
        row_0 = [0x7a46, 0x86b97d9c, 0.842150092124939, 0.5340359913176319]

        f.write(b'\x00')
        f.write(pk_u2le.pack(row_0[0]))
        f.write(pk_u4le.pack(row_0[1]))
        f.write(pk_f4le.pack(row_0[2]))
        f.write(pk_f8le.pack(row_0[3]))

    for y in range(n_rows - 1):
        f.write(b'\x00')
        for t in column_types:
            if t == COL_U2:
                f.write(pk_u2le.pack(random.randrange(0, 0xffff)))
            elif t == COL_U4:
                f.write(pk_u4le.pack(random.randrange(0, 0xffffffff)))
            elif t == COL_F4:
                f.write(pk_f4le.pack(random.random()))
            elif t == COL_F8:
                f.write(pk_f8le.pack(random.random()))
    print('{} bytes written'.format(f.tell()))
