from django.contrib import admin

from .models import Post
from .forms import PostChangeForm, PostCreationForm


class PostAdmin(admin.ModelAdmin):
    model = Post

    form = PostChangeForm
    add_form = PostCreationForm

    list_display = ('id', 'post_desc', 'posted_on', 'posted_by')
    list_display_links = ('id',)

    add_fieldsets = (
        (None, {'fields': ('post_desc', 'post_body', 'posted_by')}),
    )

    search_fields = ('post_desc', 'posted_by')
    ordering = ('posted_on',)


admin.site.register(Post, PostAdmin)
