from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import calendar
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from connection import connection, cursor, close_connection
import picture
from psycopg2.extensions import AsIs
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
import sys
import shutil 
import os

__version__ = '1.0'
__author__ = 'Chhaikheang Sok & Panha Teng'

'''
START OF Font FORMATTING
'''

SmallKhmerFont = QtGui.QFont()
SmallKhmerFont.setFamily("Khmer OS New")
SmallKhmerFont.setPointSize(11)

BigKhmerFont = QtGui.QFont()
BigKhmerFont.setBold(True)
BigKhmerFont.setFamily("Khmer OS New")
BigKhmerFont.setPointSize(12)

ENGFont = QtGui.QFont()
ENGFont.setFamily("Palatino Linotype")
ENGFont.setPointSize(15)


'''
END OF Font FORMATTING
'''


class Ui_MainWindow(object):

    #class variables for setting control flow to add to database
    #DO NOT MOVE
    complete_input = 0 #tells when all required inputs are completed by user
    added_customer = 0 #tells when successfully added customer
    added_order = 0 #tells when successfully added order
    added_material = 0  #tells when successfully added material
    added_measurements = 0 #tells when successfully added measurements
    clothes_type = "អាវ" #tell which clothes type is selected by user
    updating = 0 #tell when order is being edited
    customer_id = 0 #store customer id 
    uploaded_pictures_dir_list = [] #list to add photo directories
    new_pic_added_in_edit_list = [] #tell index of new photo to copy to local database folder
    selected_pic = 0 #tell which photo is selected for viewing

    def setupUi(self, MainWindow):

        ''' 
        this function inherits from MainWindow class
        and UI is setup
        '''

        '''
        START OF MAIN WINDOW
        '''
        MainWindow.setWindowTitle("Tailor Management System")
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
        self.CustomerNameLabel.setStyleSheet("background-color: #B2E2F2")

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
        self.CustomerNameBox.setStyleSheet("background-color: white; border: 1px solid blue;")

        self.PhoneBox = QtWidgets.QLineEdit()
        self.PhoneBox.setMaximumSize(300, 50)
        self.PhoneBox.setFont(SmallKhmerFont)
        self.onlyInt = QtGui.QIntValidator()
        self.PhoneBox.setValidator(self.onlyInt)
        self.PhoneBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PhoneBox.setObjectName("PhoneBox")
        self.PhoneBox.setStyleSheet("background-color: white; border: 1px solid blue;")
        
        self.AddressBox = QtWidgets.QPlainTextEdit()
        self.AddressBox.setMaximumSize(300, 50)
        self.AddressBox.setFont(SmallKhmerFont)
        self.AddressBox.setObjectName("AddressBox")
        self.AddressBox.setStyleSheet("background-color: white; border: 1px solid blue;")


        '''
        add to main layout
        '''

        #customer box
        self.CustomerBoxGroup = QtWidgets.QGroupBox()
        self.CustomerBoxGroup.setStyleSheet("background-color: #B8E2F2;")
        self.CustomerBoxGroup.setMaximumSize(550, 400)
        
        CustomerBoxLayout = QGridLayout()

        CustomerBoxLayout.addWidget(self.CustomerInfoTitle, 0, 0, 1, 1)
        
        CustomerBoxLayout.addWidget(self.CustomerNameLabel, 1, 0)
        CustomerBoxLayout.addWidget(self.PhoneLabel, 2, 0)
        CustomerBoxLayout.addWidget(self.AddressLabel, 3, 0)
        

        CustomerBoxLayout.addWidget(self.CustomerNameBox, 1, 1)
        CustomerBoxLayout.addWidget(self.PhoneBox, 2, 1)
        CustomerBoxLayout.addWidget(self.AddressBox, 3, 1)

        self.CustomerBoxGroup.setLayout(CustomerBoxLayout)

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
        self.DateIcon.setIcon(QtGui.QIcon('icon/calendar.png'))
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
        self.StaffNameBox.setStyleSheet("background-color: white; border: 1px solid blue;")

        #label to show date chosen
        self.DeadlineSelectedLabel = QtWidgets.QLabel()
        self.DeadlineSelectedLabel.setMaximumSize(300,50)
        self.DeadlineSelectedLabel.setFont(SmallKhmerFont)
        self.DeadlineSelectedLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DeadlineSelectedLabel.setAutoFillBackground(True)
        self.DeadlineSelectedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DeadlineSelectedLabel.setObjectName("DeadlineSelectedLabel")

        #label to send date to database
        #not in Ui
        self.DeadlineBox = QtWidgets.QLabel()
        self.DeadlineBox.setMaximumSize(0,0) 
        self.DeadlineBox.setFont(SmallKhmerFont)
        self.DeadlineBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DeadlineBox.setAutoFillBackground(False)
        self.DeadlineBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DeadlineBox.setObjectName("DeadlineBox")
        #not in Ui

        #staff box 
        self.StaffBoxGroup = QtWidgets.QGroupBox()
        self.StaffBoxGroup.setMaximumSize(550,400)
        self.StaffBoxGroup.setStyleSheet("background-color: #B8E2F2; ")

        StaffBoxLayout = QGridLayout()
        
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
        self.MaterialsLabel.setMaximumSize(110,50)
        self.MaterialsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MaterialsLabel.setAutoFillBackground(False)
        self.MaterialsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MaterialsLabel.setObjectName("MaterialsLabel")

        #user inputs
        self.MaterialBox = QtWidgets.QLineEdit()
        self.MaterialBox.setFont(SmallKhmerFont)
        self.MaterialBox.setMaximumSize(300,50)
        self.MaterialBox.setObjectName("MaterialBox")
        self.MaterialBox.setStyleSheet("background-color: white; border: 1px solid blue;")

        self.ColorBox = QtWidgets.QLineEdit()
        self.ColorBox.setFont(SmallKhmerFont)
        self.ColorBox.setMaximumSize(300,50)
        self.ColorBox.setObjectName("ColorBox")
        self.ColorBox.setStyleSheet("background-color: white; border: 1px solid blue;")

        self.StyleBox = QtWidgets.QLineEdit()
        self.StyleBox.setFont(SmallKhmerFont)
        self.StyleBox.setMaximumSize(300,50)
        self.StyleBox.setObjectName("StyleBox")
        self.StyleBox.setStyleSheet("background-color: white; border: 1px solid blue;")

    
        #preferences box
        self.PreferencesBoxGroup = QtWidgets.QGroupBox()
        self.PreferencesBoxGroup.setMaximumSize(550,400)
        self.PreferencesBoxGroup.setStyleSheet("background-color: #B8E2F2; ")

        PreferencesBoxLayout = QGridLayout()

        PreferencesBoxLayout.addWidget(self.CustomerPreferencesTitle, 0, 0)

        PreferencesBoxLayout.addWidget(self.MaterialsLabel, 1, 0)
        PreferencesBoxLayout.addWidget(self.ColorLabel, 2, 0)
        PreferencesBoxLayout.addWidget(self.StyleLabel, 3, 0)

        PreferencesBoxLayout.addWidget(self.MaterialBox, 1, 1)
        PreferencesBoxLayout.addWidget(self.ColorBox, 2, 1)
        PreferencesBoxLayout.addWidget(self.StyleBox, 3, 1)

        self.PreferencesBoxGroup.setLayout(PreferencesBoxLayout)

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
        self.SpecialReqBox.setStyleSheet("background-color: white; border: 1px solid blue;")

        #special req box
        
        self.SpecReqBoxGroup = QtWidgets.QGroupBox()
        self.SpecReqBoxGroup.setStyleSheet("background-color: #B8E2F2; ")

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
        self.ShirtDressSkirtLayout.addWidget(self.NeckArmHoldBox, 1, 7, 1, 1)
        
        self.WaistBox = QtWidgets.QLineEdit()
        self.WaistBox.setAlignment(QtCore.Qt.AlignCenter)
        self.WaistBox.setObjectName("WaistBox")
        self.ShirtDressSkirtLayout.addWidget(self.WaistBox, 0, 7, 1, 1)

        self.ABBox = QtWidgets.QLineEdit()
        self.ABBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ABBox.setObjectName("ABBox")
        self.ShirtDressSkirtLayout.addWidget(self.ABBox, 0, 4, 1, 1)

        self.DressSkirtWaistLabel = QtWidgets.QLabel()
        self.DressSkirtWaistLabel.setObjectName("DressSkirtWaistLabel")
        self.DressSkirtWaistLabel.setFont(SmallKhmerFont)
        self.ShirtDressSkirtLayout.addWidget(self.DressSkirtWaistLabel, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)


        self.UpperHipsLabel = QtWidgets.QLabel()
        self.UpperHipsLabel.setFont(SmallKhmerFont)
        self.UpperHipsLabel.setObjectName("UpperHipsLabel")
        self.ShirtDressSkirtLayout.addWidget(self.UpperHipsLabel, 5, 6, 1, 1)
        
        self.CmUpperHips = QtWidgets.QLabel()
        self.CmUpperHips.setFont(ENGFont)
        self.CmUpperHips.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmUpperHips.setAutoFillBackground(False)
        self.CmUpperHips.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmUpperHips.setObjectName("CmUpperHips")
        self.ShirtDressSkirtLayout.addWidget(self.CmUpperHips, 5, 8, 1, 1)



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
        self.ShirtDressSkirtLayout.addWidget(self.CmNeckArmHold, 1, 8, 1, 1)


        self.NeckArmHoldLabel = QtWidgets.QLabel()
        self.NeckArmHoldLabel.setFont(SmallKhmerFont)
        self.NeckArmHoldLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NeckArmHoldLabel.setAutoFillBackground(False)
        self.NeckArmHoldLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NeckArmHoldLabel.setObjectName("NeckArmHoldLabel")
        self.ShirtDressSkirtLayout.addWidget(self.NeckArmHoldLabel, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)
        
        
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
        self.ShirtDressSkirtLayout.addWidget(self.CmAF, 1, 5, 1, 1,)


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
        self.ShirtDressSkirtLayout.addWidget(self.CmDressSkirtWaist, 0, 8, 1, 1)


        self.SleeveLengthLabel = QtWidgets.QLabel()
        self.SleeveLengthLabel.setFont(SmallKhmerFont)
        self.SleeveLengthLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SleeveLengthLabel.setAutoFillBackground(False)
        self.SleeveLengthLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SleeveLengthLabel.setObjectName("SleeveLengthLabel")
        self.ShirtDressSkirtLayout.addWidget(self.SleeveLengthLabel, 4, 6, 1, 1, QtCore.Qt.AlignHCenter)


        self.CmSleeveLength = QtWidgets.QLabel()
        self.CmSleeveLength.setFont(ENGFont)
        self.CmSleeveLength.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CmSleeveLength.setAutoFillBackground(False)
        self.CmSleeveLength.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CmSleeveLength.setObjectName("CmSleeveLength")
        self.ShirtDressSkirtLayout.addWidget(self.CmSleeveLength, 4, 8, 1, 1)

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
        self.ShirtDressSkirtLayout.addWidget(self.CmArmPit, 3, 8, 1, 1)

        self.ArmpitLabel = QtWidgets.QLabel()
        self.ArmpitLabel.setFont(SmallKhmerFont)
        self.ArmpitLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ArmpitLabel.setAutoFillBackground(False)
        self.ArmpitLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ArmpitLabel.setObjectName("ArmpitLabel")
        self.ShirtDressSkirtLayout.addWidget(self.ArmpitLabel, 3, 6, 1, 1, QtCore.Qt.AlignHCenter)



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
        self.ShirtDressSkirtLayout.addWidget(self.AFBox, 1, 4, 1, 1,)
    
        self.CenterBackBox = QtWidgets.QLineEdit()
        self.CenterBackBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CenterBackBox.setObjectName("CenterBackBox")
        self.ShirtDressSkirtLayout.addWidget(self.CenterBackBox, 4, 1, 1, 1)
        

        self.UpperHipsBox = QtWidgets.QLineEdit()
        self.UpperHipsBox.setAlignment(QtCore.Qt.AlignCenter)
        self.UpperHipsBox.setObjectName("UpperHipsBox")
        self.ShirtDressSkirtLayout.addWidget(self.UpperHipsBox, 5, 7, 1, 1)

        self.ArmpitBox = QtWidgets.QLineEdit()
        self.ArmpitBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ArmpitBox.setObjectName("ArmpitBox")
        self.ShirtDressSkirtLayout.addWidget(self.ArmpitBox, 3, 7, 1, 1)

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
        self.ShirtDressSkirtLayout.addWidget(self.SleeveLengthBox, 4, 7, 1, 1)

        self.AFLabel = QtWidgets.QLabel()
        self.AFLabel.setFont(SmallKhmerFont)
        self.AFLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AFLabel.setAutoFillBackground(False)
        self.AFLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AFLabel.setObjectName("AFLabel")
        self.ShirtDressSkirtLayout.addWidget(self.AFLabel, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        
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
        self.PreviewGroupBox.setStyleSheet("background-color: #B8E2F2")


        self.RadioGroupBoxLayout = QtWidgets.QHBoxLayout()

        self.ShirtRadio = QtWidgets.QRadioButton()
        self.ShirtRadio.setFont(SmallKhmerFont)
        self.ShirtRadio.setChecked(True)
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

        #layout for picture and delete button
        self.PictureAndDeleteLayout = QHBoxLayout()

        #add widgets for 4 pictures
        self.RadioPicLabel = QtWidgets.QLabel()
        self.RadioPicLabel.setMaximumSize(800, 600)
        self.RadioPicLabel.setObjectName("RadioPicLabel")
        
        #default settings for picture preview
        self.RadioPicLabel.setStyleSheet("image: url(:/newPrefix/shirt.jpg);background-color: #B2E2F2; margin: 0 30% 0 30%")
        self.RadioPicLabel.setScaledContents(True)
        self.InseamBox.setReadOnly(True)
        self.InseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.OutseamBox.setReadOnly(True)
        self.OutseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.ThighBox.setReadOnly(True)
        self.ThighBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.PantHipBox.setReadOnly(True)
        self.PantHipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.AnkleBox.setReadOnly(True)
        self.AnkleBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.CalfBox.setReadOnly(True)
        self.CalfBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.PantWaistBox.setReadOnly(True)
        self.PantWaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.SkirtLengthBox.setReadOnly(True)
        self.SkirtLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.HipBox.setReadOnly(True)
        self.HipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")


        self.PreviewGroupLayout.addLayout(self.RadioGroupBoxLayout)


        self.DeletePictureShownButton = QtWidgets.QPushButton()
        self.DeletePictureShownButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.DeletePictureShownButton.setAutoFillBackground(False)
        self.DeletePictureShownButton.setObjectName("DeletePictureShownButton")
        self.DeletePictureShownButton.setIcon(QtGui.QIcon('icon/delete.png'))
        size = QtCore.QSize(25, 25)
        self.DeletePictureShownButton.setIconSize(size)
        self.DeletePictureShownButton.setMaximumSize(size)


        self.PreviewGroupLayout.addWidget(self.DeletePictureShownButton)
        self.PreviewGroupLayout.addWidget(self.RadioPicLabel)
        

        #uploads group
        self.UploadGroupLayout = QtWidgets.QHBoxLayout()
        
        self.Upload = QtWidgets.QPushButton()
        self.Upload.setMaximumSize(130, 50)
        self.Upload.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Upload.setAutoFillBackground(False)
        self.Upload.setFont(SmallKhmerFont)
        self.Upload.setObjectName("Upload")
        self.Upload.setStyleSheet("background-color: white; border: 1px solid blue;")

        self.UploadButtonOne = UploadPreviewButton()
        self.UploadButtonOne.setObjectName('UploadButtonOne')

        self.UploadButtonTwo = UploadPreviewButton()
        self.UploadButtonTwo.setObjectName('UploadButtonTwo')

        self.UploadButtonThree = UploadPreviewButton()
        self.UploadButtonThree.setObjectName('UploadButtonThree')

        self.UploadButtonFour = UploadPreviewButton()
        self.UploadButtonFour.setObjectName('UploadButtonFour')

        
        self.UploadGroupFourButtons = QGroupBox()
        self.UploadGroupFourButtons.setMaximumSize(300,60)

        UploadGroupFourButtonsLayout = QHBoxLayout()
        
        UploadGroupFourButtonsLayout.addWidget(self.UploadButtonOne)
        UploadGroupFourButtonsLayout.addWidget(self.UploadButtonTwo)
        UploadGroupFourButtonsLayout.addWidget(self.UploadButtonThree)
        UploadGroupFourButtonsLayout.addWidget(self.UploadButtonFour)
        
        self.UploadGroupFourButtons.setLayout(UploadGroupFourButtonsLayout)
        
        self.UploadButtonOne.clicked.connect(self.select_upload_pic)
        self.UploadButtonTwo.clicked.connect(self.select_upload_pic)
        self.UploadButtonThree.clicked.connect(self.select_upload_pic)
        self.UploadButtonFour.clicked.connect(self.select_upload_pic)
    
        self.UploadGroupLayout.addWidget(self.Upload)
        self.UploadGroupLayout.addWidget(self.UploadGroupFourButtons)
        
        self.PreviewGroupLayout.addLayout(self.UploadGroupLayout)

        PriceLayout = QHBoxLayout()

        self.PriceBox = QtWidgets.QLineEdit()
        self.PriceBox.setMaximumSize(300, 50)
        self.PriceBox.setValidator(self.onlyInt)
        self.PriceBox.setFont(ENGFont)
        self.PriceBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PriceBox.setAutoFillBackground(False)
        self.PriceBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PriceBox.setObjectName("PriceBox")
        self.PriceBox.setStyleSheet("background-color: white; border: 1px solid blue;")

    
        self.PriceLabel = QtWidgets.QLabel()
        self.PriceLabel.setMaximumSize(120,50)
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
        self.Cancel.setStyleSheet("background-color: white; border: 1px solid blue;")

        self.Submit = QtWidgets.QPushButton()
        self.Submit.setMaximumSize(160, 50)
        self.Submit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Submit.setAutoFillBackground(False)
        self.Submit.setFont(SmallKhmerFont)
        self.Submit.setObjectName("Submit")
        self.Submit.setStyleSheet("background-color: white; border: 1px solid blue;")

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
        
        '''
        END OF PREVIEW 
        '''



        #preview group 
        MainLayout.addWidget(self.PreviewGroupBox, 0, 2, 3, 2)

        
        #column streches
        MainLayout.setColumnStretch(0,1)
        MainLayout.setRowStretch(2, 3)
        MainLayout.setColumnStretch(1,2)
        MainLayout.setColumnStretch(2,3)
        MainLayout.setSpacing(10)

        widget = QWidget()
        
        #set layout 
        widget.setLayout(MainLayout)
        MainWindow.setCentralWidget(widget)


        #menu bar

        #actions in menubar
        self.ActionNewOrder = QtWidgets.QAction(MainWindow)
        self.ActionNewOrder.setObjectName("ActionNewOrder")
        self.ActionNewOrder.setFont(SmallKhmerFont)
        
        self.ActionViewAllOrders = QtWidgets.QAction(MainWindow)
        self.ActionViewAllOrders.setObjectName("ActionViewAllOrders")
        self.ActionViewAllOrders.setFont(SmallKhmerFont)
        
        self.ActionAbout = QtWidgets.QAction(MainWindow)
        self.ActionAbout.setObjectName("ActionAbout")
        self.ActionAbout.setFont(SmallKhmerFont)
        self.ActionAbout = QtWidgets.QAction(MainWindow)
        
        #create menubar

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 20))
        self.menubar.setObjectName("menubar")
        self.menubar.setFont(SmallKhmerFont)
            
        #add actions to menubar

        self.menubar.addAction(self.ActionNewOrder)
        self.menubar.addAction(self.ActionViewAllOrders)
        self.menubar.addAction(self.ActionAbout)
        
        #put menubar into main window
        MainWindow.setMenuBar(self.menubar)



        '''
        START OF connect slots and signals for Ui 
        '''
        #date selection 
        self.DateIcon.clicked.connect(self.EditDate)

        #connect radio buttons and pictures
        self.ShirtRadio.toggled.connect(self.select_pic)
        self.DressRadio.toggled.connect(self.select_pic)
        self.PantRadio.toggled.connect(self.select_pic)
        self.SkirtRadio.toggled.connect(self.select_pic)
        
        #open view all orders dialog
        self.ActionViewAllOrders.triggered.connect(self.ViewAllOrders)
        '''
        END OF connect slots and signals
        '''
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def ShowUploadPic(self): 
        
        '''shows last uploaded picture in radiopiclabel'''

        NumPicUploaded = len(self.uploaded_pictures_dir_list)
        
        if NumPicUploaded > 0: 
            orig_pixmap = QPixmap(self.uploaded_pictures_dir_list[NumPicUploaded - 1])
            pixmap_resized = orig_pixmap.scaled(self.RadioPicLabel.width(), self.RadioPicLabel.height(), QtCore.Qt.KeepAspectRatio)
            self.RadioPicLabel.setStyleSheet("background-color: #B2E2F2; margin: 0 30% 0 30%")
            self.RadioPicLabel.setPixmap(pixmap_resized)

            self.selected_pic = NumPicUploaded - 1
        elif NumPicUploaded == 0:
            pass 

    def SetUploadPreview(self): 
        
        '''shows small picture previews in 4 boxes below radiopiclabel'''

        #find len of list of destinations
        NumPicUploaded = len(self.uploaded_pictures_dir_list)

        #set previews
            
        if NumPicUploaded >= 1: 
            #set upload preview in button 1
            self.UploadButtonOne.setIcon(QtGui.QIcon(self.uploaded_pictures_dir_list[0]))
        
        if NumPicUploaded >= 2:
            self.UploadButtonTwo.setIcon(QtGui.QIcon(self.uploaded_pictures_dir_list[1]))

        if NumPicUploaded >= 3:
            self.UploadButtonThree.setIcon(QtGui.QIcon(self.uploaded_pictures_dir_list[2]))

        if NumPicUploaded == 4:   
            self.UploadButtonFour.setIcon(QtGui.QIcon(self.uploaded_pictures_dir_list[3]))
            

    def select_upload_pic(self): 
        
        '''displays picture when a preview icon is clicked'''

        Button = self.UploadGroupFourButtons.sender()
        Button = Button.objectName()

        num_pic_uploaded = len(self.uploaded_pictures_dir_list)

        if  num_pic_uploaded == 0 : 
            pass
        else: 
            if (Button == 'UploadButtonOne' and num_pic_uploaded >= 1) : 

                self.show_pic_preview(pic_num = 0)

                #index for delete
                self.selected_pic = 0
            
            elif (Button == 'UploadButtonTwo'and num_pic_uploaded >= 2): 
                
                self.show_pic_preview(pic_num = 1)

                #index for delete
                self.selected_pic = 1

            elif (Button == 'UploadButtonThree' and num_pic_uploaded >= 3):
                
                self.show_pic_preview(pic_num = 2)

                #index for delete
                self.selected_pic = 2

            elif (Button == 'UploadButtonFour'and num_pic_uploaded == 4):  
                
                self.show_pic_preview(pic_num = 3)

                #index for delete
                self.selected_pic = 3
    

    def DeleteUploadPicMain(self): 
        
        '''this is the main function that calls the another function (controller function) to delete selected picture'''

        num_pic_uploaded = len(self.uploaded_pictures_dir_list)
        print(num_pic_uploaded)
        if  num_pic_uploaded == 0 : 
            pass
        else: 
            
            PicNum = self.selected_pic
            
            if PicNum == 0 : 
                self.DeleteUploadPicController(PicNum=PicNum,PicDir=self.uploaded_pictures_dir_list[PicNum])
            
            elif PicNum == 1: 
                self.DeleteUploadPicController(PicNum=PicNum,PicDir=self.uploaded_pictures_dir_list[PicNum])

            elif PicNum == 2:
                self.DeleteUploadPicController(PicNum=PicNum,PicDir=self.uploaded_pictures_dir_list[PicNum])

            elif PicNum == 3:  
                self.DeleteUploadPicController(PicNum=PicNum,PicDir=self.uploaded_pictures_dir_list[PicNum])
    
    def DeleteUploadPicController(self, PicNum, PicDir): 

        '''this is the controller function to manage flow of program when user deletes a picture they selected'''

        #delete from database if in edit mode and clicked submit
        if (self.updating == 1): 
            pic_dir = self.uploaded_pictures_dir_list[PicNum]
            DeleteUploadPic(pic_dir, self.customer_id)

            #delete local pictures
            try: 
                os.remove(self.uploaded_pictures_dir_list[PicNum])
                print("% s removed successfully" % self.uploaded_pictures_dir_list[PicNum]) 
            except OSError as error: 
                print(error) 
                print("File path can not be removed") 
        
        #delete from list of directories
        self.uploaded_pictures_dir_list.remove(self.uploaded_pictures_dir_list[PicNum])

        #reset views

        #reset icon to default
        self.reset_icon()

        #reset preview icons according to remaining pictures
        self.SetUploadPreview()

        #reset picture preview as 1st picture
        self.show_pic_preview(pic_num=0)
        
        #reset selected pic to 1st pic or reset to default img
        if len(self.uploaded_pictures_dir_list) >= 1:
            self.selected_pic = 0
        else: 
            #self.ResetRadioButtons()
            #cannot reset button => mess up tyype of clothes in edit
            pass

            
    def reset_icon(self): 

        '''reset picture icons to default icon picture'''

        self.UploadButtonOne.setIcon(QtGui.QIcon('icon/shirt-icon.png'))
        self.UploadButtonTwo.setIcon(QtGui.QIcon('icon/shirt-icon.png'))
        self.UploadButtonThree.setIcon(QtGui.QIcon('icon/shirt-icon.png'))
        self.UploadButtonFour.setIcon(QtGui.QIcon('icon/shirt-icon.png'))


    def show_pic_preview(self, pic_num): 
        
        '''
        this function takes in the index of the picture that is selected and shows it in radiopiclabel. 
        If no picture exists, a blank radiopiclabel is shown. 
        '''

        if len(self.uploaded_pictures_dir_list) > 0: 

            orig_pixmap = QPixmap(self.uploaded_pictures_dir_list[pic_num])
            pixmap_resized = orig_pixmap.scaled(self.RadioPicLabel.width(), self.RadioPicLabel.height(), QtCore.Qt.KeepAspectRatio)
            self.RadioPicLabel.setPixmap(pixmap_resized)

        #make radiopiclabel transparent if there are no pictures uploaded
        else: 
            
            orig_pixmap = QPixmap('pictures/transparent.png')
            pixmap_resized = orig_pixmap.scaled(self.RadioPicLabel.width(), self.RadioPicLabel.height(), QtCore.Qt.KeepAspectRatio)
            #self.RadioPicLabel.setStyleSheet("background-color: #B2E2F2; margin: 0 30% 0 30%")
            #self.select_pic()
            self.RadioPicLabel.setPixmap(pixmap_resized)

            self.selected_pic = 0

        
    def select_pic(self):
        
        '''
        this function takes in a signal from radiobuttons, and shows a default picture 
        if not pictures are uploaded
        '''

        #should break down, this function too big
        radioBtn = self.PreviewGroupBox.sender()

        #default selection
        self.clothes_type = "អាវ"
       
        self.ResetInfoRadioChanged()

        if (radioBtn.isChecked()):
        
            self.clothes_type = radioBtn.text()
            if (self.clothes_type  == "សំពត់"):
                #skirt
                
                if len(self.uploaded_pictures_dir_list) == 0 : 
                    self.RadioPicLabel.setStyleSheet("image: url(:/newPrefix/skirt.jpg);background-color: #B2E2F2; margin: 0 30% 0 30%")
                
                self.SetSkirtInputOnly()


            elif (self.clothes_type  == "រ៉ូប"):
                #dress
                
                if len(self.uploaded_pictures_dir_list) == 0 : 
                    self.RadioPicLabel.setStyleSheet("image: url(:/newPrefix/dress.jpg);background-color: #B2E2F2; margin: 0 30% 0 30%")

                self.SetDressInputOnly()
        
        
            elif (self.clothes_type  == "អាវ"):
                #shirt
                
                if len(self.uploaded_pictures_dir_list) == 0 : 
                    self.RadioPicLabel.setStyleSheet("image: url(:/newPrefix/shirt.jpg);background-color: #B2E2F2; margin: 0 30% 0 30%")

                self.SetShirtInputOnly()  

            elif (self.clothes_type  == "ខោ"):
                #pant
                
                if len(self.uploaded_pictures_dir_list) == 0 : 
                    self.RadioPicLabel.setStyleSheet("image: url(:/newPrefix/pant.jpg);background-color: #B2E2F2; margin: 0 30% 0 30%")

                self.SetPantInputOnly()

    def SetPantInputOnly(self): 
        
        '''this function sets unneeded user input boxes to readonly when pant radio button is selected'''
        
        self.AroundBustBox.setReadOnly(True)
        self.AroundBustBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        

        self.NeckArmHoldBox.setReadOnly(True)
        self.NeckArmHoldBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")

        self.WaistBox.setReadOnly(True)
        self.WaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.ABBox.setReadOnly(True)
        self.ABBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.HipBox.setReadOnly(True)
        self.HipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.AboveBustBox.setReadOnly(True)
        self.AboveBustBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.CenterFrontBox.setReadOnly(True)
        self.CenterFrontBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.ShoulderBox.setReadOnly(True)
        self.ShoulderBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.AFBox.setReadOnly(True)
        self.AFBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.CenterBackBox.setReadOnly(True)
        self.CenterBackBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.UpperHipsBox.setReadOnly(True)
        self.UpperHipsBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.ArmpitBox.setReadOnly(True)
        self.ArmpitBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.SkirtLengthBox.setReadOnly(True)
        self.SkirtLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")

        self.SleeveLengthBox.setReadOnly(True)
        self.SleeveLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.BustHeightBox.setReadOnly(True)
        self.BustHeightBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")

    def SetShirtInputOnly(self): 
        
        '''this function sets unneeded user input boxes to readonly when shirt radio button is selected'''

        self.InseamBox.setReadOnly(True)
        self.InseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.OutseamBox.setReadOnly(True)
        self.OutseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.ThighBox.setReadOnly(True)
        self.ThighBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.PantHipBox.setReadOnly(True)
        self.PantHipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.AnkleBox.setReadOnly(True)
        self.AnkleBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.CalfBox.setReadOnly(True)
        self.CalfBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.PantWaistBox.setReadOnly(True)
        self.PantWaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.SkirtLengthBox.setReadOnly(True)
        self.SkirtLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.HipBox.setReadOnly(True)
        self.HipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")

    def SetDressInputOnly(self): 

        '''this function sets unneeded user input boxes to readonly when dress radio button is selected'''

        self.InseamBox.setReadOnly(True)
        self.InseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.OutseamBox.setReadOnly(True)
        self.OutseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.ThighBox.setReadOnly(True)
        self.ThighBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.PantHipBox.setReadOnly(True)
        self.PantHipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.AnkleBox.setReadOnly(True)
        self.AnkleBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        self.CalfBox.setReadOnly(True)
        self.CalfBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")
        
        self.PantWaistBox.setReadOnly(True)
        self.PantWaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : grey;"
                                "}")

    
    def SetSkirtInputOnly(self): 

        '''this function sets unneeded user input boxes to readonly when skirt radio button is selected'''
        
        #set readonly in boxes we don't need for skirt
        self.AroundBustBox.setReadOnly(True)
        self.AroundBustBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        

        self.NeckArmHoldBox.setReadOnly(True)
        self.NeckArmHoldBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")

        self.ABBox.setReadOnly(True)
        self.ABBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")

        
        self.AboveBustBox.setReadOnly(True)
        self.AboveBustBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        
        self.CenterFrontBox.setReadOnly(True)
        self.CenterFrontBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        
        self.ShoulderBox.setReadOnly(True)
        self.ShoulderBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.AFBox.setReadOnly(True)
        self.AFBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.CenterBackBox.setReadOnly(True)
        self.CenterBackBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.UpperHipsBox.setReadOnly(True)
        self.UpperHipsBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.ArmpitBox.setReadOnly(True)
        self.ArmpitBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
    

        self.SleeveLengthBox.setReadOnly(True)
        self.SleeveLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.BustHeightBox.setReadOnly(True)
        self.BustHeightBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        

        self.InseamBox.setReadOnly(True)
        self.InseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.OutseamBox.setReadOnly(True)
        self.OutseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.ThighBox.setReadOnly(True)
        self.ThighBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.PantHipBox.setReadOnly(True)
        self.PantHipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.AnkleBox.setReadOnly(True)
        self.AnkleBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        self.CalfBox.setReadOnly(True)
        self.CalfBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
        
        self.PantWaistBox.setReadOnly(True)
        self.PantWaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : gray;"
                                "}")
    def ResetInfoRadioChanged(self): 

        '''this function resets all input boxes to empty when another clothes type is selected 
        by user'''
        
        #clear text all boxes
        _translate = QtCore.QCoreApplication.translate
        self.AroundBustBox.setText(_translate("MainWindow", ''))
        self.NeckArmHoldBox.setText(_translate("MainWindow", ''))
        self.WaistBox.setText(_translate("MainWindow", ''))
        self.ABBox.setText(_translate("MainWindow", ''))
        self.HipBox.setText(_translate("MainWindow", ''))
        self.AboveBustBox.setText(_translate("MainWindow", ''))
        self.CenterFrontBox.setText(_translate("MainWindow", ''))
        self.ShoulderBox.setText(_translate("MainWindow", ''))
        self.AFBox.setText(_translate("MainWindow", ''))
        self.CenterBackBox.setText(_translate("MainWindow", ''))
        self.UpperHipsBox.setText(_translate("MainWindow", ''))
        self.ArmpitBox.setText(_translate("MainWindow", ''))
        self.SkirtLengthBox.setText(_translate("MainWindow", ''))
        self.SleeveLengthBox.setText(_translate("MainWindow", ''))
        self.BustHeightBox.setText(_translate("MainWindow", ''))

        self.InseamBox.setText(_translate("MainWindow", ''))
        self.OutseamBox.setText(_translate("MainWindow", ''))
        self.ThighBox.setText(_translate("MainWindow", ''))
        self.PantHipBox.setText(_translate("MainWindow", ''))
        self.AnkleBox.setText(_translate("MainWindow", ''))
        self.CalfBox.setText(_translate("MainWindow", ''))
        self.PantWaistBox.setText(_translate("MainWindow", ''))

        self.AroundBustBox.setReadOnly(False)
        self.AroundBustBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.AroundBustBox.setFont(SmallKhmerFont)
        
        

        self.NeckArmHoldBox.setReadOnly(False)
        self.NeckArmHoldBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.NeckArmHoldBox.setFont(SmallKhmerFont)

        self.WaistBox.setReadOnly(False)
        self.WaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.WaistBox.setFont(SmallKhmerFont)

        self.ABBox.setReadOnly(False)
        self.ABBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.ABBox.setFont(SmallKhmerFont)


        self.HipBox.setReadOnly(False)
        self.HipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.HipBox.setFont(SmallKhmerFont)
        
        self.AboveBustBox.setReadOnly(False)
        self.AboveBustBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.AboveBustBox.setFont(SmallKhmerFont)

        self.CenterFrontBox.setReadOnly(False)
        self.CenterFrontBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.CenterFrontBox.setFont(SmallKhmerFont)
        
        self.ShoulderBox.setReadOnly(False)
        self.ShoulderBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.ShoulderBox.setFont(SmallKhmerFont)

        self.AFBox.setReadOnly(False)
        self.AFBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.AFBox.setFont(SmallKhmerFont)

        self.CenterBackBox.setReadOnly(False)
        self.CenterBackBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")

        self.CenterBackBox.setFont(SmallKhmerFont)

        self.UpperHipsBox.setReadOnly(False)
        self.UpperHipsBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.UpperHipsBox.setFont(SmallKhmerFont)


        self.ArmpitBox.setReadOnly(False)
        self.ArmpitBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.ArmpitBox.setFont(SmallKhmerFont)

        self.SkirtLengthBox.setReadOnly(False)
        self.SkirtLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.SkirtLengthBox.setFont(SmallKhmerFont)

        self.SleeveLengthBox.setReadOnly(False)
        self.SleeveLengthBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.SleeveLengthBox.setFont(SmallKhmerFont)

        self.BustHeightBox.setReadOnly(False)
        self.BustHeightBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.BustHeightBox.setFont(SmallKhmerFont)

        self.InseamBox.setReadOnly(False)
        self.InseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.InseamBox.setFont(SmallKhmerFont)

        self.OutseamBox.setReadOnly(False)
        self.OutseamBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.OutseamBox.setFont(SmallKhmerFont)

        self.ThighBox.setReadOnly(False)
        self.ThighBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.ThighBox.setFont(SmallKhmerFont)

        self.PantHipBox.setReadOnly(False)
        self.PantHipBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.PantHipBox.setFont(SmallKhmerFont)

        self.AnkleBox.setReadOnly(False)
        self.AnkleBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.AnkleBox.setFont(SmallKhmerFont)

        self.CalfBox.setReadOnly(False)
        self.CalfBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")
        self.CalfBox.setFont(SmallKhmerFont)

        self.PantWaistBox.setReadOnly(False)
        self.PantWaistBox.setStyleSheet("QLineEdit"
                                "{"
                                "background : white;"
                                "}")

        self.PantWaistBox.setFont(SmallKhmerFont)

        
    def checkRequiredInputs(self): 

        '''This function is for checking that all required fields are given by user before interaction with database'''
        
        #customer 
        customer_name = self.CustomerNameBox.text()
        telephone = self.PhoneBox.text()

        #order
        price = self.PriceBox.text()
        customer_name = self.CustomerNameBox.text()
        deadline = self.DeadlineSelectedLabel.text()
        
        color = self.ColorBox.text()	
        style = self.StyleBox.text()
        material = self.MaterialBox.text()

        #radio button
        clothes_type = self.clothes_type
        
      
        #reset color
        self.PriceLabel.setStyleSheet("color: black; background-color: light grey") 
        self.CustomerNameLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
        self.DeadlineLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
        self.PhoneLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
        self.DeadlineSelectedLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
        self.StyleLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
        self.MaterialsLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
        self.ColorLabel.setStyleSheet("color: black; background-color: #B2E2F2") 

        self.SkirtRadio.setStyleSheet("color: black; background-color: light grey")
        self.ShirtRadio.setStyleSheet("color: black; background-color: light grey")
        self.PantRadio.setStyleSheet("color: black; background-color: light grey")
        self.DressRadio.setStyleSheet("color: black; background-color: light grey") 


        
        if (price == "" or customer_name == "" or deadline == "សូមចុចរូបប្រតិទិន" or telephone == "" or style == "" or material == ""  or color == ""
        or clothes_type == ""): 

            
            if price == "": 
                self.PriceLabel.setStyleSheet("color: red; background-color: light grey") 
            if customer_name == "":
                self.CustomerNameLabel.setStyleSheet("color: red") 
            if deadline == "សូមចុចរូបប្រតិទិន":
                self.DeadlineLabel.setStyleSheet("color: red") 
            if telephone == "":
                self.PhoneLabel.setStyleSheet("color: red") 
            if style == "": 
                self.StyleLabel.setStyleSheet("color: red") 
            if material == "":
                self.MaterialsLabel.setStyleSheet("color: red") 
            if color == "":
                self.ColorLabel.setStyleSheet("color: red")
            self.feedbackSubmit(0)



        else: 
            
            self.PriceLabel.setStyleSheet("color: black; background-color: light grey") 
            self.CustomerNameLabel.setStyleSheet("color: black; background-color: #B8E2F2;") 
            self.DeadlineLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
            self.PhoneLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
            self.DeadlineSelectedLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
            self.StyleLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
            self.MaterialsLabel.setStyleSheet("color: black; background-color: #B2E2F2") 
            self.ColorLabel.setStyleSheet("color: black; background-color: #B2E2F2")
            self.SkirtRadio.setStyleSheet("color: black; background-color: light grey")
            self.ShirtRadio.setStyleSheet("color: black; background-color: light grey")
            self.PantRadio.setStyleSheet("color: black; background-color: light grey")
            self.DressRadio.setStyleSheet("color: black; background-color: light grey") 
            self.feedbackSubmit(1)
            self.complete_input = 1
            
            

    def insertCustomerDetails(self):

        '''this function is controller for inserting customer details to database'''

        if (self.complete_input == 1): 
            customer_name = self.CustomerNameBox.text()
            address = self.AddressBox.toPlainText()
            telephone = self.PhoneBox.text()
            
            
            if self.updating == 0: 

                #dummy customer id for inserting 
                customer_id = 0 

            else: 
                customer_id = self.customer_id

            insertCustomer(customer_name, address, telephone, self.updating, customer_id)

            self.added_customer = 1



    def insertOrderDetails(self): 
        
        '''this function is controller for inserting order details to database'''

        #check that all required inputs are given by user, and customer is added to database before
        #adding order

        if ((self.complete_input == 1) and (self.added_customer == 1)): 
            
            price = self.PriceBox.text()
            customer_name = self.CustomerNameBox.text()
            staff = self.StaffNameBox.text()
            deadline = self.DeadlineBox.text()
            progress = '0'
            req = self.SpecialReqBox.toPlainText()
            uploads = self.uploaded_pictures_dir_list
            
            #get customer ID
            if self.updating == 0:
                customer_id = getCustomerID()

            else: 
                #use customer id gotten by FetchOrderDetails() when updating
                customer_id = self.customer_id

            insertOrder(price, customer_name, staff, deadline, progress, customer_id, req, self.updating)

            self.added_order = 1

            #copy new photos to an organized folder for tailor shop pictures only
            self.CopyNewPhotosToDirController()

            #insert directory of pictures to database
            self.InsertUploadDetails()

            

    def insertMaterialDetails(self): 
        '''this function is controller for inserting material details to database'''
        
        #check if all required inputs are given, order and customer is added before inserting material details to database
        if ((self.complete_input == 1) and (self.added_order == 1) and (self.added_customer == 1)): 
        
            clothes_type = self.clothes_type
            style = self.StyleBox.text()
            color = self.ColorBox.text()
            material = self.MaterialBox.text()
            
            #get order and customer id 
            if self.updating == 0:
                order_id = getOrderID()
                customer_id = getCustomerID()
            else: 

                #use customer id gotten by FetchOrderDetails() when updating
                customer_id = self.customer_id
                #pass dummy order id when updating
                order_id = 0
            
           
            insertMaterial(order_id, customer_id, clothes_type, material, color, style, self.updating)
            self.added_material = 1

    def insertMeasurementDetails(self):
        
        '''this function is controller for inserting measurement details to database'''
        
        #get clothes type 
        clothes_type = self.clothes_type
        
        #make sure all required inputs are complete, and order, customer, materials details are added
        if ((self.complete_input == 1) and (self.added_order == 1) and (self.added_customer == 1) and (self.added_material == 1)): 

            #get customer & order id
            if self.updating == 0:
                order_id = getOrderID()
                customer_id = getCustomerID()
            else: 
                #dummy order id
                order_id = 0
                #use customer id gotten by FetchOrderDetails() when updating
                customer_id = self.customer_id

            if clothes_type == "សំពត់":
                
                skirt_length = self.SkirtLengthBox.text()
                skirt_waist = self.WaistBox.text()
                skirt_hip = self.HipBox.text()

                insertSkirtMeasurements(order_id, customer_id, skirt_length, skirt_waist, skirt_hip, self.updating)


            elif clothes_type == "ខោ":
                
                inseam = self.InseamBox.text()
                outseam= self.OutseamBox.text()
                pant_thigh = self.ThighBox.text()
                pant_hip = self.PantHipBox.text()
                ankle = self.AnkleBox.text()
                calf = self.CalfBox.text()
                pant_waist = self.PantWaistBox.text()

                insertPantMeasurements(order_id, customer_id, inseam, outseam,pant_thigh , pant_hip, ankle, calf, pant_waist, self.updating)

            elif clothes_type == "អាវ":
                
                around_bust = self.AroundBustBox.text()
                neck_armhold = self.NeckArmHoldBox.text()
                dress_waist = self.WaistBox.text()
                ab = self.ABBox.text()
                above_bust = self.AboveBustBox.text()
                center_front = self.CenterFrontBox.text()
                shoulder = self.ShoulderBox.text()
                af = self.AFBox.text()
                center_back = self.CenterBackBox.text()
                upper_hips = self.UpperHipsBox.text()
                armpit = self.ArmpitBox.text()
                sleeve_length = self.SleeveLengthBox.text()
                bust_height = self.BustHeightBox.text()
                
                insertShirtMeasurements(order_id, customer_id, around_bust, neck_armhold,dress_waist, ab, above_bust, center_front, shoulder, af, center_back, 
                upper_hips, armpit, sleeve_length, bust_height, self.updating)

            elif clothes_type == "រ៉ូប": 

                around_bust = self.AroundBustBox.text()
                neck_armhold = self.NeckArmHoldBox.text()
                dress_waist = self.WaistBox.text()
                ab = self.ABBox.text()
                hip = self.HipBox.text()
                above_bust = self.AboveBustBox.text()
                center_front = self.CenterFrontBox.text()
                shoulder = self.ShoulderBox.text()
                af = self.AFBox.text()
                center_back = self.CenterBackBox.text()
                upper_hips = self.UpperHipsBox.text()
                armpit = self.ArmpitBox.text()
                skirt_length = self.SkirtLengthBox.text()
                sleeve_length = self.SleeveLengthBox.text()
                bust_height = self.BustHeightBox.text()

                insertDressMeasurements(order_id, customer_id, around_bust, neck_armhold,dress_waist,ab, above_bust, center_front, shoulder, af, center_back, 
                upper_hips, armpit, sleeve_length, bust_height, hip, skirt_length, self.updating)

            self.added_measurements = 1




    def feedbackSubmit(self, completed): 
        
        '''this functions gets the status if user has completed all required information(completed), and give feedback to user'''

        _translate = QtCore.QCoreApplication.translate
        
        #clear old messages
        self.SubmitMsg.setText(_translate("MainWindow", ""))
        
        if (completed): 
            self.SubmitMsg.setText(_translate("MainWindow", "ប្រតិបត្តិការជោគជ័យ!"))
        elif (completed == 0) : 
            self.SubmitMsg.setText(_translate("MainWindow", "ប្រតិបត្តិការបរាជ័យ!សូមបំពេញព័ត៌មានបន្ថែម"))

    def retranslateUi(self, MainWindow):
        
        '''this function set the text display in Mainwindow'''

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
        self.AddressLabel.setText(_translate("MainWindow", "ឤសយដ្ឋាន:"))
        self.CustomerNameLabel.setText(_translate("MainWindow", "ឈ្មោះ:"))
        self.CustomerPreferencesTitle.setText(_translate("MainWindow", "ជម្រើសអតិថិជន"))
        self.Upload.setText(_translate("MainWindow","បញ្ចូលរូបភាព"))
        self.Cancel.setText(_translate("MainWindow", "បោះបង់"))
        self.Submit.setText(_translate("MainWindow", "បញ្ចូល"))
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
        self.DeadlineSelectedLabel.setText(_translate("MainWindow", "សូមចុចរូបប្រតិទិន"))
        self.DeadlineSelectedLabel.setStyleSheet("color: black; background-color: #d7dbdd ")
        self.SubmitMsg.setText(_translate("MainWindow", ""))
        

        #menu buttons
        self.ActionNewOrder.setText(_translate("MainWindow", "កម្មង់ថ្មី"))
        self.ActionAbout.setText(_translate("MainWindow", "អំពីកម្មវិធី"))
        self.ActionViewAllOrders.setText(_translate("MainWindow", "ទិន្នន័យ"))

        
        
    
    def PrintDate(self, day, month, year):
        
        '''Get date inputs from calendar dialog, format, then print date in MainWindow as dd/mm/yyyy'''

        _translate = QtCore.QCoreApplication.translate
        
        self.DeadlineSelectedLabel.setText(_translate("MainWindow", f'{day}/{month}/{year}'))
        self.DeadlineSelectedLabel.setStyleSheet("color: black; background-color: #d7dbdd") 
        
    def getDate(self, day, month, year): 

        '''Get date inputs from calendar dialog for sending to database'''

        _translate = QtCore.QCoreApplication.translate
        self.DeadlineBox.setText(_translate("MainWindow", f'{year}/{month}/{day}'))
        
    def EditDate(self):
        
        '''function to open calendar dialog, and get deadline from user'''
        
        self.dialog = CalendarWindow()
        self.dialog.submitted.connect(self.PrintDate)
        self.dialog.submitted.connect(self.getDate)
        self.dialog.exec_()

    def ViewAllOrders(self):

        '''function to view all orders inside tableview dialog and help send customer ID for editing order'''
        self.orderdialog = TableView()
        self.orderdialog.customerEditID.connect(self.GetOrderDetails)        
        self.orderdialog.show()
        self.orderdialog.loaddata(customer_name = "")
    

    def aboutdeveloper(self):

        '''function to show about developer details'''

        self.aboutdialog = AboutDialog()
        self.aboutdialog.show()

    def GetOrderDetails(self, customer_id):
        
        '''controller function to fetch order details using customer id, and put into boxes for staff to edit'''

        self.customer_id = customer_id

        OrderDetails = FetchOrdersDetailsEdit(customer_id)


        #remove msg from prev trans
        self.SubmitMsg.setText("")

        #alter view 
        _translate = QtCore.QCoreApplication.translate
        
        if (len(OrderDetails) > 0): 
        
            self.CustomerNameBox.setText(_translate("MainWindow", str(OrderDetails['customer_name'])))
            self.PhoneBox.setText(_translate("MainWindow", str(OrderDetails['telephone'])))
            self.AddressBox.setPlainText(_translate("MainWindow", str(OrderDetails['address'])))

        
            self.StaffNameBox.setText(_translate("MainWindow", str(OrderDetails['staff'])))
            self.DeadlineBox.setText(_translate("MainWindow", str(OrderDetails['deadline'])))
            deadline = OrderDetails['deadline'].strftime("%d/%m/%Y")
            self.DeadlineSelectedLabel.setFont(SmallKhmerFont)
            self.DeadlineSelectedLabel.setText(_translate("MainWindow", deadline))

            self.StyleBox.setText(_translate("MainWindow", str(OrderDetails['style'])))
            self.MaterialBox.setText(_translate("MainWindow", str(OrderDetails['material'])))
            self.ColorBox.setText(_translate("MainWindow", str(OrderDetails['color'])))
            self.SpecialReqBox.setPlainText(_translate("MainWindow", str(OrderDetails['special'])))
            
            
            
            #radio 
            if OrderDetails['type'] == "សំពត់": 
                
                self.SkirtRadio.setChecked(True)

                self.WaistBox.setText(_translate("MainWindow", str(OrderDetails['skirt_waist'])))
                
                self.HipBox.setText(_translate("MainWindow", str(OrderDetails['skirt_hip'])))
                
                self.SkirtLengthBox.setText(_translate("MainWindow", str(OrderDetails['skirt_length'])))
            
                
            elif OrderDetails['type'] == "ខោ":
                
                self.PantRadio.setChecked(True)
                        
                self.InseamBox.setText(_translate("MainWindow", str(OrderDetails['inseam'])))
                
                self.OutseamBox.setText(_translate("MainWindow", str(OrderDetails['outseam'])))
                
                self.ThighBox.setText(_translate("MainWindow", str(OrderDetails['pant_thigh'])))
                
                self.PantHipBox.setText(_translate("MainWindow", str(OrderDetails['pant_hip'])))
                
                self.AnkleBox.setText(_translate("MainWindow", str(OrderDetails['ankle'])))
                
                self.CalfBox.setText(_translate("MainWindow", str(OrderDetails['calf'])))
                
                self.PantWaistBox.setText(_translate("MainWindow", str(OrderDetails['pant_waist'])))


            elif OrderDetails['type'] == "រ៉ូប":
                
                self.DressRadio.setChecked(True)
                
                self.AroundBustBox.setText(_translate('MainWindow', str(OrderDetails['around_bust'])))
                
                self.NeckArmHoldBox.setText(_translate('MainWindow', str(OrderDetails['neck_armhold'])))

                self.WaistBox.setText(_translate('MainWindow', str(OrderDetails['dress_waist'])))

                self.ABBox.setText(_translate('MainWindow', str(OrderDetails['ab'])))

                self.HipBox.setText(_translate('MainWindow', str(OrderDetails['above_bust'])))

                self.AboveBustBox.setText(_translate('MainWindow', str(OrderDetails['center_front'])))

                self.CenterFrontBox.setText(_translate('MainWindow', str(OrderDetails['shoulder'])))

                self.ShoulderBox.setText(_translate('MainWindow', str(OrderDetails['af'])))

                self.AFBox.setText(_translate('MainWindow', str(OrderDetails['center_back'])))

                self.CenterBackBox.setText(_translate('MainWindow', str(OrderDetails['upper_hips'])))

                self.UpperHipsBox.setText(_translate('MainWindow', str(OrderDetails['armpit'])))

                self.ArmpitBox.setText(_translate('MainWindow', str(OrderDetails['sleeve_length'])))

                self.SkirtLengthBox.setText(_translate('MainWindow', str(OrderDetails['bust_height'])))

                self.SleeveLengthBox.setText(_translate('MainWindow', str(OrderDetails['hip'])))

                self.BustHeightBox.setText(_translate('MainWindow', str(OrderDetails['skirt_length'])))

            elif OrderDetails['type'] == "អាវ":

                self.ShirtRadio.setChecked(True)

                self.AroundBustBox.setText(_translate('MainWindow', str(OrderDetails['around_bust'])))

                self.NeckArmHoldBox.setText(_translate('MainWindow', str(OrderDetails['neck_armhold'])))

                self.WaistBox.setText(_translate('MainWindow', str(OrderDetails['dress_waist'])))

                self.ABBox.setText(_translate('MainWindow', str(OrderDetails['ab'])))

                self.AboveBustBox.setText(_translate('MainWindow', str(OrderDetails['above_bust'])))

                self.CenterFrontBox.setText(_translate('MainWindow', str(OrderDetails['center_front'])))

                self.ShoulderBox.setText(_translate('MainWindow', str(OrderDetails['shoulder'])))

                self.AFBox.setText(_translate('MainWindow', str(OrderDetails['af'])))

                self.CenterBackBox.setText(_translate('MainWindow', str(OrderDetails['center_back'])))

                self.UpperHipsBox.setText(_translate('MainWindow', str(OrderDetails['upper_hips'])))

                self.ArmpitBox.setText(_translate('MainWindow', str(OrderDetails['armpit'])))

                self.SleeveLengthBox.setText(_translate('MainWindow', str(OrderDetails['sleeve_length'])))

                self.BustHeightBox.setText(_translate('MainWindow', str(OrderDetails['bust_height'])))
                    
            
            self.PriceBox.setText(_translate("MainWindow", str(OrderDetails['price'])))
            
            #pictures module
            if OrderDetails['uploads'] != None: 
                self.uploaded_pictures_dir_list = OrderDetails['uploads']
            else: 
                self.uploaded_pictures_dir_list = list()
            
            #reset selected picture
            self.selected_pic = 0 

            
            #in case there are existing pictures
            if self.uploaded_pictures_dir_list: 
                self.show_pic_preview(pic_num=0)
                self.SetUploadPreview()
            else: 
                pass
            
            
            self.ShirtRadio.setEnabled(False)
            self.DressRadio.setEnabled(False)
            self.SkirtRadio.setEnabled(False)
            self.PantRadio.setEnabled(False)

            self.updating = 1
        else: 
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find customer from the database.')
    
    def NewOrder(self): 
        '''clear input when new order menu button is clicked'''
        self.clearInput(ClearClicked = 0)

    def CancelOrder(self): 
        '''clear input when clear order button is clicked'''
        self.clearInput(ClearClicked = 1)

    def clearInput(self, ClearClicked): 

        '''function to clear all inputs by staff'''

        _translate = QtCore.QCoreApplication.translate
        self.CustomerNameBox.setText(_translate("MainWindow", ''))
        self.StaffNameBox.setText(_translate("MainWindow", ''))
        self.MaterialBox.setText(_translate("MainWindow", ''))
        self.ColorBox.setText(_translate("MainWindow", ''))
        self.PhoneBox.setText(_translate("MainWindow", ''))
        self.AddressBox.setPlainText(_translate("MainWindow", ''))
        self.StyleBox.setText(_translate("MainWindow", ''))
        self.PriceBox.setText(_translate("MainWindow", ''))
        self.DeadlineBox.setText(_translate("MainWindow", 'សូមចុចរូបប្រតិទិន'))
        self.SubmitMsg.setText(_translate("MainWindow", ''))
        self.SpecialReqBox.setPlainText(_translate("MainWindow", ''))
        self.PriceLabel.setStyleSheet("color: black; background-color: light grey") 
        self.CustomerNameLabel.setStyleSheet("color: black") 
        self.DeadlineLabel.setStyleSheet("color: black") 
        self.PhoneLabel.setStyleSheet("color: black") 
        self.DeadlineBox.setStyleSheet("color: black; background-color: white")
        self.DeadlineSelectedLabel.setText(_translate("MainWindow", 'សូមចុចរូបប្រតិទិន'))
        self.StyleLabel.setStyleSheet("color: black")
        self.MaterialsLabel.setStyleSheet("color: black")
        self.ColorLabel.setStyleSheet("color: black")




        #clear measurement boxes
        self.AroundBustBox.setText(_translate("MainWindow", ''))
        self.NeckArmHoldBox.setText(_translate("MainWindow", ''))
        self.WaistBox.setText(_translate("MainWindow", ''))
        self.ABBox.setText(_translate("MainWindow", ''))
        self.HipBox.setText(_translate("MainWindow", ''))
        self.AboveBustBox.setText(_translate("MainWindow", ''))
        self.CenterFrontBox.setText(_translate("MainWindow", ''))
        self.ShoulderBox.setText(_translate("MainWindow", ''))
        self.AFBox.setText(_translate("MainWindow", ''))
        self.CenterBackBox.setText(_translate("MainWindow", ''))
        self.UpperHipsBox.setText(_translate("MainWindow", ''))
        self.ArmpitBox.setText(_translate("MainWindow", ''))
        self.SkirtLengthBox.setText(_translate("MainWindow", ''))
        self.SleeveLengthBox.setText(_translate("MainWindow", ''))
        self.BustHeightBox.setText(_translate("MainWindow", ''))

        self.InseamBox.setText(_translate("MainWindow", ''))
        self.OutseamBox.setText(_translate("MainWindow", ''))
        self.ThighBox.setText(_translate("MainWindow", ''))
        self.PantHipBox.setText(_translate("MainWindow", ''))
        self.AnkleBox.setText(_translate("MainWindow", ''))
        self.CalfBox.setText(_translate("MainWindow", ''))
        self.PantWaistBox.setText(_translate("MainWindow", ''))

        
        self.UploadButtonOne.setStyleSheet("background-color: white; border: 1px solid blue;")
        self.UploadButtonOne.setIcon(QtGui.QIcon('icon/shirt-icon.png'))
        self.UploadButtonTwo.setStyleSheet("background-color: white; border: 1px solid blue;")
        self.UploadButtonTwo.setIcon(QtGui.QIcon('icon/shirt-icon.png'))        
        self.UploadButtonThree.setStyleSheet("background-color: white; border: 1px solid blue;")
        self.UploadButtonThree.setIcon(QtGui.QIcon('icon/shirt-icon.png'))        
        self.UploadButtonFour.setStyleSheet("background-color: white; border: 1px solid blue;")
        self.UploadButtonFour.setIcon(QtGui.QIcon('icon/shirt-icon.png'))        

        self.uploaded_pictures_dir_list = list()
        self.selected_pic = 0 
        self.new_pic_added_in_edit_list = list()

        self.ResetRadioButtons()
        

        #return to view orders dialog if clear button is clicked
        if (self.updating == 1 and ClearClicked == 1): 
            self.ViewAllOrders()
        

        self.updating = 0
    
    def ResetRadioButtons(self): 

        '''function to set radio button to default value when clearInput is called'''
        
        self.SkirtRadio.setStyleSheet("color: black; background-color: light grey")
        self.ShirtRadio.setStyleSheet("color: black; background-color: light grey")
        self.PantRadio.setStyleSheet("color: black; background-color: light grey")
        self.DressRadio.setStyleSheet("color: black; background-color: light grey") 
        
        self.SkirtRadio.setEnabled(True)
        self.SkirtRadio.setAutoExclusive(False)
        self.SkirtRadio.setChecked(False)
        self.SkirtRadio.setAutoExclusive(True)

        self.PantRadio.setEnabled(True)
        self.PantRadio.setAutoExclusive(False)
        self.PantRadio.setChecked(False)
        self.PantRadio.setAutoExclusive(True)

        self.DressRadio.setEnabled(True)
        self.DressRadio.setAutoExclusive(False)
        self.DressRadio.setChecked(False) 
        self.DressRadio.setAutoExclusive(True)

        self.ShirtRadio.setEnabled(True)
        self.ShirtRadio.setAutoExclusive(False)
        self.ShirtRadio.setChecked(True)
        self.ShirtRadio.setAutoExclusive(True)

        
        #picture previews
        orig_pixmap = QPixmap('pictures/transparent.png')
        pixmap_resized = orig_pixmap.scaled(self.RadioPicLabel.width(), self.RadioPicLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.RadioPicLabel.setStyleSheet("image: url(:/newPrefix/shirt.jpg);background-color: #B2E2F2")
        self.RadioPicLabel.setPixmap(pixmap_resized)
        
    

    def InsertUploadView(self):

            '''controller function to ask for location of picture to upload, and show it in radiopiclabel'''
            
            #try: 
            OldFile = self.GetPictureDir()   

            #if directory successfully added, show picture in view
            if OldFile: 
                self.ShowUploadPic()
                self.SetUploadPreview()

            else: 
                QMessageBox.warning(QMessageBox(), 'Error', 'Cannot upload Image')

                


    
    def GetPictureDir(self):
        
        '''function to open a dialog to copy picture to tailor store pictures folder'''

        dialog = UploadDialog()
        fileName, _ = QFileDialog.getSaveFileName(dialog,"Upload Image","","Images (*.png *jpeg *.jpg *jfif *bmp *gif)")
        
        if fileName:
            
            NumPicUploaded = len(self.uploaded_pictures_dir_list)

            #a limit of 4 pictures is set
            if ( NumPicUploaded < 4 ): 
            
                self.uploaded_pictures_dir_list.append(fileName)

                OldFile = self.uploaded_pictures_dir_list[NumPicUploaded - 1]

                return OldFile

        return False

    def CopyNewPhotosToDirController(self): 

        '''controller to copy and rename all newly inserted photo directory
        this function also sets the location of tailor store picture folder, and use order id as 
        name of copied pictures'''

        if ((self.added_order == 1) and (self.updating == 0)) : 

            order_id = getOrderID()
            
            dest_path =  "D:/tailor-store-pic/"
            dest_path += (str(order_id[0])+"/")
            self.CopyNewPhotosToDir(dest_path = dest_path)
            
            
        
        elif (self.updating == 1 and self.added_order == 1) : 
            
            #customer id is same as order id
            #this is because customer id is autogenerated when each order is added
            #will change it to make customer id the same for the same customer in later versions
            order_id = self.customer_id

            dest_path =  "D:/tailor-store-pic/"
            dest_path += (str(order_id)+"/")
            
            self.CopyNewPhotosToDir(dest_path = dest_path)
                    


        
    def CopyNewPhotosToDir(self, dest_path): 

        '''copies photos from old directory to tailor store photos folder'''

        try:         
            i = 1
            
            for old_dir in self.uploaded_pictures_dir_list: 
                Suffix = 'MODEL_'

                #get original image name 
                old_dir_list = old_dir.split('/')
                old_img_name = old_dir_list[-1]

                print(old_dir)
                print(dest_path)

                
                if Suffix in old_img_name: 

                    pass

                else: 
                    
                    #note index of new dir in list
                    index = i - 1
                    self.new_pic_added_in_edit_list.append(index)

                    #make directory, if folder not yet exist, then copy file to new directory
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                    #copy files from old folder to new folder
                    shutil.copy(old_dir, dest_path)

                    #rename file

                    try: 
                        #add suffix to image name to avoid same name error
                        new_img_name = Suffix + old_img_name 
                        os.rename(dest_path + old_img_name, dest_path + new_img_name)

                        #add image name to dest_path
                        dest_path_img = dest_path + new_img_name
                        
                        #replace old destination with new ones
                        self.uploaded_pictures_dir_list[i-1] = dest_path_img

                        i+=1
                    
                    except FileExistsError: 
                        TryAgain = True
                        
                        while TryAgain: 
                            try: 
                                Suffix += 'SameFileName_'
                                #add suffix to image name to avoid same name error
                                new_img_name = Suffix + old_img_name 
                                os.rename(dest_path + old_img_name, dest_path + new_img_name)
                                TryAgain = False
                            except FileExistsError: 
                                print('file exist error')
                                TryAgain = True
                            
                            
                        #add image name to dest_path
                        dest_path_img = dest_path + new_img_name

                        #replace old destination with new ones
                        self.uploaded_pictures_dir_list[i-1] = dest_path_img

                        i+=1

            
        # If source and destination are same 
        except shutil.SameFileError: 
            print("Source and destination represents the same file.") 
        
        # If destination is a directory. 
        except IsADirectoryError: 
            print("Destination is a directory.") 
        
        # If there is any permission issue 
        except PermissionError: 
            print("Permission denied.") 
        
        #enable after developement done
        # For other errors 
        #except: 
        #    print("Error occurred while copying file.") 
        

            
            
            
        

    def InsertUploadDetails(self): 

        '''this function controls the flow of adding photo directory to
        database'''

        #for new insert
        if ((self.added_order == 1) and (self.updating == 0)):
            
            customer_id = getCustomerID()
            customer_id = customer_id[0]

            #add img names to database 
            for new_dir in self.uploaded_pictures_dir_list: 
                InsertUploadDir(new_dir,customer_id)


        #for edit
        elif ((self.added_order == 1) and (self.updating == 1)): 

            customer_id = self.customer_id

            #insert only new pictures that are selected
            for i in self.new_pic_added_in_edit_list: 
                InsertUploadDir(self.uploaded_pictures_dir_list[i],customer_id)
            
            #empty list of new pic added in edit
            self.new_pic_added_in_edit_list = list()






class UploadDialog(QWidget):

    '''dialog for relocating photos'''

    def __init__(self):
        super().__init__()
        self.title = 'Upload Image'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


class AboutDialog(QDialog):
    
    '''dialog about developer information'''

    def __init__ (self):
        super(AboutDialog, self).__init__()
        self.setWindowTitle("About Dev")
        self.setGeometry(0, 0, 200, 100)
        self.setMaximumSize(QtCore.QSize(200, 100))
        self.setMinimumSize(QtCore.QSize(200, 100))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.initUI()

    def initUI(self):
        
        Panha = QLabel()
        Kheang = QLabel()
        Panha.setText("PANHA 0965622000\nUX/UI Designer")
        Kheang.setText("Kheang 085811647\nBackend Developer")
        Panha.setAlignment(Qt.AlignCenter)
        Kheang.setAlignment(Qt.AlignCenter)

        Vbox = QVBoxLayout()
        Vbox.addWidget(Panha)
        Vbox.addStretch()
        Vbox.addWidget(Kheang)
        self.setLayout(Vbox)
        #self.btn.clicked.connect(self.ActionAbout)

class UploadPreviewButton(QPushButton): 

    '''button class that can store small picture previews as icons
    after picture is uploaded'''

    def __init__(self):
        super(UploadPreviewButton, self).__init__()
        self.setMaximumSize(50, 50)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(False)
        self.setFont(SmallKhmerFont)
        self.setStyleSheet("background-color: white; border: 1px solid blue;")
        self.setIcon(QtGui.QIcon('icon/shirt-icon.png'))


class CalendarWindow(QDialog):
    '''calendar class for staff to select deadline'''
    global currentYear, currentMonth, currentDay

    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    submitted = QtCore.pyqtSignal(int, int, int)

    # constructor
    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setWindowTitle('Calendar')
        self.setGeometry(300, 300, 350, 250)
        self.setMinimumSize(QtCore.QSize(350, 250))
        self.setMaximumSize(QtCore.QSize(350, 250))
        self.initUI()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowStaysOnTopHint
            )
        
    def initUI(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.move(20, 20)
        self.calendar.setGridVisible(True)
        
        self.calendar.setSelectedDate(QDate(currentYear, currentMonth, currentDay))
        self.datelabel = QtWidgets.QLabel(self)
        self.datelabel.resize(200, 20) 
        date = self.calendar.selectedDate()
        self.datelabel.setText(date.toString())
        self.datelabel.move(20, 220)
        self.calendar.clicked.connect(self.sendDateMainWindow)

    def sendDateMainWindow(self, qDate):

        '''function to send date selected by user in this dialog to mainwindow'''

        date = self.calendar.selectedDate()
        self.datelabel.setText(date.toString())
        
        self.submitted.emit(
            qDate.day(), qDate.month(), qDate.year()
        )


class TableView(QDialog):

    '''dialog to view all orders, delete, edit, and search for all orders of one customer'''

    customerEditID = QtCore.pyqtSignal(str)


    # constructor
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle('All Orders')
        
        self.setMinimumSize(QtCore.QSize(1200, 800))
        self.showMaximized()
        self.initUI()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        toolbar = QToolBar()

        toolbar.setMovable(False)

        #var for number of total columns
        self.NumCol = 9

        layout.addWidget(toolbar)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(self.NumCol)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("លេខកម្មង់", "តម្លៃ", "ឈ្មោះអតិថិជន", "ឈ្មោះបុគ្គលិក","ថ្ងែទទួល", "ថ្ងែកំណត់", "ដំណើរការ", "លុប", "កែសម្រួល", "រូបភាព"))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setFont(BigKhmerFont)
        self.tableWidget.setSortingEnabled(True)

        #add scrollbar 
        self.tableWidget.resizeRowsToContents()
    
        layout.addWidget(self.tableWidget)

        #refresh icon
        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Refresh",self)  
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)
        

        #search icon
        btn_ac_search = QAction(QIcon("icon/search.png"), "Search", self)  
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search Customer")
        toolbar.addAction(btn_ac_search)

        

    def loaddata(self, customer_name):
        
        '''function that receive customer_name as input, and query the database for some order details'''
        
        #list all customers
        if customer_name == "" or customer_name == False : 
            sql_select_query = 'SELECT "ID" , price, customer_name, staff, to_char(date_ordered,\'dd.mm.YYYY\'), to_char(deadline,\'dd.mm.YYYY\'), progress FROM %s'
            record_to_query = (AsIs("orders"),)
            cursor.execute(sql_select_query, record_to_query)
            all_rows = cursor.fetchall()

        #search one customer name 
        else: 
            sql_select_query = 'SELECT "ID" , price, customer_name, staff, to_char(date_ordered,\'dd.mm.YYYY\'), to_char(deadline,\'dd.mm.YYYY\'), progress FROM %s WHERE customer_name = %s'
            record_to_query = (AsIs("orders"), customer_name)
            cursor.execute(sql_select_query, record_to_query)
            all_rows = cursor.fetchall()

        #set font 
        self.tableWidget.horizontalHeader().setFont(BigKhmerFont)
        self.tableWidget.setFont(SmallKhmerFont)
        self.tableWidget.setRowCount(0)

        #show all rows/ show searched customer name
        if len(all_rows) > 0: 
            for row_number, row_data in enumerate(all_rows):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    
                    item = QTableWidgetItem(str(data))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.tableWidget.setItem(row_number, column_number,item)
                    self.tableWidget.setRowHeight(row_number, 50)

        #customer name cannot be found 
        else: 
            self.tableWidget.insertRow(0)
            for i in range(0, self.NumCol): 
                
                data = "(គ្មានទិន្នន័យ)"
                item = QTableWidgetItem(str(data))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.tableWidget.setRowHeight(0, 50)
                self.tableWidget.setItem(0, (self.NumCol/2), item)
                
        #progress percentage
        for row_number in range(0,len(all_rows)): 
            #combo box
            combo_box_options1 = ["0%","25%","50%","75%", "100%"]

            combo = QComboBox()

            #get current index from db
            combo.addItems(combo_box_options1)
            combo.setCurrentIndex(int(all_rows[row_number][6])) 
            combo.currentIndexChanged.connect(self.UpdateProgressPercent)

            #add to table 
            self.tableWidget.setCellWidget(row_number,6,combo)	
        
        #add delete button for each row
        for row_number in range(0,len(all_rows)): 


            btn_ac_delete = QtWidgets.QPushButton()
            btn_ac_delete.setLayoutDirection(QtCore.Qt.LeftToRight)
            btn_ac_delete.setAutoFillBackground(False)
            btn_ac_delete.setObjectName("btn_ac_delete")
            btn_ac_delete.setIcon(QtGui.QIcon('icon/delete.png'))
            size = QtCore.QSize(25, 25)
            btn_ac_delete.setIconSize(size)
            btn_ac_delete.clicked.connect(self.delete)

            #add to table
            self.tableWidget.setCellWidget(row_number,7,btn_ac_delete)	

        #add edit button for each row
        for row_number in range(0,len(all_rows)): 
            
            btn_ac_edit = QtWidgets.QPushButton()
            btn_ac_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
            btn_ac_edit.setAutoFillBackground(False)
            btn_ac_edit.setObjectName("btn_ac_edit")
            btn_ac_edit.setIcon(QtGui.QIcon('icon/edit.png'))
            size = QtCore.QSize(25, 25)
            btn_ac_edit.setIconSize(size)
            btn_ac_edit.clicked.connect(self.edit)

            #add to table
            self.tableWidget.setCellWidget(row_number,8,btn_ac_edit)	


    def UpdateProgressPercent(self, index):

        '''this function gets row number of table as input, and update the progress percentages when user changes it'''
        
        #get customer ID from selected row 
        r = self.tableWidget.currentRow()
        customer_id = self.tableWidget.item(r,0).text()

        #update table 
        UpdateProcess(index, customer_id)


    def delete(self):

        '''this function deletes an order's details using customer'''

        r = self.tableWidget.currentRow()
        customer_id = self.tableWidget.item(r,0).text()
        customer_name = self.tableWidget.item(r,2).text()
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f"Are you sure you want to delete customer {customer_name} ?")
        msgBox.setWindowTitle("Delete Customer")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    
                
        #delete from database
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.deletecustomer(customer_id=customer_id)
        

        #refresh automatically
        self.loaddata(customer_name= "")
    

    def edit(self): 

        '''this function gets the customer id of row selected and send it to MainWindow'''

        r = self.tableWidget.currentRow()

        #using as temporary in place of order id
        customer_id = self.tableWidget.item(r,0).text()

        #send customer id to submit order window 

        self.EditCustomerID(customer_id=customer_id)




    def search(self):

        '''this function shows search dialog for user to input customer name and sends it to 
        view orders dialog for searching'''

        self.Searchdlg = SearchDialog()
        self.Searchdlg.customer_name.connect(self.loaddata)
        self.Searchdlg.exec_()

    def EditCustomerID(self, customer_id):

        ''' this function recieves customer id as input, and relays it to another function'''
        
        self.customerEditID.emit(
            customer_id
        )

        self.close()


    def deletecustomer(self, customer_id):
        
        ''' function to delete all customer details from database'''

        delrol = customer_id
        if delrol != "":
            try:
                #delete customer
                postgres_delete_query = 'DELETE from customers WHERE "ID"='+str(delrol)
                connection.commit()
                count = cursor.rowcount
                cursor.execute(postgres_delete_query)
                print(count, "Record remaining in customers table after delete")
                
                #delete order
                postgres_delete_query = 'DELETE from orders WHERE customer_id ='+str(delrol)
                connection.commit()
                count = cursor.rowcount
                cursor.execute(postgres_delete_query)
                print(count, "Record deleted successfully in orders table")


                #delete measurements

                #check which type 
                sql_select_query = 'SELECT type FROM materials WHERE customer_id ='+str(delrol)
                cursor.execute(sql_select_query)
                clothes_type = cursor.fetchone()

                if clothes_type[0] == "សំពត់":
                    table = 'skirt_measurements'
                elif clothes_type[0] == "ខោ":
                    table = 'pant_measurements'
                elif clothes_type[0] == "រ៉ូប":
                    table = 'dress_measurements'
                elif clothes_type[0] == "អាវ":
                    table = 'shirt_measurements'

                #delete from measurements
                postgres_delete_query = 'DELETE from %s WHERE customer_id ='+str(delrol)
                record_to_delete = (AsIs(table),)
                cursor.execute(postgres_delete_query, record_to_delete)
                connection.commit()
                count = cursor.rowcount
                print(count, f"Record deleted successfully in {table} table")

                #delete preferences/materials
                postgres_delete_query = 'DELETE from materials WHERE customer_id ='+str(delrol)
                connection.commit()
                count = cursor.rowcount
                cursor.execute(postgres_delete_query)
                print(count, "Record deleted successfully in materials table")

                QMessageBox.information(QMessageBox(),'Successful','Deleted From Table Successful')

            except Exception:

                QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete customer from the database.')






