"""empty message

Revision ID: c5cc272e8919
Revises: 
Create Date: 2017-03-19 18:43:55.691605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5cc272e8919'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feira_livre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registro', sa.String(length=10), nullable=False),
    sa.Column('nome_feira', sa.String(length=100), nullable=False),
    sa.Column('bairro', sa.String(length=100), nullable=False),
    sa.Column('logradouro', sa.String(length=255), nullable=False),
    sa.Column('numero', sa.String(length=10), nullable=True),
    sa.Column('referencia', sa.String(length=300), nullable=True),
    sa.Column('lat', sa.Integer(), nullable=True),
    sa.Column('long', sa.Integer(), nullable=True),
    sa.Column('setcens', sa.BigInteger(), nullable=True),
    sa.Column('areap', sa.BigInteger(), nullable=True),
    sa.Column('coddist', sa.Integer(), nullable=True),
    sa.Column('distrito', sa.String(length=100), nullable=True),
    sa.Column('codsubpref', sa.Integer(), nullable=True),
    sa.Column('subprefe', sa.String(length=100), nullable=True),
    sa.Column('regiao5', sa.String(length=100), nullable=True),
    sa.Column('regiao8', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('registro')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feira_livre')
    # ### end Alembic commands ###