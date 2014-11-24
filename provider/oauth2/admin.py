from django.contrib import admin
from provider import scope
from .models import AccessToken, Grant, Client, RefreshToken


class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'token', 'expires', 'scopes',)
    raw_id_fields = ('user',)

    def scopes(self, access_token):
        return ';'.join(scope.to_names(access_token.scope))


class GrantAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'code', 'expires',)
    raw_id_fields = ('user',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'redirect_uri', 'client_id', 'client_type')
    raw_id_fields = ('user',)

admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(RefreshToken)
