#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re
import subprocess
import xlrd
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_RecordInfo import Ui_RecordBug
from Ui_PullFile import Ui_PullFile
from Ui_ChoosePull import Ui_ChoosePull
from Ui_AdbPull import Ui_AdbPull
from Ui_ScpPull import Ui_ScpPull
from Ui_ChoosePush import Ui_ChoosePush
from Ui_AdbPush import Ui_AdbPush
from Ui_ScpPush import Ui_ScpPush
from Ui_OpenRviz import Ui_OpenRviz
from Ui_BrushSoc import Ui_BrushSoc


class Record_Info_Views(QMainWindow, Ui_RecordBug):
    '''
        主界面
    '''

    def __init__(self):
        '''
        初始化主界面,设置定时器用于显示时间,设置定时器状态time_count,设置第二界面问题保存标志pushButton_savecount
        time_count 1 开始 0 暂停
        pushButton_savecount 0 初始状态 1 2 3 对应当前测试次数 4 添加了问题
        '''
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        try:
            self.timer.timeout.connect(self.show_time)
            self.timer.start()
        except BaseException as e:
            if isinstance(e, KeyboardInterrupt):
                self.timer.stop()
                os._exit(0)
        self.time_count = 1
        self.pushButton_savecount = 0
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.initUI()

    def initUI(self):
        '''
        设置问题保存路径,给按钮绑定事件,给下拉框绑定事件,给列表和表格绑定点击事件
        '''
        self.test_type()
        self.file_path = '/home/user/Data/Record_Info'
        self.pushButton.clicked.connect(self.get_info)
        self.pushButton_2.clicked.connect(self.clear_all)
        self.pushButton_3.clicked.connect(self.pull_file)
        self.pushButton_4.clicked.connect(self.choose_push)
        self.pushButton_5.clicked.connect(self.save_update)
        self.pushButton_6.clicked.connect(self.save_info)
        self.pushButton_7.clicked.connect(self.open_xlsx)
        self.pushButton_8.clicked.connect(self.stop_time)
        self.pushButton_9.clicked.connect(self.choose_pull)
        self.pushButton_10.clicked.connect(self.test_save_fail)
        self.pushButton_11.clicked.connect(self.first_test)
        self.pushButton_12.clicked.connect(self.second_test)
        self.pushButton_13.clicked.connect(self.third_test)
        self.pushButton_14.clicked.connect(self.stop_time)
        self.pushButton_15.clicked.connect(self.test_save_pass)
        self.pushButton_16.clicked.connect(self.save_to_txt)
        self.pushButton_17.clicked.connect(self.open_rviz)
        self.pushButton_18.clicked.connect(self.test_save_info)
        self.pushButton_19.clicked.connect(self.brush_soc)
        self.pushButton_20.clicked.connect(self.get_carinfo)
        self.comboBox_2.currentIndexChanged.connect(self.test_type)
        self.tableWidget.clicked.connect(self.table_click)
        self.listWidget.itemClicked.connect(self.update_info)

