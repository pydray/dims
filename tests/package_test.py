# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2024 Pydray contributors (https://github.com/pydray)
import dims as pkg


def test_has_version():
    assert hasattr(pkg, '__version__')
