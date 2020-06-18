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
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)

    def test_read_6(self):
        s = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 10)

    def test_read_7(self):
        s = "1 10000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    # Failure cases
    # def test_eval_3(self):
    #     v = collatz_eval(201, 210)
    #     self.assertEqual(v, 1)
    #
    # def test_eval_4(self):
    #     v = collatz_eval(900, 1000)
    #     self.assertEqual(v, 1)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # Test for a reversed interval
    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # Test for i == j
    def test_eval_6(self):
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    # Test for a large interval
    def test_eval_7(self):
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)

    # Test for the simplest optimization
    def test_eval_8(self):
        v = collatz_eval(1500, 4500)
        self.assertEqual(v, 238)

    def test_eval_9(self):
        v = collatz_eval(1, 1500)
        self.assertEqual(v, 182)

    def test_eval_10(self):
        v = collatz_eval(80000, 90000)
        self.assertEqual(v, 333)
        
    def test_eval_11(self):
        v = collatz_eval(10001, 11111)
        self.assertEqual(v, 268)


    # -----
    # print
    # -----

    def test_print(self):
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

    # Test for a reversed interval
    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    # Test for i == j
    def test_print_6(self):
        w = StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertEqual(w.getvalue(), "10 10 7\n")

    # Test for a large interval
    def test_print_7(self):
        w = StringIO()
        collatz_print(w, 1, 10000, 262)
        self.assertEqual(w.getvalue(), "1 10000 262\n")


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
        r = StringIO("10 1\n10 10\n1 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n10 10 7\n1 10000 262\n")

    def test_solve_3(self):
        r = StringIO("1500 4500\n1 1500\n80000 90000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1500 4500 238\n1 1500 182\n80000 90000 333\n")
    
    # Edge cases: blank input or new line only
    def test_solve_4(self):
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")
            
    def test_solve_5(self):
        r = StringIO("\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

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
