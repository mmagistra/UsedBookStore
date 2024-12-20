from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Creating data...')

        print('Creating groups')

        groups = {
            'visitor': {
                'name': 'Visitor',
                'permissions': [
                    'view_profile',
                    'view_book',
                    'view_bookinstance',
                    'view_condition',
                    'view_genre',
                    'view_author',
                    'view_publisher',
                ]
            },
            'employee': {
                'name': 'Employee',
                'permissions': [
                    'add_profile',
                    'change_profile',
                    'delete_profile',
                    'view_profile',
                    'add_book',
                    'change_book',
                    'delete_book',
                    'view_book',
                    'add_bookinstance',
                    'change_bookinstance',
                    'delete_bookinstance',
                    'view_bookinstance',
                    'add_condition',
                    'change_condition',
                    'delete_condition',
                    'view_condition',
                    'add_genre',
                    'change_genre',
                    'delete_genre',
                    'view_genre',
                    'add_author',
                    'change_author',
                    'delete_author',
                    'view_author',
                    'add_publisher',
                    'change_publisher',
                    'delete_publisher',
                    'view_publisher',
                ]
            }
        }

        for group_name, group_data in groups.items():
            group, created = Group.objects.get_or_create(name=group_data['name'])

            for permission in group_data['permissions']:
                perm, created = Permission.objects.get_or_create(codename=permission, content_type__app_label='Store')
                group.permissions.add(perm)
        print('Done!')
