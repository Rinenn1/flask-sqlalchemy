from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer, Float
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = Column("id", Integer, primary_key=True)
    magnitude = Column("magnitude", Float)
    location = Column("location", String)
    year = Column("year", Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
