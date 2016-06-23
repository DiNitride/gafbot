import discord
from discord.ext import commands
from utils import checks


class Moderation():
    def __init__(self, bot):
        self.bot = bot

    #Changes the bot's game
    @commands.command(pass_conext=True)
    @checks.is_admin()
    async def changegame(self, *, game: str):
        """Updates the Bot's game"""
        await self.bot.change_status(discord.Game(name=game))
        await self.bot.say("Game updated.")
        print("Updated Bot's Game")

    #Bans a member
    @commands.command()
    @checks.is_admin()
    async def ban(self, member: discord.Member = None):
        """Bans a member"""
        #Are they trying to ban nobody? Are they stupid?
        #Why do they have mod powers if they're this much of an idiot?
        if member is None:
            return
        #Is the person being banned me? No we don't allow that
        elif member.id == '95953002774413312':
            await self.bot.say("http://i.imgur.com/BSbBniw.png")
            return
        #Bans the user
        await self.bot.ban(member, delete_message_days=1)
        #Prints to console
        print("{0.name} has been banned".format(member))

    #Softbans a member
    @commands.command(pass_context=True)
    @checks.is_admin()
    async def softban(self, ctx, member: discord.Member = None):
        """Softbans a member"""
        server = ctx.message.server
        #Are they trying to ban nobody? Are they stupid?
        #Why do they have mod powers if they're this much of an idiot?
        if member is None:
            return
        # Is the person being banned me? No we don't allow that
        elif member.id == '95953002774413312':
            await self.bot.say("http://i.imgur.com/BSbBniw.png")
            return
        #Sends messages to the user being softbanned with a new invite link
        softbanmessage = "You were softbanned to clear messages, rejoin:"
        await self.bot.send_message(member, softbanmessage)
        await self.bot.send_message(member, "https://discord.gg/0xiHA3yQkE0pu2Qp")
        #Outputs to console
        print("{0.name} has been softbanned".format(member))
        #
        await self.bot.ban(member, delete_message_days=1)
        await self.bot.unban(server, member)

    #Adds a community member
    @commands.command(pass_context=True)
    @checks.is_admin()
    async def addcommunity(self, ctx, member: discord.Member = None):
        """Adds a community member"""
        server = ctx.message.server
        role = discord.utils.get(server.roles, id='172427010310799361')
        if member is None:
            return
        await self.bot.add_roles(member, role)
        print("{0.name} is now a community member".format(member))

    #Removes a community member
    @commands.command(pass_context=True)
    @checks.is_admin()
    async def removecommunity(self, ctx, member: discord.Member = None):
        """Removes a community member"""
        server = ctx.message.server
        role = discord.utils.get(server.roles, id='172427010310799361')
        if member is None:
            return
        await self.bot.remove_roles(member, role)
        print("{0.name} is no longer a community member".format(member))

    #Gives the user some basic info on a user
    @commands.command(pass_context=True)
    async def info(self, ctx, member : discord.Member = None):
        """Gives basic info and shows profile image of a user."""
        if member == None:
            member = ctx.message.author
        await self.bot.say(
            "```xl\n" +
            "Name: {0.name}\n".format(member) +
            "Joined server: {0.joined_at}\n".format(member) +
            "ID: {0.id}\n".format(member) +
            "Has existed since: {0.created_at}\n".format(member) +
            "Bot?: {0.bot}\n".format(member) +
            "```" +
            "\n{0.avatar_url}".format(member))
        print("Run: info on {0.name}".format(member))

    #Server Info
    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Basic info on the server."""
        server = ctx.message.server
        afk = server.afk_timeout / 60
        await self.bot.say(
            "```xl\n" +
            "Name: {0.name}\n".format(server) +
            "Server ID: {0.id}\n".format(server) +
            "Region: {0.region}\n".format(server) +
            "Existed since: {0.created_at}\n".format(server) +
            "Owner: {0.owner}\n".format(server) +
            "AFK Timeout and Channel: {0} minutes in '{1.afk_channel}'\n".format(afk, server) +
            "Member Count: {0.member_count}\n".format(server) +
            "```")
        print("Run: Server Info")

    #Displays members
    @commands.command(hidden=True, pass_context=True)
    async def members(self, ctx):
        """Basic info on the server."""
        server = ctx.message.server
        members = []
        for user in server.members:
            members.extend(user.name)
        await self.bot.say(
            "```xl\n" +
            "Name: {0.name}\n".format(server) +
            "Owner: {0.owner}\n".format(server) +
            "Members: {0}\n".format(members) +
            "```")
        print("Run: Member List")

    #Tells the user their ID
    @commands.command(pass_context=True)
    async def id(self, ctx):
        """Tells you your ID."""
        member = ctx.message.author
        message = "You ID is {0.id}"
        await self.bot.say(message.format(member))
        print("Run: ID for {0.name}".format(member))

def setup(bot):
    bot.add_cog(Moderation(bot))
