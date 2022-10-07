# Generated by Django 4.1.1 on 2022-10-01 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='syllabus_sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('section_name', models.CharField(max_length=100)),
                ('section_status', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Syllabus Section',
                'verbose_name_plural': 'Syllabus Sections',
                'db_table': 'syllabus_sections',
            },
        ),
        migrations.CreateModel(
            name='syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(choices=[('english', 'English'), ('hindi', 'Hindi'), ('assamese', 'Assamese'), ('bengali', 'Bengali'), ('gujarati', 'Gujarati'), ('kannada', 'Kannada'), ('malayalam', 'Malayalam'), ('marathi', 'Marathi'), ('odia', 'Odia'), ('punjabi', 'Punjabi'), ('tamil', 'Tamil'), ('telugu', 'Telugu'), ('urdu', 'Urdu'), ('arabic', 'Arabic'), ('bodo', 'Bodo'), ('chinese', 'Chinese'), ('dogri', 'Dogri'), ('french', 'French'), ('german', 'German'), ('italian', 'Italian'), ('japanese', 'Japanese'), ('kashmiri', 'Kashmiri'), ('konkani', 'Konkani'), ('maithili', 'Maithili'), ('manipuri', 'Manipuri'), ('nepali', 'Nepali'), ('persian', 'Persian'), ('russian', 'Russian'), ('santhali', 'Santhali'), ('sindhi', 'Sindhi'), ('spanish', 'Spanish'), ('tibetan', 'Tibetan'), ('sanskrit', 'Sanskrit'), ('accountancy', 'Accountancy'), ('agriculture', 'Agriculture'), ('anthropology', 'Anthropology'), ('art_education_sculpture', 'Art Education Sculpture'), ('biology', 'Biology'), ('business_studies', 'Business Studies'), ('chemistry', 'Chemistry'), ('computer_science', 'Computer Science'), ('economics_business_economics', 'Economics/Business Economics'), ('engineering_graphics', 'Engineering Graphics'), ('entrepreneurship', 'Entrepreneurship'), ('environmental_studies', 'Environmental Studies'), ('general_test', 'General Test'), ('geography', 'Geography'), ('history', 'History'), ('home_science', 'Home Science'), ('knowledge_tradition_practices_india', 'Knowledge Tradition – Practices India'), ('languages_ia_ib', 'Languages (IA & IB)'), ('legal_studies', 'Legal Studies'), ('mass_media_mass_communication', 'Mass Media/ Mass Communication'), ('mathematics', 'Mathematics'), ('performing_arts', 'Performing Arts'), ('physical_education', 'Physical Education'), ('physics', 'Physics'), ('political_science', 'Political Science'), ('psychology', 'Psychology'), ('sanskrit', 'Sanskrit'), ('sociology', 'Sociology'), ('teaching_aptitude', 'Teaching Aptitude')], max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('syllabus_name', models.CharField(blank=True, max_length=100, null=True)),
                ('syllabus_file', models.FileField(blank=True, null=True, upload_to='syllabus')),
                ('syllabus_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('syllabus_status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('syllabus_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='syllabus_sections', to='study_material.syllabus_sections')),
                ('updated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Syllabus',
                'verbose_name_plural': 'Syllabus',
                'db_table': 'syllabus',
            },
        ),
        migrations.CreateModel(
            name='study_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(choices=[('english', 'English'), ('hindi', 'Hindi'), ('assamese', 'Assamese'), ('bengali', 'Bengali'), ('gujarati', 'Gujarati'), ('kannada', 'Kannada'), ('malayalam', 'Malayalam'), ('marathi', 'Marathi'), ('odia', 'Odia'), ('punjabi', 'Punjabi'), ('tamil', 'Tamil'), ('telugu', 'Telugu'), ('urdu', 'Urdu'), ('arabic', 'Arabic'), ('bodo', 'Bodo'), ('chinese', 'Chinese'), ('dogri', 'Dogri'), ('french', 'French'), ('german', 'German'), ('italian', 'Italian'), ('japanese', 'Japanese'), ('kashmiri', 'Kashmiri'), ('konkani', 'Konkani'), ('maithili', 'Maithili'), ('manipuri', 'Manipuri'), ('nepali', 'Nepali'), ('persian', 'Persian'), ('russian', 'Russian'), ('santhali', 'Santhali'), ('sindhi', 'Sindhi'), ('spanish', 'Spanish'), ('tibetan', 'Tibetan'), ('sanskrit', 'Sanskrit'), ('accountancy', 'Accountancy'), ('agriculture', 'Agriculture'), ('anthropology', 'Anthropology'), ('art_education_sculpture', 'Art Education Sculpture'), ('biology', 'Biology'), ('business_studies', 'Business Studies'), ('chemistry', 'Chemistry'), ('computer_science', 'Computer Science'), ('economics_business_economics', 'Economics/Business Economics'), ('engineering_graphics', 'Engineering Graphics'), ('entrepreneurship', 'Entrepreneurship'), ('environmental_studies', 'Environmental Studies'), ('general_test', 'General Test'), ('geography', 'Geography'), ('history', 'History'), ('home_science', 'Home Science'), ('knowledge_tradition_practices_india', 'Knowledge Tradition – Practices India'), ('languages_ia_ib', 'Languages (IA & IB)'), ('legal_studies', 'Legal Studies'), ('mass_media_mass_communication', 'Mass Media/ Mass Communication'), ('mathematics', 'Mathematics'), ('performing_arts', 'Performing Arts'), ('physical_education', 'Physical Education'), ('physics', 'Physics'), ('political_science', 'Political Science'), ('psychology', 'Psychology'), ('sanskrit', 'Sanskrit'), ('sociology', 'Sociology'), ('teaching_aptitude', 'Teaching Aptitude')], max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('material_name', models.CharField(blank=True, max_length=100, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='study_material')),
                ('material_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('material_status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Study Material',
                'verbose_name_plural': 'Study Materials',
                'db_table': 'study_material',
            },
        ),
    ]