# 第一界面
    def get_info(self):
        '''
        car_name 车辆信息,question_time 问题时间,test_type 测试类型,test_path 测试路线,question_place 问题位置,
        fault_rate 故障频率 question_describe 问题描述,err_info 详细问题记录
        '''
        car_name = self.label_17.text()
        question_time = self.label_3.text()
        test_type = self.comboBox_2.currentText()
        test_path = self.lineEdit.text()
        question_place = self.lineEdit_2.text()
        fault_rate = self.comboBox_3.currentText()
        question_describe = self.comboBox_4.currentText()+' ' + \
            self.plainTextEdit.toPlainText()
        err_info = "车辆信息 : {}\n问题时间 : {}\n测试类型 : {}\n测试路线 : {}\n问题位置 : {}\n故障频率 : {}\n问题描述 : {}\n".format(
            car_name, question_time, test_type, test_path, question_place, fault_rate, question_describe)
        self.record_info(err_info)

    def get_carinfo(self):
        '''
        创建default.xml文件文件保存路径,通过adb方式拉取default.xml,读取文件中的车辆信息
        '''
        self.label_10.setText('')
        res = Mkdir_Path_Views().mkdir_file_path('/home/user/Data/car_instance/')
        if res:
            res = subprocess.call(
                'timeout 1 adb pull /data/zros/res/car_instance/default.xml /home/user/Data/car_instance/', shell=True)
            if res:
                self.create_pop('adb is not connect')
            else:
                data = os.popen('cat /home/user/Data/car_instance/default.xml')
                car_info = re.findall(
                    '<car_instance>(.*?)</car_instance>', data.read())[0]
                self.label_17.setText(car_info)
        else:
            self.create_pop('创建/home/user/Data/car_instance/文件夹失败')

    def record_info(self, err_info):
        '''
        err_info:问题信息
        记录问题,重置右侧内容,设置记录成功的标记
        '''
        self.listWidget.addItem(err_info)
        self.clear_all()
        self.label_10.setText("记录成功")

    def clear_all(self):
        '''
        重置界面右侧填写的所有信息
        '''
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.plainTextEdit.setPlainText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.time_count = 1
        self.timer.start()
        self.pushButton_8.setText("暂停")
        self.pushButton_14.setText("暂停")
        self.label_10.setText("")

    def stop_time(self):
        '''
        暂停和开始记录时间
        '''
        if self.time_count:
            self.timer.stop()
            self.time_count = 0
            self.pushButton_8.setText("开始")
            self.pushButton_14.setText("开始")
        else:
            self.timer.start()
            self.time_count = 1
            self.pushButton_8.setText("暂停")
            self.pushButton_14.setText("暂停")

    def show_time(self):
        '''
        显示时间
        '''
        try:
            datetime = QDateTime.currentDateTime()
            years = datetime.toString().split(' ')[-1]
            days = datetime.toString().split(' ')[2]
            months = datetime.toString().split(' ')[1][0:2]
            times = datetime.toString().split(' ')[3]
            self.label_3.setText(
                '{}年-{}-{}日 {}'.format(years, months, days, times))
            self.label_13.setText(
                '{}年-{}-{}日 {}'.format(years, months, days, times))
        except BaseException as e:
            if isinstance(e, KeyboardInterrupt):
                self.timer.stop()
                os._exit(0)

    def keyPressEvent(self, event):
        '''
        键盘事件监听函数, Esc 暂停和开始时间,Ctrl+c 关闭主界面窗口
        '''
        if event.key() == Qt.Key_Escape:
            self.stop_time()
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.closeEvent(event)

    def save_info(self):
        '''
        将左侧问题记录中的所有信息保存到文件中,清除问题记录列表中所有信息
        '''
        if self.listWidget.count():
            res = Mkdir_Path_Views().mkdir_file_path(self.file_path)
            if res:
                with open('{}/bug_file.txt'.format(self.file_path), 'a') as f:
                    for count in range(self.listWidget.count()):
                        f.write(self.listWidget.item(count).text()+'\n')
                self.label_10.setText(
                    "问题记录已保存到{}/bug_file.txt".format(self.file_path))
                self.listWidget.clear()
            else:
                self.create_pop("创建{}文件夹失败".format(file_path))
        else:
            self.create_pop("没有问题记录")

    def test_type(self):
        '''
        设置测试类型
        '''
        self.comboBox_4.clear()
        if self.comboBox_2.currentText() == "接驾":
            err_list = ['接驾未完成', '过弯靠外侧', '过弯靠内侧', '障碍物误检测', '定位飘了', '其他']
        elif self.comboBox_2.currentText() == "泊车":
            err_list = ['泊车歪了', '挂p档', '泊车未完成', '障碍物误检测', '定位飘了', '其他']
        elif self.comboBox_2.currentText() == "跨层":
            err_list = ['未进线控', '路径规划时间过长', '溜坡', '障碍物误检测', '定位飘了', '其他']
        elif self.comboBox_2.currentText() == "避障":
            err_list = ['障碍物未识别', '障碍物误检测', '障碍物检测成功,未刹车',
                        '障碍物检测成功并避障,障碍物移除之后不能继续接驾', '其他']
        elif self.comboBox_2.currentText() == "定位":
            err_list = ['定位失败', '定位成功地图未切换', '其他']
        self.comboBox_4.addItems(err_list)

    def update_info(self, item):
        '''
        将左侧问题记录中的信息显示在右侧对应位置
        '''
        self.comboBox_2.setCurrentText(re.findall(
            '测试类型 : (.*?)\n', str(item.text()))[0])
        self.lineEdit.setText(re.findall(
            '测试路线 : (.*?)\n', str(item.text()))[0])
        self.lineEdit_2.setText(re.findall(
            '问题位置 : (.*?)\n', str(item.text()))[0])
        self.comboBox_3.setCurrentText(re.findall(
            '故障频率 : (.*?)\n', str(item.text()))[0])
        self.comboBox_4.setCurrentText(re.findall(
            '问题描述 : (.*?)\n', str(item.text()))[0].split(' ')[0])
        self.plainTextEdit.setPlainText(re.findall(
            '问题描述 : (.*?)\n', str(item.text()))[0].split(' ')[1])

    def save_update(self):
        '''
        保存修改后的信息,将右侧各个问题描述记录保存在右侧问题记录列表中
        '''
        if self.listWidget.count():
            if self.listWidget.currentItem():
                car_name = self.label_17.text()
                question_time = re.findall(
                    '问题时间 : (.*?)\n', self.listWidget.currentItem().text())[0]
                test_type = self.comboBox_2.currentText()
                test_path = self.lineEdit.text()
                question_place = self.lineEdit_2.text()
                fault_rate = self.comboBox_3.currentText()
                question_describe = self.comboBox_4.currentText()+' ' + \
                    self.plainTextEdit.toPlainText()
                item = "车辆信息 : {}\n问题时间 : {}\n测试类型 : {}\n测试路线 : {}\n问题位置 : {}\n故障频率 : {}\n问题描述 : {}\n".format(
                    car_name, question_time, test_type, test_path, question_place, fault_rate, question_describe)
                self.listWidget.insertItem(self.listWidget.currentRow(), item)
                self.listWidget.takeItem(self.listWidget.currentRow())
                self.clear_all()
            else:
                self.create_pop('请选择要修改的记录')
        else:
            self.create_pop('没有问题记录')

    def create_pop(self, info):
        '''
        设置提醒弹窗
        '''
        msg_box = QMessageBox(QMessageBox.Warning, '提示', info)
        msg_box.exec_()
# 第一界面

