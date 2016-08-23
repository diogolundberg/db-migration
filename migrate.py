from api import db, migration
import os

migration.create_schema_version()
migrations = migration.get_filenames("migrations")

versions = [f.split('__')[0] for f in migrations]

applied = migration.get_schema_version()

print migrations
print applied

if migration.verify_applied_migrations(versions, applied):
    migration.apply_migrations(migrations, applied)
    print "Migration success!"
else:
    print "Migration failed."
