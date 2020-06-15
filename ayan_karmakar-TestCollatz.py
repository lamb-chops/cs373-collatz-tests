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
        s = "-200 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -200)
        self.assertEqual(j, 1)
        
    def test_read_3(self):
        s = "100000 20000000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100000 )
        self.assertEqual(j, 20000000000)

    def test_read_4(self):
        s = "\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

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
        v = collatz_eval(1, 1000)
        self.assertEqual(v, 179)

    def test_eval_6(self):
        v = collatz_eval(77, 78)
        self.assertEqual(v, 36)

    def test_eval_7(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_8(self):
        v = collatz_eval(99, 100)
        self.assertEqual(v, 26)


    def test_eval_9(self):
        v = collatz_eval(9999, 10000)
        self.assertEqual(v, 92)

    def test_eval_10(self):
        v = collatz_eval(1, 5000)
        self.assertEqual(v, 238)
    
    def test_eval_11(self):
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)

    def test_eval_12(self):
        v = collatz_eval(2143, 3475)
        self.assertEqual(v, 217)


    def test_eval_13(self):
        v = collatz_eval(234, 2352)
        self.assertEqual(v, 183)

    def test_eval_14(self):
        v = collatz_eval(4433, 4444)
        self.assertEqual(v, 184)

    def test_eval_15(self):
        v = collatz_eval(9999, 9876)
        self.assertEqual(v, 242)

    def test_eval_16(self):
        v = collatz_eval(999,16)
        self.assertEqual(v, 179)
    
    # -----
    # print
    # -----
    
    
    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100000, 20000000000, 44) 
        self.assertEqual(w.getvalue(), "100000 20000000000 44\n")   
        
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, -200, 1, 31)
        self.assertEqual(w.getvalue(), "-200 1 31\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 100, -300, -20)
        self.assertEqual(w.getvalue(), "100 -300 -20\n")
    
    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n-201 -210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 1000\n77 78\n1 1\n99 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1000 179\n77 78 36\n1 1 1\n99 100 26\n")
    
    def test_solve_3(self):
        r = StringIO("9999 10000\n1 5000\n1 10000\n2 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "9999 10000 92\n1 5000 238\n1 10000 262\n2 2 2\n")
 
    def test_solve_4(self):
        r = StringIO("234 2352\n4433 4444\n\n16 999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "234 2352 183\n4433 4444 184\n16 999 179\n")

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
