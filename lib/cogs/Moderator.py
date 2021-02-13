import discord
from discord.ext import commands

class Moderator(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def list(self,ctx):
        print(await ctx.guild.bans())

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def ban(self,ctx,member: discord.Member=None,*reason):
        if member == None:
            await ctx.channel.send(f'N\'oubliez pas de mentionner le membre que vous voulez bannir.\n\nExemple: ```!ban @MyBOT Non-respect des règles.```')
            return

        if member == ctx.author or member.bot:
            await ctx.channel.send('Vous ne pouvez pas vous auto-bannir du serveur ou bannir le bot.')
            return
        
        if not reason:
            reason = 'Non-respect des règles de notre communauté'
        else:
            reason = ' '.join(reason)
        
        log_channel = ctx.guild.get_channel(806938230251323433)
        log_msg = f'@here La pelle du banissement a frappé pour {member.mention} !\n\nhttps://media.giphy.com/media/CnUuUlNHW59ZeDqdIo/giphy.gif'
        banned_msg = f'Tu as été banni du serveur pour {reason}.'
        
        await member.send(banned_msg)
        await ctx.guild.ban(member,reason=reason)
        await log_channel.send(content=log_msg)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def unban(self,ctx,member: discord.Member=None,*reason):
        if member == None:
            await ctx.channel.send(f'N\'oubliez pas de mentionner le membre que vous voulez bannir.\n\nExemple: ```!ban @MyBOT Non-respect des règles.```')
            return

        if member == ctx.author or member.bot:
            await ctx.channel.send('Vous ne pouvez pas vous auto-bannir du serveur ou bannir le bot.')
            return

        banned_msg = f'Tu as été banni du serveur pour {reason}.'
        
        await member.send(banned_msg)
        await ctx.guild.ban(member,reason=reason)
        
def setup(bot):
    bot.add_cog(Moderator(bot))