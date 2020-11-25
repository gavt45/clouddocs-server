from django.db import models


# Create your models here.

# class Protocol(models.Model):
#     description = models.CharField(max_length=45)
#     complains = models.CharField(max_length=45)
#     diagnose = models.CharField(max_length=45)
#     comorbidities = models.CharField(max_length=45)
#     therapy_plan = models.CharField(max_length=45)
#     drug_prescription = models.CharField(max_length=45)
#     doctor_report = models.CharField(max_length=45)
#     doctor = models.CharField(max_length=45)
#     sh_dt = models.DateTimeField(auto_now=True)
#     del_dt = models.DateTimeField(null=True)
#     # def get_json(self):
#     #     return {
#     #         "id": self.id,
#     #         "description": self.description,
#     #         "complains": self.complains,
#     #         "diagnose": self.diagnose,
#     #         "comorbidities": self.comorbidities,
#     #         "therapy_plan": self.therapy_plan
#     #     }
#     class Meta:
#         db_table = "protocols"


class Tag(models.Model):
    name = models.CharField(max_length=45)
    sh_dt = models.DateTimeField(auto_now=True)
    del_dt = models.DateTimeField(null=True)
    class Meta:
        db_table = "tags"


class EventType(models.Model):
    name = models.CharField(max_length=45)
    sh_dt = models.DateTimeField(auto_now=True)
    del_dt = models.DateTimeField(null=True)
    class Meta:
        db_table = "event_types"


class File(models.Model):
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=256)
    file_type = models.CharField(max_length=45)
    sh_dt = models.DateTimeField(auto_now=True)
    del_dt = models.DateTimeField(null=True)
    class Meta:
        db_table = "files"


# class Biomaterial(models.Model):
#     name = models.CharField(max_length=45)
#     units = models.CharField(max_length=45)
#     normal_value = models.CharField(max_length=45)
#     sh_dt = models.DateTimeField(auto_now=True)
#     del_dt = models.DateTimeField(null=True)
#     class Meta:
#         db_table = "biomaterials"


class Direction(models.Model):
    name = models.CharField(max_length=45)
    sh_dt = models.DateTimeField(auto_now=True)
    del_dt = models.DateTimeField(null=True)
    class Meta:
        db_table = "directions"


# тэги
# направления 1-1
# тип
# описание
# название
# дата
# место
# файлы

class Event(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)
    sh_dt = models.DateTimeField(auto_now=True)
    del_dt = models.DateTimeField(null=True)
    id_type = models.ForeignKey(EventType, null=True, on_delete=models.CASCADE)
    id_direction = models.ForeignKey(Direction, null=True, on_delete=models.CASCADE)
    # id_protocol = models.ForeignKey(Protocol, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, null=True)
    tags = models.ManyToManyField(Tag)
    # biomaterials = models.ManyToManyField(Biomaterial)
    files = models.ManyToManyField(File)
    class Meta:
        db_table = "events"

# class EventBiomaterials(models.Model):
#     id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     id_biomaterial = models.ForeignKey(Biomaterial, primary_key=True, on_delete=models.CASCADE)
#     sh_dt = models.DateTimeField(auto_now=True)
#     del_dt = models.DateTimeField(null=True)
#     class Meta:
#         db_table = "event_biomaterials"
#
#
# class EventFiles(models.Model):
#     id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     id_file = models.ForeignKey(File, primary_key=True, on_delete=models.CASCADE)
#     sh_dt = models.DateTimeField(auto_now=True)
#     del_dt = models.DateTimeField(null=True)
#     class Meta:
#         db_table = "event_files"
#
#
# class EventTags(models.Model):
#     id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     id_tag = models.ForeignKey(Tag, primary_key=True, on_delete=models.CASCADE)
#     sh_dt = models.DateTimeField(auto_now=True)
#     del_dt = models.DateTimeField(null=True)
#     class Meta:
#         db_table = "event_tags"
