from tbay import Item, User, Bid, session

# Add three users to the database
ryan = User(username='ryanm', password='Ryan1')
amy = User(username='amym', password='Amy1')
audrey = User(username='audreym', password='Audrey1')
paul = User(username='paulb', password='Paul1')

session.add_all([ryan, amy, audrey, paul])
session.commit()

# Make one user auction a baseball
baseball = Item(
  name='Autographed Baseball', 
  description='A baseball signed by David Ortiz', 
  start_time='2015-08-02 17:00:00.000000', 
  owner=ryan
)
football = Item(
  name='Autographed Football', 
  description='A football signed by the Super Bowl Champion New England Patriots ', 
  start_time='2015-08-02 17:00:00.000000', 
  owner=audrey
)
puck = Item(
  name='Autographed Hockey Puck', 
  description='A hockey puck signed by Tuuka Rask', 
  start_time='2015-08-02 17:00:00.000000', 
  owner=ryan
)
soccer = Item(
  name='Autographed Soccer Ball', 
  description='A soccer ball signed by the whole New England Revolution team', 
  start_time='2015-08-02 17:00:00.000000', 
  owner=amy
)

session.add_all([baseball, football, puck, soccer])
session.commit()

# Have each other user place two bids on the baseball

bid1 = Bid(price=60.50, bidder=audrey, auction_item=baseball)
bid2 = Bid(price=75.00, bidder=amy, auction_item=baseball)
bid9 = Bid(price=92.50, bidder=paul, auction_item=baseball)
bid3 = Bid(price=100.00, bidder=ryan, auction_item=football)
bid4 = Bid(price=50.30, bidder=amy, auction_item=football)
bid5 = Bid(price=7.75, bidder=audrey, auction_item=puck)
bid6 = Bid(price=15.00, bidder=amy, auction_item=puck)
bid7 = Bid(price=1000.00, bidder=ryan, auction_item=soccer)
bid8 = Bid(price=11.50, bidder=audrey, auction_item=soccer)

session.add_all([bid1, bid2, bid3, bid4, bid5, bid6, bid7, bid8, bid9])
session.commit()