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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

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

    def test_read_1(self):
        s = "20 21\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 20)
        self.assertEqual(j, 21)

    def test_read_2(self):
        s = "980 1001\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 980)
        self.assertEqual(j, 1001)

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

    # ----
    # cycle_length
    # ----
    def test_cycle_length_0(self):
        v = cycle_length(1)
        self.assertEqual(v, 1)

    def test_cycle_length_1(self):
        v = cycle_length(27)
        self.assertEqual(v, 112)

    def test_cycle_length_2(self):
        v = cycle_length(56780)
        self.assertEqual(v, 61)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 2, 3)
        self.assertEqual(w.getvalue(), "1 2 3\n")
        
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 300)
        self.assertEqual(w.getvalue(), "100 200 300\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve_1(self):
        r = StringIO("2 20\n23 27\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
                w.getvalue(), "2 20 21\n23 27 112\n")
        
    def test_solve_2(self):
        r = StringIO("1 1000\n20000 30000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
                w.getvalue(), "1 1000 179\n20000 30000 308\n")
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
