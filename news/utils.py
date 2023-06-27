import openpyxl
import xlsxwriter

from news.models import Place, WeatherSummary


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


def export_weather_summary_to_xlsx(file_path, place_id, start_date, end_date):
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    # Здесь вы можете настроить форматирование и структуру таблицы

    # Получите сводку погоды согласно фильтру
    weather_summaries = WeatherSummary.objects.filter(place_id=place_id, date__range=(start_date, end_date))

    row = 0
    for weather_summary in weather_summaries:
        # Здесь вы можете заполнить таблицу данными из сводки погоды
        worksheet.write(row, 0, weather_summary.date)
        worksheet.write(row, 1, weather_summary.temperature)
        worksheet.write(row, 2, weather_summary.humidity)
        worksheet.write(row, 3, weather_summary.pressure)
        worksheet.write(row, 4, weather_summary.wind_direction)
        worksheet.write(row, 5, weather_summary.wind_speed)
        row += 1

    workbook.close()
