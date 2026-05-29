from restapi.models.test_template import (
    Template,
    TemplateParameter
)

class TemplateService:

    @staticmethod
    def get_all():
        return Template.objects.filter(
            is_deleted=False
        )

    @staticmethod
    def get_by_id(pk):
        return Template.objects.filter(
            pk=pk,
            is_deleted=False
        ).first()

    @staticmethod
    def create(data):
        return Template.objects.create(**data)

    @staticmethod
    def update(instance, data):

        for key, value in data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    @staticmethod
    def soft_delete(instance):
        instance.is_deleted = True
        instance.save()
        return instance


class TemplateParameterService:

    @staticmethod
    def get_all():
        return TemplateParameter.objects.filter(
            is_deleted=False
        )

    @staticmethod
    def get_by_id(pk):
        return TemplateParameter.objects.filter(
            pk=pk,
            is_deleted=False
        ).first()

    @staticmethod
    def create(data):
        return TemplateParameter.objects.create(**data)

    @staticmethod
    def update(instance, data):

        for key, value in data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    @staticmethod
    def soft_delete(instance):
        instance.is_deleted = True
        instance.save()
        return instance