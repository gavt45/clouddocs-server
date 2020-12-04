# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.views import View
from json import loads
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import clouddocs_app.models as models
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def _model_to_dict(model):
    mod = model_to_dict(model)
    if 'del_dt' in mod.keys():
        mod.pop('del_dt')
    return mod


def handle404(request, exception):
    logger.warn("404 error: {}".format(exception))
    return JsonResponse({"code": 1, "msg": "Destination {} not found".format(request.path)}, status=404)


def handle500(request):
    logger.warn("Internal error")
    return JsonResponse({"code": 1, "msg": "Internal server error"}, status=500)


# Create your views here.
def base(request):
    return JsonResponse({"code": 0, "msg": "Working!"})


def get_event_types(request):
    # return JsonResponse({"code": 1, "msg": "Unimplemented"}, status=500)
    types = []
    for event_type in models.EventType.objects.all():
        if not event_type.del_dt:
            event_type_serialized = _model_to_dict(event_type)
            types.append(event_type_serialized)
    return JsonResponse(types, safe=False)


def get_directions(request):
    # return JsonResponse({"code": 1, "msg": "Unimplemented"}, status=500)
    types = []
    for event_type in models.Direction.objects.all():
        if not event_type.del_dt:
            event_type_serialized = _model_to_dict(event_type)
            types.append(event_type_serialized)
    return JsonResponse(types, safe=False)


def get_last_event(request):
    event = models.Event.objects.last()
    if not event:
        return JsonResponse({"code": 1, "msg": "Database is empty!"}, safe=False, status=400)
    
    event_serialized = _model_to_dict(event)
    # logger.warn("Serialized event before ops: {}".format(event_serialized))

    event_serialized['date'] = event_serialized['date'].strftime("%d-%m-%Y")

    # logger.warn("id type: {}".format(type(event_serialized['id_type'])))

    if event_serialized['id_type'] != None:
        event_serialized['type'] = _model_to_dict(
            models.EventType.objects.get(id=event_serialized['id_type']))
        del event_serialized['id_type']
    else:
        event_serialized['type'] = None

    # if event_serialized['id_protocol'] != None:
    #     event_serialized['protocol'] = _model_to_dict(
    #         models.Protocol.objects.get(id=event_serialized['id_protocol']))
    #     del event_serialized['id_protocol']
    # else:
    #     event_serialized['protocol'] = None

    if event_serialized['id_direction'] != None:
        event_serialized['direction'] = _model_to_dict(
            models.Direction.objects.get(id=event_serialized['id_direction']))
        del event_serialized['id_direction']
    else:
        event_serialized['direction'] = None

    for i in range(len(event_serialized["tags"])):
        event_serialized["tags"][i] = _model_to_dict(event_serialized["tags"][i])
    # for i in range(len(event_serialized["biomaterials"])):
    #     event_serialized["biomaterials"][i] = _model_to_dict(event_serialized["biomaterials"][i])
    # if len(event_serialized["biomaterials"]) == 0:
    #     event_serialized["biomaterials"] = None
    for i in range(len(event_serialized["files"])):
        event_serialized["files"][i] = _model_to_dict(event_serialized["files"][i])
    # for i in range(len(event_serialized["directions"])):
    #     event_serialized["directions"][i] = _model_to_dict(event_serialized["directions"][i])

    # logger.warn("Serialized event: {}".format(event_serialized))
    return JsonResponse(event_serialized, safe=False)

def get_events(request):
    events = []
    for event in models.Event.objects.all():
        # logger.warn("del dt: {}".format(event.del_dt))
        if not event.del_dt:
            event_serialized = _model_to_dict(event)
            # logger.warn("Serialized event before ops: {}".format(event_serialized))

            event_serialized['date'] = event_serialized['date'].strftime("%d-%m-%Y")

            # logger.warn("id type: {}".format(type(event_serialized['id_type'])))

            if event_serialized['id_type'] != None:
                event_serialized['type'] = _model_to_dict(
                    models.EventType.objects.get(id=event_serialized['id_type']))
                del event_serialized['id_type']
            else:
                event_serialized['type'] = None

            # if event_serialized['id_protocol'] != None:
            #     event_serialized['protocol'] = _model_to_dict(
            #         models.Protocol.objects.get(id=event_serialized['id_protocol']))
            #     del event_serialized['id_protocol']
            # else:
            #     event_serialized['protocol'] = None

            if event_serialized['id_direction'] != None:
                event_serialized['direction'] = _model_to_dict(
                    models.Direction.objects.get(id=event_serialized['id_direction']))
                del event_serialized['id_direction']
            else:
                event_serialized['direction'] = None

            for i in range(len(event_serialized["tags"])):
                event_serialized["tags"][i] = _model_to_dict(event_serialized["tags"][i])
            # for i in range(len(event_serialized["biomaterials"])):
            #     event_serialized["biomaterials"][i] = _model_to_dict(event_serialized["biomaterials"][i])
            # if len(event_serialized["biomaterials"]) == 0:
            #     event_serialized["biomaterials"] = None
            for i in range(len(event_serialized["files"])):
                event_serialized["files"][i] = _model_to_dict(event_serialized["files"][i])
            # for i in range(len(event_serialized["directions"])):
            #     event_serialized["directions"][i] = _model_to_dict(event_serialized["directions"][i])

            # logger.warn("Serialized event: {}".format(event_serialized))

            events.append(event_serialized)
    return JsonResponse(events, safe=False)


