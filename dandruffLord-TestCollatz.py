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
        s = "803450 767731\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  803450)
        self.assertEqual(j, 767731)

    def test_read_2(self):
        s = "20 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  20)
        self.assertEqual(j, 10)

    def test_read_3(self):
        s = "5 5\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  5)
        self.assertEqual(j, 5)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(22338, 604076)
        self.assertEqual(v, 470)

    def test_eval_3(self):
        v = collatz_eval(599551, 491387)
        self.assertEqual(v, 470)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(780228, 875377)
        self.assertEqual(v, 525)
    
    def test_eval_6(self):
        v = collatz_eval(34, 34)
        self.assertEqual(v, 14)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("372238 419245\n873550 404080\n95341 771212\n895076 986127\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "372238 419245 449\n873550 404080 525\n95341 771212 509\n895076 986127 507\n")

    def test_solve_2(self):
        r = StringIO("5 5\n30 10\n1 100\n23 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5 5 6\n30 10 112\n1 100 119\n23 1 21\n")

    def test_solve_3(self):
        r = StringIO("1234 2342\n23776 24535\n12000 12999\n749948 935826\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1234 2342 183\n23776 24535 251\n12000 12999 263\n749948 935826 525\n")

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
