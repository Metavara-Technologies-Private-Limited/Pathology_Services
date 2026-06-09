from restapi.models import Tube

def get_all_tubes():
    return Tube.objects.all()

def get_tube(pk):
    return Tube.objects.get(pk=pk)

def create_tube(data):
    return Tube.objects.create(**data)

def update_tube(instance, data):
    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance

def delete_tube(instance):
    instance.delete()