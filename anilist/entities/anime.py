import aiohttp


class Anime:
    async def get(id):
        """Get anime by id"""

        url = "https://graphql.anilist.co"
        variables = {"id": id}
        query = """
        query ($id: Int) {
        Media (id: $id, type: ANIME) {
            id
            title {
            romaji
            english
            native
            }}}
        """
        async with aiohttp.ClientSession() as cs:
            async with cs.post(
                url, json={"query": query, "variables": variables}
            ) as req:
                return await req.json()
