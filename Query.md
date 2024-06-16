
### import models from the app to perform different operations using shell-plus

from apps.school.models import Author

### Creating authors objects

Author.objects.create(name='samiksha khadka')
Author.objects.create(name='sudip khanal')

### Querying all authors

authors = Author.objects.all()
print(authors)

### Output

<QuerySet [<Author: samiksha khadka>, <Author: sudip khanal>]>

### Get Author by Name

id_samiksha = Author.objects.get(name='samiksha khadka')
print(id_samiksha)

### Output

samiksha khadka

### Create Book Entries

from apps.school.models import Book

### Creating books

book = Book.objects.create(
name='two scoop of django',
author=id_samiksha,
isbn_number='12323',
pages=545
)
book.save()

sudip_id = Author.objects.get(name='sudip khanal')

book3 = Book.objects.create(
name='django for everyone',
author=sudip_id,
isbn_number='18323',
pages=1000
)
book3.save()

### Querying all books

books = Book.objects.all()
print(books)

### Output

<QuerySet [<Book: two scoop of django>, <Book: django for everyone>]>

### Create Student Entries

from apps.school.models import Student

### Creating students

Student.objects.create(full_name='sandesh thapa', roll_no=1, grade='12')
Student.objects.create(full_name='kashyap ghimire', roll_no=2, grade='11')

from apps.school.models import Course, Student

### Creating courses and assigning students

course1 = Course.objects.create(name='CS')
student1 = Student.objects.get(full_name='sandesh thapa')
course1.student.add(student1)

course2 = Course.objects.create(name='CSIT')
student2 = Student.objects.get(full_name='kashyap ghimire')
course2.student.add(student2)

### Querying all courses

courses = Course.objects.all()
print(courses)

### Output

<QuerySet [<Course: CS>, <Course: CSIT>]>

### Filter Courses by Name

cs_courses = Course.objects.filter(name='CS')
print(cs_courses)

### output

<QuerySet [<Course: CS>]>

### Using select_related to get books with authors

books_with_authors = Book.objects.select_related('author')
for b in books_with_authors:
print(b)

### Output

two scoop of django
django for everyone

### Using prefetch_related to get courses with students

courses_with_students = Course.objects.prefetch_related('student')
for course in courses_with_students:
print(course, course.student.all())

### output

CS school.Student.None <QuerySet [<Student: sandesh thapa>]>
CSIT school.Student.None <QuerySet [<Student: kashyap ghimire>]>
