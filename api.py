from fastapi import FastAPI, HTTPException, Query
import datetime
from typing import Optional
from odmantic import ObjectId
from models import (
    Student, Guardian, Course, Teacher, Classroom
)
from database import engine

app = FastAPI()

# CRUD ALUNO
@app.post("/students/", tags=["Student"])
async def create_student(student: Student):
    new_student = Student(**student.model_dump())
    if new_student.guardian_id:
        guardian = await engine.find_one(Guardian, Guardian.id == new_student.guardian_id)
        if not guardian:
            raise HTTPException(status_code=404, detail="Guardian not found")
        guardian.student_id = new_student.id
        await engine.save(guardian)
    else:
        raise HTTPException(status_code=404, detail="Guardian not found")
    
    for classroom_id in new_student.classroom_ids:
        classroom = await engine.find_one(Classroom, Classroom.id == classroom_id)
        if not classroom:
            raise HTTPException(status_code=404, detail="Classroom not found")
        classroom.student_ids.append(new_student.id)
        await engine.save(classroom)
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
async def update_student(student_id: ObjectId, student_data: Student):
    student = await engine.find_one(Student, Student.id == student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.model_update(student_data.model_dump(), exclude={"classroom_ids", "guardian_id", "id"})
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
async def create_guardian(guardian: Guardian):
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
async def update_guardian(guardian_id: ObjectId, guardian_data: Guardian):
    guardian = await engine.find_one(Guardian, Guardian.id == guardian_id)
    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")
    guardian.model_update(guardian_data.model_dump(), exclude={"student_id","id"})
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
async def create_course(course: Course):
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
async def update_course(course_id: ObjectId, course_data: Course):
    course = await engine.find_one(Course, Course.id == course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.model_update(course_data.model_dump(), exclude={"classroom_ids","id"})
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
async def create_teacher(teacher: Teacher):
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
async def update_teacher(teacher_id: ObjectId, teacher_data: Teacher):
    teacher = await engine.find_one(Teacher, Teacher.id == teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    teacher.model_update(teacher_data.model_dump(), exclude={"classroom_ids", "id"})
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
async def create_classroom(classroom: Classroom):
    new_classroom = Classroom(**classroom.model_dump())
    course = await engine.find_one(Course, Course.id == new_classroom.course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.classroom_ids.append(new_classroom.id)
    teacher = await engine.find_one(Teacher, Teacher.id == new_classroom.teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    teacher.classroom_ids.append(new_classroom.id)

    await engine.save(course)
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
async def update_classroom(classroom_id: ObjectId, classroom_data: Classroom):
    classroom = await engine.find_one(Classroom, Classroom.id == classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    classroom.model_update(classroom_data.model_dump(), exclude={"teacher_id", "course_id", "student_ids", "id"})
    await engine.save(classroom)
    return classroom

@app.delete("/classrooms/{classroom_id}", tags=["Classroom"])
async def delete_classroom(classroom_id: ObjectId):
    classroom = await engine.find_one(Classroom, Classroom.id == classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    await engine.delete(classroom)
    return {"message": "Classroom deleted"}

# QUANTIDADE DE ENTIDADES
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

# PAGINAÇÃO
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

# FILTRAR ENTIDADES POR ATRIBUTOS ESPECÍFICOS
@app.get("/filter/{collection_name}", tags=["Filtering"])
async def filter_entities(
    collection_name: str,
    name: Optional[str] = Query(None),
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
        query["name"] = {"$regex": name, "$options": "i"}
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

# CONSULTAS COMPLEXAS
@app.get("/classroom/{classroom_id}/students-with-guardians", tags=["Complex Queries"])
async def get_classroom_students_with_guardians(classroom_id: str):
    try:
        classroom_object_id = ObjectId(classroom_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid classroom ID format")

    classroom = await engine.find_one(Classroom, Classroom.id == classroom_object_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Course not found")

    students = await engine.find(Student, Student.classroom_ids == classroom_object_id)

    guardian_ids = [s.guardian_id for s in students if s.guardian_id]
    guardians = await engine.find(Guardian, Guardian.id.in_(guardian_ids))
    guardian_map = {g.id: g for g in guardians}

    return {
        "classroom": classroom,
        "students": [
            {
                "student": student,
                "guardian": guardian_map.get(student.guardian_id)
            } 
            for student in students
        ]
    }

@app.get("/teachers/{teacher_id}/courses-with-details", tags=["Complex Queries"])
async def get_teacher_classroom_with_details(teacher_id: str):
    try:
        obj_teacher_id = ObjectId(teacher_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid teacher ID format")

    teacher = await engine.find_one(Teacher, Teacher.id == obj_teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    classrooms = await engine.find(Classroom, Classroom.teacher_id == obj_teacher_id)

    student_ids = list({sid for classroom in classrooms for sid in classroom.student_ids})
    students = await engine.find(Student, Student.id.in_(student_ids))
    student_map = {s.id: s for s in students}

    course_ids = [c.course_id for c in classrooms]
    
    courses = await engine.find(Course, Course.id.in_(course_ids))
    courses_map = {c.id: c for c in courses}

    return {
        "teacher": teacher.name,
        "classrooms": [
            {
                "classroom": classroom,
                "courses": courses_map.get(classroom.course_id),
                "students": [student_map[sid] for sid in classroom.student_ids if sid in student_map]
            }
            for classroom in classrooms
        ]
    }

# DEMAIS CONSULTAS
# 1. Listagens filtradas por relacionamentos
@app.get("/students/by-guardian/{guardian_id}", tags=["Relationship Filtering"])
async def get_students_by_guardian(guardian_id: ObjectId):
    guardian = await engine.find_one(Guardian, Guardian.id == guardian_id)
    if not guardian:
        raise HTTPException(status_code=404, detail="Guardian not found")
    students = await engine.find(Student, Student.guardian_id == guardian_id)
    return students

# 2. Busca por texto parcial
@app.get("/courses/search", tags=["Text Search"])
async def search_courses(query: str = Query(...)):
    courses = await engine.find(Course, {
        "$or": [
            {"name": {"$regex": query, "$options": "i"}},
            {"description": {"$regex": query, "$options": "i"}}
        ]
    })
    return courses

# 3. Filtros por data/ano
@app.get("/students/by-graduation-year/{year}", tags=["Year Filter"])
async def get_students_by_graduation_year(year: int):
    current_year = datetime.now().year
    estimated_age = current_year - year + 18  # Supondo ano de formatura do ensino médio
    students = await engine.find(Student, Student.age >= estimated_age)
    return students

# 4. Agregações e contagens
@app.get("/courses/student-count", tags=["Aggregations"])
async def get_courses_student_count():
    pipeline = [
        {
            "$lookup": {
                "from": "classroom",
                "localField": "classroom_ids",
                "foreignField": "_id",
                "as": "classrooms"
            }
        },
        {
            "$project": {
                "name": 1,
                "total_students": {
                    "$sum": {
                        "$map": {
                            "input": "$classrooms",
                            "as": "class",
                            "in": {"$size": "$$class.student_ids"}
                        }
                    }
                }
            }
        }
    ]
    result = await engine.aggregate(Course, pipeline)
    return list(result)

# 5. Classificações e ordenações
@app.get("/students/", tags=["Student"])
async def list_students(
    sort_by: Optional[str] = None,
    order: Optional[str] = Query("asc", regex="^(asc|desc)$")
):
    sort = []
    if sort_by:
        if sort_by not in Student.__fields__:
            raise HTTPException(status_code=400, detail="Invalid sort field")
        sort_order = 1 if order == "asc" else -1
        sort.append((sort_by, sort_order))
    return await engine.find(Student, sort=sort)
