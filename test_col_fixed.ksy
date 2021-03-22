meta:
  id: test_col_fixed
  license: MIT
  ks-version: 0.9 # using `valid`
  endian: le
seq:
  - id: table
    type: data_table
types:
  data_table:
    seq:
    - id: n_rows
      type: u4
    - id: n_columns
      type: u1
    - id: column_types
      type: u2
      repeat: expr
      repeat-expr: n_columns
    - id: check_column_types
      size: 0
      valid:
        expr: |
          column_types.size == 4
          and column_types[0] == 1
          and column_types[1] == 2
          and column_types[2] == 3
          and column_types[3] == 4
    - id: table_rows
      type: table_row
      repeat: expr
      repeat-expr: n_rows
  table_row:
    seq:
    - id: flags
      type: u1
    - id: a
      type: u2
    - id: b
      type: u4
    - id: c
      type: f4
    - id: d
      type: f8
