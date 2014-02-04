__author__ = 'gwindes'


from PySide.QtCore import *
from PySide.QtGui import *

from translator import Translator
import sys
import translator_gui

class MainDialog(QDialog, translator_gui.Ui_Dialog):
  translator = Translator()

  def __init__(self, parent=None):
    super(MainDialog, self).__init__(parent)
    self.setupUi(self)

    self.translateButton.clicked.connect(self.translate)

  def translate(self):
    self.translatedTextBox.setText("Translating...")
    src = self.originalTextBox.toPlainText()
    if src != "":
      translatedText = self.translator.translate(src)
      self.translatedTextBox.setText(translatedText)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  form = MainDialog()
  form.show()
  app.exec_()