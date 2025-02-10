from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from odmantic import ObjectId
from models import (
    Student, Guardian, Course, Teacher, Classroom,
    StudentCreate, GuardianCreate, CourseCreate, TeacherCreate, ClassroomCreate
)
from database import engine

app = FastAPI()

# CRUD ALUNO
@app.post("/students/", tags=["Student"])
async def create_student(student: StudentCreate):
    new_student = Student(**student.model_dump())
    print(new_student)
    await engine.save(new_student)
    return new_student

@app.get("/students/{student_id}", tags=["Student"])
async def get_student_by_id(student_id: ObjectId):
    student = await engine.find_one(Student, Student.id == student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

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

# CRUD RESPONSÁVEL
@app.post("/guardians/", tags=["Guardian"])
async def create_guardian(guardian: GuardianCreate):
    new_guardian = Guardian(**guardian.model_dump())
    await engine.save(new_guardian)
    return new_guardian

@app.get("/guardians/{guardian_id}", tags=["Guardian"])
async def get_guardian_by_id(guardian_id: ObjectId):
    guardian = await engine.find_one(Guardian, Guardian.id == guardian_id)
    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")
    return guardian

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

# CRUD CURSO
@app.post("/courses/", tags=["Course"])
async def create_course(course: CourseCreate):
    new_course = Course(**course.model_dump())
    await engine.save(new_course)
    return new_course

@app.get("/courses/{course_id}", tags=["Course"])
async def get_course_by_id(course_id: ObjectId):
    course = await engine.find_one(Course, Course.id == course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

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

# CRUD PROFESSOR
@app.post("/teachers/", tags=["Teacher"])
async def create_teacher(teacher: TeacherCreate):
    new_teacher = Teacher(**teacher.model_dump())
    await engine.save(new_teacher)
    return new_teacher

@app.get("/teachers/{teacher_id}", tags=["Teacher"])
async def get_teacher_by_id(teacher_id: ObjectId):
    teacher = await engine.find_one(Teacher, Teacher.id == teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

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

# CRUD SALA DE AULA
@app.post("/classrooms/", tags=["Classroom"])
async def create_classroom(classroom: ClassroomCreate):
    new_classroom = Classroom(**classroom.model_dump())
    await engine.save(new_classroom)
    return new_classroom

@app.get("/classrooms/{classroom_id}", tags=["Classroom"])
async def get_classroom_by_id(classroom_id: ObjectId):
    classroom = await engine.find_one(Classroom, Classroom.id == classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom

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

@app.get("/count/{collection_name}", tags=["Count"])
async def count_entities(collection_name: str):
    collections = {
        "students": Student,
        "guardians": Guardian,
        "courses": Course,
        "teachers": Teacher,
        "classrooms": Classroom,
    }

    if collection_name not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")

    model = collections[collection_name]
    count = await engine.count(model)
    return {"collection": collection_name, "count": count}

@app.get("/paginate/{collection_name}", tags=["Pagination"])
async def paginate_entities(
    collection_name: str,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    collections = {
        "students": Student,
        "guardians": Guardian,
        "courses": Course,
        "teachers": Teacher,
        "classrooms": Classroom,
    }

    if collection_name not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")

    total = await engine.count(collections[collection_name])
    model = collections[collection_name]
    skip = (page - 1) * limit
    entities = await engine.find(model, skip=skip, limit=limit)
    return {
        "total": total,
        "collection": collection_name,
        "page": page,
        "limit": limit,
        "results": entities
    }

@app.get("/filter/{collection_name}", tags=["Filtering"])
async def filter_entities(
    collection_name: str,
    name: Optional[str] = Query(None),
    grade: Optional[str] = Query(None),
    subject: Optional[str] = Query(None),
    min_age: Optional[int] = Query(None),
    max_age: Optional[int] = Query(None)
):
    collections = {
        "students": Student,
        "guardians": Guardian,
        "courses": Course,
        "teachers": Teacher,
        "classrooms": Classroom,
    }

    if collection_name not in collections:
        raise HTTPException(status_code=404, detail="Collection not found")

    model = collections[collection_name]
    query = {}

    if name:
        query["name"] = name
    if grade:
        query["grade"] = grade
    if subject:
        query["subject"] = subject
    if min_age is not None:
        query["age"] = {"$gte": min_age}
    if max_age is not None:
        query["age"] = {**query.get("age", {}), "$lte": max_age}

    entities = await engine.find(model, query)
    return {
        "collection": collection_name,
        "filters": query,
        "results": entities
    }