class SearchDialog(QDialog):
    '''dialog class to search for customer's orders'''

    customer_name = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowStaysOnTopHint
            )       

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search customer")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchcustomer)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.searchinput.setFont(SmallKhmerFont)
        self.searchinput.setPlaceholderText("ឈ្មោះអតិធិជន")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        

    def searchcustomer(self):

        '''function to send customer name to view orders dialog to search '''

        searchrol = ""
        searchrol = self.searchinput.text()
        if searchrol != "": 
            self.customer_name.emit(
                searchrol
            )

            self.close()


class appController:

    """Controller class to receive signal from MainWindow, and connect to functions in MainWindow"""

    def __init__(self, view):
        """Controller initializer."""
        
        self._view = view

        # Connect signals and slots
        self._connectSignals()


    def _connectSignals(self):
        """Connect signals and slots in MainWindow"""
    
        #check that all required inputs are entered by user
        self._view.Submit.clicked.connect(self._view.checkRequiredInputs)	
        
        #insert to customers table
        self._view.Submit.clicked.connect(self._view.insertCustomerDetails)

        #insert to orders table 
        self._view.Submit.clicked.connect(self._view.insertOrderDetails)

        #insert to materials table 
        self._view.Submit.clicked.connect(self._view.insertMaterialDetails)

        #insert to measurements table
        self._view.Submit.clicked.connect(self._view.insertMeasurementDetails)


        #clear all inputs
        self._view.Cancel.clicked.connect(self._view.CancelOrder)
        self._view.ActionNewOrder.triggered.connect(self._view.NewOrder)

        
        #view all orders
        self._view.ActionViewAllOrders.triggered.connect(self._view.ViewAllOrders)
 
        #About Developer 
        self._view.ActionAbout.triggered.connect(self._view.aboutdeveloper)

        #show picture in view
        self._view.Upload.clicked.connect(self._view.InsertUploadView)


        #delete photos
        self._view.DeletePictureShownButton.clicked.connect(self._view.DeleteUploadPicMain)
        
        
             
        
