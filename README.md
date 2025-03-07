<!--
SPDX-FileCopyrightText: 2021 Petr Pucil <petr.pucil@seznam.cz>

SPDX-License-Identifier: CC0-1.0
-->

# Kaitai Struct table format Python parsing benchmark

[![REUSE compliant](https://github.com/generalmimon/ks-table-py-benchmark/actions/workflows/reuse-lint.yml/badge.svg)](
  https://github.com/generalmimon/ks-table-py-benchmark/actions/workflows/reuse-lint.yml
)

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

## Maintenance

### Licensing

> **Note:** requires https://github.com/fsfe/reuse-tool/. If `reuse --version` is not working for you,
> get the tool by following the steps on https://github.com/fsfe/reuse-tool#install.

Check for license/copyright issues:

```shell
reuse lint
```

Add comment headers with copyright and licensing information:

```shell
shopt -s globstar
reuse addheader --copyright="Petr Pucil <petr.pucil@seznam.cz>" --license="CC0-1.0" **/.gitignore README.md .github/workflows/reuse-lint.yml
reuse addheader --copyright="Petr Pucil <petr.pucil@seznam.cz>" --license="MIT" --style=python **/*.py **/*.ksy .github/workflows/main.yml
```
