from django.contrib import admin

from .models import Post
from .forms import PostChangeForm, PostCreationForm


class PostAdmin(admin.ModelAdmin):
    model = Post

    form = PostChangeForm
    add_form = PostCreationForm

    list_display = ('title', 'description', 'posted_on')
    list_display_links = ('title',)

    add_fieldsets = (
        (None, {'fields': ('title', 'description', 'body', 'user')}),
    )

    search_fields = ('title',)
    ordering = ('posted_on',)


admin.site.register(Post, PostAdmin)