#MODEL FUNCTIONS
def insertCustomer(customer_name, address, telephone, update, customer_id):
    
    '''function to insert customer details to customer tables'''
   
    table = 'customers'
    if update == 0: 
        postgres_insert_query = 'INSERT INTO %s (customer_name, address, telephone) VALUES (%s,%s,%s)'
        record_to_insert = (AsIs(table), customer_name, address, telephone,)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into customers table")
    else: 
        postgres_update_query = 'UPDATE %s SET customer_name = %s, address = %s, telephone = %s WHERE "ID" = %s'
        record_to_update = (AsIs(table), customer_name, address, telephone, customer_id)
        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into customers table")

    

def insertOrder(price, customer_name, staff, deadline, progress, customer_id, req, update):
    
    '''function to insert Order details to Order tables'''
    
    table = 'orders'
    
    if update == 0:
        #add 1 entry to table
        postgres_insert_query = 'INSERT INTO %s (price, customer_name, staff, deadline, progress, customer_id, requests) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        record_to_insert = (AsIs(table), price, customer_name, staff, deadline, progress, customer_id, req)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into orders table")


    else: 
        postgres_update_query = 'UPDATE %s SET price = %s , customer_name = %s, staff = %s, deadline = %s, requests = %s WHERE customer_id = %s'
        record_to_update = (AsIs(table), price, customer_name, staff, deadline, req, customer_id)
        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into orders table")

