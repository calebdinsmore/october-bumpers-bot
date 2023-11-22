import nextcord
import sentry_sdk
from nextcord.ext import commands

from bot.cogs import AutoDeleteCommands, ImageMessageDeleteCommands
from bot.cogs.activity.activity_commands import ActivityCommands
from bot.cogs.admin.admin_commands import AdminCommands
from bot.cogs.secret_santa.secret_santa_commands import SecretSantaCommands
from bot.config import Config
from bot.events import on_member_join_event
from bot.events.on_message_event import register_event
from bot.utils import logger

intents = nextcord.Intents.all()
config = Config()
bot = commands.Bot(intents=intents)

sentry_sdk.init(
    dsn="https://00565c13fed21a6b54e808aad5acaea1@o250406.ingest.sentry.io/4505959527284736",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name='Mrs. Santa Claus'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


def run():
    bot.add_cog(AutoDeleteCommands(bot))
    bot.add_cog(ImageMessageDeleteCommands(bot))
    bot.add_cog(ActivityCommands(bot))
    bot.add_cog(SecretSantaCommands(bot))
    bot.add_cog(AdminCommands(bot))
    logger.register_bot(bot)
    on_member_join_event.register_event(bot)
    register_event(bot)
    bot.run(config.BOT_TOKEN)

