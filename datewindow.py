import sys
from datetime import datetime
import calendar
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QDialog
from PyQt5.QtCore import QDate
from PyQt5 import QtCore
#from new-app import Ui_MainWindow

class CalendarDemo(QDialog):
	global currentYear, currentMonth

	currentMonth = datetime.now().month
	currentYear = datetime.now().year

	# constructor
	def __init__(self):
		super(CalendarDemo, self).__init__()
		self.setWindowTitle('Calendar')
		self.setGeometry(300, 300, 450, 300)
		self.initUI()
		self.setWindowModality(QtCore.Qt.ApplicationModal)

	def initUI(self):
		self.calendar = QCalendarWidget(self)
		self.calendar.move(20, 20)
		self.calendar.setGridVisible(True)

		self.calendar.setMinimumDate(QDate(currentYear, currentMonth - 1, 1))
		self.calendar.setMaximumDate(QDate(
			currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth)[1]))

		#self.calendar.setSelectedDate(QDate(currentYear, currentMonth, 1))

		self.calendar.clicked.connect(self.sendDateMainWindow)

	def sendDateMainWindow(self, qDate):
		print('{0}/{1}/{2}'.format(type(qDate.month()), qDate.day(), qDate.year()))
		
		print(f'Day Number of the year: {qDate.dayOfYear()}')
		print(f'Day Number of the week: {qDate.dayOfWeek()}')
		
		



	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = CalendarDemo()
	demo.show()
	sys.exit(app.exec_())
