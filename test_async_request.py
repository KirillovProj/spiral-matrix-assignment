import unittest
import async_request
import asyncio

loop = asyncio.get_event_loop()

class TestAsyncRequest(unittest.TestCase):

    def test_nonsquare_matrix(self):
        input_url = 'https://pastebin.com/raw/tgd3JEY0'
        result = loop.run_until_complete(async_request.get_matrix(input_url))
        self.assertEqual(result, 'Passed non-square matrix')

    def test_timeout(self):
        input_url = 'https://www.google.com:81'
        result = loop.run_until_complete(async_request.get_matrix(input_url))
        self.assertEqual(result, 'Timeout Error occured. Check URL or try again later')

    def test_invalid_url(self):
        input_url = '1'
        result = loop.run_until_complete(async_request.get_matrix(input_url))
        self.assertEqual(result, 'Invalid URL. Please try again')



