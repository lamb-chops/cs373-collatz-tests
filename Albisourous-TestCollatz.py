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


class TestCollatz(TestCase):
	# ----
	# read
	# ----

	def test_read(self):
		s = "1 10\n"
		i, j = collatz_read(s)
		self.assertEqual(i, 1)
		self.assertEqual(j, 10)

	def test_read_2(self):
		s = "100 100\n"
		i, j = collatz_read(s)
		self.assertEqual(i, 100)
		self.assertEqual(j, 100)

	def test_read_3(self):
		s = "10 0\n"
		i, j = collatz_read(s)
		self.assertEqual(i, 10)
		self.assertEqual(j, 0)

	# # test too many spaces
	# def test_read_4(self):
	#     s = "0     100\n"
	#     i, j = collatz_read(s)
	#     self.assertEqual(i,  0)
	#     self.assertEqual(j, 100)
	#
	# # test string input
	# def test_read_4(self):
	#     s = "HI \n"
	#     i, j = collatz_read(s)
	#     self.assertEqual(i == False)
	#     self.assertEqual(j == False)

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

	# test if reversed
	def test_eval_5(self):
		v = collatz_eval(1000, 900)
		self.assertEqual(v, 174)

	# test if same numbers
	def test_eval_6(self):
		v = collatz_eval(1000, 1000)
		self.assertEqual(v, 112)

	def test_eval_7(self):
		v = collatz_eval(837799, 837000)
		self.assertEqual(v, 525)

	def test_eval_8(self):
		v = collatz_eval(626331, 626000)
		self.assertEqual(v, 509)

	# # test of every value, works but commented out to run test faster
	# def test_eval_9(self):
	# 	v = collatz_eval(1, 999999)
	# 	self.assertEqual(v, 525)

	# # test neg number
	# def test_eval_10(self):
	#     v = collatz_eval(-1, 1000)
	#     self.assertEqual(v, 112)

	# test check if items are being cached
	def test_eval_11(self):
		v = collatz_eval(1, 100)
		self.assertEqual(v, 119)
		print("break")
		v = collatz_eval(1, 100)
		self.assertEqual(v, 119)

	# -----
	# print
	# -----

	def test_print(self):
		w = StringIO()
		collatz_print(w, 1, 10, 20)
		self.assertEqual(w.getvalue(), "1 10 20\n")

	# test corner
	def test_print_2(self):
		w = StringIO()
		collatz_print(w, 1, 999999, 525)
		self.assertEqual(w.getvalue(), "1 999999 525\n")

	# test if both 1
	def test_print_3(self):
		w = StringIO()
		collatz_print(w, 1, 1, 1)
		self.assertEqual(w.getvalue(), "1 1 1\n")

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
		r = StringIO("1 1")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "1 1 1\n")

	def test_solve_3(self):
		r = StringIO("1 999")
		w = StringIO()
		collatz_solve(r, w)
		self.assertEqual(
			w.getvalue(), "1 999 179\n")


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

coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1
cat TestCollatz.out
coverage report -m                   >> TestCollatz.out
cat TestCollatz.out

Albins-MacBook-Pro:collatz albisourous$ coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1
Albins-MacBook-Pro:collatz albisourous$ cat TestCollatz.out
...............
----------------------------------------------------------------------
Ran 15 tests in 0.088s

OK
Albins-MacBook-Pro:collatz albisourous$ coverage report -m                   >> TestCollatz.out
Albins-MacBook-Pro:collatz albisourous$ cat TestCollatz.out
...............
----------------------------------------------------------------------
Ran 15 tests in 0.088s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          28      0     10      0   100%
TestCollatz.py      66      0      0      0   100%
------------------------------------------------------------
TOTAL               94      0     10      0   100%

"""
