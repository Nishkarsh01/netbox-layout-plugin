from django_filters import FilterSet
from extras.filters import TagFilter

class RackAreaFilterSet(FilterSet):
    tag = TagFilter()