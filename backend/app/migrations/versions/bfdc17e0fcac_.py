"""

Revision ID: bfdc17e0fcac
Revises: b3a48d86e3f5
Create Date: 2019-05-09 17:32:59.555722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfdc17e0fcac'
down_revision = 'b3a48d86e3f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'UserProfile', 'UserLogin', ['UserID'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'comment', 'UserProfile', ['ToUserGlobalID'], ['UserGlobalID'], use_alter=True)
    op.create_foreign_key(None, 'comment', 'UserLogin', ['FromUserID'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'commentEndorse', 'UserLogin', ['EndorseBy'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'commentEndorse', 'comment', ['CommentID'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'userEndorse', 'UserLogin', ['EndorseBy'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'userEndorse', 'UserProfile', ['UserGlobalID'], ['UserGlobalID'], use_alter=True)
    op.create_foreign_key(None, 'userEndorse', 'endorsement', ['EndorseID'], ['id'], use_alter=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'userEndorse', type_='foreignkey')
    op.drop_constraint(None, 'userEndorse', type_='foreignkey')
    op.drop_constraint(None, 'userEndorse', type_='foreignkey')
    op.drop_constraint(None, 'commentEndorse', type_='foreignkey')
    op.drop_constraint(None, 'commentEndorse', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'UserProfile', type_='foreignkey')
    # ### end Alembic commands ###
