import re
from spiral_algorithm import counter_clock_spiral
import aiohttp
import asyncio

async def get_matrix(url: str) -> list[int]:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=5) as resp:
                status = str(resp.status)
                if status[0] == 5:
                    return 'Internal server error or server is not available. Try again later'
                if status == '404':
                    return 'Page not found'
                if status == '403':
                    return 'Forbidden'
                if status == '400':
                    return 'Bad request'
                response = await resp.text()
        except asyncio.exceptions.TimeoutError:
            return 'Timeout Error occured. Check URL or try again later'
        except aiohttp.InvalidURL:
            return 'Invalid URL. Please try again'
    # Uses regular exression to get a list of numbers from matrix
    listed_nums = [int(num) for num in re.findall('\d+', response)]
    # Calculates squared root of number of integers to get size of matrix
    size = len(listed_nums) ** (1 / 2)
    # If calculated number is not integer, it means that matrix is not squared
    if size.is_integer() == False:
        return 'Passed non-square matrix'
    size = int(size)
    return counter_clock_spiral(listed_nums, size)