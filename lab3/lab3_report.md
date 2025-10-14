University: ITMO University

Faculty: FICT

Course: Введение в веб технологии

Year: 2025/2026

Author: Boyko Ekaterina Olegovna

Lab: Lab3

Date of create: 14.10.2025

Date of finished: 14.10.2025

1. Создание конфигурации Prometheus:

- Создать папку prometheus для конфигурации
  
- Создать файл prometheus/prometheus.yml
<img width="944" height="486" alt="image" src="https://github.com/user-attachments/assets/6895e7d0-cf51-47be-969f-b24a0f56aa9b" />

2. Запустить контейнер Node Exporter для сбора системных метрик:
<img width="1280" height="224" alt="image" src="https://github.com/user-attachments/assets/0ae3a8fc-3328-486f-9388-eb8f31ea11d6" />

3. Проверить работу:
<img width="1002" height="395" alt="image" src="https://github.com/user-attachments/assets/c9d05afa-c434-4782-8a63-f08c032f9eae" />
<img width="1280" height="679" alt="image" src="https://github.com/user-attachments/assets/e28d7a6a-0c61-4e24-b949-20378eb2999d" />


4. Запуск Prometheus:
   
- Создать том для данных Prometheus
  <img width="1153" height="46" alt="image_2025-10-14_14-37-14" src="https://github.com/user-attachments/assets/f649d3e6-2403-4dfd-acc7-96078a533c7a" />

- Запустить контейнер Prometheus
  <img width="1280" height="341" alt="image" src="https://github.com/user-attachments/assets/09fee024-6182-4c35-855d-b620b9d42edc" />

- Проверить работу
  <img width="1280" height="708" alt="image" src="https://github.com/user-attachments/assets/54e96160-c9d0-4a8c-b70a-a403170a3e6e" />

5. Запуск Grafana:
   
- Создать том для данных Grafana
  
- Запустить контейнер Grafana:
<img width="1280" height="405" alt="image" src="https://github.com/user-attachments/assets/c36e17a7-e3ca-4b54-9dd4-db44bd53a438" />

- Проверить работу:
  <img width="1219" height="603" alt="image" src="https://github.com/user-attachments/assets/8bf08f00-3f13-4fd7-b09e-6aa0038e362e" />

6. Настройки Grafana:
   
- Вошла в Grafana: Добавила источник данных Prometheus, Выбрала Prometheus, нажала Save & Test
 <img width="1194" height="586" alt="image" src="https://github.com/user-attachments/assets/82c5be50-df1e-4393-bb26-8f6dcf2a400a" />

- Создала дашборд: Выбрала источник данных Prometheus, Добавила отслеживаемую метрику, сохранила его
  <img width="1227" height="609" alt="image" src="https://github.com/user-attachments/assets/ce8dd7d9-f3c5-4efa-ba2c-dd04283aa39c" />

7. Протестировала систему:

- Проверила контейнеры
<img width="1280" height="164" alt="image" src="https://github.com/user-attachments/assets/356cfbd9-3fe9-4c11-97b7-0f949ac534c7" />

- Проверила работу Grafana и Prometheus
  
- Добавила новые дашборды в графану
  <img width="940" height="633" alt="image" src="https://github.com/user-attachments/assets/b35b2eaf-6fd5-401e-84a7-506d31aa2302" />




