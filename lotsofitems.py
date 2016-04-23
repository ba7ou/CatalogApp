from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalogapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='http://i.imgur.com/5yWXB0x.png')
session.add(user1)
session.commit()

# Item for snowboarding
category1 = Category(name="Snowboarding")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Helmet", description="To protect your skull from rocks and trees", category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Board", description="A good board to enjoy freeride and snowpark", category=category1)

session.add(item2)
session.commit()


# Item for skiing
category2 = Category(name="Skiing")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Freestyle Ski", description="Do sick tricks with this wonderful stuff", category=category2)


session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Ski Gloves", description="Keep your hands dry", category=category2)

session.add(item2)
session.commit()



# Category for sport cams
category3 = Category(name="Sport Cams")

session.add(category3)
session.commit()


item1 = Item(user_id=1, name="FHD Cam", description="Film all your exploits", category=category3)


session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Auto Follow Drone", description="Your personnal filming quadcopter", category=category3)

session.add(item2)
session.commit()


print "added users, category and items!"
