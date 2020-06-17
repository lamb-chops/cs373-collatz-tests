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

    # my tests

    def test_read_1(self):
        s = "1 10 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 999999)

    def test_read_3(self):
        s = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 10)

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

    # my tests

    def test_eval_5(self):
        v = collatz_eval(10 , 1)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(10 , 10)
        self.assertEqual(v, 7)

    def test_eval_7(self):
        v = collatz_eval(5 , 6)
        self.assertEqual(v, 9)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # my tests

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 5, 99, 119)
        self.assertEqual(w.getvalue(), "5 99 119\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertEqual(w.getvalue(), "10 10 7\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 5, 6, 9)
        self.assertEqual(w.getvalue(), "5 6 9\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # my tests

    def test_solve_1(self):
        r = StringIO("1 10\n100 100\n99 100\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 100 26\n99 100 26\n10 1 20\n")

    def test_solve_2(self):
        r = StringIO("999999 999999\n1 1\n52 99\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "999999 999999 259\n1 1 1\n52 99 119\n")

    def test_solve_3(self):
        r = StringIO("1 100\n101 200\n500 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 100 119\n101 200 125\n500 1000 179\n")
    def test_solve_4(self):
        r = StringIO("\n\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")

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
