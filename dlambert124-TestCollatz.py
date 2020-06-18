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

	#test if pos numbers can be read
    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1) 
        self.assertEqual(j, 10)

	#test negative numbers
    def test_read_1(self): #possible -1 error?
        s = "-1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  -1)
        self.assertEqual(j, 1)
	
	#test if 0 can be read
    def test_read_2(self):
        s = "0 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  0)
        self.assertEqual(j, 1)
	
	#test if numbers can be read out of order from big to small
    def test_read_3(self):
        s = "1 -1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, -1)
		
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
		
	#test 1,1	1
    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
		
	#test 1,2	2
    def test_eval_6(self):
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)
		
	#test 10,1	20
    def test_eval_7(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)
		
	#test 50, 50	25
    def test_eval_8(self):
        v = collatz_eval(50, 50)
        self.assertEqual(v, 25)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
		
	#test negative numbers
    def test_print_1(self):
        w = StringIO()
        collatz_print(w, -1, 10, 20)
        self.assertEqual(w.getvalue(), "-1 10 20\n")
		
	#test 0
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 0, 10, 20)
        self.assertEqual(w.getvalue(), "0 10 20\n")
		
	#test out of order numbers
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, -6, 20)
        self.assertEqual(w.getvalue(), "1 -6 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
			
	# test if my evals work
    def test_solve_1(self):
        r = StringIO("1 1\n1 2\n10 1\n50 50\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n1 2 2\n10 1 20\n50 50 25\n")	
			
    def test_solve_2(self):
        r = StringIO("2 1596\n99 9999\n1 1999\n340 30100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2 1596 182\n99 9999 262\n1 1999 182\n340 30100 308\n")
			
    def test_solve_3(self):
        r = StringIO("2 10\n3 10\n4 10\n4 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2 10 20\n3 10 20\n4 10 20\n4 10000 262\n")
			
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
