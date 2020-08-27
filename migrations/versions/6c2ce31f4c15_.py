"""empty message

Revision ID: 6c2ce31f4c15
Revises: 6757ddf93a55
Create Date: 2020-08-08 12:45:00.288705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c2ce31f4c15'
down_revision = '6757ddf93a55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('run',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('benchmark_id', sa.Integer(), nullable=True),
    sa.Column('solver_id', sa.Integer(), nullable=True),
    sa.Column('arguments', sa.String(length=1024), nullable=True),
    sa.Column('performance', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('start_date', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['benchmark_id'], ['benchmark.id'], ),
    sa.ForeignKeyConstraint(['solver_id'], ['solver.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('run_id', sa.Integer(), nullable=True),
    sa.Column('instance_id', sa.Integer(), nullable=True),
    sa.Column('result', sa.Enum('no_result', 'sat', 'unsat', 'timeout', 'unknown', 'error', name='solverresponseenum'), nullable=True),
    sa.Column('stdout', sa.UnicodeText(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['instance_id'], ['instance.id'], ),
    sa.ForeignKeyConstraint(['run_id'], ['run.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    op.drop_table('run')
    # ### end Alembic commands ###