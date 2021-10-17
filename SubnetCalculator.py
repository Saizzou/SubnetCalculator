from PyQt5 import QtCore, QtGui, QtWidgets
import ipaddress


class Ui_SubnetCalculator(object):
    def setupUi(self, SubnetCalculator):

        # ComboBox SubnetMask Items
        self.SubnetMaskA = ['255.0.0.0', '255.128.0.0', '255.192.0.0', '255.224.0.0', '255.240.0.0', '255.248.0.0',
                       '255.252.0.0', '255.254.0.0',
                       '255.255.0.0', '255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0',
                       '255.255.248.0', '255.255.252.0', '255.255.254.0',
                       '255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240',
                       '255.255.255.248', '255.255.255.252']

        self.SubnetMaskB = ['255.255.0.0', '255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0',
                       '255.255.248.0', '255.255.252.0', '255.255.254.0',
                       '255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240',
                       '255.255.255.248', '255.255.255.252']

        self.SubnetMaskC = ['255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240',
                       '255.255.255.248', '255.255.255.252']

        # Subnet Bits Items
        self.SubnetBitsA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                       '17', '18', '19', '20', '21', '22']

        self.SubnetBitsB = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

        self.SubnetBitsC = ['0', '1', '2', '3', '4', '5', '6']

        # Subnet ID Items
        self.SubnetIDA = ['10.0.0.0']
        self.SubnetIDB = ['172.16.0.0']
        self.SubnetIDC = ['192.168.0.0']

        # Maximum Subnet Items
        self.MaximumSubnetA = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192',
                          '16384', '32768', '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304']

        self.MaximumSubnetB = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512',
                          '1024', '2048', '4096', '8192', '16384']

        self.MaximumSubnetC = ['1', '2', '4', '8', '16', '32', '64']

        # Mask Bits Items
        self.MaskBitsA = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                     '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', ]

        self.MaskBitsB = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

        self.MaskBitsC = ['24', '25', '26', '27', '28', '29', '30']

        # Host per Subnets Items
        self.HostperSubnetA = ['16777214', '8388606', '4194302', '2097150', '1048574', '524286', '262142', '131070',
                          '65534', '32766', '16382', '8190', '4094', '2046', '1022', '510',
                          '254', '126', '62', '30', '14', '6', '2']

        self.HostperSubnetB = ['65534', '32766', '16382', '8190', '4094', '2046', '1022', '510',
                          '254', '126', '62', '30', '14', '6', '2']

        self.HostperSubnetC = ['254', '126', '62', '30', '14', '6', '2']

        # Wildcard Mask Items
        self.WildcardA = ['0.255.255.255', '0.127.255.255', '0.63.255.255', '0.31.255.255', '0.15.255.255',
                     '0.7.255.255', '0.3.255.255', '0.1.255.255',
                     '0.0.255.255', '0.0.127.255', '0.0.63.255', '0.0.31.255', '0.0.15.255', '0.0.7.255', '0.0.3.255',
                     '0.0.1.255',
                     '0.0.0.255', '0.0.0.127', '0.0.0.63', '0.0.0.31', '0.0.0.15', '0.0.0.7', '0.0.0.3']

        self.WildcardB = ['0.0.255.255', '0.0.127.255', '0.0.63.255', '0.0.31.255', '0.0.15.255', '0.0.7.255', '0.0.3.255',
                     '0.0.1.255',
                     '0.0.0.255', '0.0.0.127', '0.0.0.63', '0.0.0.31', '0.0.0.15', '0.0.0.7', '0.0.0.3']

        self.WildcardC = ['0.0.0.255', '0.0.0.127', '0.0.0.63', '0.0.0.31', '0.0.0.15', '0.0.0.7', '0.0.0.3']

        # Host Address Range Items
        self.HostRangeA = ['10.0.0.1 - 10.255.255.254', '10.0.0.1 - 10.127.255.254', '10.0.0.1 - 10.63.255.254',
                      '10.0.0.1 - 10.31.255.254', '10.0.0.1 - 10.15.255.254', '10.0.0.1 - 10.7.255.254',
                      '10.0.0.1 - 10.3.255.254', '10.0.0.1 - 10.1.255.254', '10.0.0.1 - 10.0.255.254',
                      '10.0.0.1 - 10.0.127.254', '10.0.0.1 - 10.0.63.254', '10.0.0.1 - 10.0.31.254',
                      '10.0.0.1 - 10.0.15.254', '10.0.0.1 - 10.0.7.254', '10.0.0.1 - 10.0.3.254',
                      '10.0.0.1 - 10.0.1.254', '10.0.0.1 - 10.0.0.254', '10.0.0.1 - 10.0.0.126', '10.0.0.1 - 10.0.0.62',
                      '10.0.0.1 - 10.0.0.30', '10.0.0.1 - 10.0.0.14', '10.0.0.1 - 10.0.0.6', '10.0.0.1 - 10.0.0.2']

        self.HostRangeB = ['172.16.0.1 - 172.16.255.254', '172.16.0.1 - 172.16.127.254', '172.16.0.1 - 172.16.63.254',
                      '172.16.0.1 - 172.16.31.254', '172.16.0.1 - 172.16.15.254', '172.16.0.1 - 172.16.7.254',
                      '172.16.0.1 - 172.16.3.254', '172.16.0.1 - 172.16.1.254', '172.16.0.1 - 172.16.0.254',
                      '172.16.0.1 - 172.16.0.126', '172.16.0.1 - 172.16.0.62', '172.16.0.1 - 172.16.0.30',
                      '172.16.0.1 - 172.16.0.14', '172.16.0.1 - 172.16.0.6', '172.16.0.1 - 172.16.0.2']

        self.HostRangeC = ['192.168.0.1 - 192.168.0.254', '192.168.0.1 - 192.168.0.126', '192.168.0.1 - 192.168.0.62',
                      '192.168.0.1 - 192.168.0.30', '192.168.0.1 - 192.168.0.14', '192.168.0.1 - 192.168.0.6',
                      '192.168.0.1 - 192.168.0.2']

        # Broadcast Address Items
        self.BroadcastA = ['10.255.255.255', '10.127.255.255', '10.63.255.255', '10.31.255.255', '10.15.255.255',
                      '10.7.255.255', '10.3.255.255', '10.1.255.255', '10.0.255.255', '10.0.127.255', '10.0.63.255',
                      '10.0.31.255', '10.0.15.255', '10.0.7.255', '10.0.3.255', '10.0.1.255', '10.0.0.255',
                      '10.0.0.127',
                      '10.0.0.63', '10.0.0.31', '10.0.0.15', '10.0.0.7', '10.0.0.3']

        self.BroadcastB = ['172.16.255.255', '172.16.127.255', '172.16.63.255', '172.16.31.255', '172.16.15.255',
                      '172.16.7.255', '172.16.3.255', '172.16.1.255', '172.16.0.255', '172.16.0.127', '172.16.0.63',
                      '172.16.0.31', '172.16.0.15', '172.16.0.7', '172.16.0.3']

        self.BroadcastC = ['192.168.0.255', '192.168.0.127', '192.168.0.63,', '192.168.0.31', '192.168.0.15', '192.168.0.7',
                      '192.168.0.3']


        SubnetCalculator.setObjectName("SubnetCalculator")
        SubnetCalculator.resize(400, 508)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SubnetCalculator.sizePolicy().hasHeightForWidth())
        SubnetCalculator.setSizePolicy(sizePolicy)
        self.label_SubnetCalculator = QtWidgets.QLabel(SubnetCalculator)
        self.label_SubnetCalculator.setGeometry(QtCore.QRect(130, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SubnetCalculator.setFont(font)
        self.label_SubnetCalculator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SubnetCalculator.setObjectName("label_SubnetCalculator")
        self.label_NetworkClass = QtWidgets.QLabel(SubnetCalculator)
        self.label_NetworkClass.setGeometry(QtCore.QRect(10, 40, 181, 18))
        self.label_NetworkClass.setObjectName("label_NetworkClass")
        self.radioButton_A = QtWidgets.QRadioButton(SubnetCalculator)
        self.radioButton_A.setGeometry(QtCore.QRect(10, 70, 41, 23))
        self.radioButton_A.setChecked(True)
        self.radioButton_A.setObjectName("radioButton_A")
        self.radioButton_B = QtWidgets.QRadioButton(SubnetCalculator)
        self.radioButton_B.setGeometry(QtCore.QRect(60, 70, 41, 23))
        self.radioButton_B.setObjectName("radioButton_B")
        self.radioButton_C = QtWidgets.QRadioButton(SubnetCalculator)
        self.radioButton_C.setGeometry(QtCore.QRect(110, 70, 41, 23))
        self.radioButton_C.setObjectName("radioButton_C")
        self.label_FirstOctet = QtWidgets.QLabel(SubnetCalculator)
        self.label_FirstOctet.setGeometry(QtCore.QRect(220, 40, 171, 18))
        self.label_FirstOctet.setObjectName("label_FirstOctet")
        self.lineEdit_FirstOctet = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_FirstOctet.setGeometry(QtCore.QRect(220, 60, 171, 32))
        self.lineEdit_FirstOctet.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_FirstOctet.setReadOnly(True)
        self.lineEdit_FirstOctet.setObjectName("lineEdit_FirstOctet")
        self.label_HexIpAddress = QtWidgets.QLabel(SubnetCalculator)
        self.label_HexIpAddress.setGeometry(QtCore.QRect(220, 100, 171, 18))
        self.label_HexIpAddress.setObjectName("label_HexIpAddress")
        self.lineEdit_HexIpAddress = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_HexIpAddress.setGeometry(QtCore.QRect(220, 120, 171, 32))
        self.lineEdit_HexIpAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_HexIpAddress.setReadOnly(True)
        self.lineEdit_HexIpAddress.setObjectName("lineEdit_HexIpAddress")
        self.label_IpAddress = QtWidgets.QLabel(SubnetCalculator)
        self.label_IpAddress.setGeometry(QtCore.QRect(10, 100, 171, 18))
        self.label_IpAddress.setObjectName("label_IpAddress")
        self.lineEdit_IpAddress = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_IpAddress.setGeometry(QtCore.QRect(10, 120, 171, 32))
        self.lineEdit_IpAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_IpAddress.setReadOnly(False)
        self.lineEdit_IpAddress.setObjectName("lineEdit_IpAddress")
        self.label_WildcardMask = QtWidgets.QLabel(SubnetCalculator)
        self.label_WildcardMask.setGeometry(QtCore.QRect(220, 160, 171, 18))
        self.label_WildcardMask.setObjectName("label_WildcardMask")
        self.lineEdit_WildcardMask = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_WildcardMask.setGeometry(QtCore.QRect(220, 180, 171, 32))
        self.lineEdit_WildcardMask.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_WildcardMask.setReadOnly(True)
        self.lineEdit_WildcardMask.setObjectName("lineEdit_WildcardMask")
        self.label_SubnetMask = QtWidgets.QLabel(SubnetCalculator)
        self.label_SubnetMask.setGeometry(QtCore.QRect(10, 160, 171, 18))
        self.label_SubnetMask.setObjectName("label_SubnetMask")
        self.comboBox_SubnetMask = QtWidgets.QComboBox(SubnetCalculator)
        self.comboBox_SubnetMask.setGeometry(QtCore.QRect(10, 180, 171, 32))
        self.comboBox_SubnetMask.setObjectName("comboBox_SubnetMask")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetMask.addItem("")
        self.comboBox_SubnetBits = QtWidgets.QComboBox(SubnetCalculator)
        self.comboBox_SubnetBits.setGeometry(QtCore.QRect(10, 240, 171, 32))
        self.comboBox_SubnetBits.setObjectName("comboBox_SubnetBits")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.comboBox_SubnetBits.addItem("")
        self.label_SubnetBits = QtWidgets.QLabel(SubnetCalculator)
        self.label_SubnetBits.setGeometry(QtCore.QRect(10, 220, 171, 18))
        self.label_SubnetBits.setObjectName("label_SubnetBits")
        self.comboBox_MaskBits = QtWidgets.QComboBox(SubnetCalculator)
        self.comboBox_MaskBits.setGeometry(QtCore.QRect(220, 240, 171, 32))
        self.comboBox_MaskBits.setObjectName("comboBox_MaskBits")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.comboBox_MaskBits.addItem("")
        self.label_MaskBits = QtWidgets.QLabel(SubnetCalculator)
        self.label_MaskBits.setGeometry(QtCore.QRect(220, 220, 171, 18))
        self.label_MaskBits.setObjectName("label_MaskBits")
        self.label_MaximumSubnet = QtWidgets.QLabel(SubnetCalculator)
        self.label_MaximumSubnet.setGeometry(QtCore.QRect(10, 280, 171, 18))
        self.label_MaximumSubnet.setObjectName("label_MaximumSubnet")
        self.comboBox_MaxSubnet = QtWidgets.QComboBox(SubnetCalculator)
        self.comboBox_MaxSubnet.setGeometry(QtCore.QRect(10, 300, 171, 32))
        self.comboBox_MaxSubnet.setObjectName("comboBox_MaxSubnet")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.comboBox_MaxSubnet.addItem("")
        self.label_HostPerSubnet = QtWidgets.QLabel(SubnetCalculator)
        self.label_HostPerSubnet.setGeometry(QtCore.QRect(220, 280, 171, 18))
        self.label_HostPerSubnet.setObjectName("label_HostPerSubnet")
        self.comboBox_HostPerSubnet = QtWidgets.QComboBox(SubnetCalculator)
        self.comboBox_HostPerSubnet.setGeometry(QtCore.QRect(220, 300, 171, 32))
        self.comboBox_HostPerSubnet.setObjectName("comboBox_HostPerSubnet")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.comboBox_HostPerSubnet.addItem("")
        self.label_HostRange = QtWidgets.QLabel(SubnetCalculator)
        self.label_HostRange.setGeometry(QtCore.QRect(10, 350, 171, 18))
        self.label_HostRange.setObjectName("label_HostRange")
        self.lineEdit_HostRange = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_HostRange.setGeometry(QtCore.QRect(10, 370, 371, 32))
        self.lineEdit_HostRange.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_HostRange.setReadOnly(True)
        self.lineEdit_HostRange.setObjectName("lineEdit_HostRange")
        self.lineEdit_SubnetID = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_SubnetID.setGeometry(QtCore.QRect(10, 430, 171, 32))
        self.lineEdit_SubnetID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_SubnetID.setReadOnly(True)
        self.lineEdit_SubnetID.setObjectName("lineEdit_SubnetID")
        self.label_SubnetID = QtWidgets.QLabel(SubnetCalculator)
        self.label_SubnetID.setGeometry(QtCore.QRect(10, 410, 171, 18))
        self.label_SubnetID.setObjectName("label_SubnetID")
        self.lineEdit_BroadcastAddress = QtWidgets.QLineEdit(SubnetCalculator)
        self.lineEdit_BroadcastAddress.setGeometry(QtCore.QRect(210, 430, 171, 32))
        self.lineEdit_BroadcastAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_BroadcastAddress.setReadOnly(True)
        self.lineEdit_BroadcastAddress.setObjectName("lineEdit_BroadcastAddress")
        self.label_BroadcastAddress = QtWidgets.QLabel(SubnetCalculator)
        self.label_BroadcastAddress.setGeometry(QtCore.QRect(210, 410, 171, 18))
        self.label_BroadcastAddress.setObjectName("label_BroadcastAddress")
        self.btn_ExitSubnetCalculator = QtWidgets.QPushButton(SubnetCalculator)
        self.btn_ExitSubnetCalculator.setGeometry(QtCore.QRect(290, 470, 88, 34))
        self.btn_ExitSubnetCalculator.setObjectName("btn_ExitSubnetCalculator")

        # Button, RadioButton, LineEdit, Combobox Connections
        self.radioButton_A.clicked.connect(self.changes_radioButton)
        self.radioButton_B.clicked.connect(self.changes_radioButton)
        self.radioButton_C.clicked.connect(self.changes_radioButton)
        self.btn_ExitSubnetCalculator.clicked.connect(self.close)
        self.comboBox_SubnetMask.currentIndexChanged.connect(self.changes_comboBox)
        self.comboBox_SubnetBits.currentIndexChanged.connect(self.changes_comboBox)
        self.comboBox_MaxSubnet.currentIndexChanged.connect(self.changes_comboBox)
        self.comboBox_MaskBits.currentIndexChanged.connect(self.changes_comboBox)
        self.comboBox_HostPerSubnet.currentIndexChanged.connect(self.changes_comboBox)
        self.lineEdit_IpAddress.returnPressed.connect(self.changes_ip_address)

        self.retranslateUi(SubnetCalculator)
        QtCore.QMetaObject.connectSlotsByName(SubnetCalculator)

    def retranslateUi(self, SubnetCalculator):
        _translate = QtCore.QCoreApplication.translate
        SubnetCalculator.setWindowTitle(_translate("SubnetCalculator", "Subnet Calculator"))
        self.label_SubnetCalculator.setText(_translate("SubnetCalculator", "Subnet Calculator"))
        self.label_NetworkClass.setText(_translate("SubnetCalculator", "Network Class:"))
        self.radioButton_A.setText(_translate("SubnetCalculator", "A"))
        self.radioButton_B.setText(_translate("SubnetCalculator", "B"))
        self.radioButton_C.setText(_translate("SubnetCalculator", "C"))
        self.label_FirstOctet.setText(_translate("SubnetCalculator", "First Octet Range:"))
        self.lineEdit_FirstOctet.setText(_translate("SubnetCalculator", "1-126"))
        self.label_HexIpAddress.setText(_translate("SubnetCalculator", "Hex IP Address:"))
        self.lineEdit_HexIpAddress.setText(_translate("SubnetCalculator", "0A.00.00.01"))
        self.label_IpAddress.setText(_translate("SubnetCalculator", "IP Address:"))
        self.lineEdit_IpAddress.setText(_translate("SubnetCalculator", "10.0.0.1"))
        self.label_WildcardMask.setText(_translate("SubnetCalculator", "Wildcard Mask:"))
        self.lineEdit_WildcardMask.setText(_translate("SubnetCalculator", "0.255.255.255"))
        self.label_SubnetMask.setText(_translate("SubnetCalculator", "Subnet Mask:"))
        self.comboBox_SubnetMask.setItemText(0, _translate("SubnetCalculator", "255.0.0.0"))
        self.comboBox_SubnetMask.setItemText(1, _translate("SubnetCalculator", "255.128.0.0"))
        self.comboBox_SubnetMask.setItemText(2, _translate("SubnetCalculator", "255.192.0.0"))
        self.comboBox_SubnetMask.setItemText(3, _translate("SubnetCalculator", "255.224.0.0"))
        self.comboBox_SubnetMask.setItemText(4, _translate("SubnetCalculator", "255.240.0.0"))
        self.comboBox_SubnetMask.setItemText(5, _translate("SubnetCalculator", "255.248.0.0"))
        self.comboBox_SubnetMask.setItemText(6, _translate("SubnetCalculator", "255.252.0.0"))
        self.comboBox_SubnetMask.setItemText(7, _translate("SubnetCalculator", "255.254.0.0"))
        self.comboBox_SubnetMask.setItemText(8, _translate("SubnetCalculator", "255.255.0.0"))
        self.comboBox_SubnetMask.setItemText(9, _translate("SubnetCalculator", "255.255.128.0"))
        self.comboBox_SubnetMask.setItemText(10, _translate("SubnetCalculator", "255.255.192.0"))
        self.comboBox_SubnetMask.setItemText(11, _translate("SubnetCalculator", "255.255.224.0"))
        self.comboBox_SubnetMask.setItemText(12, _translate("SubnetCalculator", "255.255.240.0"))
        self.comboBox_SubnetMask.setItemText(13, _translate("SubnetCalculator", "255.255.248.0"))
        self.comboBox_SubnetMask.setItemText(14, _translate("SubnetCalculator", "255.255.252.0"))
        self.comboBox_SubnetMask.setItemText(15, _translate("SubnetCalculator", "255.255.254.0"))
        self.comboBox_SubnetMask.setItemText(16, _translate("SubnetCalculator", "255.255.255.0"))
        self.comboBox_SubnetMask.setItemText(17, _translate("SubnetCalculator", "255.255.255.128"))
        self.comboBox_SubnetMask.setItemText(18, _translate("SubnetCalculator", "255.255.255.192"))
        self.comboBox_SubnetMask.setItemText(19, _translate("SubnetCalculator", "255.255.255.224"))
        self.comboBox_SubnetMask.setItemText(20, _translate("SubnetCalculator", "255.255.255.240"))
        self.comboBox_SubnetMask.setItemText(21, _translate("SubnetCalculator", "255.255.255.248"))
        self.comboBox_SubnetMask.setItemText(22, _translate("SubnetCalculator", "255.255.255.252"))
        self.comboBox_SubnetBits.setItemText(0, _translate("SubnetCalculator", "0"))
        self.comboBox_SubnetBits.setItemText(1, _translate("SubnetCalculator", "1"))
        self.comboBox_SubnetBits.setItemText(2, _translate("SubnetCalculator", "2"))
        self.comboBox_SubnetBits.setItemText(3, _translate("SubnetCalculator", "3"))
        self.comboBox_SubnetBits.setItemText(4, _translate("SubnetCalculator", "4"))
        self.comboBox_SubnetBits.setItemText(5, _translate("SubnetCalculator", "5"))
        self.comboBox_SubnetBits.setItemText(6, _translate("SubnetCalculator", "6"))
        self.comboBox_SubnetBits.setItemText(7, _translate("SubnetCalculator", "7"))
        self.comboBox_SubnetBits.setItemText(8, _translate("SubnetCalculator", "8"))
        self.comboBox_SubnetBits.setItemText(9, _translate("SubnetCalculator", "9"))
        self.comboBox_SubnetBits.setItemText(10, _translate("SubnetCalculator", "10"))
        self.comboBox_SubnetBits.setItemText(11, _translate("SubnetCalculator", "11"))
        self.comboBox_SubnetBits.setItemText(12, _translate("SubnetCalculator", "12"))
        self.comboBox_SubnetBits.setItemText(13, _translate("SubnetCalculator", "13"))
        self.comboBox_SubnetBits.setItemText(14, _translate("SubnetCalculator", "14"))
        self.comboBox_SubnetBits.setItemText(15, _translate("SubnetCalculator", "15"))
        self.comboBox_SubnetBits.setItemText(16, _translate("SubnetCalculator", "16"))
        self.comboBox_SubnetBits.setItemText(17, _translate("SubnetCalculator", "17"))
        self.comboBox_SubnetBits.setItemText(18, _translate("SubnetCalculator", "18"))
        self.comboBox_SubnetBits.setItemText(19, _translate("SubnetCalculator", "19"))
        self.comboBox_SubnetBits.setItemText(20, _translate("SubnetCalculator", "20"))
        self.comboBox_SubnetBits.setItemText(21, _translate("SubnetCalculator", "21"))
        self.comboBox_SubnetBits.setItemText(22, _translate("SubnetCalculator", "22"))
        self.label_SubnetBits.setText(_translate("SubnetCalculator", "Subnet Bits:"))
        self.comboBox_MaskBits.setItemText(0, _translate("SubnetCalculator", "8"))
        self.comboBox_MaskBits.setItemText(1, _translate("SubnetCalculator", "9"))
        self.comboBox_MaskBits.setItemText(2, _translate("SubnetCalculator", "10"))
        self.comboBox_MaskBits.setItemText(3, _translate("SubnetCalculator", "11"))
        self.comboBox_MaskBits.setItemText(4, _translate("SubnetCalculator", "12"))
        self.comboBox_MaskBits.setItemText(5, _translate("SubnetCalculator", "13"))
        self.comboBox_MaskBits.setItemText(6, _translate("SubnetCalculator", "14"))
        self.comboBox_MaskBits.setItemText(7, _translate("SubnetCalculator", "15"))
        self.comboBox_MaskBits.setItemText(8, _translate("SubnetCalculator", "16"))
        self.comboBox_MaskBits.setItemText(9, _translate("SubnetCalculator", "17"))
        self.comboBox_MaskBits.setItemText(10, _translate("SubnetCalculator", "18"))
        self.comboBox_MaskBits.setItemText(11, _translate("SubnetCalculator", "19"))
        self.comboBox_MaskBits.setItemText(12, _translate("SubnetCalculator", "20"))
        self.comboBox_MaskBits.setItemText(13, _translate("SubnetCalculator", "21"))
        self.comboBox_MaskBits.setItemText(14, _translate("SubnetCalculator", "22"))
        self.comboBox_MaskBits.setItemText(15, _translate("SubnetCalculator", "23"))
        self.comboBox_MaskBits.setItemText(16, _translate("SubnetCalculator", "24"))
        self.comboBox_MaskBits.setItemText(17, _translate("SubnetCalculator", "25"))
        self.comboBox_MaskBits.setItemText(18, _translate("SubnetCalculator", "26"))
        self.comboBox_MaskBits.setItemText(19, _translate("SubnetCalculator", "27"))
        self.comboBox_MaskBits.setItemText(20, _translate("SubnetCalculator", "28"))
        self.comboBox_MaskBits.setItemText(21, _translate("SubnetCalculator", "29"))
        self.comboBox_MaskBits.setItemText(22, _translate("SubnetCalculator", "30"))
        self.label_MaskBits.setText(_translate("SubnetCalculator", "Mask Bits:"))
        self.label_MaximumSubnet.setText(_translate("SubnetCalculator", "Maximum Subnet:"))
        self.comboBox_MaxSubnet.setItemText(0, _translate("SubnetCalculator", "1"))
        self.comboBox_MaxSubnet.setItemText(1, _translate("SubnetCalculator", "2"))
        self.comboBox_MaxSubnet.setItemText(2, _translate("SubnetCalculator", "4"))
        self.comboBox_MaxSubnet.setItemText(3, _translate("SubnetCalculator", "8"))
        self.comboBox_MaxSubnet.setItemText(4, _translate("SubnetCalculator", "16"))
        self.comboBox_MaxSubnet.setItemText(5, _translate("SubnetCalculator", "32"))
        self.comboBox_MaxSubnet.setItemText(6, _translate("SubnetCalculator", "64"))
        self.comboBox_MaxSubnet.setItemText(7, _translate("SubnetCalculator", "128"))
        self.comboBox_MaxSubnet.setItemText(8, _translate("SubnetCalculator", "256"))
        self.comboBox_MaxSubnet.setItemText(9, _translate("SubnetCalculator", "512"))
        self.comboBox_MaxSubnet.setItemText(10, _translate("SubnetCalculator", "1024"))
        self.comboBox_MaxSubnet.setItemText(11, _translate("SubnetCalculator", "2048"))
        self.comboBox_MaxSubnet.setItemText(12, _translate("SubnetCalculator", "4096"))
        self.comboBox_MaxSubnet.setItemText(13, _translate("SubnetCalculator", "8192"))
        self.comboBox_MaxSubnet.setItemText(14, _translate("SubnetCalculator", "16384"))
        self.comboBox_MaxSubnet.setItemText(15, _translate("SubnetCalculator", "32768"))
        self.comboBox_MaxSubnet.setItemText(16, _translate("SubnetCalculator", "65536"))
        self.comboBox_MaxSubnet.setItemText(17, _translate("SubnetCalculator", "131072"))
        self.comboBox_MaxSubnet.setItemText(18, _translate("SubnetCalculator", "262144"))
        self.comboBox_MaxSubnet.setItemText(19, _translate("SubnetCalculator", "524288"))
        self.comboBox_MaxSubnet.setItemText(20, _translate("SubnetCalculator", "1048576"))
        self.comboBox_MaxSubnet.setItemText(21, _translate("SubnetCalculator", "2097152"))
        self.comboBox_MaxSubnet.setItemText(22, _translate("SubnetCalculator", "4194304"))
        self.label_HostPerSubnet.setText(_translate("SubnetCalculator", "Hosts per Subnet:"))
        self.comboBox_HostPerSubnet.setItemText(0, _translate("SubnetCalculator", "16777214"))
        self.comboBox_HostPerSubnet.setItemText(1, _translate("SubnetCalculator", "8388606"))
        self.comboBox_HostPerSubnet.setItemText(2, _translate("SubnetCalculator", "4194302"))
        self.comboBox_HostPerSubnet.setItemText(3, _translate("SubnetCalculator", "2097150"))
        self.comboBox_HostPerSubnet.setItemText(4, _translate("SubnetCalculator", "1048574"))
        self.comboBox_HostPerSubnet.setItemText(5, _translate("SubnetCalculator", "524286"))
        self.comboBox_HostPerSubnet.setItemText(6, _translate("SubnetCalculator", "262142"))
        self.comboBox_HostPerSubnet.setItemText(7, _translate("SubnetCalculator", "131070"))
        self.comboBox_HostPerSubnet.setItemText(8, _translate("SubnetCalculator", "65534"))
        self.comboBox_HostPerSubnet.setItemText(9, _translate("SubnetCalculator", "32766"))
        self.comboBox_HostPerSubnet.setItemText(10, _translate("SubnetCalculator", "16382"))
        self.comboBox_HostPerSubnet.setItemText(11, _translate("SubnetCalculator", "8190"))
        self.comboBox_HostPerSubnet.setItemText(12, _translate("SubnetCalculator", "4094"))
        self.comboBox_HostPerSubnet.setItemText(13, _translate("SubnetCalculator", "2046"))
        self.comboBox_HostPerSubnet.setItemText(14, _translate("SubnetCalculator", "1022"))
        self.comboBox_HostPerSubnet.setItemText(15, _translate("SubnetCalculator", "510"))
        self.comboBox_HostPerSubnet.setItemText(16, _translate("SubnetCalculator", "254"))
        self.comboBox_HostPerSubnet.setItemText(17, _translate("SubnetCalculator", "126"))
        self.comboBox_HostPerSubnet.setItemText(18, _translate("SubnetCalculator", "62"))
        self.comboBox_HostPerSubnet.setItemText(19, _translate("SubnetCalculator", "30"))
        self.comboBox_HostPerSubnet.setItemText(20, _translate("SubnetCalculator", "14"))
        self.comboBox_HostPerSubnet.setItemText(21, _translate("SubnetCalculator", "6"))
        self.comboBox_HostPerSubnet.setItemText(22, _translate("SubnetCalculator", "2"))
        self.label_HostRange.setText(_translate("SubnetCalculator", "Host Address Range:"))
        self.lineEdit_HostRange.setText(_translate("SubnetCalculator", "10.0.0.1-10.255.255.255"))
        self.lineEdit_SubnetID.setText(_translate("SubnetCalculator", "10.0.0.0"))
        self.label_SubnetID.setText(_translate("SubnetCalculator", "Subnet ID:"))
        self.lineEdit_BroadcastAddress.setText(_translate("SubnetCalculator", "10.255.255.255"))
        self.label_BroadcastAddress.setText(_translate("SubnetCalculator", "Broadcast Address:"))
        self.btn_ExitSubnetCalculator.setText(_translate("SubnetCalculator", "Exit"))


    def changes_ip_address(self):
        """ Automatically changes the Values in the LineEdits depends on the lineEdit_IpAddress and the Subnet. """
        try:
            ipaddr = self.lineEdit_IpAddress.text()
            subnet = self.comboBox_MaskBits.currentText()
            ip_subnet = ipaddr + "/" + subnet
            interface= ipaddress.IPv4Interface(ip_subnet)
            ipcidr = ipaddress.IPv4Network(interface.network)
            broadcast = ipcidr.broadcast_address
            hexal_ip = '.'.join([hex(int(x) + 256)[3:] for x in ipaddr.split('.')]).upper()
            range_start = interface.network.network_address + 1
            range_end = broadcast - 1
            self.lineEdit_BroadcastAddress.setText(str(broadcast))
            self.lineEdit_HexIpAddress.setText(hexal_ip)
            self.lineEdit_HostRange.setText(str(range_start) + " - " + str(range_end))
        except:
            self.lineEdit_IpAddress.setText("Unresolved IP")

    def changes_comboBox(self, value):
        """ Automatically changes the Values in the ComboBoxes, LineEdits and RadioButtons for a Possible Subnet. """

        if self.radioButton_A.isChecked():
            self.comboBox_MaxSubnet.setCurrentIndex(value)
            self.comboBox_SubnetMask.setCurrentIndex(value)
            self.comboBox_SubnetBits.setCurrentIndex(value)
            self.comboBox_MaskBits.setCurrentIndex(value)
            self.comboBox_HostPerSubnet.setCurrentIndex(value)
            self.lineEdit_HostRange.setText(self.HostRangeA[value])
            self.lineEdit_SubnetID.setText(self.SubnetIDA[0])
            self.lineEdit_BroadcastAddress.setText(self.BroadcastA[value])
            self.lineEdit_WildcardMask.setText(self.WildcardA[value])
            self.lineEdit_BroadcastAddress.setText(self.BroadcastA[value])


        elif self.radioButton_B.isChecked():
            self.comboBox_MaxSubnet.setCurrentIndex(value)
            self.comboBox_SubnetMask.setCurrentIndex(value)
            self.comboBox_SubnetBits.setCurrentIndex(value)
            self.comboBox_MaskBits.setCurrentIndex(value)
            self.comboBox_HostPerSubnet.setCurrentIndex(value)
            self.lineEdit_HostRange.setText(self.HostRangeB[value])
            self.lineEdit_SubnetID.setText(self.SubnetIDB[0])
            self.lineEdit_BroadcastAddress.setText(self.BroadcastB[value])
            self.lineEdit_WildcardMask.setText(self.WildcardB[value])
            self.lineEdit_BroadcastAddress.setText(self.BroadcastB[value])

        elif self.radioButton_C.isChecked():
            self.comboBox_MaxSubnet.setCurrentIndex(value)
            self.comboBox_SubnetMask.setCurrentIndex(value)
            self.comboBox_SubnetBits.setCurrentIndex(value)
            self.comboBox_MaskBits.setCurrentIndex(value)
            self.comboBox_HostPerSubnet.setCurrentIndex(value)
            self.lineEdit_HostRange.setText(self.HostRangeC[value])
            self.lineEdit_SubnetID.setText(self.SubnetIDC[0])
            self.lineEdit_BroadcastAddress.setText(self.BroadcastC[value])
            self.lineEdit_WildcardMask.setText(self.WildcardC[value])
            self.lineEdit_BroadcastAddress.setText(self.BroadcastC[value])



    def changes_radioButton(self):
        """ Automatically changes the Values in the ComboBoxes, LineEdits and RadioButtons for a Possible Subnet. """

        if self.radioButton_A.isChecked():
            self.lineEdit_FirstOctet.setText("1-126")
            self.lineEdit_IpAddress.setText("10.0.0.1")
            self.lineEdit_HexIpAddress.setText("0A.00.00.01")
            self.lineEdit_WildcardMask.setText("0.255.255.255")
            self.lineEdit_HostRange.setText("10.0.0.1 - 10.255.255.254")
            self.lineEdit_SubnetID.setText(self.SubnetIDA[0])
            self.lineEdit_BroadcastAddress.setText("10.255.255.255")
            # Combobox Edit
            self.comboBox_SubnetMask.clear()
            self.comboBox_SubnetMask.addItems(self.SubnetMaskA)
            self.comboBox_MaskBits.clear()
            self.comboBox_MaskBits.addItems(self.MaskBitsA)
            self.comboBox_MaxSubnet.clear()
            self.comboBox_MaxSubnet.addItems(self.MaximumSubnetA)
            self.comboBox_HostPerSubnet.clear()
            self.comboBox_HostPerSubnet.addItems(self.HostperSubnetA)
            self.comboBox_SubnetBits.clear()
            self.comboBox_SubnetBits.addItems(self.SubnetBitsA)

        elif self.radioButton_B.isChecked():
            self.lineEdit_FirstOctet.setText("128-191")
            self.lineEdit_IpAddress.setText("172.16.0.1")
            self.lineEdit_HexIpAddress.setText("AC.10.00.01")
            self.lineEdit_WildcardMask.setText("0.0.255.255")
            self.lineEdit_HostRange.setText("172.16.0.1 - 172.16.255.254")
            self.lineEdit_SubnetID.setText(self.SubnetIDB[0])
            self.lineEdit_BroadcastAddress.setText("172.16.255.255")
            # Combobox Edit
            self.comboBox_SubnetMask.clear()
            self.comboBox_SubnetMask.addItems(self.SubnetMaskB)
            self.comboBox_MaskBits.clear()
            self.comboBox_MaskBits.addItems(self.MaskBitsB)
            self.comboBox_MaxSubnet.clear()
            self.comboBox_MaxSubnet.addItems(self.MaximumSubnetB)
            self.comboBox_HostPerSubnet.clear()
            self.comboBox_HostPerSubnet.addItems(self.HostperSubnetB)
            self.comboBox_SubnetBits.clear()
            self.comboBox_SubnetBits.addItems(self.SubnetBitsB)

        elif self.radioButton_C.isChecked():
            self.lineEdit_FirstOctet.setText("192-223")
            self.lineEdit_IpAddress.setText("192.168.0.1")
            self.lineEdit_HexIpAddress.setText("C0.A8.00.01")
            self.lineEdit_WildcardMask.setText("0.0.0.255")
            self.lineEdit_HostRange.setText("192.168.0.1 - 192.168.0.254")
            self.lineEdit_SubnetID.setText(self.SubnetIDC[0])
            self.lineEdit_BroadcastAddress.setText("192.168.0.255")
            # Combobox Edit
            self.comboBox_SubnetMask.clear()
            self.comboBox_SubnetMask.addItems(self.SubnetMaskC)
            self.comboBox_MaskBits.clear()
            self.comboBox_MaskBits.addItems(self.MaskBitsC)
            self.comboBox_MaxSubnet.clear()
            self.comboBox_MaxSubnet.addItems(self.MaximumSubnetC)
            self.comboBox_HostPerSubnet.clear()
            self.comboBox_HostPerSubnet.addItems(self.HostperSubnetC)
            self.comboBox_SubnetBits.clear()
            self.comboBox_SubnetBits.addItems(self.SubnetBitsC)

    def close(self):
        """ Closes the Subnet Calculator Window"""

        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubnetCalculator = QtWidgets.QWidget()
    ui = Ui_SubnetCalculator()
    ui.setupUi(SubnetCalculator)
    SubnetCalculator.show()
    sys.exit(app.exec_())
