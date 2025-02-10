
from odmantic import Model, Field, Reference
from typing import List, Optional
from pydantic import BaseModel

# Entidade: Aluno
class Student(Model):
    name: str
    age: int
    grade: str  # Ano escolar
    guardian_id: Optional[int] = Field(default=None, foreign_key="guardian.id")  # Relação 1x1
    courses: List[int] = Field(default_factory=list)  # Relação NxN

# Entidade: Responsável
class Guardian(Model):
    name: str
    phone: str
    email: str
    address: str
    student_id: Optional[int] = Field(default=None, foreign_key="student.id")  # Relação 1x1

# Entidade: Curso
class Course(Model):
    name: str
    description: str
    teacher_id: int = Field(foreign_key="teacher.id")  # Relação 1xN
    students: List[int] = Field(default_factory=list)  # Relação NxN

# Entidade: Professor
class Teacher(Model):
    name: str
    subject: str
    email: str
    phone: str
    courses: List[int] = Field(default_factory=list)  # Relação 1xN

# Entidade: Sala de Aula
class Classroom(Model):
    room_number: str
    capacity: int
    course_id: int = Field(foreign_key="course.id")  # Relação 1x1
    teacher_id: int = Field(foreign_key="teacher.id")  # Relação 1x1

# Schemas Pydantic para validação de entrada
class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str
    guardian_id: Optional[int] = None
    courses: List[int] = []

class GuardianCreate(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    student_id: Optional[int] = None

class CourseCreate(BaseModel):
    name: str
    description: str
    teacher_id: int
    students: List[int] = []

class TeacherCreate(BaseModel):
    name: str
    subject: str
    email: str
    phone: str
    courses: List[int] = []

class ClassroomCreate(BaseModel):
    room_number: str
    capacity: int
    course_id: int
    teacher_id: int
