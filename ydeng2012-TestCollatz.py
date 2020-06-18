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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, collatz_eval_helper

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
        s = "999 10001\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  999)
        self.assertEqual(j, 10001)

    def test_read_3(self):
        s = "123 789\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  123)
        self.assertEqual(j, 789)

    def test_read_4(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999999)

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
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_5(self):
        v = collatz_eval(33333, 33)
        self.assertEqual(v, 308)

    def test_eval_6(self):
        v = collatz_eval(553355, 777)
        self.assertEqual(v, 470)

    def test_eval_7(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 198, 798, 171)
        self.assertEqual(w.getvalue(), "198 798 171\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 54, 1000, 179)
        self.assertEqual(w.getvalue(), "54 1000 179\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 9, 45678, 324)
        self.assertEqual(w.getvalue(), "9 45678 324\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("198 798\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "198 798 171\n")

    def test_solve_3(self):
        r = StringIO("54 1000\n9 45678\n33 33333\n10000 99999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "54 1000 179\n9 45678 324\n33 33333 308\n10000 99999 351\n")

    def test_solve_4(self):
        r = StringIO("777 776\n250 500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "777 776 122\n250 500 144\n")

    # ------------
    # cycle_length
    # ------------

    def test_length_0(self):
        v = cycle_length(960963)
        self.assertEqual(v, 414)

    def test_length_1(self):
        v = cycle_length(99999)
        self.assertEqual(v, 227)

    def test_length_2(self):
        v = cycle_length(555555)
        self.assertEqual(v, 147)

    # ------------
    # eval_helper
    # ------------

    def test_eval_helper_0(self):
        v = collatz_eval(1, 345566)
        self.assertEqual(v, 443)

    def test_eval_helper_1(self):
        v = collatz_eval(960963, 999999)
        self.assertEqual(v, 458)

    def test_eval_helper_2(self):
        v = collatz_eval(555555, 888888)
        self.assertEqual(v, 525)


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
