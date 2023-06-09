# Generated by Django 4.2 on 2023-05-29 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ouvrages', '0005_avisouvrages_image'),
        ('Aso', '0011_remove_aso_dossier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aso',
            name='armoire',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='aso_num',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='avis_ouvrage',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='balise_a_solder',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='document',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='edossier',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='etape',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='imprime',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='maestro',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='mel',
        ),
        migrations.RemoveField(
            model_name='aso',
            name='nos_reference',
        ),
        migrations.AddField(
            model_name='aso',
            name='ouvrage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ouvrages.ouvrages'),
        ),
        migrations.AddField(
            model_name='aso',
            name='redacteur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aso',
            name='statut',
            field=models.CharField(choices=[(0, 'En cours'), (1, 'Accepté'), (2, 'Classé'), (4, 'diffusé')], default=0, max_length=50),
        ),
    ]