def UpdateProcess(progress, customer_id):

    '''function to update progress in view all orders'''

    table = 'orders'
    postgres_update_query = 'UPDATE %s SET progress = %s WHERE customer_id = %s'
    record_to_update = (AsIs(table), progress, customer_id)
    cursor.execute(postgres_update_query, record_to_update)
    connection.commit()
    count = cursor.rowcount
    print(count, "Progress updated successfully into orders table")


def insertSkirtMeasurements(order_id, customer_id, skirt_length, skirt_waist, skirt_hip, update):
    
    '''function to insert Order details to skirt_measurement tables'''
    
    table = 'skirt_measurements'
    
    if update == 0:
        #add 1 entry to table
        postgres_insert_query = 'INSERT INTO %s (order_id, customer_id, skirt_length, skirt_waist, skirt_hip) VALUES (%s,%s,%s,%s,%s)'
        record_to_insert = (AsIs(table), order_id, customer_id, skirt_length, skirt_waist, skirt_hip)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into skirt table")


    else: 
        postgres_update_query = 'UPDATE %s SET skirt_length = %s , skirt_waist = %s, skirt_hip = %s WHERE customer_id = %s'
        record_to_update = (AsIs(table), skirt_length, skirt_waist, skirt_hip, customer_id)
        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into skirt table")
    

