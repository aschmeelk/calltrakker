from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
calls = Table('calls', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date),
    Column('caller', String(length=64)),
    Column('phone', String(length=12)),
    Column('franchise', String(length=64)),
    Column('location', String(length=64)),
    Column('tech', String(length=64)),
    Column('machine', String(length=64)),
    Column('problem', String(length=128)),
    Column('comment', String(length=128)),
    Column('downtime', Integer),
    Column('plant_num', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['calls'].columns['phone'].create()
    post_meta.tables['calls'].columns['plant_num'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['calls'].columns['phone'].drop()
    post_meta.tables['calls'].columns['plant_num'].drop()