# 第二界面
    def open_xlsx(self):
        '''
        读取xlsx文件中信息,格式化之后生成表格
        创建id case step result列表
        '''
        if self.choosexlsxfile():
            return
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(self.table.nrows-1)
        self.tableWidget.setHorizontalHeaderLabels(
            ['测试用例ID', '测试用例', '测试路线', '测试次数'])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.id_list = []
        self.case_list = []
        self.step_list = []
        self.result_list = []
        for cols_index in range(self.table.ncols):
            cols_name = self.table.cell_value(0, cols_index)
            if cols_name == '测试用例':
                self.list_append_value(self.case_list, cols_index)
            elif cols_name == "测试用例ID":
                self.list_append_value(self.id_list, cols_index)
            elif cols_name == '测试步骤':
                self.list_append_value(self.step_list, cols_index)
            elif cols_name == '期望结果':
                self.list_append_value(self.result_list, cols_index)
        self.show_table()

    def list_append_value(self, cols_name_list, cols_index):
        '''
        将表格中对应信息添加进对应列表
        '''
        for rows_index in range(self.table.nrows):
            cols_name_list.append(
                self.table.cell_value(rows_index, cols_index))

    def choosexlsxfile(self):
        '''
        生成文件选择窗口
        根据sheet名为测试用例读取表格
        '''
        self.fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                     "选取文件",
                                                                     "/home/user/",
                                                                     "Text Files (*.xlsx)")
        if self.fileName_choose == "":
            return 1
        self.table_data = xlrd.open_workbook(
            self.fileName_choose)
        try:
            self.table = self.table_data.sheet_by_name("测试用例")
        except:
            self.create_pop('选择文件格式错误')
            return 1

    def show_table(self):
        '''
        从对应列表中按顺序生成表格,设置测试用例ID字典table_case_id,设置测试次数标志pushButton_count,初始化问题记录标志pushButton_savecount
        table_case_id {'test_id1':1,'test_id2':0} index 测试用例id value 测试次数
        '''
        self.textBrowser_2.setText('')
        self.textBrowser_3.setText('')
        self.textBrowser_6.setText('')
        self.plainTextEdit_2.setPlainText('')
        self.textBrowser_4.setPlainText('')
        self.table_case_id = {}
        self.pushButton_savecount = 0
        self.pushButton_count = 0
        for case_index in range(1, len(self.case_list)):
            self.table_case_id[self.id_list[case_index]] = 0
            case = self.case_list[case_index].split('\n')[0]
            try:
                path = self.case_list[case_index].split('\n')[1][1:-1]
            except:
                path = ''
            self.tableWidget.setItem(
                case_index-1, 0, QTableWidgetItem(self.id_list[case_index]))
            self.tableWidget.setItem(case_index-1, 1, QTableWidgetItem(case))
            self.tableWidget.setItem(case_index-1, 2, QTableWidgetItem(path))
            self.tableWidget.setItem(case_index-1, 3, QTableWidgetItem(''))
        # 设置表格内容不可修改(导致表格内容显示不完全)
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def table_click(self):
        '''
        切换表格,判断pushButton_savecount,如果为0,直接切换(问题记录框没有信息),如果为1 2 3,清空问题记录框中的信息并切换(只选择了测试次数没有添加测试问题),
        如果为4,弹出提示框(问题记录框中已添加了问题)
        '''
        if self.pushButton_savecount == 0:
            pass
        elif self.pushButton_savecount in [1, 2, 3]:
            self.textBrowser_4.setText('')
        else:
            if self.textBrowser_4.toPlainText():
                quitMsgBox = QMessageBox()
                quitMsgBox.setWindowTitle('确认提示')
                quitMsgBox.setText('你还没有保存问题,继续切换测试用例吗?')
                quitMsgBox.setStandardButtons(
                    QMessageBox.Yes | QMessageBox.No)
                buttonY = quitMsgBox.button(QMessageBox.Yes)
                buttonY.setText('保存并切换')
                buttonN = quitMsgBox.button(QMessageBox.No)
                buttonN.setText('不保存切换')
                quitMsgBox.exec_()
                if quitMsgBox.clickedButton() == buttonY:
                    self.save_to_txt()
                    return
        self.pushButton_count = 0
        self.show_test_info()
        self.err_list()
        self.pushButton_savecount = 0

    def show_test_info(self):
        '''
        显示测试信息,根据测试用例id读取测试步骤列表step_list和期望结果列表result_list中的内容添加到对应的显示框
        '''
        self.plainTextEdit_2.setPlainText('')
        self.textBrowser_4.setPlainText('')
        for i in range(1, len(self.step_list)):
            if i == self.tableWidget.selectedItems()[0].row()+1:
                self.textBrowser_3.setText("测试步骤:\n"+self.step_list[i])
                self.textBrowser_2.setText("期望结果:\n"+self.result_list[i])
                try:
                    self.textBrowser_6.setText(
                        "测试次数:\n"+re.findall('完成(.*)复测', self.step_list[i])[0])
                except:
                    self.textBrowser_6.setText('')

    def err_list(self):
        '''
        问题列表,读取保存文件,根据当前选择的测试用例ID将文件中记录的问题分离,显示在对应的显示框
        将table_case_id字典中索引对应的值修改为文件中的次数
        '''
        try:
            with open('{}/case_problem.txt'.format(self.file_path), 'r')as f:
                data = f.read()
        except:
            self.tableWidget.setItem(
                self.tableWidget.currentRow(), 3, QTableWidgetItem('还没有进行测试'))
            self.table_case_id[self.tableWidget.selectedItems()[0].text()] = 0
            self.color_change(Qt.black)
            return
        info = ''
        for res in data.split('\n\n'):
            if self.tableWidget.selectedItems()[0].text() in res[5:20]:
                info = info + res + '\n\n'
        if not info[-9:-8]:
            self.tableWidget.setItem(
                self.tableWidget.currentRow(), 3, QTableWidgetItem('还没有进行测试'))
            self.table_case_id[self.tableWidget.selectedItems()[0].text()] = 0
            self.color_change(Qt.black)
        elif info[-9:-8] in ['1', '2', '3']:
            self.table_case_id[self.tableWidget.selectedItems()[
                0].text()] = int(info[-9:-8])
            self.tableWidget.setItem(
                self.tableWidget.currentRow(), 3, QTableWidgetItem('已进行过{}次测试'.format(self.table_case_id[self.tableWidget.selectedItems()[
                    0].text()])))
            self.color_change(Qt.red)
            self.textBrowser_6.setText(info)

    def test_save_info(self):
        '''
        记录测试问题,将右侧问题输入框中的内容记录在左侧问题显示框
        '''
        try:
            self.tableWidget.selectedItems()[0].text()
        except:
            return
        if self.pushButton_count:
            if self.plainTextEdit_2.toPlainText():
                self.change_info(self.plainTextEdit_2.toPlainText())
            else:
                self.create_pop('请输入测试问题描述')
                return
        else:
            self.choose_test_pop()

    def test_save_pass(self):
        '''
        记录测试问题为pass,生成一条问题为pass的记录,记录在左侧问题显示框
        '''
        try:
            self.tableWidget.selectedItems()[0].text()
        except:
            return
        if self.pushButton_count:
            self.change_info('PASS')
        else:
            self.choose_test_pop()

    def test_save_fail(self):
        '''
        记录测试问题为fail,生成一条问题为fail的记录,记录在左侧问题显示框
        '''
        try:
            self.tableWidget.selectedItems()[0].text()
        except:
            return
        if self.pushButton_count:
            self.change_info('FAIL')
        else:
            self.choose_test_pop()

    def choose_test_pop(self):
        '''
        选择测试次数弹窗,根据table_case_id字典中的数据得到当前选择的测试用例已经测试的次数,进行弹窗显示
        '''
        try:
            self.table_case_id[self.tableWidget.selectedItems()[
                0].text()]
        except:
            self.create_pop('当前选择测试用例ID为空')
            return
        if self.table_case_id[self.tableWidget.selectedItems()[
                0].text()] == 3:
            self.create_pop("{}测试用例已经进行过三次测试".format(self.tableWidget.selectedItems()[
                0].text()))
        else:
            self.create_pop('请选择测试次数')

    def change_info(self, err_info):
        '''
        生成测试问题,根据测试用例ID,右侧问题时间,问题输入框的内容生成一条问题记录,修改pushButton_savecount为4
        '''
        info = "测试用例ID : {}\n时间 : {}\n问题描述 : {}\n".format(
            self.tableWidget.selectedItems()[0].text(), self.label_13.text(), err_info)
        self.save_test_info(info)
        self.pushButton_savecount = 4
        self.pushButton_count = 0

    def save_test_info(self, info):
        '''
        将生成的测试问题记录在左侧问题显示框中,将右侧问题输入框中的内容清空,设置时间为开始状态
        '''
        if not info:
            self.create_pop('请输入问题描述')
            return
        if self.textBrowser_4.toPlainText():
            info = self.textBrowser_4.toPlainText() + info
        else:
            info = info
        self.textBrowser_4.setPlainText(info)
        self.plainTextEdit_2.setPlainText('')
        self.time_count = 1
        self.timer.start()
        self.pushButton_8.setText("暂停")
        self.pushButton_14.setText("暂停")

    def first_test(self):
        # 第一次测试
        try:
            self.tableWidget.selectedItems()[0].text()
        except:
            return
        self.count_for_test(1)

    def second_test(self):
        # 第二测测试
        try:
            self.tableWidget.selectedItems()[0].text()
        except:
            return
        self.count_for_test(2)

    def third_test(self):
        # 第三次测试
        try:
            self.tableWidget.selectedItems()[0].text()
        except:
            return
        self.count_for_test(3)

    def count_for_test(self, count):
        '''
        根据当前选择的table_case_id中的数据判断当前测试用例的测试次数,生成一条信息显示在左侧问题显示框中
        设置pushButton_count为当前测试次数
        '''
        try:
            self.table_case_id[self.tableWidget.selectedItems()[0].text()]
        except:
            self.create_pop('当前选择测试用例ID为空')
            return
        if not self.tableWidget.selectedItems()[0].text():
            self.create_pop('当前选择测试用例ID为空')
            return
        if self.pushButton_savecount == 0:
            if self.table_case_id[self.tableWidget.selectedItems()[0].text()] == 3:
                self.create_pop("已经完成三次测试")
                return
            if self.table_case_id[self.tableWidget.selectedItems()[0].text()] == count-1:
                self.pushButton_count = count
                self.textBrowser_4.setText("====={}第{}次=====\n".format(
                    self.tableWidget.selectedItems()[0].text(), count))
                self.pushButton_savecount = count
            else:
                self.create_pop('请进行第{}次测试'.format(
                    self.table_case_id[self.tableWidget.selectedItems()[0].text()]+1))

    def save_to_txt(self):
        '''
        将测试问题保存在txt文件中,将左侧问题显示框中的内容保存在文件中,根据pushButton_count判断table_case_id中
        的数据,将pushButton_savecount设置为0(初始状态)
        '''
        if self.textBrowser_4.toPlainText():
            try:
                test_id = re.findall('测试用例ID : (.*?)\n',
                                     self.textBrowser_4.toPlainText())[0]
            except:
                return
            info = '{}{}\n\n'.format(
                self.textBrowser_4.toPlainText(), "====={}第{}次=====".format(test_id, self.table_case_id[test_id]+1))
            res = Mkdir_Path_Views().mkdir_file_path(self.file_path)
            if res:
                with open('{}/case_problem.txt'.format(self.file_path), 'a') as f:
                    f.write(info)
                if self.pushButton_count == 1:
                    self.table_case_id[test_id] = 1
                elif self.pushButton_count == 2:
                    self.table_case_id[test_id] = 2
                elif self.pushButton_count == 3:
                    self.table_case_id[test_id] = 3
                self.textBrowser_4.setText('')
                self.err_list()
                self.pushButton_savecount = 0
        else:
            self.create_pop('请添加问题')
            return

    def color_change(self, color):
        '''
        改变测试用例的背景颜色
        '''
        for colum in range(4):
            self.tableWidget.item(
                self.tableWidget.currentRow(), colum).setForeground(color)
