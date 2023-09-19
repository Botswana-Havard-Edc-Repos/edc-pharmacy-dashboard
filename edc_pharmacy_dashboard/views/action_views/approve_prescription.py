from django.apps import apps as django_apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from edc_pharmacy.medications import (
    PrescriptionApprovalValidator, PrescriptionApprovalValidatorError)

from .base_action_view import BaseActionView


app_config = django_apps.get_app_config('edc_pharmacy_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class ApprovePrescriptionView(BaseActionView):

    post_url_name = app_config.listboard_url_name
    listboard_url_name = app_config.prescription_listboard_url_name
    valid_form_actions = [
        'approve_selected_prescription']
    prescription_model = django_apps.get_model(
        *edc_pharma_app_config.prescription_model.split('.'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._selected_manifest = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def process_form_action(self):
        if self.action == 'approve_selected_prescription':
            self.approved_selected_prescriptions()

    def approved_selected_prescriptions(self):
        """Adds the selected items to the selected manifest.
        """
        if not self.selected_items:
            message = ('Nothing to do. No items have been selected.')
            messages.warning(self.request, message)
        else:
            approved = 0
            prescription = None
            for selected_item in self.selected_items:
                prescription = self.prescription_model.objects.get(
                    pk=selected_item)
                try:
                    PrescriptionApprovalValidator(prescriptions=[prescription])
                except PrescriptionApprovalValidatorError as e:
                    message = e
                else:
                    approved += 1
                    prescription.is_approved = True
                    prescription.save()
            if approved > 0:
                message = (
                    '{} items have been approved.'.format(
                        approved))
                messages.success(self.request, message)
            else:
                messages.error(self.request, message)
