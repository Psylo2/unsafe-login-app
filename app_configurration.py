

class AppConfiguration:
    def __init__(self, app):
        self._app = app
        self.add_configurations()

    @property
    def app(self):
        return self._app

    def add_configurations(self) -> None:
        self.app.secret_key = "Secret_Key"
        self.app.config.update(ADMIN="Admin")
