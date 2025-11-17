
import sys
import time
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QTimeEdit,QPushButton,QLabel,QMessageBox
from PyQt5.QtCore import Qt,QTime,QTimer
import winsound

class Alarmclock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm clock")
        self.setGeometry(100,100,300,200)
        self.Alarm_time=None

        self.clock_label=QLabel()
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setStyleSheet("font-size:24px")
        self.timeEdit=QTimeEdit()

        self.timeEdit.setDisplayFormat("HH:mm:ss")
        self.setBtn=  QPushButton("Setalarm")
        self.StopBtn=QPushButton("stop alarm")

        self.setBtn.clicked.connect(self.set_alarm) 
        self.StopBtn.clicked.connect(self.stop_alarm) 

        layout=QVBoxLayout()
        layout.addWidget(self.clock_label)

        h_layout=QHBoxLayout()
        h_layout.addWidget(self.timeEdit)
        h_layout.addWidget(self.setBtn)  
        h_layout.addWidget(self.StopBtn)

        layout.addLayout(h_layout)

        self.setLayout(layout)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def update_clock(self):
        current_time=QTime.currentTime().toString("HH:mm:ss")
        self.clock_label.setText(current_time)
        if self.Alarm_time==current_time:
            self.ring_alarm()

    def set_alarm(self):
        self.Alarm_time=self.timeEdit.time().toString("HH:mm:ss")
        QMessageBox.information(self,"Alarm set",f"alarm set for{self.Alarm_time}")

    def stop_alarm(self):
        self.Alarm_time=None
        QMessageBox.information(self,"alarm stopped", f"alarm stopped for {self.Alarm_time}")
    
    def ring_alarm(self):
        winsound.Beep(5000,5000)
        QMessageBox.information(self,"Time to wake up","Alarm time is up!")
        self.Alarm_time=None


     

    

                                       

if __name__=="__main__":
    app=QApplication(sys.argv)
    window =Alarmclock()
    window.show()

    sys.exit(app.exec_())
