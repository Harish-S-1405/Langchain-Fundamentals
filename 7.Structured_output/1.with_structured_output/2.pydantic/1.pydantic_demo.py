from pydantic import BaseModel, EmailStr , Field
from typing import Optional



class Student(BaseModel):
#    name:str # basic example
     name:str = 'harish' # default example
     age: Optional[int] = None # Optional 
     email: EmailStr # builtin validation
     cgpa:  float = Field(gt=0 , lt=10 , default =5 , description='A decimal value representing the cgpa of the student') # field function with default, contraint , description , regex


# new_student={'name': 'harish'} # basic example
new_student={} # default example
new_student={"age": 32 } # Optional new_student={} = None 
new_student={"age": "32" } # coerce example - implicit type conversion
new_student={"age": 32 , 'email': 'abc@gmail.com' } # built in validation
new_student={"age": 32 , 'email': 'abc@gmail.com', 'cgpa': 5.6} # field function
new_student={"age": 32 , 'email': 'abc@gmail.com'} # field with default value
new_student={"age": 32 , 'email': 'abc@gmail.com', 'cgpa': 5.6}

student = Student(**new_student)  # pydantic object 

# print(student)   - using pydantic object
# print(student.age) - using Pydantic object

# convertiong to json or python dictionary from pydantic object

# student_dict = dict(student)

# print(student_dict)
# print(student_dict['age'])

student_json = student.model_dump_json()

print(student_json)
