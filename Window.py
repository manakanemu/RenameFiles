from RenameUI import Ui_RenameWidget
from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
import os,re
from functools import partial
import traceback

class Window(Ui_RenameWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.init_vars()
        self.register_widget()
        self.bind_event()
        self.setQSS()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        try:
            url = e.mimeData().urls()[0]
            path = url.toLocalFile()
            print(path)
            if not path or not os.path.isdir(path):
                return
            self.clear_widget_vars()
            self.path = path
            self.edit_path.setText(path)
            self._files = [file for file in sorted(os.listdir(path)) if not file.startswith('.')]
            self.filter_files(self.edit_filter.text())

        except:
            return


    def init_vars(self):
        self.path = ''
        self._files = []
        self.filted_files = []
        self.changed_files = []

    def register_widget(self):
        self.dialog_file = QFileDialog(self)

    def list_scroll(self,bar,value):
        bar.blockSignals(True)
        bar.verticalScrollBar().setValue(value)
        bar.blockSignals(False)

    def bind_event(self):
        self.button_select_path.clicked.connect(self.select_dir)
        self.edit_filter.textChanged.connect(self.filter_files)
        self.edit_match_pattern.textChanged.connect(self.update_changed_files)
        self.edit_start.textChanged.connect(self.update_changed_files)
        self.edit_match_result.textChanged.connect(self.update_changed_files)
        self.button_change_name.clicked.connect(self.change_file_name)
        self.listview_filted.itemClicked.connect(self.copy_file_name)

        bar_filter = self.listview_filted.verticalScrollBar()
        bar_changed = self.listview_changed.verticalScrollBar()
        bar_filter.valueChanged.connect(partial(self.list_scroll, self.listview_changed))
        bar_changed.valueChanged.connect(partial(self.list_scroll, self.listview_filted))

    def copy_file_name(self):

        self.edit_match_result.setText(os.path.splitext(self.filted_files[self.listview_filted.currentRow()])[0])

    def update_filted_files(self):
        self.listview_filted.clear()
        self.listview_filted.addItems(self.filted_files)

    def update_changed_files(self):
        patterns = self._get_match_patterns()
        counter_start,counter_length = self._get_start()
        match_model = self._get_match_model()
        if not match_model:
            self.changed_files = self.filted_files
        else:
            changed_files = []
            for i in range(len(self.filted_files)):
                file = self.filted_files[i]
                file_name,sub = os.path.splitext(file)
                try:
                    match_titles = [re.search(pattern,file_name)  for pattern in patterns]
                    match_titles = ['' if not title else title[0] if not title.lastindex else title[title.lastindex] for title in match_titles]
                    new_name = match_model.format(*match_titles)
                    new_name = new_name.replace('$count', str(counter_start + i).zfill(counter_length))
                    changed_files.append(new_name + sub)
                except :
                    traceback.print_exc()
                    return
            self.changed_files = changed_files

        self.listview_changed.clear()
        self.listview_changed.addItems(self.changed_files)
        for i in range(self.listview_changed.count()):
            it = self.listview_changed.item(i)
            it.setFlags(it.flags() & ~Qt.ItemIsSelectable)



    def filter_files(self,pattern):
        filted_files = []
        for file in self._files:
            try:
                if re.search(pattern, file) is not None:
                    filted_files.append(file)
            except:
                return
        self.filted_files = filted_files
        self.update_filted_files()
        self.update_changed_files()


    def select_dir(self):
        path = self.dialog_file.getExistingDirectory(self, '选择目录', '/', QFileDialog.ShowDirsOnly)
        if not path:
            return
        self.clear_widget_vars()
        self.path = path
        self.edit_path.setText(path)
        self._files = [file for file in sorted(os.listdir(path)) if not file.startswith('.')]
        self.filter_files(self.edit_filter.text())

    def _get_start(self):
        try:
            return (int(self.edit_start.text()),len(self.edit_start.text()))
        except:
            return (1,2)

    def _get_match_patterns(self):
        patterns = self.edit_match_pattern.text()
        if not patterns:
            return []
        return self.edit_match_pattern.text().split(':')

    def _get_match_model(self):
        return self.edit_match_result.text()

    def clear_widget_vars(self):
        self.init_vars()
        self.edit_path.clear()
        self.edit_filter.clear()
        self.edit_match_pattern.clear()
        self.edit_match_result.clear()
        self.edit_start.clear()
        self.listview_changed.clear()
        self.listview_filted.clear()

    def change_file_name(self):
        if len(set(self.changed_files)) == len(self.filted_files) and self.filted_files:
            for i in range(len(self.filted_files)):
                old_file = os.path.join(self.path,self.filted_files[i])
                new_file = os.path.join(self.path,self.changed_files[i])
                os.rename(old_file,new_file)

            self.clear_widget_vars()


    def setQSS(self):

        edit_style = '''
        QLineEdit{padding-left:7px;border:0px;border-radius:2px;height:30px;}
        '''
        self.edit_path.setStyleSheet(edit_style)
        self.edit_filter.setStyleSheet(edit_style)
        self.edit_match_pattern.setStyleSheet(edit_style)
        self.edit_match_result.setStyleSheet(edit_style)
        self.edit_start.setStyleSheet(edit_style)


        listwidget_style = '''QListWidget{
            border:0px;
            border-radius:5px;
            margin-right:0px;
        }
        QListWidget:item{
        padding-left:8px;
        height:30px;
        border-bottom:1px solid #e5e5e5;
        }
        QListWidget:item:selected{
        background:#409EFF;
        }
        '''
        self.listview_filted.setStyleSheet(listwidget_style)
        self.listview_changed.setStyleSheet(listwidget_style)
        self.listview_filted.verticalScrollBar().setStyleSheet('''
        QScrollBar{
        width:0px;
        }''')


        self.button_change_name.setStyleSheet('''
        QPushButton{
        background:#409EFF;
        color:white;
        border-radius:2px;height:30px;
        }
        QPushButton:hover{
        background:rgb(121, 187, 255);
        }
        ''')
        self.button_select_path.setStyleSheet('''
        QPushButton{
        background:#409EFF;
        color:white;
        border-radius:2px;height:30px;
        }
        QPushButton:hover{
        background:rgb(121, 187, 255);
        }
        ''')

