class SessionState:
    def __init__(self):
        self.state = {}
        self.checkpoints = []

    def update(self, key, value):
        self.state[key] = value

    def checkpoint(self):
        self.checkpoints.append(self.state.copy())

    def rollback(self, index=-1):
        if self.checkpoints:
            self.state = self.checkpoints[index].copy()

    def serialize(self):
        import json
        return json.dumps(self.state)

    def restore(self, serialized_state):
        import json
        self.state = json.loads(serialized_state)
