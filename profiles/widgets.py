from django_countries.widgets import CountrySelectWidget

class CustomCountrySelectWidget(CountrySelectWidget):
    @property
    def choices(self):
        # Force evaluation of self._choices into a list
        return [choice for choice in self._choices]

    @choices.setter
    def choices(self, value):
        # Force iteration, regardless of underlying iterator type
        self._choices = [choice for choice in value]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self._choices  # force evaluation via property setter
        self._choices = list(self._choices)  # ensure _choices is a list

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if 'choices' in context['widget']:
            context['widget']['choices'] = [choice for choice in context['widget']['choices']]
        return context

    # Override get_choices() to ensure a list is always returned.
    def get_choices(self):
        # Ensure _choices has __len__; if not, force conversion to list
        if not hasattr(self._choices, '__len__'):
            self._choices = list(self._choices)
        return self._choices

    # Override __iter__ to force iterable to list.
    def __iter__(self):
        return iter(list(self._choices))

    def valid_value(self, value):
        # Ensure choices are a list before iterating
        for k, v in list(self.choices):
            if value == k:
                return True
        return False

# This widget can be used in forms to provide a country selection dropdown.





