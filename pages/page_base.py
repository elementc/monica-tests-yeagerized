class PageBase:
    def initial_status(self):
        pass

    def __init__(self, driver):
        self.driver = driver
        self.initial_status()
