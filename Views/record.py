import sys
import sip
from PyQt5.QtWidgets import QApplication
# MAIN_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
# BASE_PATH = os.path.dirname(MAIN_FILE_PATH)
# sys.path.append(os.path.join(BASE_PATH, "Ui/"))
from RecordInfo import Record_Info_Views

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Record_Info_Views()
    mainWindow.show()
    sys.exit(app.exec_())