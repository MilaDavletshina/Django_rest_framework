import re
from rest_framework.serializers import ValidationError


#11.1
class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Проверка полученного value."""
        reg = re.compile('^[a-zA-Z0-9\,\-\ ]+$')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)): #reg.match вернет True если удовлетворяет условиям, если нет-False
            raise ValidationError('Title is not ok')