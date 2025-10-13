University: ITMO University

Faculty: FICT

Course: Введение в веб технологии

Year: 2025/2026

Author: Boyko Ekaterina Olegovna

Lab: Lab2

Date of create: 11.10.2025

Date of finished: 13.10.2025

Прежде чем я присутпила к выполнению Лабораторной работы #2, я создала Dockerfile из лабораторной №1 под звездочкой: 
1. app.py
   
   <img width="677" height="277" alt="image" src="https://github.com/user-attachments/assets/b8329249-64b4-4400-9e70-cde1faee87c4" />
3. Dockerfile с помощью VS-Code 
   <img width="984" height="920" alt="image" src="https://github.com/user-attachments/assets/ce260b03-7e60-4f2a-bebf-6e6b079a5711" />
4. Сложила их в одну директорию (lab2): 
<img width="836" height="133" alt="image" src="https://github.com/user-attachments/assets/47973eb3-747f-4a1e-9572-0c429566162f" />

5. С помощью PythonShell собрала образ
   <img width="1915" height="580" alt="image" src="https://github.com/user-attachments/assets/8555fe54-7ed1-4f19-ae6f-67aacffc3f2c" />
6. Запустила контейнер и создала curl
<img width="1843" height="550" alt="image" src="https://github.com/user-attachments/assets/d429fd01-82f8-4b31-aa9a-8b5b912bbece" />
<img width="764" height="143" alt="image" src="https://github.com/user-attachments/assets/08b58b67-58c9-4918-a42a-fc8d3eaf0cad" />

Основная лабораторная работа: 

1. Создала новый репозиторий https://github.com/pustaaten/devops-lab2-boiko
2. Клонировала файлы в новый репозиторий
<img width="1222" height="393" alt="image" src="https://github.com/user-attachments/assets/530e2472-6474-40bb-9b54-a2a569ce2855" />

3. Создать аккаунт на Docker Hub | Создать новый репозиторий на Docker Hub для вашего образа
<img width="1217" height="568" alt="image" src="https://github.com/user-attachments/assets/ed752548-ed22-4269-ab8a-060c0683bc31" />

5. Создала ключи 
<img width="1011" height="561" alt="image" src="https://github.com/user-attachments/assets/7e708eb5-4764-44de-a02a-bd7ccc7fb8f6" />

6. Настройка GitHub Actions:
Создать папку .github/workflows/ в корне проекта
Создать файл docker-build.yml с пайплайном, который должен:
 - Запускаться при пуше в main ветку
   
 - Использовать Ubuntu как runner
   
 - Выполнять checkout кода
   
 - Настраивать Docker Buildx
   
 - Логиниться в Docker Hub используя секреты
   
 - Собирать и пушить образ с тегом username/my-flask-app:latest
   
 - Добавлять шаг деплоя (можно просто echo сообщение)

<img width="1171" height="614" alt="image" src="https://github.com/user-attachments/assets/061a0e61-f892-43b5-9d15-246bb901fcd5" />

7. Проверила выполнение пайплайна в разделе Actions:

<img width="1221" height="475" alt="image" src="https://github.com/user-attachments/assets/0ee45aef-2a3e-4c97-a4ea-42dff176d832" />

8. Убедилась, что образ появился в Docker Hub

<img width="990" height="511" alt="image" src="https://github.com/user-attachments/assets/d0c6c9e3-c8bb-4b9b-9a67-f96547363970" />

9. Проверила все логи: 

<img width="1807" height="879" alt="image" src="https://github.com/user-attachments/assets/b80fcba2-8f48-4544-b006-0f4299fb7968" />


