from models import db, Users
def run():
    db.session.add(Users(
        first_name = 'Arthur',
        last_name = 'Pendragon',
        username = 'X-calibur',
        date_of_birth = '2/14/1989',
        email = 'once_and_future@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Gwen',
        last_name = 'Thomas',
        username = 'Style Queen',
        date_of_birth = '4/1/1991',
        email = 'queen_Thomas@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Merlin',
        last_name = 'Emrys',
        username = 'Arthur is a Dollophead',
        date_of_birth ='10/31/1990',
        email = 'wizardgod@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Morgana',
        last_name = 'Le Fay',
        username = 'True Beauty',
        date_of_birth ='1/25/1997',
        email = 'daddy_issues@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Lance',
        last_name = 'Lakely',
        username = 'Shining Armor',
        date_of_birth ='6/07/1989',
        email = 'mrstealyogurl@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Leon',
        last_name = 'Hart',
        username = 'RedMane',
        date_of_birth ='7/30/1998',
        email = 'Hart-Breaker@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Elyan',
        last_name = 'Thomas',
        username = 'The_Black_Smith',
        date_of_birth ='11/11/1997',
        email = 'loyal_AF@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Gwaine',
        last_name = 'Green',
        username = 'The Pretty One',
        date_of_birth ='12/23/1999',
        email = 'lifeofthePARTY@camelot.com'
    ))
    db.session.add(Users(
        first_name = 'Percy',
        last_name = 'Trainer',
        username = 'Mr Muscles',
        date_of_birth ='3/15/1999',
        email = 'Billy_Bones@camelot.com'
    ))
    db.session.commit()
    return 'seeds ran successfully'