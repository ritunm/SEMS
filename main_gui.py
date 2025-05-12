# main_gui.py

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QTextEdit, QHBoxLayout, QInputDialog, QMessageBox
)
import sys
import subprocess
from load_balancer_sems import LoadBalancer


class LoadBalancerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = LoadBalancer()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Smart Grid Load Balancer")
        self.setGeometry(100, 100, 800, 400)
        layout = QVBoxLayout()

        self.status_label = QLabel("Zone Status")
        self.status_display = QTextEdit()
        self.status_display.setReadOnly(True)

        self.history_label = QLabel("History Logs")
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)

        simulate_btn = QPushButton("Simulate Load")
        simulate_btn.clicked.connect(self.simulate_data)

        balance_btn = QPushButton("Balance Load")
        balance_btn.clicked.connect(self.balance_data)

        test_btn = QPushButton("Run Python Tests (test.bat)")
        test_btn.clicked.connect(self.run_test_bat)

        add_zone_btn = QPushButton("Add Zone")
        add_zone_btn.clicked.connect(self.add_zone)

        del_zone_btn = QPushButton("Delete Zone")
        del_zone_btn.clicked.connect(self.delete_zone)

        update_zone_btn = QPushButton("Update Zone Value")
        update_zone_btn.clicked.connect(self.update_zone)

        set_thresh_btn = QPushButton("Set Threshold")
        set_thresh_btn.clicked.connect(self.set_threshold)

        coming_btn = QPushButton("Other Modules - Coming Soon")

        layout.addWidget(self.status_label)
        layout.addWidget(self.status_display)
        layout.addWidget(simulate_btn)
        layout.addWidget(balance_btn)

        zone_btns = QHBoxLayout()
        zone_btns.addWidget(add_zone_btn)
        zone_btns.addWidget(del_zone_btn)
        zone_btns.addWidget(update_zone_btn)
        layout.addLayout(zone_btns)

        layout.addWidget(set_thresh_btn)
        layout.addWidget(test_btn)
        layout.addWidget(coming_btn)
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_display)

        self.setLayout(layout)
        self.update_status()

    def simulate_data(self):
        self.lb.simulate_data()
        self.lb.log_event("Simulated data.")
        self.update_status()
        self.update_history()

    def balance_data(self):
        self.lb.balance_load()
        self.update_status()
        self.update_history()

    def run_test_bat(self):
        try:
            result = subprocess.run(
                ['test.bat'],
                capture_output=True,
                text=True,
                shell=True
            )
            QMessageBox.information(
                self,
                "Test Output",
                result.stdout + "\n" + result.stderr
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def add_zone(self):
        name, ok = QInputDialog.getText(self, 'Add Zone', 'Zone name:')
        if ok and name:
            value, ok = QInputDialog.getInt(
                self, 'Add Zone', 'Initial value:', min=0, max=150
            )
            if ok:
                self.lb.add_zone(name, value)
                self.update_status()
                self.update_history()

    def delete_zone(self):
        name, ok = QInputDialog.getText(self, 'Delete Zone', 'Zone name:')
        if ok and name:
            self.lb.delete_zone(name)
            self.update_status()
            self.update_history()

    def update_zone(self):
        name, ok = QInputDialog.getText(self, 'Update Zone', 'Zone name:')
        if ok and name:
            value, ok = QInputDialog.getInt(
                self, 'Update Zone', 'New value:', min=0, max=150
            )
            if ok:
                self.lb.update_zone_value(name, value)
                self.update_status()
                self.update_history()

    def set_threshold(self):
        value, ok = QInputDialog.getInt(
            self, 'Set Threshold', 'Threshold value:', min=10, max=150
        )
        if ok:
            self.lb.set_threshold(value)
            self.update_status()
            self.update_history()

    def update_status(self):
        self.status_display.setPlainText(str(self.lb.get_status()))

    def update_history(self):
        logs = self.lb.get_history()
        formatted = "\n\n".join([
            f"{log['timestamp']}: {log['message']}\n"
            f"Status: {log['status']}\n"
            f"Threshold: {log['threshold']}"
            for log in logs[-5:]
        ])
        self.history_display.setPlainText(formatted)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadBalancerApp()
    ex.show()
    sys.exit(app.exec_())

