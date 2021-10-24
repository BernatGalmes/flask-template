import click


def register_commands(app):
    @app.cli.command("install")
    def install():
        from api.extensions import db
        db.create_all()

