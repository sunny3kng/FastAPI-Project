from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory storage using a Python dictionary
students_db = {
    1: {"id": 1, "name": "John Doe", "age": 20, "sex": "male", "height": 175.5},
    2: {"id": 2, "name": "Jane Smith", "age": 22, "sex": "female", "height": 165.0},
}


# Endpoint to create a Student resource
@app.post("/students/")
def create_student(student_id: int, name: str, age: int, sex: str, height: float):
    if student_id in students_db:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    student = {"id": student_id, "name": name, "age": age, "sex": sex, "height": height}
    students_db[student_id] = student
    return student


# Endpoint to retrieve all Student resources
@app.get("/students/")
def get_students():
    return list(students_db.values())


# Endpoint to retrieve a specific Student resource
@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# Endpoint to update a specific Student resource
@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = {"id": student_id, "name": name, "age": age, "sex": sex, "height": height}
    return students_db[student_id]


# Endpoint to delete a specific Student resource
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}
