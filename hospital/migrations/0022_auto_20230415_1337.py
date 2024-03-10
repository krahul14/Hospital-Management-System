
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_auto_20230415_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
