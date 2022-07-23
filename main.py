# Import the command handler
import lightbulb

# Instantiate a Bot instance
bot = lightbulb.BotApp(token="your_token_here", prefix="your_prefix_here")

# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "checks the bot is alive")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.PrefixCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")

# Run the bot
# Note that this is blocking meaning no code after this line will run
# until the bot is shut off
bot.run()