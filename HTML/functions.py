import sys
sys.path.insert(1, '../API')
from testDB import *


def logIn(username, password):
    return username + password

    """req = get_user_from_db(username)
    try:
        data = req['info']
    except:
        return 'Wrong Username'
    
    pwd = data['password']
    if pwd != password:
        return 'Wrong Password'
    else:
        update_user_in_db(username, 'logged_in', 'True')
        return 'Logged In'"""


def logOut(username):
    update_user_in_db(username, 'logged_in', 'False')
    return 'Home Page'


def applyForCustomer(username, password, user_email):
    req = get_user_from_db(username)
    try:
        data = req['info']
        return 'Wrong Username'
    except:
        sendUserInfoToEmployee(username, password, user_email, 'customer')


def approveCust(accept, username, password, email, user_type):
    if accept:
        add_user_to_db(username, password, user_type, email)
    else:
        denyCust(username, password, email, 'customer')


def denyCust(username, password, email, user_type):
    sendToOwner(username, password, email, user_type, 'Denied Customer App')


def veto(approved, username, password, email, user_type):
    if approved:
        add_user_to_db(username, password, user_type, email)
    else:
        sendEmailToUser


def deposit(card_error, username, money):
    if card_error:
        return 'Bad credit card'
    else:
        balance = int(get_user_from_db(username)['info']['balance'])
        update_user_in_db(username, 'balance', balance)



    