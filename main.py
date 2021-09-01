import asyncio
from async_request import get_matrix

def main():
    SOURCE_URL = input('Paste URL:\n')
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(get_matrix(SOURCE_URL)))

if __name__ == '__main__':
    main()

