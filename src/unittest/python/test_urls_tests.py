from mockito import mock, verify
import unittest

from test_urls import x

class X(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        x(out)

        verify(out).write("test case passed")