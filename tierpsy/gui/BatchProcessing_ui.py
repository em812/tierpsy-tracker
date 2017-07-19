# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BatchProcessing.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchProcessing(object):
    def setupUi(self, BatchProcessing):
        BatchProcessing.setObjectName("BatchProcessing")
        BatchProcessing.resize(702, 483)
        self.centralwidget = QtWidgets.QWidget(BatchProcessing)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.p_video_dir_root = QtWidgets.QLineEdit(self.centralwidget)
        self.p_video_dir_root.setObjectName("p_video_dir_root")
        self.gridLayout_2.addWidget(self.p_video_dir_root, 0, 2, 1, 1)
        self.pushButton_videosDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_videosDir.setObjectName("pushButton_videosDir")
        self.gridLayout_2.addWidget(self.pushButton_videosDir, 0, 1, 1, 1)
        self.p_tmp_dir_root = QtWidgets.QLineEdit(self.centralwidget)
        self.p_tmp_dir_root.setObjectName("p_tmp_dir_root")
        self.gridLayout_2.addWidget(self.p_tmp_dir_root, 5, 2, 1, 1)
        self.p_videos_list = QtWidgets.QLineEdit(self.centralwidget)
        self.p_videos_list.setEnabled(True)
        self.p_videos_list.setObjectName("p_videos_list")
        self.gridLayout_2.addWidget(self.p_videos_list, 1, 2, 1, 1)
        self.p_mask_dir_root = QtWidgets.QLineEdit(self.centralwidget)
        self.p_mask_dir_root.setObjectName("p_mask_dir_root")
        self.gridLayout_2.addWidget(self.p_mask_dir_root, 2, 2, 1, 1)
        self.pushButton_tmpDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tmpDir.setObjectName("pushButton_tmpDir")
        self.gridLayout_2.addWidget(self.pushButton_tmpDir, 5, 1, 1, 1)
        self.pushButton_txtFileList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_txtFileList.setEnabled(True)
        self.pushButton_txtFileList.setObjectName("pushButton_txtFileList")
        self.gridLayout_2.addWidget(self.pushButton_txtFileList, 1, 1, 1, 1)
        self.pushButton_masksDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_masksDir.setObjectName("pushButton_masksDir")
        self.gridLayout_2.addWidget(self.pushButton_masksDir, 2, 1, 1, 1)
        self.p_results_dir_root = QtWidgets.QLineEdit(self.centralwidget)
        self.p_results_dir_root.setObjectName("p_results_dir_root")
        self.gridLayout_2.addWidget(self.p_results_dir_root, 3, 2, 1, 1)
        self.pushButton_paramFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paramFile.setObjectName("pushButton_paramFile")
        self.gridLayout_2.addWidget(self.pushButton_paramFile, 4, 1, 1, 1)
        self.pushButton_resultsDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_resultsDir.setObjectName("pushButton_resultsDir")
        self.gridLayout_2.addWidget(self.pushButton_resultsDir, 3, 1, 1, 1)
        self.checkBox_txtFileList = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_txtFileList.sizePolicy().hasHeightForWidth())
        self.checkBox_txtFileList.setSizePolicy(sizePolicy)
        self.checkBox_txtFileList.setText("")
        self.checkBox_txtFileList.setObjectName("checkBox_txtFileList")
        self.gridLayout_2.addWidget(self.checkBox_txtFileList, 1, 0, 1, 1)
        self.checkBox_tmpDir = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_tmpDir.sizePolicy().hasHeightForWidth())
        self.checkBox_tmpDir.setSizePolicy(sizePolicy)
        self.checkBox_tmpDir.setText("")
        self.checkBox_tmpDir.setObjectName("checkBox_tmpDir")
        self.gridLayout_2.addWidget(self.checkBox_tmpDir, 5, 0, 1, 1)
        self.p_json_file = QtWidgets.QComboBox(self.centralwidget)
        self.p_json_file.setEditable(True)
        self.p_json_file.setObjectName("p_json_file")
        self.gridLayout_2.addWidget(self.p_json_file, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.p_pattern_exclude = QtWidgets.QLineEdit(self.centralwidget)
        self.p_pattern_exclude.setObjectName("p_pattern_exclude")
        self.gridLayout_3.addWidget(self.p_pattern_exclude, 1, 2, 1, 1)
        self.p_copy_unfinished = QtWidgets.QCheckBox(self.centralwidget)
        self.p_copy_unfinished.setObjectName("p_copy_unfinished")
        self.gridLayout_3.addWidget(self.p_copy_unfinished, 5, 1, 1, 2)
        self.p_is_copy_video = QtWidgets.QCheckBox(self.centralwidget)
        self.p_is_copy_video.setObjectName("p_is_copy_video")
        self.gridLayout_3.addWidget(self.p_is_copy_video, 6, 1, 1, 2)
        self.p_only_summary = QtWidgets.QCheckBox(self.centralwidget)
        self.p_only_summary.setObjectName("p_only_summary")
        self.gridLayout_3.addWidget(self.p_only_summary, 7, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 3, 1, 1)
        self.label_patternExc = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_patternExc.sizePolicy().hasHeightForWidth())
        self.label_patternExc.setSizePolicy(sizePolicy)
        self.label_patternExc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_patternExc.setWordWrap(True)
        self.label_patternExc.setObjectName("label_patternExc")
        self.gridLayout_3.addWidget(self.label_patternExc, 0, 2, 1, 1)
        self.p_pattern_include = QtWidgets.QLineEdit(self.centralwidget)
        self.p_pattern_include.setObjectName("p_pattern_include")
        self.gridLayout_3.addWidget(self.p_pattern_include, 1, 1, 1, 1)
        self.label_patternIn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_patternIn.sizePolicy().hasHeightForWidth())
        self.label_patternIn.setSizePolicy(sizePolicy)
        self.label_patternIn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_patternIn.setWordWrap(True)
        self.label_patternIn.setObjectName("label_patternIn")
        self.gridLayout_3.addWidget(self.label_patternIn, 0, 1, 1, 1)
        self.p_unmet_requirements = QtWidgets.QCheckBox(self.centralwidget)
        self.p_unmet_requirements.setObjectName("p_unmet_requirements")
        self.gridLayout_3.addWidget(self.p_unmet_requirements, 7, 3, 1, 2)
        self.p_max_num_process = QtWidgets.QSpinBox(self.centralwidget)
        self.p_max_num_process.setObjectName("p_max_num_process")
        self.gridLayout_3.addWidget(self.p_max_num_process, 3, 1, 1, 1)
        self.label_numMaxProc = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_numMaxProc.sizePolicy().hasHeightForWidth())
        self.label_numMaxProc.setSizePolicy(sizePolicy)
        self.label_numMaxProc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_numMaxProc.setWordWrap(True)
        self.label_numMaxProc.setObjectName("label_numMaxProc")
        self.gridLayout_3.addWidget(self.label_numMaxProc, 2, 1, 1, 1)
        self.p_force_start_point = QtWidgets.QComboBox(self.centralwidget)
        self.p_force_start_point.setObjectName("p_force_start_point")
        self.gridLayout_3.addWidget(self.p_force_start_point, 1, 3, 1, 3)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 6, 5, 2, 1)
        self.p_end_point = QtWidgets.QComboBox(self.centralwidget)
        self.p_end_point.setObjectName("p_end_point")
        self.gridLayout_3.addWidget(self.p_end_point, 3, 3, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        BatchProcessing.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BatchProcessing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 22))
        self.menubar.setObjectName("menubar")
        BatchProcessing.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BatchProcessing)
        self.statusbar.setObjectName("statusbar")
        BatchProcessing.setStatusBar(self.statusbar)

        self.retranslateUi(BatchProcessing)
        QtCore.QMetaObject.connectSlotsByName(BatchProcessing)

    def retranslateUi(self, BatchProcessing):
        _translate = QtCore.QCoreApplication.translate
        BatchProcessing.setWindowTitle(_translate("BatchProcessing", "Batch Processing"))
        self.pushButton_videosDir.setText(_translate("BatchProcessing", "Original Videos Dir"))
        self.pushButton_tmpDir.setText(_translate("BatchProcessing", "Temporary Dir"))
        self.pushButton_txtFileList.setText(_translate("BatchProcessing", "Individual Files List"))
        self.pushButton_masksDir.setText(_translate("BatchProcessing", "Masked Videos Dir"))
        self.pushButton_paramFile.setText(_translate("BatchProcessing", "Parameters File"))
        self.pushButton_resultsDir.setText(_translate("BatchProcessing", "Tracking Results Dir"))
        self.p_copy_unfinished.setText(_translate("BatchProcessing", "Copy Unfinished Analysis"))
        self.p_is_copy_video.setText(_translate("BatchProcessing", "Copy Raw Videos to Temp Dir"))
        self.p_only_summary.setText(_translate("BatchProcessing", "Only Display Progress Summary"))
        self.label.setText(_translate("BatchProcessing", "Analysis Start Point"))
        self.label_2.setText(_translate("BatchProcessing", "Analysis End Point"))
        self.label_patternExc.setText(_translate("BatchProcessing", "File Pattern to Exclude"))
        self.label_patternIn.setText(_translate("BatchProcessing", "File Pattern to Include"))
        self.p_unmet_requirements.setText(_translate("BatchProcessing", "Print Unmet Requirements"))
        self.label_numMaxProc.setText(_translate("BatchProcessing", "Maximum Number of Processes"))
        self.pushButton_start.setText(_translate("BatchProcessing", "START"))

