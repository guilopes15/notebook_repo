#django
#python brasil - https://www.youtube.com/watch?v=CSvs1CcwBWw


def migrate_table1_field1_format(apps, schema_editor):
    table1 = apps.get_model('my_app', 'table1')


    def _generator():
        for row in table1.objects.all().iterator():
            row.field1 = f'prefix_{row.field1}'
            yield row

    
    table1.objetcts.bulk_update(
        _generator(), 
        update_fields=['field1'], 
        batch_size=1000
    )


class Migration(migrations.Migration):
    depedencies = [('my_app', '0001_initial')]
    
    operations = [
        migrations.RunPython(
            migrate_table1_field1_format, 
            migrations.RunPython.noop,
            ),
    ]
