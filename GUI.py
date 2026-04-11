import sys
from PySide6.QtGui import QFont,QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit,QVBoxLayout,QPushButton
from PySide6.QtMultimedia import QSoundEffect, QAudioFormat
from PySide6.QtCore import QUrl
from PySide6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CYBER GUARD")
        self.setGeometry(100, 100, 400, 200) # (x, y, width, height)
        #صورة الواجهة
        back1 = QLabel(self)
        back1.setPixmap(QPixmap(r"C:\Users\PC\Desktop\OOP cyber guard project\2.png"))
        back1.setScaledContents(True)
        back1.setGeometry(0, 0, 1540, 790)
        #اظهار label و تصميمه
        label1=QLabel("Welcome to CYBER GUARD Solutions",self)
        label1.setFont(QFont("Rubik Glitch", 30))
        label1.move(400,250)
        label1.setStyleSheet("font-size:40px;color:#b5dcff;")
        label1.adjustSize()

        label2 = QLabel("Choose a file",self)
        label2.setStyleSheet("QLabel { color: #b5dcff; }")
        label2.setFont(QFont("Rubik Glitch", 30))
        label2.move(640,300)
        label2.setStyleSheet("font-size:40px;color:#b5dcff;")
        label2.adjustSize()
#تصميم زر التشفير
        self.btn_encrypt = QPushButton("Encrypt", self)
        self.btn_encrypt.setGeometry(650, 400, 200, 50)
        self.btn_encrypt.raise_()
        self.btn_encrypt.setStyleSheet("""
            QPushButton {
                background-color: #0a1f44;
                color: #b5dcff;
                border-radius: 15px;
                padding: 10px;
                font-size: 16px;
                font-family: "Bungee";
                
            }

            QPushButton:hover {
                background-color: #143d7a;
            }

            QPushButton:pressed {
                background-color: #08142b;
            }
        """)
#تصميم زر فك التشفير
        self.btn_decrypt = QPushButton("Decrypt", self)
        self.btn_decrypt.setGeometry(650, 600, 200, 50)
        self.btn_decrypt.setStyleSheet("""
                    QPushButton {
                        background-color: #0a1f44;
                        color: #b5dcff;
                        border-radius: 15px;
                        padding: 10px;
                        font-size: 16px;
                        font-family: "Bungee";

                    }

                    QPushButton:hover {
                        background-color: #143d7a;
                    }

                    QPushButton:pressed {
                        background-color: #08142b;
                    }
                """)



    #حقل كتابة او text field وتصميمه
        self.ent_message = QLineEdit(self)
        self.ent_message.setGeometry(600, 500,300, 40)
        self.ent_message.setStyleSheet("font-size:10px;color:#b5dcff;font-family:'Bungee';background-color:#281C59;")
# صوت زر التشفير
        self.sound = QSoundEffect(self)
        self.sound.setSource(QUrl.fromLocalFile(r"C:\Users\PC\Downloads\universfield-button-124476.wav"))
        self.sound.setVolume(1.0)
        self.btn_encrypt.clicked.connect(self.play_sound)
#صوت الزر مال فك الشفرة
        self.sound=QSoundEffect(self)
        self.sound.setSource(QUrl.fromLocalFile(r"C:\Users\PC\Downloads\universfield-button-124476.wav"))
        self.sound.setVolume(1.0)
        self.btn_decrypt.clicked.connect(self.play_sound)

    def play_sound(self):
        self.sound.play()
        #tesssssssssssssst

#لغرض تجربة و اظهار الواجهة
if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Start the application event loop
    sys.exit(app.exec())
