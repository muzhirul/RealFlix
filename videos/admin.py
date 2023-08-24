from django.contrib import admin
from .models import Video, VideoPublishedProxy, VideoAllProxy

# Register your models here.


class VideoAllProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'state', 'video_id',
                    'is_published', 'publish_timestamp']
    list_filter = ['video_id', 'state']
    search_fields = ['title', 'video_id']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllProxy

    # def published(self, obj, *args, **kwargs):
    #     return obj.active


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    list_filter = ['video_id']
    search_fields = ['title', 'video_id']

    class Meta:
        model = VideoPublishedProxy

    ''' 
    Only show the active videos list
    '''

    def get_queryset(self, request):
        return Video.objects.filter(active=True)


admin.site.register(VideoAllProxy, VideoAllProxyAdmin)
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
# admin.site.register(VideoAllProxy)