# 第二界面

# 第三界面
    def pull_file(self):
        self.pull = Pull_File_Views()
        self.pull.show()

    def choose_push(self):
        self.choosepush = Choose_Push_Views()
        self.choosepush.show()

    def choose_pull(self):
        self.choosepull = Choose_Pull_Views()
        self.choosepull.show()

    def open_rviz(self):
        self.recordbag = Open_Rviz_Views()
        self.recordbag.show()

    def brush_soc(self):
        self.brushsoc = Brush_Soc_Views()
        self.brushsoc.show()
# 第三界面

# 退出提示
    def closeEvent(self, event):
        # 监听窗口关闭事件
        if self.listWidget.count():
            problem_res = self.problem_record(event)
        else:
            problem_res = True
        if self.pushButton_savecount == 4:
            case_res = self.case_record(event)
        else:
            case_res = True
        if problem_res and case_res:
            os._exit(0)

    def problem_record(self, event):
        tips_msg = '你还没有保存问题,继续退出吗?'
        res = self.quit_box(event, tips_msg, self.save_info)

    def case_record(self, event):
        tips_msg = '你还没有保存用例记录,继续退出吗?'
        self.quit_box(event, tips_msg, self.save_to_txt)

    def quit_box(self, event, tips_msg, handle_fun):
        # 有问题记录没有保存的时候生成退出提醒框
        quitMsgBox = QMessageBox()
        quitMsgBox.setWindowTitle('确认提示')
        quitMsgBox.setText(tips_msg)
        quitMsgBox.setStandardButtons(
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok)
        buttonY = quitMsgBox.button(QMessageBox.Yes)
        buttonY.setText('保存并退出')
        buttonN = quitMsgBox.button(QMessageBox.No)
        buttonN.setText('取消')
        buttonO = quitMsgBox.button(QMessageBox.Ok)
        buttonO.setText('直接退出')
        quitMsgBox.exec_()
        if quitMsgBox.clickedButton() == buttonY:
            handle_fun()
            event.accept()
            os._exit(0)
        elif quitMsgBox.clickedButton() == buttonO:
            event.accept()
            os._exit(0)
        else:
            event.ignore()
