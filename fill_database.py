# -*- coding: UTF-8 -*-

from clouddocs_app.models import *
from datetime import datetime


def fill():
    Direction.objects.all().delete()
    directions = []
    dir_names = [
        'Аллергология',
        'Беременность',
        'Другое',
        'Педиатрия',
        'Гастроэнтерология'
    ]
    for dir_name in dir_names:
        direction1 = Direction()
        direction1.name = dir_name
        direction1.save()
        directions.append(direction1)

    Tag.objects.all().delete()
    tags = []
    tag_names = [
        'анализы',
        'гастроэнтерология',
        'другое',
        'матлогика'
    ]
    for tag_name in tag_names:
        direction1 = Tag()
        direction1.name = tag_name
        direction1.save()
        tags.append(direction1)

    EventType.objects.all().delete()
    event_types = []
    event_type_names = [
        'Анализы',
        'Прием специалиста',
        'Обследование',
        'Прививка',
        'какая-то фигня'
    ]
    for event_name in event_type_names:
        direction1 = EventType()
        direction1.name = event_name
        direction1.save()
        event_types.append(direction1)

    File.objects.all().delete()
    file1 = File()
    file1.name = "Анализ кала"
    file1.file_type = "image/jpg"
    file1.url = "https://sosud-ok.ru/wp-content/uploads/2019/01/analizy-pochvy-vody-urozhaya-udobreniy-1044314.jpg"
    file1.save()

    # File.objects.all().delete()
    file2 = File()
    file2.name = "Анализ твоего зрения"
    file2.file_type = "image/jpg"
    file2.url = "https://pasteboard.co/JC1sUL1.jpg"
    file2.save()

    # File.objects.all().delete()
    file3 = File()
    file3.name = "Анализ неба"
    file3.file_type = "image/jpg"
    file3.url = "https://pasteboard.co/JC1tr54.jpg"
    file3.save()

    file4 = File()
    file4.name = "Анализ твоего е***** ой лица всмысле"
    file4.file_type = "image/jpg"
    file4.url = "https://pasteboard.co/JC1vyX2.jpg"
    file4.save()

    file5 = File()
    file5.name = "Анализ твоего code"
    file5.file_type = "image/jpg"
    file5.url = "https://pasteboard.co/JC1vZqN.jpg"
    file5.save()

    file6 = File()
    file6.name = "Анализ твоего Андрея"
    file6.file_type = "image/jpg"
    file6.url = "https://pasteboard.co/JC1w9fvb.jpg"
    file6.save()

    file7 = File()
    file7.name = "Анализ твоего еще чего-та"
    file7.file_type = "image/jpg"
    file7.url = "https://pasteboard.co/JC1w9fvb.jpg"
    file7.save()

    # Protocol.objects.all().delete()
    Event.objects.all().delete()
    # Biomaterial.objects.all().delete()
    for i in range(8):
        # protocol_as_picture = Protocol()
        # protocol_as_picture.description = "Плановый визит к гастрику {}".format(i)
        # protocol_as_picture.complains = "Изжога по ночам"
        # protocol_as_picture.diagnose = "ГЭРБ"
        # protocol_as_picture.comorbidities = "Нет"
        # protocol_as_picture.therapy_plan = "УЗИ желудка, ФГДС"
        # protocol_as_picture.drug_prescription = "[{\"name\": \"Нексиум\", " \
        #                                         "\"dosage\": \"40мг 2р\\д\", \"period\": \"4 недели\"}]"#"Нексиум 40мг 2р\\д 4 недели"
        # protocol_as_picture.doctor_report = "Диета, дробное питание"
        # protocol_as_picture.doctor = "Кириллова Анна Леонидовна"
        # protocol_as_picture.save()

        # print("Directions: {}".format(directions))

        gastrik = Event()
        gastrik.save()
        gastrik.name = "Прием гастроэнтеролога {}".format(i)
        gastrik.place = "Джиклиник, Ульянова-Ленина 13"
        gastrik.date = datetime(2020, 10, i+1)
        gastrik.id_type = event_types[1]
        # gastrik.id_protocol = protocol_as_picture
        gastrik.id_direction = directions[4]
        gastrik.description = "По сути Swagger – это фреймворк для спецификации RESTful API. Его прелесть заключается в том, что он дает возможность не только интерактивно просматривать спецификацию, но и отправлять запросы – так называемый Swagger UI, вот так это выглядит:"
        gastrik.tags.add(tags[0])
        gastrik.tags.add(tags[1])
        gastrik.files.add(file1)
        gastrik.files.add(file2)
        gastrik.save()

        # helico_biomaterial = Biomaterial()
        # helico_biomaterial.name = "Хеликобактер тест {}".format(i)
        # helico_biomaterial.units = "ммоль"
        # helico_biomaterial.normal_value = "7.13"
        # helico_biomaterial.save()

        anal_izy = Event()
        anal_izy.save()
        anal_izy.name = "Анализы для гастрика {}".format(i)
        anal_izy.place = "Инвитро"
        anal_izy.date = datetime(2020, 10, i+1)
        anal_izy.id_type = event_types[0]
        anal_izy.description = "Ана́лиз — метод исследования, характеризующийся выделением и изучением отдельных частей объектов исследования. Анализ — совокупность разделов математики, выросших из классического математического анализа..."
        anal_izy.id_direction = directions[4]
        # anal_izy.biomaterials.add(helico_biomaterial)
        anal_izy.tags.add(tags[0])
        anal_izy.tags.add(tags[1])
        anal_izy.tags.add(tags[2])
        anal_izy.files.add(file1)
        anal_izy.files.add(file2)
        anal_izy.files.add(file3)
        anal_izy.files.add(file4)
        # anal_izy.files.add(file5)
        # anal_izy.files.add(file6)
        # anal_izy.files.add(file7)
        anal_izy.save()
