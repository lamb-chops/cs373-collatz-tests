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
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)
        
    def test_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)
        
    def test_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)
        
    def test_read_5(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)
        
    def test_read_6(self):
        s = "1 10000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10000)
        
    def test_read_7(self):
        s = "1 2\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 2)
    
    def test_read_8(self):
        s = "9999 10000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9999)
        self.assertEqual(j, 10000)
        
    def test_read_9(self):
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)
        
    def test_read_10(self):
        s = "10000 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10000)
        self.assertEqual(j, 1)
        
    def test_read_11(self):
        s = "2 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 2)
        self.assertEqual(j, 1)
        
    def test_read_12(self):
        s = "10000 9999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10000)
        self.assertEqual(j, 9999)
    '''
    def test_read_13(self):
        s = "0 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 1)
    '''
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
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
    
    def test_eval_6(self):
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)
        
    def test_eval_7(self):
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)
        
    def test_eval_8(self):
        v = collatz_eval(9999, 10000)
        self.assertEqual(v, 92)

    def test_eval_9(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)
        
    def test_eval_10(self):
        v = collatz_eval(10000, 1)
        self.assertEqual(v, 262)
    
    def test_eval_11(self):
        v = collatz_eval(2, 1)
        self.assertEqual(v, 2)
    
    def test_eval_12(self):
        v = collatz_eval(10000, 9999)
        self.assertEqual(v, 92)
    '''
    def test_eval_13(self):
        v = collatz_eval(0, 1)
        self.assertEqual(v, 1)
    '''
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
        
    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")
        
    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")
        
    def test_print_6(self):
        w = StringIO()
        collatz_print(w, 1, 10000, 262)
        self.assertEqual(w.getvalue(), "1 10000 262\n")
        
    def test_print_7(self):
        w = StringIO()
        collatz_print(w, 1, 2, 2)
        self.assertEqual(w.getvalue(), "1 2 2\n")
        
    def test_print_8(self):
        w = StringIO()
        collatz_print(w, 9999, 10000, 92)
        self.assertEqual(w.getvalue(), "9999 10000 92\n")
        
    def test_print_9(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")
    
    def test_print_10(self):
        w = StringIO()
        collatz_print(w, 10000, 1, 262)
        self.assertEqual(w.getvalue(), "10000 1 262\n")
    
    def test_print_11(self):
        w = StringIO()
        collatz_print(w, 2, 1, 2)
        self.assertEqual(w.getvalue(), "2 1 2\n")
    
    def test_print_12(self):
        w = StringIO()
        collatz_print(w, 10000, 9999, 92)
        self.assertEqual(w.getvalue(), "10000 9999 92\n")
    '''
    def test_print_13(self):
        w = StringIO()
        collatz_print(w, 0, 1, 1)
        self.assertEqual(w.getvalue(), "0 1 1\n")
    '''
    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1 1 1\n")
            
    def test_solve_2(self):
        r = StringIO("1 10000\n1 2\n9999 10000\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10000 262\n1 2 2\n9999 10000 92\n10 1 20\n")
            
    def test_solve_3(self):
        r = StringIO("10000 1\n2 1\n10000 9999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10000 1 262\n2 1 2\n10000 9999 92\n")

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