# 退出提示


class Pull_File_Views(QDialog, Ui_PullFile):
    '''
        拉取最新的DailyBuild
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.clicked_pull)
        self.timer = QTimer()
        self.timer.timeout.connect(self.pull)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.choosedir)

    def clicked_pull(self):
        '''
        验证用户选择的文件夹是否是/home/user/,验证成功之后调用pull()函数
        '''
        if self.lineEdit.text() == '/home/user':
            pass
        else:
            if self.lineEdit.text()[0:11] == '/home/user/':
                pass
            else:
                self.label_2.setText("请选择/home/user/下的路径")
                self.label_3.setText("")
                self.label_4.setText("")
                return
        self.filepath = self.lineEdit.text()+"/"
        self.label_2.setText("正在拉取文件,请稍候")
        self.label_3.setText("")
        self.label_4.setText("")
        self.timer.start(1)

    def pull(self):
        '''
        运行pull_file.sh,拉取文件,根据pull_file.sh脚本返回的结果判断文件拉取结果
        '''
        self.timer.stop()
        try:
            data = os.popen(Generate_File_Path().base_path(
                'Sh/pull_file.sh')+' '+self.filepath)
            data = str(data.read())
        except Exception as e:
            self.label_3.setText("Unknown Err")
            return
        if data.split('\n')[0] == "连接服务器失败...":
            self.label_3.setText(data.split('\n')[0])
        elif data.split('\n')[0][-2:] == "确定":
            self.label_3.setText(data.split('\n')[1])
            self.label_4.setText("文件拉取完成")
        elif data.split('\n')[0] == "已经有最新的DailyBuild...":
            self.label_3.setText(data.split('\n')[0])

    def choosedir(self):
        # 选择文件夹
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "/home/user/")
        if dir_choose == "":
            return
        self.lineEdit.setText(dir_choose)


class Choose_Pull_Views(QDialog, Ui_ChoosePull):
    '''
        选择拉取方式
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.radioButton.toggled.connect(self.choose_method)
        self.radioButton_2.toggled.connect(self.choose_method)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.close)

    def choose_method(self):
        '''
        选择拉取方式
        '''
        self.label_5.setText('')
        if self.radioButton.isChecked():
            self.label_3.setText('当前选择: 通过adb方式拉取文件')
        else:
            self.label_3.setText('当前选择: 通过scp方式拉取文件')

    def check(self):
        '''
        执行所选择拉取方式对应的函数
        '''
        if self.label_3.text():
            if self.radioButton.isChecked():
                self.adb_pull()
            elif self.radioButton_2.isChecked():
                self.scp_pull()
        else:
            self.label_3.setText('请选择拉取文件的方式')

    def scp_pull(self):
        self.scppull = Scp_Pull_Views()
        self.scppull.show()
        self.close()

    def adb_pull(self):
        self.adbpull = Adb_Pull_Views()
        self.adbpull.show()
        self.close()


