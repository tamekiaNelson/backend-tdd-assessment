#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess
# Your test case class goes here


def setUp(self):
    self.parser = echo.create_parser()


def test_parser(self):
    args = ["--lower", "--upper", "--title", "HELLO"]
    t = self.parser.parse_args(args)
    self.assertTrue(t.lower)
    self.assertTrue(t.upper)
    self.assertTrue(t.title)
    self.assertTrue(t.text)
    self.assertEquals(echo.main(args), "Hello")


def test_lower(self):
    args = ["--lower", 'HELLO']
    self.assertEquals(echo.main(args), 'hello')


def test_upper(self):
    args = ["--upper", 'hello']
    self.assertEquals(echo.main(args), 'HELLO')


def test_title(self):
    args = ["--title", 'hello']
    self.assertEquals(echo.main(args), 'Hello')


def test_help(self):
    """ Running the program without arguments should show usage. """
    # Run the command `python ./echo.py -h` in a separate process, then
    # collect it's output.
    process = subprocess.Popen(
        ["python", "./echo.py", "-h"],
        stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    usage = open("./USAGE", "r").read()

    self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
