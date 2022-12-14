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

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "2 15\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 2)
        self.assertEqual(j, 15)

    def test_read_3(self):
        s = "9999 3\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9999)
        self.assertEqual(j, 3)

    # ----
    # eval
    # ----

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

    def test_eval_5(self):
        v = collatz_eval(2500, 487)
        self.assertEqual(v, 209)

    def test_eval_6(self):
        v = collatz_eval(50, 8940)
        self.assertEqual(v, 262)

    def test_eval_7(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 50, 8940, 262)
        self.assertEqual(w.getvalue(), "50 8940 262\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 1\n999 1001\n657 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n999 1001 143\n657 10000 262\n")

    def test_solve_3(self):
        r = StringIO("1 99999\n500 35\n1 999999")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 99999 351\n500 35 144\n1 999999 525\n")

    def test_solve_4(self):
        r = StringIO("200 400\n \n999 1001\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "200 400 144\n999 1001 143\n")


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