class Adb_Pull_Views(QDialog, Ui_AdbPull):
    '''
        Adb拉取文件
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.check_input)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.choosedir)
        self.timer = QTimer()
        self.timer.timeout.connect(self.pull_file)

    def choosedir(self):
        '''
        选择文件夹
        '''
        self.label_3.setText('')
        self.label_2.setText('')
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "/home/user/")
        if dir_choose == "":
            return
        self.lineEdit.setText(dir_choose)

    def check_input(self):
        '''
        检测用户输入信息是否符合要求
        '''
        self.label_3.setText('')
        self.label_2.setText('')
        filepath = self.lineEdit_2.text()
        savepath = self.lineEdit.text()
        if filepath:
            if savepath:
                if filepath[0:6] == '/data/':
                    if savepath[0:11] == '/home/user/':
                        self.label_2.setText("正在拉取文件,请稍等")
                        self.timer.start(1)
                        self.filepath = filepath
                        self.savepath = savepath
                    else:
                        self.label_2.setText("请选择/home/user/下的路径")
                else:
                    self.label_2.setText("请输入/data/下的路径")
            else:
                self.label_2.setText('请选择保存文件路径')
        else:
            self.label_2.setText('请输入拉取文件路径')

    def pull_file(self):
        '''
        拉取文件
        '''
        self.timer.stop()
        res = subprocess.call('adb pull {} {}'.format(
            self.filepath, self.savepath), shell=True)
        if res:
            self.label_3.setText('拉取失败,检查adb连接或adb权限!!!')
        else:
            self.label_3.setText('拉取文件完成')


class Scp_Pull_Views(QDialog, Ui_ScpPull):
    '''
        Scp拉取文件
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.pulllog)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.choosedir)
        self.timer = QTimer()
        self.timer.timeout.connect(self.pull)

    def choosedir(self):
        self.label_3.setText("")
        self.label_4.setText("")
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "/home/user/")
        if dir_choose == "":
            return
        self.lineEdit_3.setText(dir_choose)

    def pulllog(self):
        '''
        检测用户输入信息是否符合要求
        '''
        self.label_3.setText("")
        self.label_4.setText("")
        host = self.lineEdit.text()
        host_re = "^\d{3}\.\d{3}\.\d{1,}\.\d{3}$"
        hostres = re.findall(host_re, host)
        filepath = self.lineEdit_2.text()
        savepath = self.lineEdit_3.text()
        if hostres:
            if filepath:
                if filepath[0:6] == "/data/":
                    if savepath:
                        if savepath == "/home/user":
                            pass
                        else:
                            if savepath[0:11] == "/home/user/":
                                pass
                            else:
                                self.label_3.setText("请选择/home/user/下的路径")
                                return
                        self.save_logfile(hostres[0], filepath, savepath)
                    else:
                        self.label_3.setText("请选择文件保存路径")
                else:
                    self.label_3.setText("请输入/data/下的路径")
            else:
                self.label_3.setText("请输入文件所在目录")
        else:
            self.label_3.setText('请输入正确的IP地址')

    def save_logfile(self, host, filepath, savepath):
        '''
        创建timer定时器,拉取文件
        '''
        res = subprocess.call("cd {}".format(savepath), shell=True)
        if res:
            self.label_3.setText("保存路径不是一个文件夹")
        else:
            self.label_3.setText('正在拉取文件')
            self.host = host
            self.filepath = filepath
            self.savepath = savepath
            self.timer.start(0.1)

    def pull(self):
        self.timer.stop()
        if os.path.isfile(self.filepath):
            res = subprocess.call(
                'scp root@{}:{} {}'.format(self.host, self.filepath, self.savepath), shell=True)
        else:
            res = subprocess.call(
                'scp -r root@{}:{} {}'.format(self.host, self.filepath, self.savepath), shell=True)
        if res:
            self.label_4.setText("文件拉取失败,请检查路径是否正确")
        else:
            self.label_4.setText('文件拉取成功')


class Choose_Push_Views(QDialog, Ui_ChoosePush):
    '''
        选择推送文件方式
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.radioButton.toggled.connect(self.choose_method)
        self.radioButton_2.toggled.connect(self.choose_method)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.close)

    def choose_method(self):
        '''
        选择方式
        '''
        self.label_5.setText('')
        if self.radioButton.isChecked():
            self.label_3.setText('当前选择: 通过adb方式推送文件')
        else:
            self.label_3.setText('当前选择: 通过scp方式推送文件')

    def check(self):
        '''
        执行所选择方式对应的函数
        '''
        if self.label_3.text():
            if self.radioButton.isChecked():
                self.adb_push()
            elif self.radioButton_2.isChecked():
                self.scp_push()
        else:
            self.label_3.setText('请选择推送文件的方式')

    def adb_push(self):
        self.adbpush = Adb_Push_Views()
        self.adbpush.show()
        self.close()

    def scp_push(self):
        self.scppush = Scp_Push_Views()
        self.scppush.show()
        self.close()


class Adb_Push_Views(QDialog, Ui_AdbPush):
    '''
        Adb推送文件
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton_3.clicked.connect(self.choosefile)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.pushfile)
        self.timer = QTimer()
        self.timer.timeout.connect(self.push)

    def choosefile(self):
        self.label_3.setText('')
        self.label_2.setText('')
        files, ok1 = QFileDialog.getOpenFileName(self,
                                                 "文件选择",
                                                 "/home/user/",
                                                 "All Files (*);;Text Files (*.txt)")
        self.lineEdit.setText(files)

    def pushfile(self):
        '''
        检测用户输入信息是否符合要求
        '''
        pushpath = self.lineEdit_2.text()
        filepath = self.lineEdit.text()
        self.label_2.setText('')
        self.label_3.setText('')
        if pushpath:
            if filepath:
                if pushpath[0:6] == '/data/':
                    res = subprocess.call(
                        '[ -d {} ]'.format(filepath), shell=True)
                    if res:
                        self.label_2.setText("正在推送文件,请稍等")
                        self.pushpath = pushpath
                        self.filepath = filepath
                        self.timer.start(1)
                    else:
                        self.label_2.setText('请选择正确的文件')
                else:
                    self.label_2.setText("请输入/data/下的路径")
            else:
                self.label_2.setText("请选择本地文件")
        else:
            self.label_2.setText("请输入目标路径")

    def push(self):
        '''
        推送文件
        '''
        self.timer.stop()
        res = subprocess.call('adb push {} {}'.format(
            self.filepath, self.pushpath), shell=True)
        if res:
            self.label_3.setText('文件推送失败,请检查adb连接或adb权限!!!')
        else:
            self.label_3.setText('文件推送成功')


