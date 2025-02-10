from odmantic import Model, Field
from typing import List, Optional
from bson import ObjectId

# Entidade: Aluno
class Student(Model):
    name: str
    age: int
    grade: str  
    guardian_id: Optional[ObjectId] = None  # Relação 1x1
    classroom_ids: List[ObjectId] = Field(default_factory=list)  # Relação NxN

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
    credits: int
    prerequisites: List[str] = Field(default_factory=list)
    classroom_ids: List[ObjectId] = Field(default_factory=list)  # Relação 1xN

# Entidade: Professor
class Teacher(Model):
    name: str
    subject: str
    email: str
    phone: str
    classroom_ids: List[ObjectId] = Field(default_factory=list)  # Relação 1xN

# Entidade: Sala de Aula
class Classroom(Model):
    room_number: str
    capacity: int
    course_id: ObjectId = Field(...)  # Relação 1xN
    teacher_id: ObjectId = Field(...)  # Relação 1xN
    student_ids: List[ObjectId] = Field(default_factory=list)  # Relação NxN
