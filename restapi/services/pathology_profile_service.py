from restapi.models.pathology_profile import Pathology_profile


class PathologyProfileService:

    @staticmethod
    def get_all_profiles():

        return Pathology_profile.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_profile_by_id(profile_id):

        return Pathology_profile.objects.filter(
            id=profile_id,
            is_deleted=False
        ).first()

    @staticmethod
    def create_profile(validated_data):

        tests = validated_data.pop('tests', [])

        profile = Pathology_profile.objects.create(
            **validated_data
        )

        profile.tests.set(tests)

        return profile

    @staticmethod
    def update_profile(instance, validated_data):

        tests = validated_data.pop('tests', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tests is not None:
            instance.tests.set(tests)

        return instance

    @staticmethod
    def delete_profile(instance):

        instance.is_deleted = True
        instance.save()

        return True