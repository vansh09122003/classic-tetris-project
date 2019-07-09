from ..util import Platform

class ArgException(Exception):
    pass


class Command:
    def __init__(self, context):
        self.context = context
        self.args = context.args

    @property
    def supported_platforms(self):
        return [Platform.DISCORD, Platform.TWITCH]



    def check_support_and_execute(self):
        if self.context.PLATFORM in self.supported_platforms:
            try:
                self.execute(*self.args)
            except ArgException:
                self.send_usage()
        else:
            self.send_message("Command not supported on this platform.")

    def send_message(self, message):
        self.context.send_message(message)

    def send_usage(self):
        # Add `wrapper` if in Discord
        formatted = self.context.format_code("{prefix}{usage}".format(
            prefix=self.context.PREFIX,
            usage=self.USAGE
        ))
        self.send_message(f"Usage: {formatted}")




COMMAND_MAP = {}

def register_command(*aliases):
    def register(command):
        for alias in aliases:
            COMMAND_MAP[alias] = command
        return command
    return register