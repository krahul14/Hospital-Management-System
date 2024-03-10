
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
