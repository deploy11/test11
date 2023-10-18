# Generated by Django 4.2.6 on 2023-10-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sinf_alter_books_book_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='savolingiz'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sinf', verbose_name='sinfingiz'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='student_name',
            field=models.CharField(max_length=500, verbose_name='ismingiz'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teachers', verbose_name='o`qtuvchini tanlang'),
        ),
        migrations.CreateModel(
            name='Javob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comment')),
            ],
        ),
    ]
