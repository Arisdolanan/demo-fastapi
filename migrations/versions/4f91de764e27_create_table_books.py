"""create table books

Revision ID: 4f91de764e27
Revises:
Create Date: 2024-07-27 15:20:05.544701

"""
from typing import Sequence, Union
from sqlalchemy.sql import func

from alembic import op
import sqlalchemy as sa
from faker import Faker


# revision identifiers, used by Alembic.
revision: str = '4f91de764e27'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
fake = Faker(locale='id_ID')

def upgrade():
    book_table = op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255)),
        sa.Column('category', sa.String(255)),
        sa.Column('publisher', sa.String(255)),
        sa.Column('number_of_pages', sa.Integer),
        sa.Column('start_reading', sa.DateTime),
        sa.Column('end_reading', sa.DateTime),
        sa.Column('created_at', sa.DateTime(timezone=True), default=func.now())
    )

    op.bulk_insert(
        book_table,
        [{
            'name': fake.name(),
            'category': 'Fiction',
            'publisher': fake.company(),
            'number_of_pages': 300,
            'start_reading': fake.past_date(),
            'end_reading': fake.future_datetime(),
        } for x in range(5)]
    )


def downgrade():
    op.drop_table('books')
