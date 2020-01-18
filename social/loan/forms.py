from django import forms
from .models import Rule


class RulesForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['utility_bills', 'utility_bills_value', 'utility_bills_weight',
                  'traffic_challan', 'traffic_challan_value', 'traffic_challan_weight',
                  'charges_electric', 'charges_electric_value', 'charges_electric_weight',
                  'penalty_tax', 'penalty_tax_value', 'penalty_tax_weight',
                  'threshold', 'threshold_value', 'threshold_weight']