def insertDressMeasurements(order_id, customer_id, around_bust, neck_armhold,dress_waist,ab, above_bust, center_front, shoulder, af, center_back, 
    upper_hips, armpit, sleeve_length, bust_height, hip, skirt_length, update):

    '''function to insert Order details to dress_measurement tables'''

    table = 'dress_measurements'
    
    if update == 0:
        #add 1 entry to table
        postgres_insert_query = 'INSERT INTO %s (order_id, customer_id, around_bust, neck_armhold,dress_waist,ab, above_bust, center_front, shoulder, af, center_back, upper_hips, armpit, sleeve_length, bust_height, hip, skirt_length) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        record_to_insert = (AsIs(table), order_id, customer_id, around_bust, neck_armhold,dress_waist,ab, above_bust, center_front, shoulder, af, center_back, 
        upper_hips, armpit, sleeve_length, bust_height, hip, skirt_length)

        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into dress table")

    else: 
        postgres_update_query = 'UPDATE %s SET around_bust= %s, neck_armhold= %s, dress_waist= %s, ab= %s, above_bust= %s, center_front= %s, shoulder= %s, af= %s, center_back= %s, upper_hips= %s, armpit= %s, sleeve_length= %s, bust_height= %s, hip= %s, skirt_length= %s WHERE customer_id = %s'
        
        record_to_update = (AsIs(table), around_bust, neck_armhold,dress_waist,ab, above_bust, center_front, shoulder, af, center_back, 
        upper_hips, armpit, sleeve_length, bust_height, hip, skirt_length, customer_id)

        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into dress table")

