import asyncio
from anilist.entities import Anime


async def main():
    print(await Anime.get(1))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())