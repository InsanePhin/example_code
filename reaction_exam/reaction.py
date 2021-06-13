        emojis = ['1️⃣', '2️⃣', '3️⃣']
        
        msg=await ctx.message.reply("선택하세요")

        for a in emojis:
            await msg.add_reaction(a)

        await msg.edit(embed=basic)

        def checks(reaction, user):
            if str(reaction.emoji) in emojis and not msg==reaction.message.id:
                return True

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=checks, timeout=30)
            except asyncio.TimeoutError:
                await ctx.message.add_reaction("🗑️")
                return await msg.delete()

            await msg.remove_reaction(reaction, user)
            if user==self.bot.user:
                pass
            elif reaction.emoji == emojis[0]:
