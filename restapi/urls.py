from rest_framework.routers import DefaultRouter

from restapi.views import (
    SampleViewSet,
    TubeViewSet,
    ParameterViewSet,
    ParameterReferenceRangeViewSet,
    TemplateViewSet,
    TemplateParameterViewSet,
    TestViewSet,
    CategoryViewSet,
    PathologyProfileViewSet,
    AgencyViewSet,
    MachineViewSet,
    MachineParameterViewSet,
    AgencyServiceViewSet,
    ClinicViewSet,
    AgencyClinicViewSet,
    TestParameterLinkViewSet,
    TestSampleLinkViewSet,
    TestTemplateLinkViewSet
)


router = DefaultRouter()

router.register(r'samples', SampleViewSet, basename='samples')
router.register(r'tubes', TubeViewSet, basename='tubes')

router.register(r'parameters', ParameterViewSet, basename='parameters')

router.register(
    r'parameter-reference-ranges',
    ParameterReferenceRangeViewSet,
    basename='parameter-reference-ranges'
)

router.register(
    r'templates',
    TemplateViewSet,
    basename='templates'
)

router.register(
    r'template-parameters',
    TemplateParameterViewSet,
    basename='template-parameters'
)
router.register(
    r'tests',
    TestViewSet,
    basename='tests'
)
router.register(
    r'categories',
    CategoryViewSet,
    basename='categories'
)

router.register(
    r'profiles',
    PathologyProfileViewSet,
    basename='profiles'
)

router.register(
    r'agencies',
    AgencyViewSet,
    basename='agencies'
)

router.register(
    r'machines',
    MachineViewSet,
    basename='machines'
)

router.register(
    r'machine-parameters',
    MachineParameterViewSet,
    basename='machine-parameters'
)

router.register(
    r'agency-services',
    AgencyServiceViewSet,
    basename='agency-services'
)

router.register(
    r'clinics',
    ClinicViewSet,
    basename='clinics'
)
router.register(
    r'agency-clinics',
    AgencyClinicViewSet,
    basename='agency-clinics'
)

router.register(
    r'test-parameter-links',
    TestParameterLinkViewSet,
    basename='test-parameter-links'
)

router.register(
    r'test-sample-links',
    TestSampleLinkViewSet,
    basename='test-sample-links'
)

router.register(
    r'test-template-links',
    TestTemplateLinkViewSet,
    basename='test-template-links'
)

urlpatterns = router.urls