def remove_event(request):
    ass = {"code": 0, "msg": "DELETE is unimplemented"}
    req_json = loads(request.body)
    logger.warn("JSON: {}".format(req_json))
    if not "id" in req_json.keys():
        ass["code"] = 1
        ass["msg"] = "id is required"
        return JsonResponse(ass)
    id = req_json["id"]
    try:
        models.Event.objects.get(id=id).delete()
    except:
        ass["code"] = 1
        ass["msg"] = "no Event object with this id found!"
        return JsonResponse(ass)
    ass["msg"] = "OK"
    return JsonResponse(ass)


@csrf_exempt
def add_event(request):
    if request.method != "POST" and request.method != "DELETE":
        return JsonResponse({"code": 1, "msg": "Method is not allowed!"}, status=405)
    elif request.method == "DELETE":
        return remove_event(request)
    elif request.method == "POST":
        req_json = loads(request.body)
        logger.warn("JSON: {}".format(req_json))
        new_event = models.Event()
        new_event.name = req_json["name"]
        if not new_event.name:
            handle500(request)
        new_event.date = datetime.strptime(req_json["date"], "%d-%m-%Y")
        logger.warn("Date: {}".format(new_event.date))
        if not new_event.date:
            handle500(request)
        new_event.id_type = models.EventType.objects.get(id=req_json["type"])
        if not new_event.id_type:
            handle500(request)
        new_event.id_direction = models.Direction.objects.get(id=req_json["direction"])
        if not new_event.id_direction:
            handle500(request)
        new_event.save()
        for file_id in req_json["files"]:
            try: # todo remove in non MVP!!
                new_event.files.add(models.File.objects.get(id=file_id))
            except models.File.DoesNotExist:
                new_event.files.add(models.File.objects.get(name__icontains="кала")) # Берем анализ кала by default
                break
        for tag_id in req_json["tags"]:
            try: # todo remove in non MVP!!
                new_event.tags.add(models.Tag.objects.get(id=tag_id))
            except models.File.DoesNotExist:
                new_event.tags.add(models.Tag.objects.get(name__icontains="анализы"))  # Берем анализы by default
                break
        # for dir_id in req_json["directions"]:
        #     new_event.directions.add(models.Direction.objects.get(id=dir_id))
        new_event.description = req_json["description"]
        if not new_event.description:
            handle500(request)
        new_event.place = req_json["place"]
        if not new_event.place:
            handle500(request)
        # for biomaterial_json in req_json["biomaterials"]:
        #     biomaterial = models.Biomaterial()
        #     biomaterial.name = biomaterial_json["name"]
        #     biomaterial.normal_value = biomaterial_json["value"]
        #     biomaterial.units = biomaterial_json["units"]
        #     biomaterial.save()
        #     new_event.biomaterials.add(biomaterial)

        # protocol = models.Protocol()
        # protocol.description = req_json["protocol"]["description"]
        # if not protocol.description:
        #     handle500(request)
        # protocol.complains = req_json["protocol"]["complains"]
        # if not protocol.complains:
        #     handle500(request)
        # protocol.diagnose = req_json["protocol"]["diagnose"]
        # if not protocol.diagnose:
        #     handle500(request)
        # protocol.comorbidities = req_json["protocol"]["comorbidities"]
        # if not protocol.comorbidities:
        #     handle500(request)
        # protocol.therapy_plan = req_json["protocol"]["therapy_plan"]
        # if not protocol.therapy_plan:
        #     handle500(request)
        # protocol.doctor_report = req_json["protocol"]["doctor_report"]
        # if not protocol.doctor_report:
        #     handle500(request)
        # protocol.doctor = req_json["protocol"]["doctor"]
        # if not protocol.doctor:
        #     handle500(request)
        # protocol.drug_prescription = str(req_json["protocol"]["drug_prescription"])
        # if not protocol.drug_prescription:
        #     handle500(request)
        # protocol.save()
        # logger.warn("New protocol: {}".format(protocol.id))
        # new_event.id_protocol = protocol
        new_event.save()
        return JsonResponse({"code": 0, "msg": "OK"}, status=200)