class Scp_Push_Views(QDialog, Ui_ScpPush):
    '''
        Scp推送文件
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.pushfile)
        self.pushButton_3.clicked.connect(self.choosefile)
        self.pushButton_2.clicked.connect(self.close)
        self.timer = QTimer()
        self.timer.timeout.connect(self.push)

    def pushfile(self):
        '''
        检测用户输入信息是否符合要求
        '''
        self.label_3.setText("")
        self.label_4.setText("")
        host = self.lineEdit.text()
        pushpath = self.lineEdit_2.text()
        filepath = self.lineEdit_3.text()
        host_re = "^\d{3}\.\d{3}\.\d{1,}\.\d{3}$"
        hostres = re.findall(host_re, host)
        if hostres:
            if pushpath[0:6] == "/data/":
                if filepath[0:11] == "/home/user/":
                    self.label_3.setText("正在推送文件,请稍等")
                    self.host = hostres[0]
                    self.pushpath = pushpath
                    self.filepath = filepath
                    self.timer.start(1)
                else:
                    self.label_3.setText("请选择/home/user/下的文件")
            else:
                self.label_3.setText("请输入/data/路径下的目标路径")
        else:
            self.label_3.setText("请输入正确的IP")

    def choosefile(self):
        self.label_3.setText("")
        self.label_4.setText("")
        files, ok1 = QFileDialog.getOpenFileName(self,
                                                 "文件选择",
                                                 "/home/user/",
                                                 "All Files (*);;Text Files (*.txt)")
        self.lineEdit_3.setText(files)

    def push(self):
        '''
        推送文件
        '''
        self.timer.stop()
        if os.path.isfile(self.filepath):
            res = subprocess.call(
                "scp {} root@{}:{}".format(self.filepath, self.host, self.pushpath), shell=True)
        else:
            res = subprocess.call(
                "scp -r {} root@{}:{}".format(self.filepath, self.host, self.pushpath), shell=True)
        if res:
            self.label_4.setText("文件推送失败,请检查目标路径或本地文件是否正确")
        else:
            self.label_4.setText("文件推送成功")


class Open_Rviz_Views(QDialog, Ui_OpenRviz):
    '''
        打开Rviz
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.ip = ''
        self.filepath = Find_File().find_dir_path('zros_dbg_dev_record', '/home/user/')
        self.pushButton.clicked.connect(self.record_bag)
        self.pushButton_2.clicked.connect(self.close)
        # self.pushButton_3.clicked.connect(self.record_bag)

    def check_ip(self):
        '''
        检测输入的ip地址是否符合要求
        '''
        self.label_2.setText('')
        address = self.lineEdit.text()
        if not address:
            self.label_2.setText('请输入ip地址')
            return 0
        address_re = "^\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
        res = re.findall(address_re, address)
        if not res:
            self.label_2.setText('输入ip格式错误')
            return 0
        self.ip = res[0]
        return 1

    def record_bag(self):
        '''
            修改zros_dbg_dev_record中localization.launch中的ip
            执行start_all.sh 传入参数
        '''
        if not self.check_ip():
            return
        launchfile = Find_File().find_file_path(
            'localization.launch', self.filepath)[0]
        with open(launchfile, 'r') as f:
            server_address = re.findall(
                '"server_address">(.*)</rosparam>', f.read())
        subprocess.call(
            "sed -i 's/{}/{}/g' {}".format(server_address[0], self.ip, launchfile), shell=True)
        os.popen(Generate_File_Path().base_path('Sh/start_all.sh')+' ' +
                 Generate_File_Path().base_path('Sh/record_bag.sh')+' '+Generate_File_Path().base_path('Sh/rviz_e.sh')+' '+self.filepath+' '+self.ip)
        sleep(1)
        self.close()

    # def open_rviz(self):
    #     '''
    #     修改zros_dbg_dev_record中localization.launch中的ip
    #     执行open_rviz.sh传入参数
    #     第一个参数: rviz_e.sh运行路径
    #     第二个参数:zors_dbg_dev_record文件目录
    #     '''
    #     if not self.check_ip():
    #         return
    #     launchfile = Find_File().find_file_path('localization.launch', self.filepath)[0]
    #     with open(launchfile, 'r') as f:
    #         server_address = re.findall(
    #             '"server_address">(.*)</rosparam>', f.read())
    #     subprocess.call(
    #         "sed -i 's/{}/{}/g' {}".format(server_address[0], self.ip, launchfile), shell=True)
    #     os.popen(Generate_File_Path().base_path('Sh/open_rviz.sh')+' ' +
    #              Generate_File_Path().base_path('Sh/rviz_e.sh')+' '+self.filepath)

    # def record_bag(self):
    #     '''
    #     执行open_record.sh传入参数
    #     第一个参数:record_bag.sh文件路径
    #     第二个参数:zros_dbg_dev_record文件目录
    #     第三个参数:self.lineEdit控件中输入的ip地址
    #     '''
    #     if not self.check_ip():
    #         return
    #     self.label_2.setText('')
    #     os.popen(Generate_File_Path().base_path('Sh/open_record.sh')+' ' +
    #              Generate_File_Path().base_path('Sh/record_bag.sh')+' '+self.filepath+' ' + self.ip)


