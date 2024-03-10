

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_auto_20230415_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patientemail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
