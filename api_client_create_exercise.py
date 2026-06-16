from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict, CreateCourseResponseDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email


# Инициализируем запросы на создание пользователя, файла
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
    )





# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем пользователя для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)

# Создаем клиенты для работы с файлами, курсами и упражнениями
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Инициализируем словарь с файлом для загрузки
create_file_request = CreateFileRequestDict(
    filename="example.png",
    directory='courses',
    upload_file='testdata/files/example.png'
)

# Используем метод create_file
file_data = files_client.create_file(request=create_file_request)
print(f"Create file data: {file_data}")

# Инициализируем словарь с данными для создания курса
create_course_request = CreateCourseRequestDict(
    title="Python API Tests",
    maxScore=100,
    minScore=75,
    description="Course for Python API tests",
    estimatedTime="2 decades",
    previewFileId=file_data['file']["id"],
    createdByUserId=create_user_response["user"]["id"],
)

# Используем метод create_course
create_course_data = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_data}")

# Инициализируем словарь с данными для создания упражнения
create_exercise_request = CreateExerciseRequestDict(
    title='Делаем красиво',
    courseId=create_course_data["course"]["id"],
    maxScore=100,
    minScore=75,
    orderIndex=0,
    description="Сделай красиво",
    estimatedTime="12 минут"
)

#Используем метод create_exercise
create_exercise_data = exercises_client.create_exercise(create_exercise_request)
print(f'Create exercise data: {create_exercise_data}')