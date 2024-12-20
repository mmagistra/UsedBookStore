from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import IntegrityError

from Store.models import Book, BookInstance, Genre, Author, Publisher, Condition, Profile
from django.contrib.auth.models import User, Group

UserModel = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Creating test data')

        print('Creating admin if not exists')
        if UserModel.objects.filter(username='admin').exists():
            print('Admin already exists')
        else:
            print('Creating admin...')
            # Create a superuser
            User.objects.create_superuser(
                username='admin',
                email='lXK7t@example.com',
                password='admin',
            )
            print('Admin created')

        # Create a publisher
        test_data = {
            'Authors': [
                'Александр Пушкин',
                'Лев Толстой',
                'Михаил Лермонтов',
                'Николай Гоголь',
                'Федор Достоевский',
            ],
            'Genres': [
                'Роман',
                'Поэзия',
                'Приключения',
                'Фантастика',
                'Детектив',
            ],
            'Publishers': [
                'Эксмо',
                'АСТ',
                'Молодая гвардия',
                'Азбука-Аттикус',
                'Просвещение'
            ],
            'Conditions': [
                {
                    'degree_of_wear': 1,
                    'description': 'Идеальное',
                },
                {
                    'degree_of_wear': 2,
                    'description': 'Хорошее',
                },
                {
                    'degree_of_wear': 3,
                    'description': 'Удовлетворительное',
                },
                {
                    'degree_of_wear': 4,
                    'description': 'Плохое',
                },
                {
                    'degree_of_wear': 5,
                    'description': 'Критическое',
                }
            ],
            'Users': [
                {
                    'username': 'employee1',
                    'email': 'employee@example.com',
                    'password': 'cjnhelybr1',
                    'group': ['Employee'],
                },
                {
                    'username': 'visitor1',
                    'email': 'client@example.com',
                    'password': 'gjctnbntkm1',
                    'group': ['Visitor'],
                }
            ],
            'Profiles': [
                {
                    'username': 'admin',
                },
                {
                    'username': 'employee1',
                },
                {
                    'username': 'visitor1',
                }
            ],
            'Books': [
                {
                    'title': 'Война и мир',
                    'description': 'Описание книги',
                    'cover': '',
                    'publisher': 'Эксмо',
                    'published_year': 1869,
                    'genres': ['Роман', 'Приключения'],
                    'authors': ['Лев Толстой'],
                },
                {
                    'title': 'Преступление и наказание',
                    'description': 'Описание книги',
                    'cover': '',
                    'publisher': 'Просвещение',
                    'published_year': 1866,
                    'genres': ['Роман', 'Приключения'],
                    'authors': ['Федор Достоевский'],
                },
                {
                    'title': 'Мастер и Маргарита',
                    'description': 'Описание книги',
                    'cover': '',
                    'publisher': 'Просвещение',
                    'published_year': 1867,
                    'genres': ['Роман', 'Приключения'],
                    'authors': ['Михаил Лермонтов'],
                }
            ],
            'BookInstances': [
                {
                    'book': {
                        'title': 'Война и мир',
                        'publisher': 'Эксмо',
                        'published_year': 1869
                    },
                    'condition': 1,
                    'storage_cell': 'A1',
                    'purchase_price': 100,
                    'sale_price': 50,
                },
                {
                    'book': {
                        'title': 'Преступление и наказание',
                        'publisher': 'Просвещение',
                        'published_year': 1866
                    },
                    'condition': 2,
                    'storage_cell': 'A2',
                    'purchase_price': 200,
                    'sale_price': 100,
                },
                {
                    'book': {
                        'title': 'Мастер и Маргарита',
                        'publisher': 'Просвещение',
                        'published_year': 1867
                    },
                    'condition': 3,
                    'storage_cell': 'A3',
                    'purchase_price': 300,
                    'sale_price': 150,
                },
                {
                    'book': {
                        'title': 'Война и мир',
                        'publisher': 'Эксмо',
                        'published_year': 1869
                    },
                    'condition': 4,
                    'storage_cell': 'A4',
                    'purchase_price': 400,
                    'sale_price': 200,
                },
            ],
        }

        print('Creating authors, genres, publishers, conditions, users, profiles, books and book instances...')
        try:
            # Authors
            authors = [Author(name=author) for author in test_data['Authors']]
            Author.objects.bulk_create(authors)
            print('+ Authors created')
        except IntegrityError:
            print('- Authors already exist')

        try:
            # Genres
            genres = [Genre(name=genre) for genre in test_data['Genres']]
            Genre.objects.bulk_create(genres)
            print('+ Genres created')
        except IntegrityError:
            print('- Genres already exist')

        try:
            # Publishers
            publishers = [Publisher(name=publisher) for publisher in test_data['Publishers']]
            Publisher.objects.bulk_create(publishers)
            print('+ Publishers created')
        except IntegrityError:
            print('- Publishers already exist')

        try:
            # Conditions
            conditions = [Condition(**condition) for condition in test_data['Conditions']]
            Condition.objects.bulk_create(conditions)
            print('+ Conditions created')
        except IntegrityError:
            print('- Conditions already exist')

        try:
            # Users
            users = []
            for data in test_data['Users']:
                user = UserModel(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                )
                users.append(user)
            UserModel.objects.bulk_create(users)
            for i, user in enumerate(users):
                for group_name in test_data['Users'][i]['group']:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)

            print('+ Users created')
        except IntegrityError as e:
            print('- Users already exist')

        try:
            # Profiles
            profiles = [
                Profile(
                    user=UserModel.objects.get(username=user['username'])
                )
                for user in test_data['Profiles']
            ]
            Profile.objects.bulk_create(profiles)
            print('+ Profiles created')
        except IntegrityError:
            print('- Profiles already exist')

        # Books
        try:
            # Books
            books = [
                Book(
                    title=book['title'],
                    description=book['description'],
                    cover=book['cover'],
                    publisher=Publisher.objects.get(name=book['publisher']),
                    published_year=book['published_year'],
                )
                for book in test_data['Books']
            ]
            Book.objects.bulk_create(books)
            for i, book in enumerate(books):
                for genre_name in test_data['Books'][i]['genres']:
                    genre = Genre.objects.get(name=genre_name)
                    book.genres.add(genre)
                for author_name in test_data['Books'][i]['authors']:
                    author = Author.objects.get(name=author_name)
                    book.authors.add(author)
            print('+ Books created')
        except IntegrityError:
            print('- Books already exist')

        # BookInstances
        try:
            for book_instance in test_data['BookInstances']:
                book = Book.objects.get(
                    title=book_instance['book']['title'],
                    publisher=Publisher.objects.get(name=book_instance['book']['publisher']),
                    published_year=book_instance['book']['published_year'],
                )
                condition = Condition.objects.get(degree_of_wear=book_instance['condition'])
                BookInstance.objects.create(
                    book=book,
                    condition=condition,
                    storage_cell=book_instance['storage_cell'],
                    purchase_price=book_instance['purchase_price'],
                    sale_price=book_instance['sale_price'],
                )
            print('+ BookInstances created')
        except IntegrityError:
            print('- BookInstances can not be created')

        print('Done!')
