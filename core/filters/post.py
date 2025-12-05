import django_filters
from django_filters.rest_framework import FilterSet

from core.models import Post, Category, Tag



class PostFilter(FilterSet):
    category = django_filters.ModelChoiceFilter(
        field_name='categories',
        queryset=Category.objects.all(),
        label='Category'
    )

    tags = django_filters.ModelChoiceFilter(
        field_name='tags',
        queryset=Tag.objects.all(),
        label='Tag'
    )

    author = django_filters.CharFilter(
        field_name='author__phone_number',
        lookup_expr='icontains',
        label='Author'
    )

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr="icontains",
        label='Title'
    )

    class Meta:
        model = Post
        fields = ['category', 'tags', 'author', 'title']
