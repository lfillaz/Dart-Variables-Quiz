import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton, QButtonGroup, QMessageBox
from PyQt5.QtGui import QPixmap

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.questions = [
            ("What is the correct way to declare a variable of type int in Dart?",
             ["int number = \"10\";", "var number = 10;", "int number = 10;", "float number = 10.0;"], 2, "dart.png"),
            ("What is the difference between var and final in Dart?",
             ["var can be changed after assignment, while final cannot be changed after assignment.",
              "var is used only for numbers, while final is used for all types.",
              "var requires specifying the data type, while final does not require specifying the data type.",
              "var and final are used in the same way with no difference between them."], 0, "dart.png"),
            ("What is the correct way to declare a variable of type double in Dart?",
             ["double value = 20;", "double value = 20.5;", "float value = 20.5;", "var value = 20.5;"], 1, "dart.png"),
            ("What is the difference between const and final in Dart?",
             ["const can be changed after assignment, while final cannot be changed after assignment.",
              "final can be used with mutable variables, while const must be constant at compile time.",
              "const is used for numbers only, while final is used for all types.",
              "final and const have no difference between them."], 1, "dart.png"),
            ("What is the correct way to declare a variable of type String in Dart?",
             ["String name = \"Alice\";", "string name = \"Alice\";", "var name = 'Alice';", "String name = 'Alice';"], 0, "dart.png"),
            ("What is the data type used to store true or false value in Dart?",
             ["bool", "boolean", "Boolean", "var"], 0, "dart.png"),
            ("What is the keyword used to specify a variable that can be empty (nullable) in Dart?",
             ["nullable", "?", "null", "optional"], 1, "dart.png"),
            ("What is the correct way to declare a list in Dart containing integer numbers?",
             ["List<int> numbers = [1, 2, 3];", "var numbers = [1, 2, 3];", "int[] numbers = {1, 2, 3};", "List numbers = [1, 2, 3];"], 0, "dart.png"),
            ("Which of the following code snippets is not valid in Dart?",
             ["var x = 5;", "int y;", "const double z = 3.14;", "bool isTrue = \"true\";"], 3, "dart.png"),
            ("What is the expected output of the following code?\nvoid main() {\n  var a;\n  print(a);\n}",
             ["null", "0", "Error during execution", "Nothing"], 0, "dart.png")
        ]
        
        self.current_question = 0
        self.score = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dart Variables Quiz')
        self.layout = QVBoxLayout()
        
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)
        
        self.question_label = QLabel(self.questions[self.current_question][0])
        self.layout.addWidget(self.question_label)
        
        self.button_group = QButtonGroup(self)
        
        self.radio_buttons = []
        for i in range(4):
            radio_button = QRadioButton(self.questions[self.current_question][1][i])
            self.layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)
            self.button_group.addButton(radio_button, i)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)
        
        self.setLayout(self.layout)
        
        self.update_question()
    
    def check_answer(self):
        selected = self.button_group.checkedId()
        if selected == self.questions[self.current_question][2]:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()
    
    def update_question(self):
        self.question_label.setText(self.questions[self.current_question][0])
        for i, radio_button in enumerate(self.radio_buttons):
            radio_button.setText(self.questions[self.current_question][1][i])
            radio_button.setChecked(False)
        
        pixmap = QPixmap(self.questions[self.current_question][3])
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def show_result(self):
        QMessageBox.information(self, "Result", f"Your final score: {self.score} out of {len(self.questions)}")
        self.close()

def main():
    app = QApplication(sys.argv)
    quiz = QuizApp()
    quiz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()