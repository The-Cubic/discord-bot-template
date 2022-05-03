from disnake.ext import commands


class DevCommands(commands.Cog, name='Developer Commands'):
    '''These are the developer commands'''

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, inter):
        return inter.author.id == self.bot.author_id

    @commands.slash_command(name='reload')
    async def reload(self, inter, cog):
        '''
        Reloads a cog.
        '''
        extensions = self.bot.extensions
        if cog == 'all':
            for extension in extensions:
                self.bot.unload_extension(cog)
                self.bot.load_extension(cog)
            await inter.send('Done')
        if cog in extensions:
            self.bot.reload_extension(cog)
            await inter.send('Done')
        else:
            await inter.send('Unknown Cog')

    @commands.slash_command(name="unload")
    async def unload(self, inter, cog):
        '''
        Unload a cog.
        '''
        extensions = self.bot.extensions
        if cog not in extensions:
            await inter.send("Cog is not loaded!")
            return
        self.bot.unload_extension(cog)
        await inter.send(f"`{cog}` has successfully been unloaded.")

    @commands.slash_command(name="load")
    async def load(self, inter, cog):
        '''
        Loads a cog.
        '''
        try:

            self.bot.load_extension(cog)
            await inter.send(f"`{cog}` has successfully been loaded.")

        except commands.errors.ExtensionNotFound:
            await inter.send(f"`{cog}` does not exist!")

    @commands.slash_command(name="listcogs", aliases=['lc'])
    async def listcogs(self, inter):
        '''
        Returns a list of all enabled commands.
        '''
        base_string = "```css\n"
        base_string += "\n".join([str(cog) for cog in self.bot.extensions])
        base_string += "\n```"
        await inter.send(base_string)

def setup(bot):
    bot.add_cog(DevCommands(bot))