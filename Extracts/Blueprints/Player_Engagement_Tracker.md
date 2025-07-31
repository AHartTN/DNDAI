# Player Engagement Metrics Logic (Python Example)

See: Extracts/Scripts/engagement_tracker.py

```python
class EngagementTracker:
    def __init__(self):
        self.metrics = {"choices": 0, "dialogue": 0, "feedback": []}

    def record_choice(self):
        self.metrics["choices"] += 1

    def record_dialogue(self):
        self.metrics["dialogue"] += 1

    def add_feedback(self, feedback):
        self.metrics["feedback"].append(feedback)

    def engagement_score(self):
        # Simple formula: more choices/dialogue = higher engagement
        return self.metrics["choices"] + self.metrics["dialogue"] + len(self.metrics["feedback"])
```
