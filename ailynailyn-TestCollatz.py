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
        s = "1000 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1000)
        self.assertEqual(j, 20)

    def test_read_2(self):
        s = "1 100000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 100000)

    def test_read_3(self):
        s = "984759 70024\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  984759)
        self.assertEqual(j, 70024)

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
        v = collatz_eval(345, 12)
        self.assertEqual(v, 144)

    def test_eval_6(self):
        v = collatz_eval(90, 9879)
        self.assertEqual(v, 262)

    def test_eval_7(self):
        v = collatz_eval(1, 99999)
        self.assertEqual(v, 351)

    def test_eval_8(self):
        v = collatz_eval(999992, 999999)
        self.assertEqual(v, 259)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 999992, 999999, 259)
        self.assertEqual(w.getvalue(), "999992 999999 259\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 90, 9879, 262)
        self.assertEqual(w.getvalue(), "90 9879 262\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n\n900 1000\n345 12\n10000 20000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n345 12 144\n10000 20000 279\n")

    def test_solve_2(self):
        r = StringIO("90 9879\n1 99999\n43457 78844\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "90 9879 262\n1 99999 351\n43457 78844 351\n")

    def test_solve_3(self):
        r = StringIO("999992 999999\n56 4\n56 65665\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "999992 999999 259\n56 4 113\n56 65665 340\n")

    def test_solve_4(self):
        r = StringIO("676 7676\n35 3546\n3778 8787\n676 879\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "676 7676 262\n35 3546 217\n3778 8787 262\n676 879 179\n")

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
