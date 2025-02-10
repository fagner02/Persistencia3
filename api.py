
from fastapi import FastAPI, HTTPException
from odmantic import ObjectId
from models import (
    Student, Guardian, Course, Teacher, Classroom,
    StudentCreate, GuardianCreate, CourseCreate, TeacherCreate, ClassroomCreate
)
from database import engine

app = FastAPI()

# CRUD para Aluno
@app.post("/students/")
async def create_student(student: StudentCreate):
    new_student = Student(**student.model_dump())
    await engine.save(new_student)
    return new_student

@app.get("/students/")
async def list_students():
    return await engine.find(Student)

@app.put("/students/{student_id}")
async def update_student(student_id: ObjectId, student_data: StudentCreate):
    student = await engine.find_one(Student, Student.id == student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.update(student_data.dict())
    await engine.save(student)
    return student

@app.delete("/students/{student_id}")
async def delete_student(student_id: ObjectId):
    student = await engine.find_one(Student, Student.id == student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    await engine.delete(student)
    return {"message": "Student deleted"}
