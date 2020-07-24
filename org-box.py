from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import calendar
from PyQt5.QtWidgets import *
from psycopg2.extensions import AsIs
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import sys
import picture

'''
START OF Font FORMATTING
'''

SmallKhmerFont = QtGui.QFont()
SmallKhmerFont.setFamily("Khmer OS")
SmallKhmerFont.setPointSize(14)

BigKhmerFont = QtGui.QFont()
BigKhmerFont.setBold(True)
BigKhmerFont.setFamily("Khmer OS")
BigKhmerFont.setPointSize(14)

DeadlineSmallKhmerFont = QtGui.QFont()
DeadlineSmallKhmerFont.setFamily("Khmer OS")
DeadlineSmallKhmerFont.setPointSize(14)

ENGFont = QtGui.QFont()
ENGFont.setFamily("Palatino Linotype")
ENGFont.setPointSize(15)



'''
END OF Font FORMATTING
'''


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        
        self.setWindowTitle("My Awesome App")
        MainLayout = QGridLayout()
        MainLayout.setContentsMargins(10,10,10,10)
        '''
        START OF CUSTOMER BOX
        '''
        
     
        #CustomerTitle 
        self.CustomerInfoTitle = QtWidgets.QLabel()
        self.CustomerInfoTitle.setFont(BigKhmerFont)
        self.CustomerInfoTitle.setMaximumSize(200,50)
        self.CustomerInfoTitle.setAutoFillBackground(False)
        self.CustomerInfoTitle.setObjectName("CustomerInfoTitle")
        


        #CustomerAddress
        self.AddressLabel = QtWidgets.QLabel()
        self.AddressLabel.setFont(SmallKhmerFont)
        self.AddressLabel.setMaximumSize(110,50)
        self.AddressLabel.setAutoFillBackground(False)
        self.AddressLabel.setObjectName("AddressLabel")

        #CustomerName
        self.CustomerNameLabel = QtWidgets.QLabel()
        self.CustomerNameLabel.setFont(SmallKhmerFont)
        self.CustomerNameLabel.setMaximumSize(110,50)
        self.CustomerNameLabel.setAutoFillBackground(False)
        self.CustomerNameLabel.setObjectName("CustomerNameLabel")



        #CustomerTelephone
        self.PhoneLabel = QtWidgets.QLabel()
        self.PhoneLabel.setEnabled(True)
        self.PhoneLabel.setFont(SmallKhmerFont)
        self.PhoneLabel.setMaximumSize(110,50)
        self.PhoneLabel.setAutoFillBackground(False)
        self.PhoneLabel.setObjectName("PhoneLabel")
        
        #line edits for CUSTOMER
        self.CustomerNameBox = QtWidgets.QLineEdit()
        self.CustomerNameBox.setMaximumSize(300, 50)
        self.CustomerNameBox.setAlignment(Qt.AlignLeft)
        self.CustomerNameBox.setFont(SmallKhmerFont)
        self.CustomerNameBox.setObjectName("CustomerNameBox")

        self.PhoneBox = QtWidgets.QLineEdit()
        self.PhoneBox.setMaximumSize(300, 50)
        self.PhoneBox.setFont(SmallKhmerFont)
        self.PhoneBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PhoneBox.setObjectName("PhoneBox")
        
        self.AddressBox = QtWidgets.QPlainTextEdit()
        self.AddressBox.setMaximumSize(300, 50)
        self.AddressBox.setFont(SmallKhmerFont)
        self.AddressBox.setObjectName("AddressBox")


        '''
        add to main layout
        '''
        #customer box

        self.CustomerBoxGroup = QtWidgets.QGroupBox()
        self.CustomerBoxGroup.setStyleSheet("background-color: #d7dbdd; ")
        self.CustomerBoxGroup.setMaximumSize(550, 400)
        
        CustomerBoxLayout = QGridLayout()
        #CustomerBoxLayout.setSpacing(10)
        
        CustomerBoxLayout.addWidget(self.CustomerInfoTitle, 0, 0, 1, 1)
        
        CustomerBoxLayout.addWidget(self.CustomerNameLabel, 1, 0)
        CustomerBoxLayout.addWidget(self.PhoneLabel, 2, 0)
        CustomerBoxLayout.addWidget(self.AddressLabel, 3, 0)
        

        CustomerBoxLayout.addWidget(self.CustomerNameBox, 1, 1)
        CustomerBoxLayout.addWidget(self.PhoneBox, 2, 1)
        CustomerBoxLayout.addWidget(self.AddressBox, 3, 1)

        

        self.CustomerBoxGroup.setLayout(CustomerBoxLayout)



        #MainLayout.addWidget(self.CustomerBoxGroup, 0, 0)

        '''
        END OF Customer BOX 
        '''

        
      


        '''
        START OF Staff BOX 
        '''

        self.StaffTitle = QtWidgets.QLabel()
        self.StaffTitle.setFont(BigKhmerFont)
        self.StaffTitle.setMaximumSize(200,50)
        self.StaffTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StaffTitle.setAutoFillBackground(False)
        self.StaffTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StaffTitle.setObjectName("StaffTitle")

        self.StaffNameLabel = QtWidgets.QLabel()
        self.StaffNameLabel.setMaximumSize(110, 50)
        self.StaffNameLabel.setFont(SmallKhmerFont)
        self.StaffNameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StaffNameLabel.setAutoFillBackground(False)
        self.StaffNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StaffNameLabel.setObjectName("StaffNameLabel")

        
        self.DeadlineLabel = QtWidgets.QLabel()
        self.DeadlineLabel.setFont(SmallKhmerFont)
        self.DeadlineLabel.setMaximumSize(110, 50)
        self.DeadlineLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DeadlineLabel.setAutoFillBackground(False)
        self.DeadlineLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DeadlineLabel.setObjectName("DeadlineLabel")
        
        self.DateIcon = QtWidgets.QPushButton()
        self.DateIcon.setMaximumSize(40,40)
        self.DateIcon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DateIcon.setAutoFillBackground(False)
        self.DateIcon.setObjectName("DateIcon")
        self.DateIcon.setIcon(QtGui.QIcon('pictures/calendar.png'))
        size = QtCore.QSize(40, 40)
        self.DateIcon.setIconSize(size)
        


        #user input name of staff
        self.StaffNameBox = QtWidgets.QLineEdit()
        self.StaffNameBox.setMaximumSize(300,50)
        self.StaffNameBox.setFont(SmallKhmerFont)
        self.StaffNameBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StaffNameBox.setAutoFillBackground(False)
        self.StaffNameBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.StaffNameBox.setText("")
        self.StaffNameBox.setAlignment(QtCore.Qt.AlignCenter)
        self.StaffNameBox.setObjectName("StaffNameBox")

        #label to show date chosen
        
        self.DeadlineSelectedLabel = QtWidgets.QLabel()
        self.DeadlineSelectedLabel.setMaximumSize(200,50)
        self.DeadlineSelectedLabel.setFont(DeadlineSmallKhmerFont)
        self.DeadlineSelectedLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DeadlineSelectedLabel.setAutoFillBackground(True)
        self.DeadlineSelectedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DeadlineSelectedLabel.setObjectName("DeadlineSelectedLabel")


        #label to send date to database
        #not in Ui
        self.DeadlineBox = QtWidgets.QLabel()
        #self.DeadlineBox.setGeometry(QtCore.QRect(0, 0, 0, 0))  
        self.DeadlineBox.setFont(SmallKhmerFont)
        self.DeadlineBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DeadlineBox.setAutoFillBackground(False)
        self.DeadlineBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DeadlineBox.setObjectName("DeadlineBox")
        #not in Ui



        #staff box 

        self.StaffBoxGroup = QtWidgets.QGroupBox()
        self.StaffBoxGroup.setMaximumSize(550,400)
        self.StaffBoxGroup.setStyleSheet("background-color: #d7dbdd; ")

        StaffBoxLayout = QGridLayout()
        #StaffBoxLayout.setSpacing(10)
        
        StaffBoxLayout.addWidget(self.StaffTitle, 0, 0)
        
        StaffBoxLayout.addWidget(self.StaffNameLabel, 1, 0)
        StaffBoxLayout.addWidget(self.DeadlineLabel, 2, 0)

        StaffBoxLayout.addWidget(self.StaffNameBox, 1, 1)

        #not in ui
        StaffBoxLayout.addWidget(self.DeadlineBox, 2, 1)
        #not in ui

        DisplayDateRow = QHBoxLayout()
        DisplayDateRow.addWidget(self.DateIcon)
        DisplayDateRow.addWidget(self.DeadlineSelectedLabel)

        StaffBoxLayout.addLayout(DisplayDateRow, 2, 1)

        self.StaffBoxGroup.setLayout(StaffBoxLayout)

        #MainLayout.addWidget(self.StaffBoxGroup, 1, 0)
               
        '''
        END OF Staff BOX 
        '''

        '''
        START OF CUSTOMER PREFERENCES BOX
        '''


        self.CustomerPreferencesTitle = QtWidgets.QLabel()
        self.CustomerPreferencesTitle.setMaximumSize(200,50)
        self.CustomerPreferencesTitle.setFont(BigKhmerFont)
        self.CustomerPreferencesTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CustomerPreferencesTitle.setAutoFillBackground(False)
        self.CustomerPreferencesTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CustomerPreferencesTitle.setObjectName("CustomerPreferencesTitle")

        self.ColorLabel = QtWidgets.QLabel()
        self.ColorLabel.setMaximumSize(110,50)
        self.ColorLabel.setFont(SmallKhmerFont)
        self.ColorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ColorLabel.setAutoFillBackground(False)
        self.ColorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ColorLabel.setObjectName("ColorLabel")

        self.StyleLabel = QtWidgets.QLabel()
        self.StyleLabel.setFont(SmallKhmerFont)
        self.StyleLabel.setMaximumSize(110,50)
        self.StyleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StyleLabel.setAutoFillBackground(False)
        self.StyleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StyleLabel.setObjectName("StyleLabel")


        self.MaterialsLabel = QtWidgets.QLabel()
        self.MaterialsLabel.setFont(SmallKhmerFont)
        self.MaterialsLabel.setMaximumSize(140,50)
        self.MaterialsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MaterialsLabel.setAutoFillBackground(False)
        self.MaterialsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MaterialsLabel.setObjectName("MaterialsLabel")

        #user inputs
        self.MaterialBox = QtWidgets.QLineEdit()
        self.MaterialBox.setFont(SmallKhmerFont)
        self.MaterialBox.setMaximumSize(300,50)
        self.MaterialBox.setObjectName("MaterialBox")

        self.ColorBox = QtWidgets.QLineEdit()
        self.ColorBox.setFont(SmallKhmerFont)
        self.ColorBox.setMaximumSize(300,50)
        self.ColorBox.setObjectName("ColorBox")

        self.StyleBox = QtWidgets.QLineEdit()
        self.StyleBox.setFont(SmallKhmerFont)
        self.StyleBox.setMaximumSize(300,50)
        self.StyleBox.setObjectName("StyleBox")

        

                
        #preferences box
        self.PreferencesBoxGroup = QtWidgets.QGroupBox()
        self.PreferencesBoxGroup.setMaximumSize(550,400)
        self.PreferencesBoxGroup.setStyleSheet("background-color: #d7dbdd; ")

        PreferencesBoxLayout = QGridLayout()

        PreferencesBoxLayout.addWidget(self.CustomerPreferencesTitle, 0, 0)

        PreferencesBoxLayout.addWidget(self.MaterialsLabel, 1, 0)
        PreferencesBoxLayout.addWidget(self.ColorLabel, 2, 0)
        PreferencesBoxLayout.addWidget(self.StyleLabel, 3, 0)

        PreferencesBoxLayout.addWidget(self.MaterialBox, 1, 1)
        PreferencesBoxLayout.addWidget(self.ColorBox, 2, 1)
        PreferencesBoxLayout.addWidget(self.StyleBox, 3, 1)

        self.PreferencesBoxGroup.setLayout(PreferencesBoxLayout)

        #MainLayout.addWidget(self.PreferencesBoxGroup, 0, 1)

        self.TopColGroup = QHBoxLayout()
        self.TopColGroup.addWidget(self.CustomerBoxGroup)
        self.TopColGroup.addWidget(self.PreferencesBoxGroup)
        self.TopColGroup.addWidget(self.StaffBoxGroup)

        MainLayout.addLayout(self.TopColGroup, 0, 0, 1, 2)
        
        '''
        END OF CUSTOMER PREFERENCES BOX
        '''

        
        '''
        START OF SPECIAL REQ BOX
        '''


        self.SpecialReqTitle = QtWidgets.QLabel()
        self.SpecialReqTitle.setFont(BigKhmerFont)
        self.SpecialReqTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SpecialReqTitle.setAutoFillBackground(False)
        self.SpecialReqTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SpecialReqTitle.setObjectName("SpecialReqTitle")

        self.SpecialReqBox = QtWidgets.QPlainTextEdit()
        self.SpecialReqBox.setFont(SmallKhmerFont)
        self.SpecialReqBox.setObjectName("SpecialReqBox")


        #special req box
        
        self.SpecReqBoxGroup = QtWidgets.QGroupBox()
        #self.SpecReqBoxGroup.setMaximumSize(550,400)
        self.SpecReqBoxGroup.setStyleSheet("background-color: #d7dbdd; ")

        SpecReqBoxLayout = QGridLayout()
    

        SpecReqBoxLayout.addWidget(self.SpecialReqTitle, 0, 0)
        SpecReqBoxLayout.addWidget(self.SpecialReqBox, 1, 0)
        
        self.SpecReqBoxGroup.setLayout(SpecReqBoxLayout)

        MainLayout.addWidget(self.SpecReqBoxGroup, 1, 0, 1, 2)


        '''
        END OF SPECIAL REQ BOX
        '''


        '''
        START OF MEASUREMENTS BOX
        '''

        #might delete
        self.MeasurementTitle = QtWidgets.QLabel()
        self.MeasurementTitle.setFont(BigKhmerFont)
        self.MeasurementTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MeasurementTitle.setAutoFillBackground(False)
        self.MeasurementTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MeasurementTitle.setObjectName("MeasurementTitle")

        self.ShirtDressSkirtBox = QtWidgets.QGroupBox()
        self.ShirtDressSkirtBox.setFont(BigKhmerFont)
        self.ShirtDressSkirtBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ShirtDressSkirtBox.setObjectName("ShirtDressSkirtBox")

        self.ShirtDressSkirtLayout = QtWidgets.QGridLayout()

        self.AroundBustBox = QtWidgets.QLineEdit()
        self.AroundBustBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AroundBustBox.setObjectName("AroundBustBox")
        self.ShirtDressSkirtLayout.addWidget(self.AroundBustBox, 4, 4, 1, 1)

        self.NeckArmHoldBox = QtWidgets.QLineEdit()
        self.NeckArmHoldBox.setAlignment(QtCore.Qt.AlignCenter)
        self.NeckArmHoldBox.setObjectName("NeckArmHoldBox")
        self.ShirtDressSkirtLayout.addWidget(self.NeckArmHoldBox, 1, 4, 1, 1)
        
        self.WaistBox = QtWidgets.QLineEdit()
        self.WaistBox.setAlignment(QtCore.Qt.AlignCenter)
        self.WaistBox.setObjectName("WaistBox")
        self.ShirtDressSkirtLayout.addWidget(self.WaistBox, 6, 4, 1, 1)

        self.ABBox = QtWidgets.QLineEdit()
        self.ABBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ABBox.setObjectName("ABBox")
        self.ShirtDressSkirtLayout.addWidget(self.ABBox, 0, 4, 1, 1)

        self.DressSkirtWaistLabel = QtWidgets.QLabel()
        self.DressSkirtWaistLabel.setObjectName("DressSkirtWaistLabel")
        self.DressSkirtWaistLabel.setFont(SmallKhmerFont)
        self.ShirtDressSkirtLayout.addWidget(self.DressSkirtWaistLabel, 6, 3, 1, 1, QtCore.Qt.AlignHCenter)


        self.UpperHipsLabel = QtWidgets.QLabel()
        self.UpperHipsLabel.setFont(SmallKhmerFont)
        self.UpperHipsLabel.setObjectName("UpperHipsLabel")
        self.ShirtDressSkirtLayout.addWidget(self.UpperHipsLabel, 3, 6, 1, 1)
        
        self.CmUpperHips = QtWidgets.QLabel()
        self.CmUpperHips.setFont(ENGFont)
        self.CmUpperHips.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmUpperHips.setAutoFillBackground(False)
        self.CmUpperHips.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmUpperHips.setObjectName("CmUpperHips")
        self.ShirtDressSkirtLayout.addWidget(self.CmUpperHips, 3, 8, 1, 1)



        self.CmAroundBust = QtWidgets.QLabel()
        self.CmAroundBust.setFont(ENGFont)
        self.CmAroundBust.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmAroundBust.setAutoFillBackground(False)
        self.CmAroundBust.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmAroundBust.setObjectName("CmAroundBust")
        self.ShirtDressSkirtLayout.addWidget(self.CmAroundBust, 4, 5, 1, 1)


        self.HipLabel = QtWidgets.QLabel()
        self.HipLabel.setFont(SmallKhmerFont)
        self.HipLabel.setObjectName("HipLabel")
        self.ShirtDressSkirtLayout.addWidget(self.HipLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.HipBox = QtWidgets.QLineEdit()
        self.HipBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HipBox.setObjectName("HipBox")
        self.ShirtDressSkirtLayout.addWidget(self.HipBox, 0, 1, 1, 1)

        
        self.CmCenterFront = QtWidgets.QLabel()
        self.CmCenterFront.setFont(ENGFont)
        self.CmCenterFront.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmCenterFront.setAutoFillBackground(False)
        self.CmCenterFront.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmCenterFront.setObjectName("CmCenterFront")
        self.ShirtDressSkirtLayout.addWidget(self.CmCenterFront, 3, 2, 1, 1)

        self.CmNeckArmHold = QtWidgets.QLabel()
        self.CmNeckArmHold.setFont(ENGFont)
        self.CmNeckArmHold.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmNeckArmHold.setAutoFillBackground(False)
        self.CmNeckArmHold.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmNeckArmHold.setObjectName("CmNeckArmHold")
        self.ShirtDressSkirtLayout.addWidget(self.CmNeckArmHold, 1, 5, 1, 1)


        self.NeckArmHoldLabel = QtWidgets.QLabel()
        self.NeckArmHoldLabel.setFont(SmallKhmerFont)
        self.NeckArmHoldLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NeckArmHoldLabel.setAutoFillBackground(False)
        self.NeckArmHoldLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NeckArmHoldLabel.setObjectName("NeckArmHoldLabel")
        self.ShirtDressSkirtLayout.addWidget(self.NeckArmHoldLabel, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        
        
        self.CmAB = QtWidgets.QLabel()
        self.CmAB.setFont(ENGFont)
        self.CmAB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmAB.setAutoFillBackground(False)
        self.CmAB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmAB.setObjectName("CmAB")
        self.ShirtDressSkirtLayout.addWidget(self.CmAB, 0, 5, 1, 1)


        self.CmHip = QtWidgets.QLabel()
        self.CmHip.setFont(ENGFont)
        self.CmHip.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmHip.setAutoFillBackground(False)
        self.CmHip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmHip.setObjectName("CmHip")
        self.ShirtDressSkirtLayout.addWidget(self.CmHip, 0, 2, 1, 1)


        self.CmBustHeight = QtWidgets.QLabel()
        self.CmBustHeight.setFont(ENGFont)
        self.CmBustHeight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmBustHeight.setAutoFillBackground(False)
        self.CmBustHeight.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmBustHeight.setObjectName("CmBustHeight")
        self.ShirtDressSkirtLayout.addWidget(self.CmBustHeight, 5, 5, 1, 1)

        self.CmAboveBust = QtWidgets.QLabel()
        self.CmAboveBust.setFont(ENGFont)
        self.CmAboveBust.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmAboveBust.setAutoFillBackground(False)
        self.CmAboveBust.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmAboveBust.setObjectName("CmAboveBust")
        self.ShirtDressSkirtLayout.addWidget(self.CmAboveBust, 3, 5, 1, 1)

        self.CmSkirtLength = QtWidgets.QLabel()
        self.CmSkirtLength.setFont(ENGFont)
        self.CmSkirtLength.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmSkirtLength.setAutoFillBackground(False)
        self.CmSkirtLength.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmSkirtLength.setObjectName("CmSkirtLength")
        self.ShirtDressSkirtLayout.addWidget(self.CmSkirtLength, 1, 2, 1, 1)
        
        self.CmAF = QtWidgets.QLabel()
        self.CmAF.setFont(ENGFont)
        self.CmAF.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmAF.setAutoFillBackground(False)
        self.CmAF.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmAF.setObjectName("CmAF")
        self.ShirtDressSkirtLayout.addWidget(self.CmAF, 6, 2, 1, 1)


        self.CmShoulder = QtWidgets.QLabel()
        self.CmShoulder.setFont(ENGFont)
        self.CmShoulder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmShoulder.setAutoFillBackground(False)
        self.CmShoulder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmShoulder.setObjectName("CmShoulder")
        self.ShirtDressSkirtLayout.addWidget(self.CmShoulder, 5, 2, 1, 1)
        
        self.ShoulderLabel = QtWidgets.QLabel()
        self.ShoulderLabel.setFont(SmallKhmerFont)
        self.ShoulderLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ShoulderLabel.setAutoFillBackground(False)
        self.ShoulderLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ShoulderLabel.setObjectName("ShoulderLabel")
        self.ShirtDressSkirtLayout.addWidget(self.ShoulderLabel, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)


        self.CmCenterBack = QtWidgets.QLabel()
        self.CmCenterBack.setFont(ENGFont)
        self.CmCenterBack.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmCenterBack.setAutoFillBackground(False)
        self.CmCenterBack.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmCenterBack.setObjectName("CmCenterBack")
        self.ShirtDressSkirtLayout.addWidget(self.CmCenterBack, 4, 2, 1, 1)


        self.CenterFrontLabel = QtWidgets.QLabel()
        self.CenterFrontLabel.setFont(SmallKhmerFont)
        self.CenterFrontLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CenterFrontLabel.setAutoFillBackground(False)
        self.CenterFrontLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CenterFrontLabel.setObjectName("CenterFrontLabel")
        self.ShirtDressSkirtLayout.addWidget(self.CenterFrontLabel, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.CmDressSkirtWaist = QtWidgets.QLabel()
        self.CmDressSkirtWaist.setFont(ENGFont)
        self.CmDressSkirtWaist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmDressSkirtWaist.setAutoFillBackground(False)
        self.CmDressSkirtWaist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmDressSkirtWaist.setObjectName("CmDressSkirtWaist")
        self.ShirtDressSkirtLayout.addWidget(self.CmDressSkirtWaist, 6, 5, 1, 1)


        self.SleeveLengthLabel = QtWidgets.QLabel()
        self.SleeveLengthLabel.setFont(SmallKhmerFont)
        self.SleeveLengthLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SleeveLengthLabel.setAutoFillBackground(False)
        self.SleeveLengthLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SleeveLengthLabel.setObjectName("SleeveLengthLabel")
        self.ShirtDressSkirtLayout.addWidget(self.SleeveLengthLabel, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)


        self.CmSleeveLength = QtWidgets.QLabel()
        self.CmSleeveLength.setFont(ENGFont)
        self.CmSleeveLength.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmSleeveLength.setAutoFillBackground(False)
        self.CmSleeveLength.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmSleeveLength.setObjectName("CmSleeveLength")
        self.ShirtDressSkirtLayout.addWidget(self.CmSleeveLength, 1, 8, 1, 1)

        self.AboveBustLabel = QtWidgets.QLabel()
        self.AboveBustLabel.setFont(SmallKhmerFont)
        self.AboveBustLabel.setObjectName("AboveBustLabel")
        self.ShirtDressSkirtLayout.addWidget(self.AboveBustLabel, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.CmArmPit = QtWidgets.QLabel()
        self.CmArmPit.setFont(ENGFont)
        self.CmArmPit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmArmPit.setAutoFillBackground(False)
        self.CmArmPit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmArmPit.setObjectName("CmArmPit")
        self.ShirtDressSkirtLayout.addWidget(self.CmArmPit, 0, 8, 1, 1)

        self.ArmpitLabel = QtWidgets.QLabel()
        self.ArmpitLabel.setFont(SmallKhmerFont)
        self.ArmpitLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ArmpitLabel.setAutoFillBackground(False)
        self.ArmpitLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ArmpitLabel.setObjectName("ArmpitLabel")
        self.ShirtDressSkirtLayout.addWidget(self.ArmpitLabel, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)



        self.ABLabel = QtWidgets.QLabel()
        self.ABLabel.setFont(SmallKhmerFont)
        self.ABLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ABLabel.setAutoFillBackground(False)
        self.ABLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ABLabel.setObjectName("ABLabel")
        self.ShirtDressSkirtLayout.addWidget(self.ABLabel, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
    
        self.AroundBustLabel = QtWidgets.QLabel()
        self.AroundBustLabel.setFont(SmallKhmerFont)
        self.AroundBustLabel.setObjectName("AroundBustLabel")
        self.ShirtDressSkirtLayout.addWidget(self.AroundBustLabel, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.BustHeightLabel = QtWidgets.QLabel()
        self.BustHeightLabel.setFont(SmallKhmerFont)
        self.BustHeightLabel.setObjectName("BustHeightLabel")
        self.ShirtDressSkirtLayout.addWidget(self.BustHeightLabel, 5, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.AboveBustBox = QtWidgets.QLineEdit()
        self.AboveBustBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AboveBustBox.setObjectName("AboveBustBox")
        self.ShirtDressSkirtLayout.addWidget(self.AboveBustBox, 3, 4, 1, 1)

        self.CenterFrontBox = QtWidgets.QLineEdit()
        self.CenterFrontBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CenterFrontBox.setObjectName("CenterFrontBox")
        self.ShirtDressSkirtLayout.addWidget(self.CenterFrontBox, 3, 1, 1, 1)

        self.ShoulderBox = QtWidgets.QLineEdit()
        self.ShoulderBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ShoulderBox.setObjectName("ShoulderBox")
        self.ShirtDressSkirtLayout.addWidget(self.ShoulderBox, 5, 1, 1, 1)

        self.AFBox = QtWidgets.QLineEdit()
        self.AFBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AFBox.setObjectName("AFBox")
        self.ShirtDressSkirtLayout.addWidget(self.AFBox, 6, 1, 1, 1)
        

        self.CenterBackBox = QtWidgets.QLineEdit()
        self.CenterBackBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CenterBackBox.setObjectName("CenterBackBox")
        self.ShirtDressSkirtLayout.addWidget(self.CenterBackBox, 4, 1, 1, 1)
        

        
        self.UpperHipsBox = QtWidgets.QLineEdit()
        self.UpperHipsBox.setAlignment(QtCore.Qt.AlignCenter)
        self.UpperHipsBox.setObjectName("UpperHipsBox")
        self.ShirtDressSkirtLayout.addWidget(self.UpperHipsBox, 3, 7, 1, 1)


        
        self.ArmpitBox = QtWidgets.QLineEdit()
        self.ArmpitBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ArmpitBox.setObjectName("ArmpitBox")
        self.ShirtDressSkirtLayout.addWidget(self.ArmpitBox, 0, 7, 1, 1)

        self.SkirtLengthLabel = QtWidgets.QLabel()
        self.SkirtLengthLabel.setObjectName("SkirtLengthLabel")
        self.SkirtLengthLabel.setFont(SmallKhmerFont)
        self.ShirtDressSkirtLayout.addWidget(self.SkirtLengthLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.SkirtLengthBox = QtWidgets.QLineEdit()
        self.SkirtLengthBox.setAlignment(QtCore.Qt.AlignCenter)
        self.SkirtLengthBox.setObjectName("SkirtLengthBox")
        self.ShirtDressSkirtLayout.addWidget(self.SkirtLengthBox, 1, 1, 1, 1)

        self.SleeveLengthBox = QtWidgets.QLineEdit()
        self.SleeveLengthBox.setAlignment(QtCore.Qt.AlignCenter)
        self.SleeveLengthBox.setObjectName("SleeveLengthBox")
        self.ShirtDressSkirtLayout.addWidget(self.SleeveLengthBox, 1, 7, 1, 1)

        self.AFLabel = QtWidgets.QLabel()
        self.AFLabel.setFont(SmallKhmerFont)
        self.AFLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AFLabel.setAutoFillBackground(False)
        self.AFLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AFLabel.setObjectName("AFLabel")
        self.ShirtDressSkirtLayout.addWidget(self.AFLabel, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        


        self.CenterBackLabel = QtWidgets.QLabel()
        self.CenterBackLabel.setFont(SmallKhmerFont)
        self.CenterBackLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CenterBackLabel.setAutoFillBackground(False)
        self.CenterBackLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CenterBackLabel.setObjectName("CenterBackLabel")
        self.ShirtDressSkirtLayout.addWidget(self.CenterBackLabel, 4, 0, 1, 1)

        self.BustHeightBox = QtWidgets.QLineEdit()
        self.BustHeightBox.setAlignment(QtCore.Qt.AlignCenter)
        self.BustHeightBox.setObjectName("BustHeightBox")
        self.ShirtDressSkirtLayout.addWidget(self.BustHeightBox, 5, 4, 1, 1)

        self.ShirtDressSkirtBox.setLayout(self.ShirtDressSkirtLayout)
        
        #pant group box     
        self.PantGroupBox = QtWidgets.QGroupBox()
        self.PantGroupBox.setGeometry(QtCore.QRect(940, 450, 320, 511))
        self.PantGroupBox.setObjectName("PantGroupBox")
        self.PantGroupBox.setFont(BigKhmerFont)

        self.PantGroupLayout = QtWidgets.QGridLayout()
        self.PantGroupLayout.setObjectName("PantGroupLayout")


        self.ThighLabel = QtWidgets.QLabel()
        self.ThighLabel.setFont(SmallKhmerFont)
        self.ThighLabel.setObjectName("ThighLabel")
        self.PantGroupLayout.addWidget(self.ThighLabel, 7, 0, 1, 1)

        self.OutseamLabel = QtWidgets.QLabel()
        self.OutseamLabel.setFont(SmallKhmerFont)
        self.OutseamLabel.setObjectName("OutseamLabel")
        self.PantGroupLayout.addWidget(self.OutseamLabel, 6, 0, 1, 1)

        self.CalfLabel = QtWidgets.QLabel()
        self.CalfLabel.setFont(SmallKhmerFont)
        self.CalfLabel.setObjectName("CalfLabel")
        self.PantGroupLayout.addWidget(self.CalfLabel, 8, 0, 1, 1)

        self.InseamLabel = QtWidgets.QLabel()
        self.InseamLabel.setFont(SmallKhmerFont)
        self.InseamLabel.setObjectName("InseamLabel")
        self.PantGroupLayout.addWidget(self.InseamLabel, 3, 0, 1, 1)
        self.InseamBox = QtWidgets.QLineEdit()
        self.InseamBox.setAlignment(QtCore.Qt.AlignCenter)
        self.InseamBox.setObjectName("InseamBox")
        self.PantGroupLayout.addWidget(self.InseamBox, 3, 1, 1, 1)
        

        self.OutseamBox = QtWidgets.QLineEdit()
        self.OutseamBox.setAlignment(QtCore.Qt.AlignCenter)
        self.OutseamBox.setObjectName("OutseamBox")
        self.PantGroupLayout.addWidget(self.OutseamBox, 6, 1, 1, 1)
        
        self.PantHipLabel = QtWidgets.QLabel()

        self.PantHipLabel.setFont(SmallKhmerFont)
        self.PantHipLabel.setObjectName("PantHipLabel")
        self.PantGroupLayout.addWidget(self.PantHipLabel, 2, 0, 1, 1)

        self.AnkleLabel = QtWidgets.QLabel()
        self.AnkleLabel.setFont(SmallKhmerFont)
        self.AnkleLabel.setObjectName("AnkleLabel")
        self.PantGroupLayout.addWidget(self.AnkleLabel, 9, 0, 1, 1)

        self.ThighBox = QtWidgets.QLineEdit()
        self.ThighBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ThighBox.setObjectName("ThighBox")
        self.PantGroupLayout.addWidget(self.ThighBox, 7, 1, 1, 1)
        
        self.PantWaistLabel = QtWidgets.QLabel()
        self.PantWaistLabel.setFont(SmallKhmerFont)
        self.PantWaistLabel.setObjectName("label")
        self.PantGroupLayout.addWidget(self.PantWaistLabel, 1, 0, 1, 1)

        self.PantHipBox = QtWidgets.QLineEdit()
        self.PantHipBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PantHipBox.setObjectName("PantHipBox")
        self.PantGroupLayout.addWidget(self.PantHipBox, 2, 1, 1, 1)

        self.AnkleBox = QtWidgets.QLineEdit()
        self.AnkleBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AnkleBox.setObjectName("AnkleBox")
        self.PantGroupLayout.addWidget(self.AnkleBox, 9, 1, 1, 1)

        self.CalfBox = QtWidgets.QLineEdit()
        self.CalfBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CalfBox.setObjectName("CalfBox")
        self.PantGroupLayout.addWidget(self.CalfBox, 8, 1, 1, 1)

        self.PantWaistBox = QtWidgets.QLineEdit()
        self.PantWaistBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PantWaistBox.setObjectName("PantWaistBox")
        self.PantGroupLayout.addWidget(self.PantWaistBox, 1, 1, 1, 1)

        self.CmInseam = QtWidgets.QLabel()
        self.CmInseam.setFont(ENGFont)
        self.CmInseam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmInseam.setAutoFillBackground(False)
        self.CmInseam.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmInseam.setObjectName("CmInseam")
        self.PantGroupLayout.addWidget(self.CmInseam, 3, 2, 1, 1)

        self.CmPantHip = QtWidgets.QLabel()
        self.CmPantHip.setFont(ENGFont)
        self.CmPantHip.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmPantHip.setAutoFillBackground(False)
        self.CmPantHip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmPantHip.setObjectName("CmPantHip")
        self.PantGroupLayout.addWidget(self.CmPantHip, 2, 2, 1, 1)
        
        self.CmPantWaist = QtWidgets.QLabel()
        self.CmPantWaist.setFont(ENGFont)
        self.CmPantWaist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmPantWaist.setAutoFillBackground(False)
        self.CmPantWaist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmPantWaist.setObjectName("CmPantWaist")
        self.PantGroupLayout.addWidget(self.CmPantWaist, 1, 2, 1, 1)

        self.CmOutseam = QtWidgets.QLabel()
        self.CmOutseam.setFont(ENGFont)
        self.CmOutseam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmOutseam.setAutoFillBackground(False)
        self.CmOutseam.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmOutseam.setObjectName("CmOutseam")
        self.PantGroupLayout.addWidget(self.CmOutseam, 6, 2, 1, 1)

        self.CmThigh = QtWidgets.QLabel()
        self.CmThigh.setFont(ENGFont)
        self.CmThigh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmThigh.setAutoFillBackground(False)
        self.CmThigh.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmThigh.setObjectName("CmThigh")
        self.PantGroupLayout.addWidget(self.CmThigh, 7, 2, 1, 1)
        
        self.CmCalf = QtWidgets.QLabel()
        self.CmCalf.setFont(ENGFont)
        self.CmCalf.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmCalf.setAutoFillBackground(False)
        self.CmCalf.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmCalf.setObjectName("CmCalf")
        self.PantGroupLayout.addWidget(self.CmCalf, 8, 2, 1, 1)
        
        self.CmAnkle = QtWidgets.QLabel()
        self.CmAnkle.setFont(ENGFont)
        self.CmAnkle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmAnkle.setAutoFillBackground(False)
        self.CmAnkle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmAnkle.setObjectName("CmAnkle")
        self.PantGroupLayout.addWidget(self.CmAnkle, 9, 2, 1, 1)

        self.PantGroupBox.setLayout(self.PantGroupLayout)


                
        #measurements group
        
        MainLayout.addWidget(self.ShirtDressSkirtBox, 2, 0)
        MainLayout.addWidget(self.PantGroupBox, 2, 1)
        
        '''
        END OF MEASUREMENTS BOX
        '''

        '''
        START OF PREVIEW
        '''
        
        self.PreviewGroupBox = QtWidgets.QGroupBox()
        self.PreviewGroupBox.setFont(BigKhmerFont)
        self.PreviewGroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PreviewGroupBox.setObjectName("PreviewGroupBox")


        self.RadioGroupBoxLayout = QtWidgets.QHBoxLayout()

        self.ShirtRadio = QtWidgets.QRadioButton()
        self.ShirtRadio.setFont(SmallKhmerFont)
        
        self.ShirtRadio.setObjectName("ShirtRadio")

        self.DressRadio = QtWidgets.QRadioButton()
        self.DressRadio.setFont(SmallKhmerFont)
        
        self.DressRadio.setObjectName("DressRadio")

        self.PantRadio = QtWidgets.QRadioButton()
        self.PantRadio.setFont(SmallKhmerFont)
        
        self.PantRadio.setObjectName("PantRadio")

        self.SkirtRadio = QtWidgets.QRadioButton()
        self.SkirtRadio.setFont(SmallKhmerFont)
        
        self.SkirtRadio.setObjectName("SkirtRadio")
        
        self.RadioGroupBoxLayout.addWidget(self.ShirtRadio)
        self.RadioGroupBoxLayout.addWidget(self.DressRadio)
        self.RadioGroupBoxLayout.addWidget(self.PantRadio)
        self.RadioGroupBoxLayout.addWidget(self.SkirtRadio)

        

        self.PreviewGroupLayout = QtWidgets.QVBoxLayout()


        #add widgets for 4 pictures
        self.RadioPicLabel = QtWidgets.QLabel()
        self.RadioPicLabel.setMaximumSize(621, 531)
        self.RadioPicLabel.setStyleSheet("\n""image: url(:/newPrefix/skirt.jpg);")
        self.RadioPicLabel.setObjectName("RadioPicLabel")

        self.PreviewGroupLayout.addLayout(self.RadioGroupBoxLayout)
        self.PreviewGroupLayout.addWidget(self.RadioPicLabel)


        PriceLayout = QHBoxLayout()

        self.PriceBox = QtWidgets.QLineEdit()
        self.PriceBox.setMaximumSize(300, 50)
        self.onlyInt = QtGui.QIntValidator()
        self.PriceBox.setValidator(self.onlyInt)
        self.PriceBox.setFont(ENGFont)
        self.PriceBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PriceBox.setAutoFillBackground(False)
        self.PriceBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PriceBox.setObjectName("PriceBox")

    
        self.PriceLabel = QtWidgets.QLabel()
        self.PriceLabel.setMaximumSize(50,50)
        self.PriceLabel.setFont(BigKhmerFont)
        self.PriceLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PriceLabel.setAutoFillBackground(False)
        self.PriceLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PriceLabel.setObjectName("PriceLabel")

        PriceLayout.addWidget(self.PriceLabel)
        PriceLayout.addWidget(self.PriceBox)

        self.PreviewGroupLayout.addLayout(PriceLayout)

        ''' START OF Submit & Cancel '''
        SubmitCancelLayout = QHBoxLayout()

        self.Cancel = QtWidgets.QPushButton()
        self.Cancel.setMaximumSize(130, 50)
        self.Cancel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Cancel.setAutoFillBackground(False)
        self.Cancel.setFont(SmallKhmerFont)
        self.Cancel.setObjectName("Cancel")

        self.Submit = QtWidgets.QPushButton()
        self.Submit.setMaximumSize(100, 50)
        self.Submit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Submit.setAutoFillBackground(False)
        self.Submit.setFont(SmallKhmerFont)
        self.Submit.setObjectName("Submit")

        SubmitCancelLayout.addWidget(self.Cancel)
        SubmitCancelLayout.addWidget(self.Submit)

        self.PreviewGroupLayout.addLayout(SubmitCancelLayout)

        self.SubmitMsg = QtWidgets.QLabel()
        self.SubmitMsg.setMaximumSize(400, 40)
        self.SubmitMsg.setFont(BigKhmerFont)
        self.SubmitMsg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SubmitMsg.setAutoFillBackground(False)

        self.PreviewGroupLayout.addWidget(self.SubmitMsg)

        ''' END OF Submit & Cancel '''


        self.PreviewGroupBox.setLayout(self.PreviewGroupLayout)
        




        #preview group 
        MainLayout.addWidget(self.PreviewGroupBox, 0, 2, 3, 2)

        
       

        


        #column strech
        MainLayout.setColumnStretch(0,1)
        MainLayout.setRowStretch(2, 3)
        MainLayout.setColumnStretch(1,2)
        MainLayout.setColumnStretch(2,3)
        MainLayout.setSpacing(10)

        widget = QWidget()
        
        #self.retranslateUi()
        
        #set layout 
        widget.setLayout(MainLayout)
        self.setCentralWidget(widget)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.StaffTitle.setText(_translate("MainWindow", "ព័ត៌មានបុគ្គលិក"))
        self.PhoneLabel.setText(_translate("MainWindow", "លេខទូរស័ព្ទ:"))
        self.DeadlineLabel.setText(_translate("MainWindow", "កាលកំណត់:"))
        self.MeasurementTitle.setText(_translate("MainWindow", "ការវាស់វែងអតិថិជន"))
        self.CustomerInfoTitle.setText(_translate("MainWindow", "ព័ត៌មានអតិថិជន"))
        self.ColorLabel.setText(_translate("MainWindow", "ពណ៌:"))
        self.StaffNameLabel.setText(_translate("MainWindow", "ឈ្មោះ:"))
        self.StyleLabel.setText(_translate("MainWindow", "រចនាបទ:"))
        self.MaterialsLabel.setText(_translate("MainWindow", "ប្រភេទក្រណាត់:"))
        self.AddressLabel.setText(_translate("MainWindow", "ឤស័យដ្ឋាន:"))
        self.CustomerNameLabel.setText(_translate("MainWindow", "ឈ្មោះ:"))
        self.CustomerPreferencesTitle.setText(_translate("MainWindow", "ជម្រើសអតិថិជន"))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))
        self.Submit.setText(_translate("MainWindow", "OK"))
        self.PriceBox.setText(_translate("MainWindow", ""))
        self.PriceLabel.setText(_translate("MainWindow", "តម្លៃ: ($)"))
        self.ShirtDressSkirtBox.setTitle(_translate("MainWindow", "អាវ រ៉ូប​ និងសំពត់"))
        self.DressSkirtWaistLabel.setText(_translate("MainWindow", "ជំុវិញចង្កេះ:"))
        self.CmUpperHips.setText(_translate("MainWindow", "cm"))
        self.UpperHipsLabel.setText(_translate("MainWindow", "ជំុវិញត្រគៀកអាវ:"))
        self.CmAroundBust.setText(_translate("MainWindow", "cm"))
        self.HipLabel.setText(_translate("MainWindow", "ត្រគៀកសំពត់:"))
        self.CmCenterFront.setText(_translate("MainWindow", "cm"))
        self.CmNeckArmHold.setText(_translate("MainWindow", "cm"))
        self.NeckArmHoldLabel.setText(_translate("MainWindow", "ជំុវិញកអាវ:"))
        self.CmAB.setText(_translate("MainWindow", "cm"))
        self.CmHip.setText(_translate("MainWindow", "cm"))
        self.CmBustHeight.setText(_translate("MainWindow", "cm"))
        self.CmAboveBust.setText(_translate("MainWindow", "cm"))
        self.CmSkirtLength.setText(_translate("MainWindow", "cm"))
        self.CmAF.setText(_translate("MainWindow", "cm"))
        self.CmShoulder.setText(_translate("MainWindow", "cm"))
        self.ShoulderLabel.setText(_translate("MainWindow", "ស្មា:"))
        self.CmCenterBack.setText(_translate("MainWindow", "cm"))
        self.CenterFrontLabel.setText(_translate("MainWindow", "គល់កមុខដល់\nចង្កេះ:"))
        self.CmDressSkirtWaist.setText(_translate("MainWindow", "cm"))
        self.SleeveLengthLabel.setText(_translate("MainWindow", "សំរុងដៃអាវ:"))
        self.CmSleeveLength.setText(_translate("MainWindow", "cm"))
        self.AboveBustLabel.setText(_translate("MainWindow", "ទ្រូងលើ:"))
        self.CmArmPit.setText(_translate("MainWindow", "cm"))
        self.ArmpitLabel.setText(_translate("MainWindow", "រង្វងគល់ក្លៀក:"))
        self.ABLabel.setText(_translate("MainWindow", "សន្ទះក្រោយ:"))
        self.AroundBustLabel.setText(_translate("MainWindow", "ជំុវិញទ្រូង:"))
        self.BustHeightLabel.setText(_translate("MainWindow", "កំពស់ដើមទ្រូង:"))
        self.SkirtLengthLabel.setText(_translate("MainWindow", "សំរុងសំពត់:"))
        self.AFLabel.setText(_translate("MainWindow", "សន្ទះមុខ:"))
        self.CenterBackLabel.setText(_translate("MainWindow", "គល់កក្រោយ\nដល់ចង្កេះ:"))
        self.SpecialReqTitle.setText(_translate("MainWindow", "សំណើពិសេស"))
        self.PreviewGroupBox.setTitle(_translate("MainWindow", "រូបគំរូ"))
        self.ShirtRadio.setText(_translate("MainWindow", "អាវ"))
        self.DressRadio.setText(_translate("MainWindow", "រ៉ូប"))
        self.PantRadio.setText(_translate("MainWindow", "ខោ"))
        self.SkirtRadio.setText(_translate("MainWindow", "សំពត់"))        
        self.PantGroupBox.setTitle(_translate("MainWindow", "ខោ"))
        self.ThighLabel.setText(_translate("MainWindow", "ទំហំភ្លៅ:"))
        self.OutseamLabel.setText(_translate("MainWindow", "សំរុងខោ:"))
        self.CalfLabel.setText(_translate("MainWindow", "កំភួនជើង:"))
        self.InseamLabel.setText(_translate("MainWindow", "សំរុងក្រលាន:"))
        self.PantHipLabel.setText(_translate("MainWindow", "ជំុវិញត្រកៀកខោ:"))
        self.AnkleLabel.setText(_translate("MainWindow", "កជើង:"))
        self.PantWaistLabel.setText(_translate("MainWindow", "ជុំវិញចង្កេះ:"))
        self.CmInseam.setText(_translate("MainWindow", "cm"))
        self.CmPantHip.setText(_translate("MainWindow", "cm"))
        self.CmPantWaist.setText(_translate("MainWindow", "cm"))
        self.CmOutseam.setText(_translate("MainWindow", "cm"))
        self.CmThigh.setText(_translate("MainWindow", "cm"))
        self.CmCalf.setText(_translate("MainWindow", "cm"))
        self.CmAnkle.setText(_translate("MainWindow", "cm"))
        self.DeadlineSelectedLabel.setText(_translate("MainWindow", 'សូមចុចរូបប្រតិទិន'))
        self.DeadlineSelectedLabel.setStyleSheet("color: black; background-color: #d7dbdd ")
        self.SubmitMsg.setText(_translate("MainWindow", ""))
        

        #menu buttons
        #self.ActionNewOrder.setText(_translate("MainWindow", "កម្មង់ថ្មី"))
        #self.ActionAbout.setText(_translate("MainWindow", "អំពីកម្មវិធី"))
        #self.ActionViewAllOrders.setText(_translate("MainWindow", "មើលការកម្មង់ទាំងអស់"))
    



        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())