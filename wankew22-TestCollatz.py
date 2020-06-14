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
        s = "2 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  2)
        self.assertEqual(j, 20)
    
    def test_read_3(self):
        s = "3 30\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  3)
        self.assertEqual(j, 30)

    def test_read_4(self):
        s = "4 40\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  4)
        self.assertEqual(j, 40)
    
    def test_read_5(self):
        s = "\n"
        z = collatz_read(s)
        self.assertEqual(z,  None)

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
        v = collatz_eval(900, 901)
        self.assertEqual(v, 55)


    def test_eval_5(self):
        v = collatz_eval(1, 1000)
        self.assertEqual(v, 179)

    def test_eval_6(self):
        v = collatz_eval(1800, 2000)
        self.assertEqual(v, 175)

    def test_eval_7(self):
        v = collatz_eval(345, 567)
        self.assertEqual(v, 142)

    def test_eval_8(self):
        v = collatz_eval(901, 901)
        self.assertEqual(v, 55)

    def test_eval_9(self):
        v = collatz_eval(25, 30)
        self.assertEqual(v, 112)
    
    def test_eval_10(self):
        v = collatz_eval(100, 1200)
        self.assertEqual(v, 182)

    def test_eval_11(self):
        v = collatz_eval(200, 2500)
        self.assertEqual(v, 209)

    def test_eval_12(self):
        v = collatz_eval(2500, 200)
        self.assertEqual(v, 209)

    def test_eval_13(self):
        v = collatz_eval(900000, 999999)
        self.assertEqual(v, 507)

    def test_eval_14(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 800, 900, 179)
        self.assertEqual(w.getvalue(), "800 900 179\n")
    
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 11, 99, 119)
        self.assertEqual(w.getvalue(), "11 99 119\n")
    
    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 100, 105, 88)
        self.assertEqual(w.getvalue(), "100 105 88\n")
    

    # # -----
    # # solve
    # # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve_2(self):
        r = StringIO("1 1000\n800 900\n11 99\n100 105\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1000 179\n800 900 179\n11 99 119\n100 105 88\n")
    
    def test_solve_3(self):
        r = StringIO("1800 2000\n345 567\n99999 100000\n8000 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1800 2000 175\n345 567 142\n99999 100000 227\n8000 10000 260\n")
    
    def test_solve_4(self):
        r = StringIO("1 99999\n16807 475249\n27544 850878\n77045 303120\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 99999 351\n16807 475249 449\n27544 850878 525\n77045 303120 443\n")
    
    def test_solve_5(self):
        r = StringIO("\n")
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
