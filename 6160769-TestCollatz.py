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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_solver

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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 2\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 2)

    def test_read_3(self):
        s = "999999 1000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 999999)
        self.assertEqual(j, 1000000)

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
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_6(self):
        v = collatz_eval(9000, 10000)
        self.assertEqual(v, 260)

    def test_eval_7(self):
        v = collatz_eval(90000, 100000)
        self.assertEqual(v, 333)

    def test_eval_8(self):
        v = collatz_eval(1, 3746)
        self.assertEqual(v, 238)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 2, 2)
        self.assertEqual(w.getvalue(), "1 2 2\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 90000, 100000, 333)
        self.assertEqual(w.getvalue(), "90000 100000 333\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 2 2\n")
    
    def test_solve_3(self):
        r = StringIO("9000 10000\n90000 100000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "9000 10000 260\n90000 100000 333\n")

    # --------------------------
    # solver, a method I created
    # --------------------------

    def test_solver_1(self):
        a = collatz_solver(5)
        self.assertEqual(a, 6)

    def test_solver_2(self):
        a = collatz_solver(23478)
        self.assertEqual(a, 52)

    def test_solver_3(self):
        a = collatz_solver(1)
        self.assertEqual(a, 1)

    def test_solver_4(self):
        a = collatz_solver(9999)
        self.assertEqual(a, 92)

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
....................
----------------------------------------------------------------------
Ran 21 tests in 0.088s

OK


% coverage report -m                   >> TestCollatz.out



% cat TestCollatz.out
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          41      0     12      0   100%
TestCollatz.py      84      0      0      0   100%
------------------------------------------------------------
TOTAL              125      0     12      0   100%

"""
