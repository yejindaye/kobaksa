# Generated by Django 3.1 on 2020-11-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningLevel', '0003_mdlcourse_mdlenrol_mdluserenrolments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexkeyword',
            fields=[
                ('keyword', models.CharField(blank=True, max_length=50, null=True)),
                ('indexnum', models.CharField(blank=True, db_column='indexNum', max_length=50, null=True)),
                ('k_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'indexKeyword',
                'managed': False,
            },
        ),
    ]