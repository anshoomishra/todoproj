# Generated by Django 4.2.3 on 2023-07-28 10:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_todouser_managers_organizationjoinrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'permissions': [('can_create_roles', 'Can create Roles'), ('can_update_roles', 'Can update Roles')],
            },
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'permissions': [('Can_create_organisation', 'Can Create Organisation'), ('can_update_organisation', 'Can Update Organisation'), ('can_delete_organisation', 'Can Delete Organisation'), ('can_apprve_join_request', 'Can Approve Join Request')]},
        ),
    ]