class Brush_Soc_Views(QDialog, Ui_BrushSoc):
    '''
        刷写Soc版本
    '''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tarfilepath = ''
        self.address = ''
        self.default_existent = 1
        self.timer = QTimer()
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.choose_file)
        self.pushButton_2.clicked.connect(self.check_pushbutton_text)
        self.pushButton_3.clicked.connect(self.close)
        self.timer.timeout.connect(self.brush_soc)

    def choose_file(self):
        files, ok1 = QFileDialog.getOpenFileName(self,
                                                 "文件选择",
                                                 "/home/user/",
                                                 "All Files (*);;Text Files (*)")
        self.tarfilepath = files

    def check_pushbutton_text(self):
        if self.pushButton_2.text() == "刷写soc":
            self.check_ip_tar()
        elif self.pushButton_2.text() == "立即重启":
            self.reboot_now()
        else:
            pass

    def check_ip_tar(self):
        '''
        检测用户输入的ip地址和选择的soc版本文件
        创建timer计时器
        '''
        "...."
        self.label_4.setText('')
        self.address = self.lineEdit.text()
        if not self.address:
            self.label_4.setText('ip不能为空')
            return
        address_re = "^\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
        res = re.findall(address_re, self.address)
        if not res:
            self.label_4.setText('输入ip格式错误')
            return
        if self.tarfilepath[-7:] != '.tar.gz':
            self.label_4.setText('请选择.tar.gz文件')
            return
        self.label_4.setText('正在刷写dailybuild,请稍等')
        self.timer.start(1)

    def brush_soc(self):
        '''
        检测板子中是否有原始文件
        '''
        self.timer.stop()
        address = 'root@{}'.format(self.address)
        res = subprocess.call('cd /home/user/Data/car_instance/', shell=True)
        if not res:
            res = subprocess.call(
                'timeout 3 ssh {} "rmdir /data/zros/"'.format(address), shell=True)
        if res:
            self.default_existent = 1
            res = subprocess.call(
                        'timeout 2 adb push {} /usr/bin/'.format(Generate_File_Path().base_path('Sh/killallnodes')), shell=True)
            if not res:
                res = subprocess.call('timeout 3 scp {}:/data/zros/res/car_instance/default* /home/user/Data/car_instance/'.format(address), shell=True)
                if not res:
                    self.default_existent = 1
                else:
                    self.default_existent = 0
                subprocess.call(
                    'timeout 2 ssh {} "killallnodes;cd /data/zros/;rm -r *"'.format(address), shell=True)
                res=self.push_tar(address)
                if res:
                    print('\nError')
                else:
                    self.label_4.setText("刷写完成")
                    print('\nSuccessful')
                    self.pushButton_2.setText('立即重启')
                    self.pushButton_3.setText('稍后重启')
                
            else:
                self.label_4.setText('请检查adb连接')
        else:
            self.default_existent=0
            res=subprocess.call(
                'timeout 3 ssh {} "mkdir /data/zros/"'.format(address), shell=True)
            res=self.push_tar(address)
            if res:
                print('\nError')
            else:
                self.label_4.setText('刷写完成')
                print('\nSuccessful')
                self.pushButton_2.setText('立即重启')
                self.pushButton_3.setText('稍后重启')

    def push_tar(self, address):
        '''
        刷写soc版本
        '''
        res=subprocess.call(
            'adb push -p {} /data/zros/'.format(self.tarfilepath), shell=True)
        if not res:
            res=subprocess.call(
                'ssh {} "cd /data/zros/;tar -zxvf *"'.format(address), shell=True)
        else:
            self.label_4.setText('推送dailybuild失败,请检查adb连接')
            return 1
        if not res:
            res=self.push_default(address)
            return res
        else:
            self.label_4.setText('解压dailybuild失败,请查看板子内存是否足够')
            return 1

    def push_default(self, address):
        if self.default_existent:
            res=subprocess.call(
                'timeout 3 scp /home/user/Data/car_instance/default* {}:/data/zros/res/car_instance/'.format(address), shell=True)
            if not res:
                return 0
            else:
                self.label_4.setText('替换default.xml和defaultDevice文件失败')
                return 1
        else:
            self.label_4.setText('请手动替换default.xml和defaultDevice')
            return 1

    def reboot_now(self):
        address='root@{}'.format(self.address)
        subprocess.call(
            'timeout 2 ssh {} "/sbin/reboot"'.format(address), shell=True)
        self.close()


class Mkdir_Path_Views(object):
    '''
        创建文件夹
    '''

    def mkdir_file_path(self, file_path):
        '''
        file_path:需要创建的文件夹路径
        return: 1 创建成功 0 创建失败
        '''
        if subprocess.call('mkdir -p {}'.format(file_path), shell=True):
            return 0
        else:
            return 1


class Find_File(object):
    '''
    查找文件
    '''

    def __init__(self):
        self.file_path_list=[]

    def find_file_path(self, filename, startdir):
        '''
        filename:需要查找的文件名;startdir:开始查找的起始路径
        return:查找到的所有文件路径列表
        '''
        for root, dirs, names in os.walk(startdir, topdown=False):
            for fname in names:
                if fname == filename:
                    filepath=os.path.join(root, fname)
                    self.file_path_list.append(filepath)
        return self.file_path_list

    def find_dir_path(self, dirname, startdir):
        '''
        dirname:需要查找的文件夹名;startdir:开始查找的起始路径
        retrun:查找到的所有文件夹路径的列表
        '''
        for root, dirs, names in os.walk(startdir):
            for dname in dirs:
                if dname == dirname:
                    dirpath=os.path.join(root, dname)
                    return dirpath


class Generate_File_Path(object):
    '''
        生成文件当前运行路径
    '''

    def base_path(self, path):
        '''
        path:文件当前位置
        retrun:文件在不同运行环境中的路径
        '''
        if getattr(sys, 'frozen', None):
            basedir=sys._MEIPASS
        else:
            basedir=os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basedir, path)
