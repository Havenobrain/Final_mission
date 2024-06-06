import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Machine, Complaint, Dictionary
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Import complaints data from an Excel file'

    def handle(self, *args, **options):
        file_path = '/Users/georgijsergeev/Desktop/GODBLESSME/silant_service/data/МЃ© С®Ђ†≠в §†≠≠л• §Ђп нЂ•™ваЃ≠≠Ѓ£Ѓ ѓ†бѓЃав† output.xlsx'
        sheet_name = 'рекламация output'

        # Чтение данных из Excel с пропуском первой строки и использованием второй строки в качестве заголовков
        data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', header=1)

        # Получение серийных номеров машин из базы данных
        serial_numbers_in_db = Machine.objects.values_list('serial_number', flat=True)
        print(f"Serial numbers in the database: {list(serial_numbers_in_db)}")

        for index, row in data.iterrows():
            try:
                serial_number = str(row['Зав. № машины']).strip().zfill(4)  # Нормализация серийного номера
                if serial_number not in serial_numbers_in_db:
                    print(f"Machine with serial number {serial_number} does not exist.")
                    continue

                machine = Machine.objects.get(serial_number=serial_number)
                failure_node = Dictionary.objects.get_or_create(name=row['Узел отказа'])[0]
                recovery_method = Dictionary.objects.get_or_create(name=row['Способ восстановления'])[0]
                service_company = User.objects.get(username='default_user')  # Замените на актуального пользователя

                complaint = Complaint(
                    machine=machine,
                    complaint_date=row['Дата отказа'],
                    operating_hours=row['Наработка, м/час'],
                    failure_node=failure_node,
                    failure_description=row['Описание отказа'],
                    recovery_method=recovery_method,
                    parts_used=row['Используемые запасные части'],
                    recovery_date=row['Дата восстановления'],
                    downtime=row['Время простоя техники'],
                    service_company=service_company
                )
                complaint.save()
            except Exception as e:
                print(f"Error importing row: {row} - {str(e)}")

        print("Import completed.")