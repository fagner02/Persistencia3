from fastapi import FastAPI, HTTPException
from odmantic import ObjectId
from models import (
    Student, Guardian, Course, Teacher, Classroom,
    StudentCreate, GuardianCreate, CourseCreate, TeacherCreate, ClassroomCreate
)
from database import engine

app = FastAPI()

# CRUD para Aluno
@app.post("/students/", tags=["Student"])
async def create_student(student: StudentCreate):
    new_student = Student(**student.model_dump())
    print(new_student)
    await engine.save(new_student)
    return new_student

@app.get("/students/", tags=["Student"])
async def list_students():
    return await engine.find(Student)

@app.put("/students/{student_id}", tags=["Student"])
async def update_student(student_id: ObjectId, student_data: StudentCreate):
    student = await engine.find_one(Student, Student.id == student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.model_update(student_data.model_dump())
    await engine.save(student)
    return student

@app.delete("/students/{student_id}", tags=["Student"])
async def delete_student(student_id: ObjectId):
    student = await engine.find_one(Student, Student.id == student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    await engine.delete(student)
    return {"message": "Student deleted"}


# CRUD para Responsável
@app.post("/guardians/", tags=["Guardian"])
async def create_guardian(guardian: GuardianCreate):
    new_guardian = Guardian(**guardian.model_dump())
    await engine.save(new_guardian)
    return new_guardian

@app.get("/guardians/", tags=["Guardian"])
async def list_guardians():
    return await engine.find(Guardian)

@app.put("/guardians/{guardian_id}", tags=["Guardian"])
async def update_guardian(guardian_id: ObjectId, guardian_data: GuardianCreate):
    guardian = await engine.find_one(Guardian, Guardian.id == guardian_id)
    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")
    guardian.model_update(guardian_data.model_dump())
    await engine.save(guardian)
    return guardian

@app.delete("/guardians/{guardian_id}", tags=["Guardian"])
async def delete_guardian(guardian_id: ObjectId):
    guardian = await engine.find_one(Guardian, Guardian.id == guardian_id)
    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")
    await engine.delete(guardian)
    return {"message": "Guardian deleted"}

# CRUD para Curso
@app.post("/courses/", tags=["Course"])
async def create_course(course: CourseCreate):
    new_course = Course(**course.model_dump())
    await engine.save(new_course)
    return new_course

@app.get("/courses/", tags=["Course"])
async def list_courses():
    return await engine.find(Course)

@app.put("/courses/{course_id}", tags=["Course"])
async def update_course(course_id: ObjectId, course_data: CourseCreate):
    course = await engine.find_one(Course, Course.id == course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.model_update(course_data.model_dump())
    await engine.save(course)
    return course

@app.delete("/courses/{course_id}", tags=["Course"])
async def delete_course(course_id: ObjectId):
    course = await engine.find_one(Course, Course.id == course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    await engine.delete(course)
    return {"message": "Course deleted"}

# CRUD para Professor
@app.post("/teachers/", tags=["Teacher"])
async def create_teacher(teacher: TeacherCreate):
    new_teacher = Teacher(**teacher.model_dump())
    await engine.save(new_teacher)
    return new_teacher

@app.get("/teachers/", tags=["Teacher"])
async def list_teachers():
    return await engine.find(Teacher)

@app.put("/teachers/{teacher_id}", tags=["Teacher"])
async def update_teacher(teacher_id: ObjectId, teacher_data: TeacherCreate):
    teacher = await engine.find_one(Teacher, Teacher.id == teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    teacher.model_update(teacher_data.model_dump())
    await engine.save(teacher)
    return teacher

@app.delete("/teachers/{teacher_id}", tags=["Teacher"])
async def delete_teacher(teacher_id: ObjectId):
    teacher = await engine.find_one(Teacher, Teacher.id == teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    await engine.delete(teacher)
    return {"message": "Teacher deleted"}

# CRUD para Sala de Aula
@app.post("/classrooms/", tags=["Classroom"])
async def create_classroom(classroom: ClassroomCreate):
    new_classroom = Classroom(**classroom.model_dump())
    await engine.save(new_classroom)
    return new_classroom

@app.get("/classrooms/", tags=["Classroom"])
async def list_classrooms():
    return await engine.find(Classroom)

@app.put("/classrooms/{classroom_id}", tags=["Classroom"])
async def update_classroom(classroom_id: ObjectId, classroom_data: ClassroomCreate):
    classroom = await engine.find_one(Classroom, Classroom.id == classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    classroom.model_update(classroom_data.model_dump())
    await engine.save(classroom)
    return classroom

@app.delete("/classrooms/{classroom_id}", tags=["Classroom"])
async def delete_classroom(classroom_id: ObjectId):
    classroom = await engine.find_one(Classroom, Classroom.id == classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    await engine.delete(classroom)
    return {"message": "Classroom deleted"}
