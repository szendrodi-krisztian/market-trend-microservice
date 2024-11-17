class DataStreamerBase(object):

    def __init__(self, callback):
        self.callback = callback

    def start(self) -> None:
        pass