        emojis = ['1️⃣', '2️⃣', '3️⃣']  #이모지 리스트
        
        
        msg=await ctx.message.reply("1 2 3 중 하나를 선택하세요.")   #이모지를 추가할 메세지

        for a in emojis:
            await msg.add_reaction(a)   #이모지 추가

        def checks(reaction, user):
            if str(reaction.emoji) in emojis and not msg==reaction.message.id:  
                return True #유저가 추가한 이모지가 리스트 안에 있는지, 반응한 메세지가 봇이 보낸 메세지가 맞는지

        while True: #반복한다 == 이모지를 계속 확인한다
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=checks, timeout=30)  #이모지 반응을 기다린다. check 함수를 확인하고 30초 카운트다운을 한다
            except asyncio.TimeoutError:
                return await msg.delete()   #30초가 지나면 봇이 보낸 메세지를 지우고 명령어 프로세스를 종료한다
                
            await msg.remove_reaction(reaction, user)   #이모지 반응을 계속 확인하기위해 유저가 추가한 이모지를 지운다
            if user==self.bot.user: #봇인지 확인
                pass
            elif reaction.emoji == emojis[0]:
                await msg.edit(content="1을 선택하셨군요.")
            elif reaction.emoji == emojis[1]:
                await msg.edit(content="2를 선택하셨군요.")
            elif reaction.emoji == emojis[2]:
                await msg.edit(content="3을 선택하셨군요.")
