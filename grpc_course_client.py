from http.client import responses

import grpc

import course_service_pb2
import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

#Отправляем запрос
response = stub.GetCource(course_service_pb2.GetCourseRequest(course_id='api-course'))
print(f'course_id: "{response.course_id}"\n'
      f'title: "Автотесты API"\n'
      f'description: "Будем изучать написание API автотестов"')