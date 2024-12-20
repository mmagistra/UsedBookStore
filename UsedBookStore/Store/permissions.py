from rest_framework.permissions import DjangoModelPermissions


class DjangoModelPermissionsWithViewAll(DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return super().has_permission(request, view)
