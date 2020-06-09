#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # (1 Custom unit tests)

    def test_read_alt(self):
        s = "44 555\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 44)
        self.assertEqual(j, 555)

    # ----
    # eval
    # ----

    # (Given unit tests)

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # (9 Custom unit tests)

    # test edge cases
    def test_eval_edge_1(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_edge_2(self):
        v = collatz_eval(999999, 999999)
        self.assertEqual(v, 259)

    # optimization consistency
    def test_eval_theorem_1(self):
        v = collatz_eval(4, 40)
        q = collatz_eval(6, 40)
        self.assertEqual(v, q)

    def test_eval_theorem_2(self):
        v = collatz_eval(15, 300)
        q = collatz_eval(51, 300)
        self.assertEqual(v, q)

    def test_eval_theorem_3(self):
        v = collatz_eval(80, 500)
        q = collatz_eval(10, 500)
        self.assertEqual(v, q)

    # general tests
    def test_eval_custom_1(self):
        v = collatz_eval(955, 960)
        self.assertEqual(v, 130)

    def test_eval_custom_2(self):
        v = collatz_eval(100, 111)
        self.assertEqual(v, 114)

    def test_eval_custom_3(self):
        v = collatz_eval(123456, 123456)
        self.assertEqual(v, 62)

    def test_eval_custom_4(self):
        v = collatz_eval(1205, 6263)
        self.assertEqual(v, 262)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # (1 Custom unit tests)

    def test_print_alt(self):
        w = StringIO()
        collatz_print(w, 955, 960, 130)
        self.assertEqual(w.getvalue(), "955 960 130\n")

    # -----
    # solve
    # -----

    # (Given unit test)

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # (1 Custom unit tests)

    def test_solve_alt_1(self):
        r = StringIO("1 10\n5 10\n21 800\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n5 10 20\n21 800 171\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
