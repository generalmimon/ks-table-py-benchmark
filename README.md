<!--
SPDX-FileCopyrightText: 2021 Petr Pucil <petr.pucil@seznam.cz>

SPDX-License-Identifier: CC0-1.0
-->

# Kaitai Struct table format Python parsing benchmark

See https://gitter.im/kaitai_struct/Lobby?at=6058ce092beb1e1da3c30cfa

Install Kaitai Struct runtime library for Python:

```shell
python3 -m pip install kaitaistruct
```

Generate test file `sample.bin`:

```shell
python3 ./generate_sample.py
```

Generate Python parsing code from `.ksy` files:

```shell
kaitai-struct-compiler -- --verbose file -d compiled -t python *.ksy
```

Run the benchmark:

```shell
python3 ./index.py
```
