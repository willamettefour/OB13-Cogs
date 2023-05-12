import json
from pathlib import Path
from .translate import Translate

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot):
    if discord.__version__[0] == "2":
        await bot.add_cog(Translate(bot))
    else:
        bot.add_cog(Translate(bot))