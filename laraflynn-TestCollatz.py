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

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
        
    def test_read2(self):
        s = "203 220\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  203)
        self.assertEqual(j, 220)
    
    def test_read3(self):
        s = "39 32\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  39)
        self.assertEqual(j, 32)
        

    # ----
    # eval
    # ----
    
    # fixed unit tests by calculating the actual collatz cycle length (CCL) with given calculator
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
        
    # corner case: CCL of 1 is 1
    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
        
    def test_eval_6(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)
        
    def test_eval_7(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_8(self):
        v = collatz_eval(7, 11)
        self.assertEqual(v, 20)
        
    def test_eval_9(self):
        v = collatz_eval(58, 28)
        self.assertEqual(v, 113)
        
    def test_eval_10(self):
        v = collatz_eval(3, 3)
        self.assertEqual(v, 8)
        
    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        
    def test_print2(self):
        w = StringIO()
        collatz_print(w, 7, 9, 11)
        self.assertEqual(w.getvalue(), "7 9 11\n")
        
    def test_print3(self):
        w = StringIO()
        collatz_print(w, 384, 21, 83)
        self.assertEqual(w.getvalue(), "384 21 83\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
            
    def test_solve2(self):
        r = StringIO("8 20\n4 90\n15 45\n110 90\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "8 20 21\n4 90 116\n15 45 112\n110 90 119\n")
            
    def test_solve3(self):
        r = StringIO("10 50\n45 40\n40 90\n100 145\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 50 112\n45 40 110\n40 90 116\n100 145 122\n")

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
