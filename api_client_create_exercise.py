from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema



# Инициализируем запросы на создание пользователя, файла
create_user_request = CreateUserRequestSchema()

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем пользователя для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Создаем клиенты для работы с файлами, курсами и упражнениями
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Инициализируем словарь с файлом для загрузки
create_file_request = CreateFileRequestSchema(upload_file='testdata/files/example.png')

# Используем метод create_file
file_data = files_client.create_file(request=create_file_request)
print(f"Create file data: {file_data}")

# Инициализируем словарь с данными для создания курса
create_course_request = CreateCourseRequestSchema(
    preview_file_id=file_data.file.id,
    created_by_user_id=create_user_response.user.id)

# Используем метод create_course
create_course_data = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_data}")

# Инициализируем словарь с данными для создания упражнения
create_exercise_request = CreateExerciseRequestSchema(course_id=create_course_data.course.id)

#Используем метод create_exercise
create_exercise_data = exercises_client.create_exercise(create_exercise_request)
print(f'Create exercise data: {create_exercise_data}')