def insertShirtMeasurements(order_id, customer_id, around_bust, neck_armhold,dress_waist, ab, above_bust, center_front, shoulder, af, center_back, 
    upper_hips, armpit, sleeve_length, bust_height, update):

    '''function to insert Order details to shirt_measurement tables'''

    table = 'shirt_measurements'
    
    if update == 0:
        #add 1 entry to table
        postgres_insert_query = 'INSERT INTO %s (order_id, customer_id, around_bust, neck_armhold, dress_waist, ab, above_bust, center_front, shoulder, af, center_back, upper_hips, armpit, sleeve_length, bust_height) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        record_to_insert = (AsIs(table), order_id, customer_id, around_bust, neck_armhold,dress_waist, ab, above_bust, center_front, shoulder, af, center_back,
        upper_hips, armpit, sleeve_length, bust_height)

        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into shirt table")
    
    else: 
        postgres_update_query = 'UPDATE %s SET around_bust= %s, neck_armhold= %s, dress_waist= %s, ab= %s, above_bust= %s, center_front= %s, shoulder= %s, af= %s, center_back= %s, upper_hips= %s, armpit= %s, sleeve_length= %s, bust_height= %s  WHERE customer_id = %s'
        
        record_to_update = (AsIs(table), around_bust, neck_armhold,dress_waist,ab, above_bust, center_front, shoulder, af, center_back, 
        upper_hips, armpit, sleeve_length, bust_height, customer_id)

        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into shirt table")
            

