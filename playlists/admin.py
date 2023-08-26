from django.contrib import admin
from .models import MovieProxy, Playlist, PlaylistItem, TVShowProxy, TVShowSeasionProxy
# Register your models here.


class MovieProxyAdmiin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'description', 'state', 'video', 'slug']

    class Meta:
        model = MovieProxy

    def get_queryset(self, request):
        return MovieProxy.objects.all()


admin.site.register(MovieProxy, MovieProxyAdmiin)


class SeasonEpisodeInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0


class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [SeasonEpisodeInline]
    list_display = ['title', 'parent']

    class Meta:
        model = TVShowSeasionProxy

    def get_queryset(self, request):
        return TVShowSeasionProxy.objects.all()


admin.site.register(TVShowSeasionProxy, TVShowSeasonProxyAdmin)


class TVShowSeasonProxyInline(admin.TabularInline):
    model = TVShowSeasionProxy
    extra = 0
    fields = ['order', 'title', 'state']


class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TVShowSeasonProxyInline]
    fields = ['title', 'description', 'state', 'video', 'slug']
    list_display = ['title']

    class Meta:
        model = TVShowProxy

    def get_queryset(self, request):
        return TVShowProxy.objects.all()


admin.site.register(TVShowProxy, TVShowProxyAdmin)


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0


class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInline]

    class Meta:
        model = Playlist

    def get_queryset(self, request):
        return Playlist.objects.filter(type=Playlist.PlaylistTypeChoices.PLAYLIST)


admin.site.register(Playlist, PlaylistAdmin)
