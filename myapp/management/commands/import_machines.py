import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Machine, Dictionary, Maintenance, Complaint

class Command(BaseCommand):
    help = 'Import machines from an Excel file'

    def handle(self, *args, **kwargs):
        file_path = 'data/МЃ© С®Ђ†≠в §†≠≠л• §Ђп нЂ•™ваЃ≠≠Ѓ£Ѓ ѓ†бѓЃав† output.xlsx'
        data = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')

        # Load machines data with proper header
        machines_data = data['машины']
        machines_data.columns = machines_data.iloc[1]
        machines_data = machines_data[2:]  # Skip the first two rows

        for index, row in machines_data.iterrows():
            model, _ = Dictionary.objects.get_or_create(name=row['Модель \nтехники'])
            engine_model, _ = Dictionary.objects.get_or_create(name=row['Модель\nдвигателя'])
            transmission_model, _ = Dictionary.objects.get_or_create(name=row['Модель трансмиссии\n(производитель, артикул)'])
            drive_axle_model, _ = Dictionary.objects.get_or_create(name=row['Модель\nведущего моста'])
            steer_axle_model, _ = Dictionary.objects.get_or_create(name=row['Модель управляемого моста'])

            Machine.objects.create(
                serial_number=row['Зав. № \nмашины'],
                model=model,
                engine_model=engine_model,
                engine_number=row['Зав. № двигателя'],
                transmission_model=transmission_model,
                transmission_number=row['Зав. № трансмиссии'],
                drive_axle_model=drive_axle_model,
                drive_axle_number=row['Зав. № ведущего моста'],
                steer_axle_model=steer_axle_model,
                steer_axle_number=row['Зав. № управляемого моста'],
                supply_date=pd.to_datetime(row['Дата \nотгрузки\nс завода'], errors='coerce').date(),
                client=row['Покупатель'],
                end_user=row['Грузополучатель\n(конечный потребитель)'],
                delivery_address=row['Адрес поставки\n(эксплуатации)'],
                additional_options=row['Комплектация \n(доп. опции)'],
                service_company=row['Сервисная компания']
            )

        maintenances_data = data['ТО']
        maintenances_data.columns = maintenances_data.iloc[0]
        maintenances_data = maintenances_data[1:]

        for index, row in maintenances_data.iterrows():
            maintenance_type, _ = Dictionary.objects.get_or_create(name=row['Вид ТО'])
            maintenance_organization, _ = Dictionary.objects.get_or_create(name=row['Организация, проводившая ТО'])
            machine = Machine.objects.get(serial_number=row['Зав. № машины'])

            Maintenance.objects.create(
                machine=machine,
                maintenance_type=maintenance_type,
                maintenance_date=pd.to_datetime(row['Дата проведения ТО'], errors='coerce').date(),
                runtime_hours=row['Наработка, м/час'],
                order_number=row['№ заказ-наряда'],
                order_date=pd.to_datetime(row['дата заказ-наряда'], errors='coerce').date(),
                organization=maintenance_organization,
                service_company=None,
                maintenance_organization=row['Организация, проводившая ТО'],
                operating_hours=row['Наработка, м/час'],
                downtime=0,
                recovery_method=''
            )

        complaints_data = data['Рекламации']
        complaints_data.columns = complaints_data.iloc[0]
        complaints_data = complaints_data[1:]

        for index, row in complaints_data.iterrows():
            machine = Machine.objects.get(serial_number=row['Зав. № машины'])

            Complaint.objects.create(
                machine=machine,
                complaint_date=pd.to_datetime(row['Дата отказа'], errors='coerce').date(),
                operating_hours=row['Наработка, м/час'],
                downtime=row['Время простоя техники'],
                parts_used=row['Используемые запасные части'],
                recovery_date=pd.to_datetime(row['Дата восстановления'], errors='coerce').date(),
                recovery_method=''
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported machines, maintenances, and complaints'))
