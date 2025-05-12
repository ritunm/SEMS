# load_balancer_sems.py

import random
import json
from datetime import datetime

DEFAULT_THRESHOLD = 80
LOG_FILE = "balance_logs.json"


class LoadBalancer:
    def __init__(self, threshold=DEFAULT_THRESHOLD):
        self.zones = {
            'zone1': 65,
            'zone2': 85,
            'zone3': 75,
            'zone4': 95,
            'ZoneA': 80
        }
        self.threshold = threshold
        self.history = []

    def simulate_data(self):
        for zone in self.zones:
            self.zones[zone] = random.randint(50, 100)

    def check_overloads(self):
        return {
            z: load for z, load in self.zones.items()
            if load > self.threshold
        }

    def balance_load(self):
        overloaded = self.check_overloads()
        for zone, load in overloaded.items():
            excess = load - self.threshold
            self.zones[zone] -= excess
            self.redistribute_load(zone, excess)
            self.log_event(
                f"Balanced {zone} by redistributing {excess}%"
            )

    def redistribute_load(self, source, excess):
        receivers = [
            z for z in self.zones
            if z != source and self.zones[z] < self.threshold
        ]
        if not receivers:
            self.log_event("No receivers available for redistribution.")
            return
        share = excess // len(receivers)
        for r in receivers:
            self.zones[r] += share

    def log_event(self, msg):
        event = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "message": msg,
            "status": self.zones.copy(),
            "threshold": self.threshold
        }
        self.history.append(event)
        with open(LOG_FILE, "w") as f:
            json.dump(self.history, f, indent=2)

    def get_status(self):
        return self.zones.copy()

    def get_history(self):
        return self.history

    def add_zone(self, name, value):
        if name not in self.zones:
            self.zones[name] = value
            self.log_event(
                f"Zone {name} added with value {value}%"
            )

    def delete_zone(self, name):
        if name in self.zones:
            del self.zones[name]
            self.log_event(f"Zone {name} deleted")

    def update_zone_value(self, name, value):
        if name in self.zones:
            self.zones[name] = value
            self.log_event(f"Zone {name} updated to {value}%")

    def update_zone(self, name, value):
        """Alias for update_zone_value to match test suite usage."""
        self.update_zone_value(name, value)

    def set_threshold(self, value):
        self.threshold = value
        self.log_event(f"Threshold updated to {value}%")
