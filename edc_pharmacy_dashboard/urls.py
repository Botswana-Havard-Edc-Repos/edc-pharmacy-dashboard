# coding=utf-8

from edc_constants.constants import UUID_PATTERN
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from edc_pharmacy_dashboard.views import HomeView, DispensingView
# from edc_pharmacy_dashboard.views.action_views import (
#     ApprovePrescriptionView, DispensePrintLabelActionView, DispensingActionView)
# from edc_pharmacy_dashboard.views.listboard_views import (
# AppointmentListboardView, PrescriptionListboardView,
# WorklistListboardView)
# from edc_pharmacy_dashboard.views.action_views import(
#    DispensePrintLabelActionView, DispensingActionView)
from edc_pharmacy_dashboard.views.listboard_views import PrescribeListboardView
# from edc_pharmacy_dashboard.views.listboard_views import AppointmentListboardView

from .patterns import subject_identifier


app_name = 'edc_pharmacy_dashboard'

urlpatterns = [
    path(r'prescribe/', PrescribeListboardView.as_view(),
         name='prescribe_listboard_url'),
    path(r'dispense/', PrescribeListboardView.as_view(),
         name='dispense_listboard_url'),
    #     #     url(r'^listboard/worklist/$', WorklistListboardView.as_view(),
    #     #         name='worklist_listboard_url'),
    #     url(r'^listboard/dispensing/$', AppointmentListboardView.as_view(),
    #         name='appointment_listboard_url'),
    #     #     url(r'^prescription/approve/$', ApprovePrescriptionView.as_view(),
    #     #         name='approve_prescription_url'),
    #     url(r'^listboard/dispensing/$', DispensingActionView.as_view(),
    #         name='dispensing_action_url'),
    #     url(r'^listboard/dispensing/'
    #         '(?P<subject_identifier>' + subject_identifier + ')/'
    #         '(?P<appointment>' + UUID_PATTERN.pattern + ')/',
    #         DispensePrintLabelActionView.as_view(),
    #         name='dispense_print_label_action_url'),
    #     url(r'^listboard/dispensing/'
    #         '(?P<subject_identifier>' + subject_identifier + ')/',
    #         AppointmentListboardView.as_view(),
    #         name='appointment_listboard_url'),
    #     url(r'^dashboard/dispensing/'
    #         '(?P<subject_identifier>' + subject_identifier + ')/'
    #         '(?P<appointment>' + UUID_PATTERN.pattern + ')/',
    #         DispensingView.as_view(), name='dispensing_form_url'),
    #     url(r'^listboard/prescription/'
    #         '(?P<subject_identifier>' + subject_identifier + ')/',
    #         PrescriptionListboardView.as_view(),
    #         name='prescription_listboard_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]
