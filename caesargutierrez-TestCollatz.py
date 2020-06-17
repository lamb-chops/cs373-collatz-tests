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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

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

    def test_read_1(self):
        s = "20 30\n"
        i, j = collatz_read(s)
        self.assertEqual(i,20)
        self.assertEqual(j,30)

    def test_read_2(self):
        s = "100 456\n"
        i, j = collatz_read(s)
        self.assertEqual(i,100)
        self.assertEqual(j,456)

    def test_read_3(self):
        s = "55 43\n"
        i, j = collatz_read(s)
        self.assertEqual(i,55)
        self.assertEqual(j,43)
    # ----
    # eval
    # ----

    # Each test has correct expected value.
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
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    # Additional unit test

    # i and j are flipped
    def test_eval_5(self):
        v = collatz_eval(100,1)
        self.assertEqual(v,119)

    # incorrect input
    def test_eval_6(self):
        v = collatz_eval(0,10)
        self.assertEqual(v,20)
    # long range
    def test_eval_7(self):
        v = collatz_eval(1,99999)
        self.assertEqual(v,351)

    def test_eval_8(self):
        v = collatz_eval(200,200)
        self.assertEqual(v,27)

    def test_eval_9(self):
        v = collatz_eval(60000,2000)
        self.assertEqual(v,340)



    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1(self):
        w = StringIO()
        collatz_print(w,10, 200, 4)
        self.assertEqual(w.getvalue(),"10 200 4\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w,21, 21, 21)
        self.assertEqual(w.getvalue(),"21 21 21\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w,1000, 1001, 1000)
        self.assertEqual(w.getvalue(),"1000 1001 1000\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w,10, 200, 125)
        self.assertEqual(w.getvalue(),"10 200 125\n")


    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        r = StringIO("10 30\n 100 567\n78 5000\n 10 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 30 112\n100 567 144\n78 5000 238\n10 200 125\n")
    
    def test_solve_2(self):
        r = StringIO("5000 5600\n786 2000\n90000 99999\n1 4500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "5000 5600 236\n786 2000 182\n90000 99999 333\n1 4500 238\n")
    
    def test_solve_3(self):
        r = StringIO("10 50\n60 100\n900 1500\n1 4500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 50 112\n60 100 119\n900 1500 182\n1 4500 238\n")

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
