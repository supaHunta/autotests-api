from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCource(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""

        print(f"Получен запрос к методу GetCourse по курсу {request.course_id}")
        #Формируем ответное сообщение
        response = {"course_id": request.course_id,
                    "title": "Автотесты API",
                    "description": "Будем изучать написание API автотестов"}
        #Отправляем ответное сообщение
        return course_service_pb2.GetCourseResponse(course_id = response["course_id"],
                                                    title = response["title"],
                                                    description = response["description"])

def serve():
    """Функция создает и запускает gRPC-Сервер"""

    # Создаем сервер с использованием пула потоков(до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    #Регистрируем сервис GetCourse на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    #Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port("[::]:50051")

    #Запускаем сервер
    server.start()
    print("Сервер запущен на порту 50051...")

    #Ожидаем завершения работы сервера
    server.wait_for_termination()

# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()