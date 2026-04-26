
import discord
from discord.ext import commands
from datetime import datetime, timezone

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.slash_command(name = "加入教學", description = "提供新玩家了解伺服器加入方式")
async def 加入教學(ctx: discord.ApplicationContext):
    bot_avatar = bot.user.display_avatar.url
    embed = discord.Embed(
        color = discord.Color.yellow(),
        timestamp = datetime.now(timezone.utc)
    )
    embed.set_author(name = "天星生存服等著你！", url = "https://media.discordapp.net/attachments/959102610751770624/1056080257674915941/1679137F-7603-4293-A913-7EE6A6B90A80.jpeg?ex=697500a2&is=6973af22&hm=57f80fcd7946560e30a5d984c382911d987e27ea1336238c8adc00f902a4017e&format=webp&width=1366&height=1366&", icon_url = "https://media.discordapp.net/attachments/959102610751770624/1056080257674915941/1679137F-7603-4293-A913-7EE6A6B90A80.jpeg?ex=697500a2&is=6973af22&hm=57f80fcd7946560e30a5d984c382911d987e27ea1336238c8adc00f902a4017e&format=webp&width=1366&height=1366&")
    embed.add_field(name = "不曉得應如何進服嗎？以下為簡單連接天星伺服器的教學喔！", value = "", inline = False)
    embed.add_field(name = "步驟一：依照你的遊玩裝置選擇ip加入", value = "- JAVA版IP: skystarmc.xyz\n- 基岩版IP: be.skystarmc.xyz\n- 基岩版端口：38156", inline = False)
    embed.add_field(name = "步驟二：連接帳號", value = "- 進入伺服器後，在聊天欄輸入`/discord link`會獲得4位數字，\n- 將數字發送在 <#1388542054849712180> 即可完成", inline = False)
    embed.add_field(name = "步驟三：開心遊玩", value = "", inline = False)
    embed.add_field(name = "常用指令", value = "- /menu - 打開伺服器選單\n- /rtp - 隨機傳送展開旅程\n- /sethome <家名稱> - 設置家點\n- /home <家名稱> - 傳送至家點\n前往[**遊戲指南論壇**](<https://discord.com/channels/809424029478944779/1121420256792039555>)找到更詳細的教學喔", inline = False)
    embed.set_footer(text = "祝福你遊玩愉快", icon_url = bot_avatar)
    await ctx.respond(embed = embed)

@bot.slash_command(name= "電梯", description = "電梯相關教學")
async def 電梯(ctx: discord.ApplicationContext):
    await ctx.respond("電梯教學頻道: https://discord.com/channels/809424029478944779/1139902766035247187")

@bot.slash_command(name= "連接帳號", description= "連接帳號教學")
async def 連接帳號(ctx: discord.ApplicationContext):
    await ctx.respond("連接帳號教學頻道: https://discord.com/channels/809424029478944779/1344269443307536414")

@bot.slash_command(name= "特殊附魔", description= "特殊附魔列表")
async def 特殊附魔(ctx: discord.ApplicationContext):
    await ctx.respond("特殊附魔說明頻道: https://discord.com/channels/809424029478944779/1344253700042133515\n**(基岩版無法附魔任何特殊附魔)**")

@bot.event
async def on_member_join(member):
    welcome_channel = member.guild.get_channel(962635362520399912)
    guild = member.guild
    count = guild.member_count
    bot_avatar = bot.user.display_avatar.url
    ROLE_ID = 959697215134265366
    role = member.guild.get_role(ROLE_ID)
    embed = discord.Embed(
        title = "哈囉第一次加入嗎？",
        description = "伺服器位置等相關資訊都在 <#967617878109061200>\n若有其他問題也可以在公頻詢問我們喔",
        color = discord.Color.random(),
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_author(name = f'{member.name}' + "歡迎加入天星生存伺服器！", url = member.avatar, icon_url = member.avatar)
    embed.set_footer(text = f"你是本群第 {count} 位用戶", icon_url = bot_avatar)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/959102610751770624/1056080257674915941/1679137F-7603-4293-A913-7EE6A6B90A80.jpeg?ex=697457e2&is=69730662&hm=545428708c48d2273b4b00017df562218627f3c1d8263d4aa6fd98dd4e34c69a&=&format=webp&width=1366&height=1366")
    if welcome_channel:
        await welcome_channel.send(f'{member.mention}')
        await welcome_channel.send(embed = embed)
        await member.add_roles(role)

@bot.event
async def on_member_remove(member):
    leave_channel = member.guild.get_channel(962635362520399912)
    guild = member.guild
    count = guild.member_count
    bot_avatar = bot.user.display_avatar.url
    embed = discord.Embed(
        title = "有人離開天星了...",
        description = "感謝你曾經待過天星生存服",
        color = discord.Color.random(),
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_author(name = f'{member.name}' + "有緣再相見了～", url = member.avatar, icon_url = member.avatar)
    embed.set_footer(text = f"本群還有 {count} 位用戶", icon_url = bot_avatar)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/959102610751770624/1056080257674915941/1679137F-7603-4293-A913-7EE6A6B90A80.jpeg?ex=697457e2&is=69730662&hm=545428708c48d2273b4b00017df562218627f3c1d8263d4aa6fd98dd4e34c69a&=&format=webp&width=1366&height=1366")
    if leave_channel:
        await leave_channel.send(f'{member.mention}')
        await leave_channel.send(embed = embed)

@bot.slash_command(escription="發送私訊", default_member_permissions=discord.Permissions(administrator=True))
async def 發送私訊(ctx: discord.ApplicationContext, user: discord.User, message: str):
    try:
        dm_channel = await user.create_dm()
        
        await dm_channel.send(f"{message}")
        
        await ctx.respond(f"已私訊給 {user.name}", ephemeral=True)
    except discord.Forbidden:
        await ctx.respond("無法私訊此使用者（可能關閉了隱私設定或封鎖機器人）", ephemeral=True)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.guild is None:
        log_channel_id = 1107217660686643241 
        log_channel = bot.get_channel(log_channel_id)

        log_msg = f"📩 **收到私訊**\n**發送者**: {message.author} ({message.author.id})\n**內容**: {message.content}"
        
        if log_channel:
            await log_channel.send(log_msg)
        
        if message.attachments:
            for attach in message.attachments:
                await log_channel.send(f"附件內容: {attach.url}")

bot.run("bot token")