def insertPantMeasurements(order_id, customer_id, inseam, outseam,pant_thigh , pant_hip, ankle, calf, pant_waist, update):

    '''function to insert Order details to pant_measurement tables'''

    table = 'pant_measurements'
    
    if update == 0:
        #add 1 entry to table
        postgres_insert_query = 'INSERT INTO %s (order_id, customer_id, inseam, outseam,pant_thigh , pant_hip, ankle, calf, pant_waist) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        record_to_insert = (AsIs(table), order_id, customer_id, inseam, outseam,pant_thigh , pant_hip, ankle, calf, pant_waist)

        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into pant table")
    
    else: 
        postgres_update_query = 'UPDATE %s SET inseam= %s, outseam= %s, pant_thigh= %s, pant_hip= %s, ankle= %s, calf= %s, pant_waist= %s WHERE customer_id = %s'
        
        record_to_update = (AsIs(table), inseam, outseam,pant_thigh , pant_hip, ankle, calf, pant_waist, customer_id)

        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into pant table")

def insertMaterial(order_id, customer_id, type_clothes, material, color, style, update):
    
    '''function to insert customer preferences into materials table'''

    table = 'materials'
    
    if update == 0:
    #add 1 entry to table
        postgres_insert_query = 'INSERT INTO %s (order_id, type, material, color, style, customer_id) VALUES (%s,%s,%s,%s,%s,%s)'
        record_to_insert = (AsIs(table), order_id, type_clothes, material, color, style, customer_id)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into materials table")
    else: 
        postgres_update_query = 'UPDATE %s SET type = %s, material = %s, color = %s, style = %s WHERE customer_id = %s'
        record_to_update = (AsIs(table), type_clothes, material, color, style, customer_id)
        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully into materials table")

