from edc_pharma.dispense import DispenseAction

from django.apps import apps as django_apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .base_action_view import BaseActionView


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispensingActionView(BaseActionView):

    post_url_name = app_config.appointment_listboard_url_name
    listboard_url_name = app_config.appointment_listboard_url_name
    valid_form_actions = ['dispensing']
    prescription_model = django_apps.get_model(
        *edc_pharma_app_config.prescription_model.split('.'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._selected_manifest = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def process_form_action(self):
        if self.action == 'dispensing':
            self.dispensing()

    def dispensing(self):
        """Adds the selected items to the selected manifest.
        """
        if not self.selected_items:
            message = ('Nothing to do. No items have been selected.')
            messages.warning(self.request, message)
        else:
            dispensed = 0
            for selected_item in self.selected_items:
                DispenseAction(appointment_id=selected_item)
            if dispensed > 0:
                message = (
                    '{} items have been dispensed.'.format(
                        dispensed))
                messages.success(self.request, message)
