meta:
  id: test_cell
  license: MIT
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
    - id: table_rows
      type: table_row
      repeat: expr
      repeat-expr: n_rows
  table_row:
    seq:
    - id: flags
      type: u1
    - id: entries
      repeat: expr
      repeat-expr: _parent.n_columns
      type:
        switch-on: _parent.column_types[_index]
        cases:
          1: u2
          2: u4
          3: f4
          4: f8
