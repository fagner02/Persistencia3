
from odmantic import Model, Field
from typing import List, Optional
from bson import ObjectId

# Entidade: Aluno
class Student(Model):
    name: str
    age: int
    grade: str  
    guardian_id: Optional[ObjectId] = None  # Relação 1x1
    course_ids: List[ObjectId] = Field(default_factory=list)  # Relação NxN

# Entidade: Responsável
class Guardian(Model):
    name: str
    phone: str
    email: str
    address: str
    student_id: Optional[ObjectId] = None  # Relação 1x1 
    
# Entidade: Curso
class Course(Model):
    name: str
    description: str
    teacher_id: ObjectId = Field(...)  # Relação 1xN 
    student_ids: List[ObjectId] = Field(default_factory=list)  # Relação NxN

# Entidade: Professor
class Teacher(Model):
    name: str
    subject: str
    email: str
    phone: str
    course_ids: List[ObjectId] = Field(default_factory=list)  # Relação 1xN

# Entidade: Sala de Aula
class Classroom(Model):
    room_number: str
    capacity: int
    course_id: ObjectId = Field(...)  # Relação 1x1 
    teacher_id: ObjectId = Field(...)  # Relação 1x1

class StudentCreate(Model):
    name: str
    age: int
    grade: str
    guardian_id: Optional[ObjectId] = None
    course_ids: List[ObjectId] = []

class GuardianCreate(Model):
    name: str
    phone: str
    email: str
    address: str
    student_id: Optional[ObjectId] = None

class CourseCreate(Model):
    name: str
    description: str
    teacher_id: ObjectId
    student_ids: List[ObjectId] = []

class TeacherCreate(Model):
    name: str
    subject: str
    email: str
    phone: str
    course_ids: List[ObjectId] = []

class ClassroomCreate(Model):
    room_number: str
    capacity: int
    course_id: ObjectId
    teacher_id: ObjectId