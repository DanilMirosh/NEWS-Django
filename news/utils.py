import openpyxl

from news.models import Place


def import_places_from_xlsx(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    for row in sheet.iter_row(min_riw=2, values_only=True):
        name = row[0]
        coordinates = row[1]
        rating = row[2]

        # Создайте новое место и сохраните его в базе данных
        place = Place(name=name, coordinates=coordinates, rating=rating)
        place.save()
