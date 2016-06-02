# From SQLalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Floorplan, Unit, User
engine = create_engine('postgresql://catalog:robspassword@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

import sys # allows python to take command-line variables 
import json # import to enable reading JSON for unit info

# Populate Floorplan Data

user1 = User(name='Unknown', email='Unknown')
session.add(user1)
session.commit()

user2 = User(name='Rob Monday', email='rob.monday@gmail.com')
session.add(user2)
session.commit()

studio1 = Floorplan(name='Cozy Studio', square_footage=550, bedrooms=1, bathrooms=1, user_id=1)
session.add(studio1)
session.commit()

studio2 = Floorplan(name='Spacious Studio', square_footage=750, bedrooms=1, bathrooms=1, user_id=1)
session.add(studio2)
session.commit()

one_bedroom = Floorplan(name='Standard', square_footage=775, bedrooms=1, bathrooms=1, user_id=1)
session.add(one_bedroom)
session.commit()

loft = Floorplan(name='Loft', square_footage=695, bedrooms=1, bathrooms=1, user_id=1)
session.add(loft)
session.commit()

two_bedroom1 = Floorplan(name='Cozy Two-Bed', square_footage=900, bedrooms=2, bathrooms=1, user_id=1)
session.add(two_bedroom1)
session.commit()

two_bedroom2 = Floorplan(name='Large Two-Bed', square_footage=1150, bedrooms=2, bathrooms=2, user_id=1)
session.add(two_bedroom2)
session.commit()

print "Floorplan data populated successfully!"

# Populate Unit Data

# try:
# 	json_data_file = '/var/www/Catalog/catalog/sample_data.json' #edited to reflect Linux folder structure
# 	print len(sys.argv)
# 	if len(sys.argv)==2:
# 		json_data_file = '/var/www/Catalog/catalog/'+sys.argv[1] #edited to reflect Linux folder structure

# 	with open(json_data_file) as json_data:  # to see much more data, try:  sample_data_extended.json
# 	    dataload = json.load(json_data)
# 	    units = dataload['Unit']
# 	    # print units
# 	    iteration_num = 0
# 	    for unit in units:
# 	    	iteration_num += 1
# 	    	print 'Add unit # '+str(iteration_num)
# 	    	entry = Unit(name=unit['name'], floorplan_id=unit['floorplan_id'], user_id=unit['user_id'])
# 	    	session.add(entry)
# 	    	session.commit()
# 	print "Unit data populated successfully!"
# except:
# 	print "JSON did not load"

entry = Unit(name='Unit #1', floorplan_id=1, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #2', floorplan_id=1, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #3', floorplan_id=1, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #4', floorplan_id=1, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #5', floorplan_id=2, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #6', floorplan_id=2, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #7', floorplan_id=3, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #8', floorplan_id=4, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #9', floorplan_id=4, user_id=1)
session.add(entry)
session.commit()

entry = Unit(name='Unit #10', floorplan_id=5, user_id=1)
session.add(entry)
session.commit()

print "Unit data populated in repetitive manner--not from JSON file"