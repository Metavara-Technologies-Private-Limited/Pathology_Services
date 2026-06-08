from rest_framework.routers import DefaultRouter
from restapi.views import *
from django.urls import path

from restapi.views import (
    SampleViewSet,
    TubeViewSet,
    ParameterViewSet,
    TemplateViewSet,
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
    TestTemplateLinkViewSet,
)

router = DefaultRouter()

router.register(r'samples', SampleViewSet, basename='samples')
router.register(r'tubes', TubeViewSet, basename='tubes')

router.register(r'parameters', ParameterViewSet, basename='parameters')

router.register(
    r'templates',
    TemplateViewSet,
    basename='templates'
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


from django.urls import path

from .views import (
    PatientView,
    PendingShipmentView,
    ScheduleShippingView,
    MoveToShippedView,
    ShipmentShippedView,
    MoveToReceivedView,
    ShipmentReceivedView,
    ActivityLogsView,

    # RECEIVE MODULE IMPORTS
    ReceiveSampleCreateAPIView,
    ReceiveSampleListAPIView,
    ReceiveSampleAPIView,
    RejectSampleAPIView,
    ReceiveActivityLogsAPIView,
    DeleteSampleAPIView,
    ActiveSamplesAPIView,
    DeletedSamplesAPIView,
    ShipmentReceivedCreateAPIView,
    PathologyOrdersAPIView,
    #RESULT ENTRY LINKS

    ResultEntryPendingSamplesAPIView,
    ResultEntryCreateAPIView,
    ResultEntryListAPIView,
    ResultEntryCompleteAPIView,

    # ORDERS MODULE IMPORTS
    VidaiOrdersView,
    VidaiOrderDetailView,
    CollectionListCreateView,
    GenerateCollectionBarcodeView,
    CollectionDetailView,
    UpdateCollectionStatusView,
    ChangeCollectionAgencyView,
)

urlpatterns = router.urls + [

    # Patient APIs
    path(
        'patients/',
        PatientView.as_view(),
        name='patients'
    ),

    # Pending Shipment APIs
    path('pending-shipment/', PendingShipmentView.as_view(), name='pending-shipment'),
   
    # ScheduleShipping
    path('schedule-shipping/',ScheduleShippingView.as_view(),name='schedule-shipping'),
    
    path(
        'pending-shipment/',
        PendingShipmentView.as_view(),
        name='pending-shipment'
    ),

    # Move Pending → Shipped
    path(
        'move-to-shipped/',
        MoveToShippedView.as_view(),
        name='move-to-shipped'
    ),

    # Shipped Shipment APIs
    path(
        'shipped-shipment/',
        ShipmentShippedView.as_view(),
        name='shipped-shipment'
    ),

    # Move Shipped → Received
    path(
        'move-to-received/',
        MoveToReceivedView.as_view(),
        name='move-to-received'
    ),

    # Received Shipment APIs
    path(
        'received-shipment/',
        ShipmentReceivedView.as_view(),
        name='received-shipment'
    ),

    # Activity Logs APIs
    path(
        'activity-logs/',
        ActivityLogsView.as_view(),
        name='activity-logs'
    ),

    # ScheduleShipping
    path(
        'schedule-shipping/',
        ScheduleShippingView.as_view(),
        name='schedule-shipping'
    ),

    # =====================================================
    # RECEIVE MODULE APIS
    # =====================================================

    path(
        "create-sample/",
        ReceiveSampleCreateAPIView.as_view(),
        name="create-sample"
    ),

    path(
        "samples/",
        ReceiveSampleListAPIView.as_view(),
        name="sample-list"
    ),

    path(
        "receive-sample/<int:sample_id>/",
        ReceiveSampleAPIView.as_view(),
        name="receive-sample"
    ),

    path(
        "reject-sample/<int:sample_id>/",
        RejectSampleAPIView.as_view(),
        name="reject-sample"
    ),

    path(
        "receive-activity-logs/",
        ReceiveActivityLogsAPIView.as_view(),
        name="receive-activity-logs"
    ),

    path(
        "delete-sample/<int:sample_id>/",
        DeleteSampleAPIView.as_view(),
        name="delete-sample"
    ),

    path(
        "active-samples/",
        ActiveSamplesAPIView.as_view(),
        name="active-samples"
    ),

    path(
        "deleted-samples/",
        DeletedSamplesAPIView.as_view(),
        name="deleted-samples"
    ),

    path(
        "create-shipment-received/",
        ShipmentReceivedCreateAPIView.as_view(),
        name="create-shipment-received"
    ),

    path(
        "pathology-orders/",
        PathologyOrdersAPIView.as_view(),
        name="pathology-orders"
    ),
#Added Receive section APIs

path("result-entry/pending-samples/", ResultEntryPendingSamplesAPIView.as_view()),
path("result-entry/create/", ResultEntryCreateAPIView.as_view()),
path("result-entry/list/", ResultEntryListAPIView.as_view()),
path("result-entry/<int:result_id>/complete/", ResultEntryCompleteAPIView.as_view()),
]
#Added Receive section APIs

# =====================================================
# ORDERS MODULE APIS
# =====================================================

urlpatterns += [

    # Orders list + detail — proxied from Vidai EMR
    path(
        "orders/",
        VidaiOrdersView.as_view(),
        name="vidai-orders-list",
    ),
    path(
        "orders/<int:order_id>/",
        VidaiOrderDetailView.as_view(),
        name="vidai-order-detail",
    ),

    # Collections
    path(
        "collections/",
        CollectionListCreateView.as_view(),
        name="collection-list-create",
    ),
    path(
        "collections/generate-barcode/",
        GenerateCollectionBarcodeView.as_view(),
        name="collection-generate-barcode",
    ),
    path(
        "collections/<uuid:collection_id>/",
        CollectionDetailView.as_view(),
        name="collection-detail",
    ),
    path(
        "collections/<uuid:collection_id>/status/",
        UpdateCollectionStatusView.as_view(),
        name="collection-status-update",
    ),
    path(
        "collections/<uuid:collection_id>/change-agency/",
        ChangeCollectionAgencyView.as_view(),
        name="collection-change-agency",
    ),
]