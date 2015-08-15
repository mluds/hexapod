class Mover:
    def __init__(self, *movements):
        self.movements = movements

    def prepare(self):
        for m in self.movements:
            m.prepare()

    def start(self):
        movements = copy(self.movements)
        i = 0
        while movements:
            for m in movements:
                # TODO: Removal condition
                if len(m):
                    pass
                m.servo.set()
