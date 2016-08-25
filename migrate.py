from api import db, migration
from os import getcwd
from os.path import join 

migration.create_schema_version()
migrations = migration.get_filenames(join(getcwd(), 'migrations'))

versions = [f.split('__')[0] for f in migrations]

applied = migration.get_schema_version()

print migrations
print applied

if migration.verify_applied_migrations(versions, applied):
    migration.apply_migrations(migrations, applied)
    print "Migration success!"
else:
    print "Migration failed."
