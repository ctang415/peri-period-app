from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import datetime

class Note(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    date: so.Mapped[datetime] = so.mapped_column(sa.DateTime)
    title: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    symptoms: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140), index=True)
    notes: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140), index=True)