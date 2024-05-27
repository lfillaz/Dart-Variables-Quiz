import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton, QButtonGroup, QMessageBox
from PyQt5.QtGui import QPixmap

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.questions = [
            ("وش الطريقة الصح لإعلان متغير من نوع int في Dart؟",
             ["int number = \"10\";", "var number = 10;", "int number = 10;", "float number = 10.0;"], 2, "dart.png"),
            ("وش الفرق بين var و final في Dart؟",
             ["var تقدر تغير قيمته بعد التعيين، بس final ما تقدر تغيرها بعد التعيين.",
              "var يستخدم للأرقام بس، و final يستخدم لكل الأنواع.",
              "var لازم تحدد نوع البيانات، بس final ما يحتاج تحدد نوع البيانات.",
              "var و final يستخدمون بنفس الطريقة وما فيه فرق بينهم."], 0, "dart.png"),
            ("وش الطريقة الصح لإعلان متغير من نوع double في Dart؟",
             ["double value = 20;", "double value = 20.5;", "float value = 20.5;", "var value = 20.5;"], 1, "dart.png"),
            ("وش الفرق بين const و final في Dart؟",
             ["const تقدر تغير قيمته بعد التعيين، بس final ما تقدر تغيرها بعد التعيين.",
              "final تقدر تستخدمه مع المتغيرات المتغيرة، بس const لازم يكون ثابت وقت التحويل البرمجي.",
              "const يستخدم للأرقام بس، و final يستخدم لكل الأنواع.",
              "final و const ما فيه فرق بينهم."], 1, "dart.png"),
            ("وش الطريقة الصح لإعلان متغير من نوع String في Dart؟",
             ["String name = \"Alice\";", "string name = \"Alice\";", "var name = 'Alice';", "String name = 'Alice';"], 0, "dart.png"),
            ("وش نوع البيانات اللي يخزن قيمة true أو false في Dart؟",
             ["bool", "boolean", "Boolean", "var"], 0, "dart.png"),
            ("وش الكلمة المفتاحية اللي تستخدم لتحديد متغير ممكن يكون فارغ (nullable) في Dart؟",
             ["nullable", "?", "null", "optional"], 1, "dart.png"),
            ("وش الطريقة الصح لإعلان قائمة (List) في Dart تحتوي على أعداد صحيحة؟",
             ["List<int> numbers = [1, 2, 3];", "var numbers = [1, 2, 3];", "int[] numbers = {1, 2, 3];", "List numbers = [1, 2, 3];"], 0, "dart.png"),
            ("أي من الأكواد التالية مو صحيح في Dart؟",
             ["var x = 5;", "int y;", "const double z = 3.14;", "bool isTrue = \"true\";"], 3, "dart.png"),
            ("وش النتيجة المتوقعة من الكود التالي؟\nvoid main() {\n  var a;\n  print(a);\n}",
             ["null", "0", "خطأ أثناء التنفيذ", "لا شيء"], 0, "dart.png")
        ]
        
        self.current_question = 0
        self.score = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('اختبار المتغيرات في Dart ')
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

        self.submit_button = QPushButton('إرسال')
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
        QMessageBox.information(self, "النتيجة", f"نتيجتك النهائية: {self.score} من {len(self.questions)}")
        self.close()

def main():
    app = QApplication(sys.argv)
    quiz = QuizApp()
    quiz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
