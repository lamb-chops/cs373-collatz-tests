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
        
    #tests I added
    def test_read_2(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)
        
    def test_read_3(self):
        s = "1000 900\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 900)
        
    def test_read_4(self):
        s = "3832807 5704926\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 3832807)
        self.assertEqual(j, 5704926)
    
    def test_read_5(self):
        s = "\n"
        i, j = collatz_read(s)
        self.assertEqual(i, None)
        self.assertEqual(j, None)

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

    # my added tests
    
    def test_eval_5(self):
        v = collatz_eval(1,1)
        self.assertEqual(v, 1)
        
    def test_eval_6(self):
        v = collatz_eval(100,1)
        self.assertEqual(v, 119)
       
    def test_eval_7(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)
    
    def test_eval_8(self):
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)
        
    def test_eval_9(self):
        v = collatz_eval(9443, 6954)
        self.assertEqual(v, 260)
        
    def test_eval_10(self):
        v = collatz_eval(838251, 101635)
        self.assertEqual(v, 525)
         
    
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        
    # my added tests
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")
        
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1000, 900, 174)
        self.assertEqual(w.getvalue(), "1000 900 174\n")
    
    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 9443, 6954, 260)
        self.assertEqual(w.getvalue(), "9443 6954 260\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
            
    #tests I wrote
    def test_solve_2(self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n")
           
    def test_solve_3(self):
        r = StringIO("1 1\n1000 900\n100 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n1000 900 174\n100 1 119\n")
            
    def test_solve_4(self):
        r = StringIO("9443 6954\n1 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "9443 6954 260\n1 10000 262\n")
            
    def test_solve_5(self):
        r = StringIO("\n\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")
            
    def test_solve_6(self):
        r = StringIO("")
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
