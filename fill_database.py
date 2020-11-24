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
        'МАТЛог',
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
        'Анализов',
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

    Protocol.objects.all().delete()
    protocol_as_picture = Protocol()
    protocol_as_picture.description = "Плановый визит к гастрику"
    protocol_as_picture.complains = "Изжога по ночам"
    protocol_as_picture.diagnose = "ГЭРБ"
    protocol_as_picture.comorbidities = "Нет"
    protocol_as_picture.therapy_plan = "УЗИ желудка, ФГДС"
    protocol_as_picture.drug_prescription = "Нексиум 40мг 2р\\д 4 недели"
    protocol_as_picture.doctor_report = "Диета, дробное питание"
    protocol_as_picture.doctor = "Кириллова Анна Леонидовна"
    protocol_as_picture.save()

    print("Directions: {}".format(directions))
    Event.objects.all().delete()
    gastrik = Event()
    gastrik.save()
    gastrik.name = "Прием гастроэнтеролога"
    gastrik.place = "Джиклиник, Ульянова-Ленина 1337"
    gastrik.date = datetime(2020, 10, 13)
    gastrik.id_type = event_types[1]
    gastrik.id_protocol = protocol_as_picture
    gastrik.id_direction = directions[5]
    gastrik.tags.add(tags[0])
    gastrik.tags.add(tags[1])
    gastrik.files.add(file1)
    gastrik.save()

    Biomaterial.objects.all().delete()
    helico_biomaterial = Biomaterial()
    helico_biomaterial.name = "Хеликобактер тест"
    helico_biomaterial.units = "ммоль"
    helico_biomaterial.normal_value = "7.13"
    helico_biomaterial.save()

    anal_izy = Event()
    anal_izy.save()
    anal_izy.name = "Анализы для гастрика"
    anal_izy.place = "Инвитро"
    anal_izy.date = datetime(2020, 10, 12)
    anal_izy.id_type = event_types[0]
    anal_izy.id_direction = directions[5]
    anal_izy.biomaterials.add(helico_biomaterial)
    anal_izy.tags.add(tags[0])
    anal_izy.tags.add(tags[1])
    anal_izy.tags.add(tags[2])
    anal_izy.files.add(file1)
    anal_izy.save()
