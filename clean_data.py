import pandas as pd

# Загрузка Excel-файла
file_path = '/mnt/data/МЃ© С®Ђ†≠в §†≠≠л• §Ђп нЂ•™ваЃ≠≠Ѓ£Ѓ ѓ†бѓЃав† output.xlsx'
data = pd.read_excel(file_path, skiprows=2)  # Пропускаем первые две строки

# Переименование столбцов
data.columns = [
    'serial_number',
    'model',
    'machine_serial_number',
    'engine_model',
    'engine_serial_number',
    'transmission_model',
    'transmission_serial_number',
    'drive_axle_model',
    'drive_axle_serial_number',
    'steer_axle_model',
    'steer_axle_serial_number',
    'shipment_date',
    'buyer',
    'end_user',
    'delivery_address',
    'equipment',
    'service_company'
]

# Сохранение очищенных данных в новый Excel-файл
cleaned_file_path = 'data/cleaned_output.xlsx'
data.to_excel(cleaned_file_path, index=False)

# Отображение очищенных данных
print(data.head())