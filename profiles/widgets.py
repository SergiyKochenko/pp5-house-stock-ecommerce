from django_countries.widgets import CountrySelectWidget

class CustomCountrySelectWidget(CountrySelectWidget):
    @property
    def choices(self):
        # Use a list comprehension to force evaluation
        return [choice for choice in self._choices]

    @choices.setter
    def choices(self, value):
        # Use a list comprehension to force iteration over value
        self._choices = [choice for choice in value]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self._choices  # force evaluation

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if 'choices' in context['widget']:
            context['widget']['choices'] = [choice for choice in context['widget']['choices']]
        return context
