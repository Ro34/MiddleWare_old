class Mission(object):
    def __init__(self):
        self._progress = 0

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, progress):
        if isinstance(progress, str):
            self._progress = int(progress)
        elif isinstance(progress, int):
            self._progress = progress

    @progress.deleter
    def progress(self):
        del self._progress


a = Mission()
Mission.progress = 50
print("%d%%" % Mission.progress)
