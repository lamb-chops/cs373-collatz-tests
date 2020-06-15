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

from Collatz import collatz_read, collatz_eval_non_cache_range, collatz_eval_cache_range, collatz_eval, collatz_print, collatz_solve

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

    def test_read_three_number_input(self):
        s = "1 10 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_one_number_input(self):
        s = "1\n"
        with self.assertRaises(IndexError):
            i, j = collatz_read(s)

    def test_read_letter_input(self):
        s = "1 a\n"
        with self.assertRaises(ValueError):
            i, j = collatz_read(s)

    # ----
    # eval_non_cache_range
    # ----

    def test_eval_non_cache_1(self):
        v = collatz_eval_non_cache_range(1, 10)
        self.assertEqual(v, 20)

    def test_eval_non_cache_2(self):
        v = collatz_eval_non_cache_range(100, 200)
        self.assertEqual(v, 125)

    def test_eval_non_cache_3(self):
        v = collatz_eval_non_cache_range(201, 210)
        self.assertEqual(v, 89)

    def test_eval_non_cache_4(self):
        v = collatz_eval_non_cache_range(900, 1000)
        self.assertEqual(v, 174)


    # ----
    # eval_cache_range
    # ----

    def test_eval_cache_1(self):
        v = collatz_eval_cache_range(1000, 1000000)
        self.assertEqual(v, 525)

    def test_eval_cache_2(self):
        v = collatz_eval_cache_range(1000, 2000)
        self.assertEqual(v, 182)

    def test_eval_cache_3(self):
        v = collatz_eval_cache_range(1000, 3000)
        self.assertEqual(v, 217)

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

    def test_eval_same_num_1(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_same_num_2(self):
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)

    def test_eval_backward_range(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_zero(self):
        with self.assertRaises(AssertionError):
            v = collatz_eval(0, 0)

    def test_eval_negative(self):
        with self.assertRaises(AssertionError):
            v = collatz_eval(-1, 0)

    def test_eval_full_range(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    def test_eval_with_cache_1(self):
        v = collatz_eval_cache_range(1000, 1000000)
        self.assertEqual(v, 525)

    def test_eval_with_cache_2(self):
        v = collatz_eval_cache_range(1000, 2000)
        self.assertEqual(v, 182)

    def test_eval_with_cache_3(self):
        v = collatz_eval_cache_range(1000, 3000)
        self.assertEqual(v, 217)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_same_number(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_descending(self):
        w = StringIO()
        collatz_print(w, 3, 2, 1)
        self.assertEqual(w.getvalue(), "3 2 1\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_extra_num(self):
        r = StringIO("1 10 20\n100 200 200\n201 210 210\n900 1000 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_incorrect_range(self):
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")


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
