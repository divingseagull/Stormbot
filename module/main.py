import nextcord
from nextcord.ext import commands
import os

path = __file__.removesuffix("\\module\\tst.py")

TOKEN = None

client = commands.Bot(
    command_prefix="?",
    intents=nextcord.Intents.all()
)

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="")
    @commands.is_owner()
    async def load(self, ctx: commands.Context, module: str):
        embed: nextcord.Embed
        try:
            embed = nextcord.Embed(
                title="완료",
                color=0x44FF44
            )
            client.load_extension(module)
        except ModuleNotFoundError:
            embed = nextcord.Embed(
                title="오류",
                description=f"{module}이란 이름의 모듈을 찾을 수 없습니다",
                color=0xFF4444
            )
        except commands.ExtensionError as E:
            embed = nextcord.Embed(
                title="오류",
                description=f"{module} 모듈에서 오류가 발생했습니다\n\n```{E}```",
                color=0xFF4444
            )
        finally:
            await ctx.send(embed=embed)

class MainError(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Main.load.error()
    async def loadError(self, ctx, error: nextcord.errors):
        if isinstance(error, nextcord.errors.InvalidArgument):
            await ctx.send(embed=nextcord.Embed(
                title="오류",
                description="모듈 이름을 입력해주세요",
                color=0xFF4444
            ))

if __name__ == "__main__":
    if os.path.exists(f"{path}\\data\\TOKEN.cnf"):
        pass
    else:
        with open(f"{path}\\data\\config", "wb") as cf:
            pass
    with open(f"{path}\\data\\config") as cf:
        pass
    client.login("OTM5NDgwNTMwOTc2NjQ5MjU3.Yf5dbQ.abliFz1CgssjpG4jR_DXV_Qtqi4")