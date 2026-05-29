from restapi.models.sample import Sample


def get_all_samples():
    return Sample.objects.all()


def create_sample(data):
    return Sample.objects.create(**data)


def get_sample(pk):
    return Sample.objects.get(id=pk)


def update_sample(instance, data):
    for key, value in data.items():
        setattr(instance, key, value)
    instance.save()
    return instance


def delete_sample(instance):
    instance.delete()