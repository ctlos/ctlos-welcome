#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import os
import subprocess

class Ui_WelcomeScreen(object):
    ######################### CUSTOM ACTIONS ##########################
    def forumButtonAction(self):
        webbrowser.open("https://forum.ctlos.ru")
    def chatButtonAction(self):
        webbrowser.open("https://tele.click/ctlos")
    def donateButtonAction(self):
        webbrowser.open("https://ctlos.github.io/donat")
    def wikiButtonAction(self):
        webbrowser.open("https://ctlos.github.io/wiki")
    def newsButtonAction(self):
        webbrowser.open("https://ctlos.github.io/wiki/changelog")
    def helpButtonAction(self):
        webbrowser.open("https://github.com/ctlos/ctlosiso/issues")
    def installButtonAction(self):
        subprocess.Popen(["calamares_polkit"])
    def startCheckAction(self):
        if self.launchAtStartCheck.isChecked():
            homedir = os.path.expanduser('~')
            autostartfile = os.path.join(homedir, ".config/autostart/ctlos-welcome.desktop")
            subprocess.Popen(["cp", "/usr/share/applications/ctlos-welcome.desktop", autostartfile])
        else:
            homedir = os.path.expanduser('~')
            autostartfile = os.path.join(homedir, ".config/autostart/ctlos-welcome.desktop")
            subprocess.Popen(["rm", autostartfile])
    #####################################################################

    def setupUi(self, WelcomeScreen):
        WelcomeScreen.setObjectName("WelcomeScreen")
        WelcomeScreen.resize(640, 480)
        WelcomeScreen.setMinimumSize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/ctlos-welcome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WelcomeScreen.setWindowIcon(icon)
        self.MainWidget = QtWidgets.QWidget(WelcomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setAutoFillBackground(False)
        self.MainWidget.setObjectName("MainWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainGrid = QtWidgets.QGridLayout()
        self.mainGrid.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.mainGrid.setObjectName("mainGrid")
        self.wikiButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wikiButton.sizePolicy().hasHeightForWidth())
        self.wikiButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/wiki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wikiButton.setIcon(icon1)
        self.wikiButton.setObjectName("wikiButton")

        ######################### WIKI BUTTON ##########################
        self.wikiButton.clicked.connect(self.wikiButtonAction)
        ################################################################

        self.mainGrid.addWidget(self.wikiButton, 7, 0, 1, 1)
        self.lineTop = QtWidgets.QFrame(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineTop.sizePolicy().hasHeightForWidth())
        self.lineTop.setSizePolicy(sizePolicy)
        self.lineTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineTop.setObjectName("lineTop")
        self.mainGrid.addWidget(self.lineTop, 4, 0, 1, 3)
        self.logoLayout = QtWidgets.QHBoxLayout()
        self.logoLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.logoLayout.setObjectName("logoLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logoLayout.addItem(spacerItem)
        self.Logo = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMaximumSize(QtCore.QSize(64, 64))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setWordWrap(False)
        self.Logo.setObjectName("Logo")
        self.logoLayout.addWidget(self.Logo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logoLayout.addItem(spacerItem1)
        self.mainGrid.addLayout(self.logoLayout, 0, 0, 1, 3)
        self.linksLabel = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linksLabel.sizePolicy().hasHeightForWidth())
        self.linksLabel.setSizePolicy(sizePolicy)
        self.linksLabel.setScaledContents(True)
        self.linksLabel.setWordWrap(True)
        self.linksLabel.setObjectName("linksLabel")
        self.mainGrid.addWidget(self.linksLabel, 5, 0, 1, 3)
        self.donateButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donateButton.sizePolicy().hasHeightForWidth())
        self.donateButton.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/donate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.donateButton.setIcon(icon2)
        self.donateButton.setObjectName("donateButton")

        ######################### DONATE BUTTON ########################
        self.donateButton.clicked.connect(self.donateButtonAction)
        ################################################################

        self.mainGrid.addWidget(self.donateButton, 7, 2, 1, 1)
        self.chatButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatButton.sizePolicy().hasHeightForWidth())
        self.chatButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chatButton.setIcon(icon3)
        self.chatButton.setObjectName("chatButton")

        ######################### CHAT BUTTON ##########################
        self.chatButton.clicked.connect(self.chatButtonAction)
        ###############################################################

        self.mainGrid.addWidget(self.chatButton, 7, 1, 1, 1)
        self.installationLabel = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installationLabel.sizePolicy().hasHeightForWidth())
        self.installationLabel.setSizePolicy(sizePolicy)
        self.installationLabel.setObjectName("installationLabel")

        ######################### INSTALL LABEL ##########################
        self.installationLabel.setVisible(False)
        ##################################################################

        self.mainGrid.addWidget(self.installationLabel, 8, 1, 1, 1)
        self.installButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installButton.sizePolicy().hasHeightForWidth())
        self.installButton.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.installButton.setIcon(icon4)
        self.installButton.setObjectName("installButton")

        ######################### INSTALL BUTTON ##########################
        self.installButton.clicked.connect(self.installButtonAction)
        self.installButton.setVisible(False)
        ###################################################################

        self.mainGrid.addWidget(self.installButton, 9, 1, 1, 1)
        self.welcomeLabel = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.mainGrid.addWidget(self.welcomeLabel, 1, 0, 1, 3)
        self.lineBottom = QtWidgets.QFrame(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineBottom.sizePolicy().hasHeightForWidth())
        self.lineBottom.setSizePolicy(sizePolicy)
        self.lineBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBottom.setObjectName("lineBottom")
        self.mainGrid.addWidget(self.lineBottom, 10, 0, 1, 3)
        self.forumsButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forumsButton.sizePolicy().hasHeightForWidth())
        self.forumsButton.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/forums.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forumsButton.setIcon(icon5)
        self.forumsButton.setObjectName("forumsButton")

        ######################### FORUM BUTTON #########################
        self.forumsButton.clicked.connect(self.forumButtonAction)
        ################################################################

        self.mainGrid.addWidget(self.forumsButton, 6, 1, 1, 1)
        self.settingsLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.settingsLayout.setObjectName("settingsLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.settingsLayout.addItem(spacerItem2)
        self.launchAtStartCheck = QtWidgets.QCheckBox(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.launchAtStartCheck.sizePolicy().hasHeightForWidth())
        self.launchAtStartCheck.setSizePolicy(sizePolicy)
        self.launchAtStartCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.launchAtStartCheck.setObjectName("launchAtStartCheck")

        ######################### LAUNCH AT START BUTTON #########################
        self.launchAtStartCheck.clicked.connect(self.startCheckAction)
        ##########################################################################

        self.settingsLayout.addWidget(self.launchAtStartCheck)
        self.mainGrid.addLayout(self.settingsLayout, 11, 0, 1, 3)
        self.helpButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/helpus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setObjectName("helpButton")

        ######################### HELP BUTTON #########################
        self.helpButton.clicked.connect(self.helpButtonAction)
        ###############################################################

        self.mainGrid.addWidget(self.helpButton, 6, 2, 1, 1)
        self.newsButton = QtWidgets.QPushButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newsButton.sizePolicy().hasHeightForWidth())
        self.newsButton.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/usr/share/ctlos-welcome/img/news.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newsButton.setIcon(icon7)
        self.newsButton.setObjectName("newsButton")

        ######################### NEWS BUTTON ##########################
        self.newsButton.clicked.connect(self.newsButtonAction)
        ################################################################

        self.mainGrid.addWidget(self.newsButton, 6, 0, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setScaledContents(True)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.mainGrid.addWidget(self.infoLabel, 2, 0, 1, 3)
        self.gridLayout.addLayout(self.mainGrid, 0, 0, 1, 1)
        WelcomeScreen.setCentralWidget(self.MainWidget)

        self.retranslateUi(WelcomeScreen)
        QtCore.QMetaObject.connectSlotsByName(WelcomeScreen)

        ######################### LIVEUSER ? ##########################
        if os.path.isfile("/usr/bin/calamares_polkit"):
            self.installButton.setVisible(True)
            self.installationLabel.setVisible(True)
        ###############################################################

        ######################### IS AUTOSTART ? ######################
        homedir = os.path.expanduser('~')
        autostartfile = os.path.join(homedir, ".config/autostart/ctlos-welcome.desktop")
        if os.path.isfile(autostartfile):
            self.launchAtStartCheck.setChecked(True)
        ###############################################################

    def retranslateUi(self, WelcomeScreen):
        _translate = QtCore.QCoreApplication.translate
        WelcomeScreen.setWindowTitle(_translate("WelcomeScreen", "Welcome Ctlos Linux"))
        self.wikiButton.setText(_translate("WelcomeScreen", "Wiki"))
        self.linksLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ССЫЛКИ/LINKS:</span></p></body></html>"))
        self.donateButton.setText(_translate("WelcomeScreen", "Donate"))
        self.chatButton.setText(_translate("WelcomeScreen", "Chat"))
        self.installationLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INSTALL CTLOS:</span></p></body></html>"))
        self.installButton.setText(_translate("WelcomeScreen", "Install"))
        self.welcomeLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Ctlos Linux start</span></p></body></html>"))
        self.forumsButton.setText(_translate("WelcomeScreen", "Forum"))
        self.launchAtStartCheck.setText(_translate("WelcomeScreen", "AutoStart"))
        self.helpButton.setText(_translate("WelcomeScreen", "Bugs"))
        self.newsButton.setText(_translate("WelcomeScreen", "News"))
        self.infoLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Добро пожаловать в Ctlos Linux. Ссылки ниже помогут вам начать работу. Наслаждайтесь и не стесняйтесь присылать нам свои отзывы.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeScreen = QtWidgets.QMainWindow()
    ui = Ui_WelcomeScreen()
    ui.setupUi(WelcomeScreen)
    WelcomeScreen.show()
    sys.exit(app.exec_())

