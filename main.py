from PyQt6.QtWidgets import*
import random

app = QApplication([])
window = QWidget()
window.resize(500,500)

nadpus = QLabel("ВІКТОРИНА")
winner_lbl = QLabel("?")
knopka = QPushButton("Визначити переможця")

dial = QDial()

data = QDateTimeEdit()

main_line = QVBoxLayout()
main_line.addWidget(nadpus)
main_line.addWidget(winner_lbl)
main_line.addWidget(knopka)

main_line.addWidget((dial))

main_line.addWidget(data)

window.setLayout(main_line)

def winner ():
    w = random.randint(1, 100)
    winner_lbl.setText(str(w))
knopka.clicked.connect(winner)

window.show()
app.exec()