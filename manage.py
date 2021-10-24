from api import create_app
from api.commands import register_commands

# initialize app
app = create_app()
app.debug = True


# register commands
register_commands(app)