def InsertUploadDir(PicDir, customer_id): 

    '''this function takes in a picture directory, and inserts it into the uploads column in orders table'''
    
    #add 1 entry to table
    postgres_insert_query = f"UPDATE orders SET uploads = array_cat(uploads, '{{ {PicDir} }}') WHERE customer_id = {customer_id}"
    cursor.execute(postgres_insert_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "picture dir inserted successfully into orders table")


def getCustomerID(): 

    '''helper function to fetch last inserted customer id into other tables'''

    postgres_getID_query = 'SELECT currval(pg_get_serial_sequence(%s,%s))'
    record_to_getID = ('customers', 'ID')
    cursor.execute(postgres_getID_query, record_to_getID)
    customerID = cursor.fetchone()
    #print(customerID, 'is customer ID for this order')

    return customerID

def DeleteUploadPic(pic_dir, customer_id): 
    
    '''function to delete one picture directory given using given customer id'''

    postgres_delete_query = f"UPDATE orders SET uploads = array_remove(uploads, '{pic_dir}') WHERE customer_id = {customer_id}"
    connection.commit()
    count = cursor.rowcount
    cursor.execute(postgres_delete_query)
    print(count, "picture directory deleted")




def getOrderID(): 

    '''function to get last inserted order ID into other tables'''

    postgres_getID_query = 'SELECT currval(pg_get_serial_sequence(%s,%s))'
    record_to_getID = ('orders', 'ID')
    cursor.execute(postgres_getID_query, record_to_getID)
    orderID = cursor.fetchone()
    #print(orderID, 'is order ID for this order')

    return orderID

def FetchOrdersDetailsEdit(customer_id): 
    
    '''this function takes in customer ID, and then fetch one order's detail with that customer ID into a dictionary 
    and returns the dictionary with all details'''

    #dictionary to store 1 order details
    order_details = dict()


    sql_select_query = 'SELECT price, customer_name, staff, requests, deadline, uploads FROM %s WHERE customer_id = %s'
    record_to_query = (AsIs("orders"), customer_id )
    cursor.execute(sql_select_query, record_to_query)
    all_rows = cursor.fetchone()

    if all_rows != None: 

        #add to dict
        order_details['price'] = all_rows[0]
        order_details['customer_name'] = all_rows[1]
        order_details['staff'] = all_rows[2]
        order_details['deadline'] = all_rows[4]
        order_details['special'] = all_rows[3]
        order_details['uploads'] = all_rows[5]


        #telephone, address
        sql_select_query = 'SELECT address, telephone FROM %s WHERE "ID" = %s'
        record_to_query = (AsIs("customers"), customer_id)
        cursor.execute(sql_select_query, record_to_query)
        all_rows = cursor.fetchone()

        #add to dict
        order_details['address'] = all_rows[0]
        order_details['telephone'] = all_rows[1]
        
        #style, material, color, type
        sql_select_query = 'SELECT material, color, style, type FROM %s WHERE customer_id = %s'
        record_to_query = (AsIs("materials"), customer_id)
        cursor.execute(sql_select_query, record_to_query)
        all_rows = cursor.fetchone()

    
        order_details['material'] = all_rows[0]
        order_details['color'] = all_rows[1]
        order_details['style'] = all_rows[2]
        order_details['type'] = all_rows[3]

        
        #fetch according to type
        if order_details['type'] == "រ៉ូប":
            sql_select_query = 'SELECT around_bust, neck_armhold, dress_waist,ab, above_bust, center_front, shoulder, af, center_back, upper_hips, armpit, sleeve_length, bust_height, hip, skirt_length FROM %s WHERE customer_id = %s'
            record_to_query = (AsIs("dress_measurements"), customer_id)
            cursor.execute(sql_select_query, record_to_query)
            all_rows = cursor.fetchone()

            order_details['around_bust'] = all_rows[0]
            order_details['neck_armhold'] = all_rows[1]
            order_details['dress_waist'] = all_rows[2]
            order_details['ab'] = all_rows[3]
            order_details['above_bust'] = all_rows[4]
            order_details['center_front'] = all_rows[5]
            order_details['shoulder'] = all_rows[6]
            order_details['af'] = all_rows[7]
            order_details['center_back'] = all_rows[8]
            order_details['upper_hips'] = all_rows[9]
            order_details['armpit'] = all_rows[10]
            order_details['sleeve_length'] = all_rows[11]
            order_details['bust_height'] = all_rows[12]
            order_details['hip'] = all_rows[13]
            order_details['skirt_length'] = all_rows[14]
            
            
        elif order_details['type'] == "សំពត់":
            sql_select_query = 'SELECT skirt_length, skirt_waist, skirt_hip FROM %s WHERE customer_id = %s'
            record_to_query = (AsIs("skirt_measurements"), customer_id)
            cursor.execute(sql_select_query, record_to_query)
            all_rows = cursor.fetchone()

            order_details['skirt_length'] = all_rows[0]
            order_details['skirt_waist'] = all_rows[1]
            order_details['skirt_hip'] = all_rows[2]

        elif order_details['type'] == "ខោ":
            
            sql_select_query = 'SELECT inseam, outseam,pant_thigh , pant_hip, ankle, calf, pant_waist FROM %s WHERE customer_id = %s'
            record_to_query = (AsIs("pant_measurements"), customer_id)
            cursor.execute(sql_select_query, record_to_query)
            all_rows = cursor.fetchone()
            
            order_details['inseam'] = all_rows[0]
            order_details['outseam'] = all_rows[1]
            order_details['pant_thigh'] = all_rows[2]
            order_details['pant_hip'] = all_rows[3]
            order_details['ankle'] = all_rows[4]
            order_details['calf'] = all_rows[5]
            order_details['pant_waist'] = all_rows[6]

        elif order_details['type'] == "អាវ":
            
                    
            sql_select_query = 'SELECT around_bust, neck_armhold,dress_waist, ab, above_bust, center_front, shoulder, af, center_back, upper_hips, armpit, sleeve_length, bust_height FROM %s WHERE customer_id = %s'
            record_to_query = (AsIs("shirt_measurements"), customer_id)
            cursor.execute(sql_select_query, record_to_query)
            all_rows = cursor.fetchone()

            order_details['around_bust'] = all_rows[0]
            order_details['neck_armhold'] = all_rows[1]
            order_details['dress_waist'] = all_rows[2]
            order_details['ab'] = all_rows[3]
            order_details['above_bust'] = all_rows[4]
            order_details['center_front'] = all_rows[5]
            order_details['shoulder'] = all_rows[6]
            order_details['af'] = all_rows[7]
            order_details['center_back'] = all_rows[8]
            order_details['upper_hips'] = all_rows[9]
            order_details['armpit'] = all_rows[10]
            order_details['sleeve_length'] = all_rows[11]
            order_details['bust_height'] = all_rows[12]
        return order_details
    
    return order_details

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    
    #import fonts
    _id1 = QtGui.QFontDatabase.addApplicationFont("font/KhmerOSNew-Regular.ttf")
    _id2 = QtGui.QFontDatabase.addApplicationFont("font/KhmerOSNew-Bold.ttf")
    #print font that is used in console
    print(QtGui.QFontDatabase.applicationFontFamilies(_id1))

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.showMaximized()

    # Create instances of the model/controller
    appController(view=ui)

    app.exec_()

    close_connection(connection, cursor)
    sys.exit()


