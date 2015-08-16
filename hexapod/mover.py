from copy import copy


class Step:
    def __init__(self, servo, position):
        self.servo = servo
        self.position = position


class Mover:
    def __init__(self, movements):
        self.movements = movements
        self.steps = []

    def prepare(self):
        for m in self.movements:
            m.prepare()

        self.steps = []
        movements = copy(self.movements)
        while movements:
            for m in copy(movements):
                if m.steps:
                    self.steps.append(
                        Step(m.servo, m.steps.popleft())
                    )
                else:
                    movements.remove(m)

    def run(self):
        for step in self.steps:
            step.servo.set(step.position)
