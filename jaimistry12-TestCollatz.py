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

    def test_read_2(self):
        s = "1003 103\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1003)
        self.assertEqual(j, 103)

    def test_read_3(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)

    def test_read_4(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
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

    # My test cases - EVAL

    def test_eval_5(self):
        v = collatz_eval(15, 3)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7(self):
        v = collatz_eval(125, 125)
        self.assertEqual(v, 109)

    def test_eval_8(self):
        v = collatz_eval(93001, 93456)
        self.assertEqual(v, 284)

    def test_eval_9(self):
        v = collatz_eval(13456, 22000)
        self.assertEqual(v, 279)

    def test_eval_10(self):
        v = collatz_eval(303, 1000)
        self.assertEqual(v, 179)
    
    def test_eval_11(self):
        v = collatz_eval(8001, 15000)
        self.assertEqual(v, 276)
    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 300, 38, 128)
        self.assertEqual(w.getvalue(), "300 38 128\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 598, 635, 132)
        self.assertEqual(w.getvalue(), "598 635 132\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 1\n874 239\n100 135\n999 999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n874 239 179\n100 135 122\n999 999 50\n")

    def test_solve_3(self):
        r = StringIO("4843 1202\n4294 5765\n5986 1867\n293 1113\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "4843 1202 238\n4294 5765 236\n5986 1867 238\n293 1113 179\n")

    def test_solve_4(self):
        r = StringIO("5001 8008\n\n5555 7000\n100001 300000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5001 8008 262\n\n5555 7000 262\n100001 300000 443\n")

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
