import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Maintenance, Dictionary, Machine
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Import maintenances from Excel file'

    def handle(self, *args, **kwargs):
        file_path = '/Users/georgijsergeev/Desktop/GODBLESSME/silant_service/data/МЃ© С®Ђ†≠в §†≠≠л• §Ђп нЂ•™ваЃ≠≠Ѓ£Ѓ ѓ†бѓЃав† output.xlsx'
        sheet_name = 'ТО output'  # Замените на правильное имя листа
        data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
 
 # Вывод всех серийных номеров из базы данных для проверки
        db_serial_numbers = [machine.serial_number for machine in Machine.objects.all()]
        print(f"Serial numbers in the database: {db_serial_numbers}")

        # Проверка на наличие пользователей
        if not User.objects.exists():
            User.objects.create_user(username='default_user', password='password123')
            print("No users found. Created a default user with username 'default_user' and password 'password123'.")

        for _, row in data.iterrows():
            try:
                serial_number = str(row['Зав. № машины']).strip().zfill(4)  # Нормализация серийного номера
                print(f"Trying to find machine with serial number: {serial_number}")
                machine = Machine.objects.get(serial_number=serial_number)
                
                maintenance_type, _ = Dictionary.objects.get_or_create(name=row['Вид ТО'].strip())
                organization, _ = Dictionary.objects.get_or_create(name=row['Организация, проводившая ТО'].strip())
                
                # Используем первого пользователя
                service_company = User.objects.first()
                
                Maintenance.objects.create(
                    maintenance_type=maintenance_type,
                    maintenance_date=row['Дата проведения ТО'],
                    runtime_hours=row['Наработка, м/час'],
                    order_number=row['№ заказ-наряда'].strip(),
                    order_date=row['дата заказ-наряда'],
                    organization=organization,
                    machine=machine,
                    service_company=service_company,
                    maintenance_organization=row['Организация, проводившая ТО'].strip(),
                    operating_hours=row['Наработка, м/час'],
                    downtime=0,  # или используйте соответствующее поле из файла
                    recovery_method=''  # или используйте соответствующее поле из файла
                )
            except Machine.DoesNotExist:
                print(f"Machine with serial number {serial_number} does not exist.")
            except Exception as e:
                print(f"Error importing row: {row} - {e}")

        print("Import completed.")