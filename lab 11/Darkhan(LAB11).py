import math
from datetime import datetime

# ===== БАЗОВЫЕ КЛАССЫ =====

class Person:
    """Базовый класс для всех персон"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._created_at = datetime.now()
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def display_info(self):
        print(f"👤 Имя: {self._name}, Возраст: {self._age}")
    
    def __str__(self):
        return f"{self._name} ({self._age} лет)"

# ===== НАСЛЕДОВАНИЕ =====

class Student(Person):
    """Класс студента"""
    
    def __init__(self, name, age, student_id, major, gpa=0.0):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.courses = []
    
    def display_info(self):
        print(f"🎓 Студент: {self._name}, ID: {self.student_id}")
        print(f"   Специальность: {self.major}, GPA: {self.gpa:.2f}")
    
    def add_course(self, course_name):
        self.courses.append(course_name)
        print(f"✅ {self._name} записан на курс: {course_name}")
    
    def study(self):
        print(f"📚 {self._name} учится по специальности {self.major}")

class Teacher(Person):
    """Класс преподавателя"""
    
    def __init__(self, name, age, department, salary):
        super().__init__(name, age)
        self.department = department
        self.salary = salary
        self.subjects = []
    
    def display_info(self):
        print(f"👨‍🏫 Преподаватель: {self._name}, Кафедра: {self.department}")
        print(f"   Зарплата: {self.salary}₸")
    
    def add_subject(self, subject):
        self.subjects.append(subject)
        print(f"📖 {self._name} преподает: {subject}")
    
    def teach(self):
        print(f"🎯 {self._name} проводит лекцию")

# ===== МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ =====

class Researcher:
    """Класс исследователя"""
    
    def __init__(self, research_area):
        self.research_area = research_area
        self.publications = []
    
    def conduct_research(self):
        print(f"🔬 Проводит исследование в области: {self.research_area}")
    
    def publish_paper(self, paper_title):
        self.publications.append(paper_title)
        print(f"📄 Опубликована статья: '{paper_title}'")

class Professor(Teacher, Researcher):
    """Класс профессора"""
    
    def __init__(self, name, age, department, salary, research_area):
        Teacher.__init__(self, name, age, department, salary)
        Researcher.__init__(self, research_area)
        self.rank = "Профессор"
    
    def display_info(self):
        print(f"🎩 {self.rank}: {self._name}")
        print(f"   Кафедра: {self.department}, Область исследований: {self.research_area}")
    
    def work(self):
        self.teach()
        self.conduct_research()

# ===== ПОЛИМОРФИЗМ С ГЕОМЕТРИЧЕСКИМИ ФИГУРАМИ =====

class Shape:
    """Базовый класс для геометрических фигур"""
    
    def area(self):
        raise NotImplementedError("Метод area должен быть переопределен")
    
    def perimeter(self):
        raise NotImplementedError("Метод perimeter должен быть переопределен")
    
    def display_info(self):
        print(f"📐 Фигура: {self.__class__.__name__}")
        print(f"   Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

# ===== ДЕМОНСТРАЦИЯ =====

def main():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ ООП В PYTHON")
    print("=" * 50)
    
    # Создание объектов
    student1 = Student("Айгерим", 20, "ST2024", "Компьютерные науки", 3.8)
    student2 = Student("Арман", 21, "ST2025", "Инженерия", 3.5)
    teacher = Teacher("Гульнара", 45, "Математика", 250000)
    professor = Professor("Алишер", 50, "Информатика", 400000, "Искусственный интеллект")
    
    # Наследование
    print("\n1. НАСЛЕДОВАНИЕ:")
    print("-" * 30)
    for person in [student1, student2, teacher, professor]:
        person.display_info()
        print()
    
    # Полиморфизм с фигурами
    print("\n2. ПОЛИМОРФИЗМ С ФИГУРАМИ:")
    print("-" * 30)
    for shape in [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]:
        shape.display_info()
        print()
    
    # Взаимодействие объектов
    print("\n3. ВЗАИМОДЕЙСТВИЕ ОБЪЕКТОВ:")
    print("-" * 30)
    student1.add_course("Программирование на Python")
    student1.add_course("Базы данных")
    student1.study()
    
    print()
    teacher.add_subject("Высшая математика")
    teacher.teach()
    
    print()
    professor.work()
    professor.publish_paper("Новые методы машинного обучения")
    
    # Информация о студентах
    print("\n4. ИНФОРМАЦИЯ О СТУДЕНТАХ:")
    print("-" * 30)
    for student in [student1, student2]:
        print(f"{student.name} (возраст: {student.age}) - {student.major}")
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА!")
    print("=" * 50)

if __name__ == "__main__":
    main()
