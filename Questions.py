class questions:

    def __init__(self, questions, a1, a2, a3, a4, answer):
        self._questions = questions
        self._a1 = a1
        self._a2 = a2
        self._a3 = a3
        self._a4 = a4
        self._answer = answer

    def set_questions(self, questions):
        self._questions = questions

    def set_a1(self, a1):
        self.a1 = a1

    def set_a2(self, a2):
        self.a2 = a2

    def set_a3(self, a3):
        self.a3 = a3

    def set_a4(self, a4):
        self.a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer


