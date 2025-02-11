# Generated by Django 5.0.6 on 2024-06-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('N_trail_dashboard', '0003_alter_treatment_treatment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_1_count_1',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_1_count_2',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_1_count_3',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_1_count_4',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_1_count_5',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_2_count_1',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_2_count_2',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_2_count_3',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_2_count_4',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_2_count_5',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_3_count_1',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_3_count_2',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_3_count_3',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_3_count_4',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='Interaction_3_count_5',
        ),
        migrations.AddField(
            model_name='experiment',
            name='DSM_SAT',
            field=models.TextField(blank=True, null=True, verbose_name='DSM_SAT'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='DSM_UAV',
            field=models.TextField(blank=True, null=True, verbose_name='DSM_UAV'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='GCP',
            field=models.TextField(blank=True, null=True, verbose_name='GCP'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Interaction_1_value',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Interaction_2_value',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Interaction_3_value',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Orthomosic_SAT',
            field=models.TextField(blank=True, null=True, verbose_name='Orthomosic_SAT'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Orthomosic_UAV',
            field=models.TextField(blank=True, null=True, verbose_name='Orthomosic_UAV'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='RAWUAV',
            field=models.TextField(blank=True, null=True, verbose_name='RAWUAV'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Soil_Sample',
            field=models.TextField(blank=True, null=True, verbose_name='Soil_Sample'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Sonic_sensor',
            field=models.TextField(blank=True, null=True, verbose_name='Sonic_sensor'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='VI_1',
            field=models.TextField(blank=True, null=True, verbose_name='VI_1'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='VI_2',
            field=models.TextField(blank=True, null=True, verbose_name='VI_2'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='VI_3',
            field=models.TextField(blank=True, null=True, verbose_name='VI_3'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='Yield_Map',
            field=models.TextField(blank=True, null=True, verbose_name='Yield_Map'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='Interaction_1_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='Interaction_2_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='Interaction_3_count',
            field=models.IntegerField(default=0),
        ),
    ]
