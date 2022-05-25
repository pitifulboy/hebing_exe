import os
import pandas as pd
import warnings
from combine_files_UI import Ui_mainWindow
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time

warnings.filterwarnings("ignore")  # 忽略warning消息


class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self, folderpath, savePath, headerline_num, skip_footer_num):
        super(Runthread, self).__init__()
        self.folderpath = folderpath
        self.savePath = savePath
        self.headerline_num = headerline_num
        self.skip_footer_num = skip_footer_num

    def __del__(self):
        self.wait()

    def run(self):
        dir_10 = self.folderpath

        for root_10, dirs_10, files_10 in os.walk(dir_10):
            if ".csv" in files_10[0]:
                self.run_csv()
            else:
                self.run_xlsx()

    def run_csv(self):
        start_time = time.time()
        dir = self.folderpath
        DFs = []  # 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框,依次读取多个相同结构的Excel文件并创建DataFrame）

        # 判断文件类型，是CSV文件还是xlsx文件。
        # 将第一个excel的sheet名称保存下来，便于汇总后命名

        self._signal.emit('开始合并' + '” \n')

        num = 0
        for root3, dirs3, file3s in os.walk(dir):
            for file3 in file3s:
                file_path3 = os.path.join(root3, file3)  # 测试的文件夹中，没有子文件夹，所以用当前文件夹和文件名组合成一个完整路径
                df = pd.read_csv(file_path3, header=self.headerline_num - 1, encoding="gb18030",
                                 skipfooter=self.skip_footer_num, dtype=str)  # 防止订单号太长，默认都是string格式
                if df.empty:
                    self._signal.emit('“' + file3 + '”是空表' + '\n')
                    if num == 0:
                        DFs.append(df)
                    else:
                        pass
                else:
                    self._signal.emit('正在合并 “' + file3 + '”\n')

                    DFs.append(df)
                num = num + 1
        alldata = pd.concat(DFs)
        # 获取待合并文件夹的名称，作为合并后文件名和sheet名称
        filename = os.path.basename(dir)
        pathssss = os.path.join(self.savePath, filename + '.xlsx')
        alldata.to_excel(pathssss, sheet_name=filename, index=False,
                         engine='openpyxl')  # index：表示是否写行索引，默认为True

        # 记录结束时间
        end_time = time.time()
        times = round(end_time - start_time, 2)

        self._signal.emit('合并完成，耗时' + format(times) + '秒' + '\n')

    def run_xlsx(self):
        start_time = time.time()
        dir = self.folderpath
        DFs = []  # 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框,依次读取多个相同结构的Excel文件并创建DataFrame）
        # 判断文件类型，是CSV文件还是xlsx文件。
        # 将第一个excel的sheet名称保存下来，便于汇总后命名
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)  # 文件夹中，没有子文件夹，用当前文件夹和文件名组合成一个完整路径
                if file == files[0]:
                    sheetnames = pd.read_excel(file_path, sheet_name=None).keys()


        for this_sheetname in sheetnames:
            self._signal.emit('开始合并sheet “' + this_sheetname + '”sheet \n')

            num = 0
            for root2, dirs2, file2s in os.walk(dir):
                for file2 in file2s:
                    file_path2 = os.path.join(root2, file2)  # 测试的文件夹中，没有子文件夹，所以用当前文件夹和文件名组合成一个完整路径
                    df = pd.read_excel(file_path2, sheet_name=this_sheetname, header=self.headerline_num - 1,
                                       skipfooter=self.skip_footer_num, dtype=str)  # 防止订单号太长，默认都是string格式
                    if df.empty:
                        self._signal.emit('“' + file2 + '”中的“' + this_sheetname + '”sheet，是空表' + '\n')
                        if num == 0:
                            DFs.append(df)
                        else:
                            pass
                    else:
                        self._signal.emit('正在合并 “' + file2 + '”中的“' + this_sheetname + '”sheet\n')

                        DFs.append(df)
                    num = num + 1
            alldata = pd.concat(DFs)
            pathssss = os.path.join(self.savePath, this_sheetname + '.xlsx')
            alldata.to_excel(pathssss, sheet_name=this_sheetname, index=False,
                             engine='openpyxl')  # index：表示是否写行索引，默认为True
            DFs = []

        # 记录结束时间
        end_time = time.time()
        times = round(end_time - start_time, 2)

        self._signal.emit('合并完成，耗时' + format(times) + '秒' + '\n')


class combine_files(QtWidgets.QMainWindow):

    # 初始化
    def __init__(self):
        super(combine_files, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.thread = None

    # 获取待合并文件夹地址
    def select_filefolderpath_click(self):
        # 选择待合并的文件夹
        file_name = QtWidgets.QFileDialog.getExistingDirectory(None, "Select File Directory to Save File", "")
        self.filename = file_name
        self.ui.TextEdit_filefolder_path.setText(file_name)

        # 默认保存在待合并文件的上一级文件夹中
        self.savePath = os.path.dirname(file_name)
        self.ui.TextEdit_savefolder_path.setText(self.savePath)

    # 选择新的文件夹保存文件
    def select_savepath_click(self):
        savepath = QtWidgets.QFileDialog.getExistingDirectory(None, "Select File Directory to Save File", "")
        self.ui.TextEdit_savefolder_path.setText(savepath)
        self.savePath = savepath

    def combine_click(self):
        self.ui.textBrowser_msg.moveCursor(self.ui.textBrowser_msg.textCursor().atEnd())

        headerline_num = int(self.ui.textEdit_top_drop_num.toPlainText())
        skipfooter_num = int(self.ui.textEdit_buttom_drop_num.toPlainText())
        # 清空进度框
        self.ui.textBrowser_msg.setText("")
        self.headerline_num = headerline_num
        self.skipfooter_num = skipfooter_num
        self.start_combine_exe()

    def start_combine_exe(self):
        self.thread = Runthread(folderpath=self.filename, savePath=self.savePath, headerline_num=self.headerline_num,
                                skip_footer_num=self.skipfooter_num)
        self.thread._signal.connect(self.call_back)
        self.thread.start()

    def call_back(self, msg):
        self.ui.textBrowser_msg.append(msg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = combine_files()
    window.show()
    sys.exit(app.exec_())
