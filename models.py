from odmantic import Model, Field
from typing import List, Optional
from bson import ObjectId

# ENTIDADE: ALUNO
class Student(Model):
    name: str
    age: int
    grade: str  
    guardian_id: Optional[ObjectId] = None  # Relação 1x1
    classroom_ids: List[ObjectId] = Field(default_factory=list)  # Relação NxN

# ENTIDADE: RESPONSÁVEL
class Guardian(Model):
    name: str
    phone: str
    email: str
    address: str
    student_id: Optional[ObjectId] = None  # Relação 1x1 

# ENTIDADE: CURSO
class Course(Model):
    name: str
    description: str
    credits: int
    prerequisites: List[str] = Field(default_factory=list)
    classroom_ids: List[ObjectId] = Field(default_factory=list)  # Relação 1xN

# ENTIDADE: PROFESSOR
class Teacher(Model):
    name: str
    subject: str
    email: str
    phone: str
    classroom_ids: List[ObjectId] = Field(default_factory=list)  # Relação 1xN

# ENTIDADE: SALA DE AULA
class Classroom(Model):
    room_number: str
    capacity: int
    course_id: ObjectId = Field(...)  # Relação 1xN
    teacher_id: ObjectId = Field(...)  # Relação 1xN
    student_ids: List[ObjectId] = Field(default_factory=list)  # Relação NxN
