from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
import clouddocs_app.models as models
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

SYSTEM_FIELDS = ['sh_dt', 'del_dt']


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
    types = []
    for event_type in models.EventType.objects.all():
        if not event_type.del_dt:
            event_type_serialized = model_to_dict(event_type)
            for sys_field in SYSTEM_FIELDS:
                if sys_field in event_type_serialized.keys():
                    event_type_serialized.pop(sys_field)
            types.append(event_type_serialized)
    return JsonResponse(types, safe=False)


def get_events(request):
    events = []
    for event in models.Event.objects.all():
        logger.warn("del dt: {}".format(event.del_dt))
        if not event.del_dt:
            event_type_serialized = model_to_dict(event)
            logger.warn("Serialized event: {}".format(event_type_serialized))

            # remove system fields
            for sys_field in SYSTEM_FIELDS:
                if sys_field in event_type_serialized.keys():
                    event_type_serialized.pop(sys_field)

    return JsonResponse(events, safe=False)
