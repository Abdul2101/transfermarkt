# Generated by Django 4.2.16 on 2024-12-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_tournament'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='assits',
            new_name='assists',
        ),
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='general.club'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='season',
            field=models.CharField(default='2023/24', max_length=9),
        ),
        migrations.CreateModel(
            name='TournamentParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to='general.club')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='general.tournament')),
            ],
            options={
                'unique_together': {('tournament', 'club')},
            },
        ),
    ]
