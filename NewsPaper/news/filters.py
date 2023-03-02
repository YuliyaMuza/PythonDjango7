import django_filters
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category

class PostFilter(FilterSet):

    category = ModelChoiceFilter(field_name='post_category',
                                 queryset=Category.objects.all(),
                                 label='Post category',
                                 empty_label='All')

    time_later = DateTimeFilter(field_name="dateCreation",
                             lookup_expr="gt",
                             label="Дата публикации после:",

                             widget=DateTimeInput(format="%Y-%m-%dT%H:%M",
                             attrs={"type": "datetime-local"},))

    post_title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название публикации'
    )

    class PostFilter(FilterSet):
        added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
        post_title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название публикации'
    )


        class Meta:
            model = Post
            fields = [
                'title',
                'dateCreation',
                'categoryType',
                'postCategory',
            ]