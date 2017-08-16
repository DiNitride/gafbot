import discord
from discord.ext import commands
import random


class RNG:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx, dice: str):
        """
        Rolls a dice in NdN format.
        """
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """
        Chooses between multiple choices, surround choices with spaces in quotes.
        """
        await ctx.send(random.choice(choices))


def setup(bot):
    bot.add_cog(RNG(bot))