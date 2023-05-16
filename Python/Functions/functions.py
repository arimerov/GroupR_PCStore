import sys
sys.path.insert(1, '../API')
from testDB import *

app = Flask(__name__)
cors = CORS(app)


@app.route("/getuser")
def getUser():
    username = request.args.get('username')
    print("USERNAME", username)
    req = get_user_from_db(username)
    data = req['info']
    return data


@app.route("/getbuild")
def getBuild():
    build_id = request.args.get('build_id')
    data = get_build_from_db(build_id)
    return data



@app.route("/getforums")
def getForums():
    data = get_forums_from_db()
    resp = jsonify({'info':data})
    resp.status_code = 200
    return resp


@app.route("/getbuilds")
def getBuilds():
    data = get_builds_from_db()
    resp = jsonify({'info':data})
    resp.status_code = 200
    return resp


@app.route("/approve")
def approveCust():
    form_id = request.args.get('form_id')
    username = request.args.get('username')
    req1 = update_forum_in_db(form_id, 'status', 'done')
    req2 = update_user_in_db(username, 'account_is_active', 'True')
    return '1'


@app.route("/login")
def logIn():
    username = request.args.get('username')
    password = request.args.get('password')
    req = get_user_from_db(username)
    try:
        data = req['info']
    except:
        return '0' #'Wrong Username'
    
    pwd = data['password']
    if pwd != password:
        return '0' #'Wrong Password'
    elif data['account_is_active'] == 'False':
        return '0' #Account not active
    elif data['account_is_active'] == 'pending':
        return '0' #Account not active
    else:
        update_user_in_db(username, 'logged_in', 'True')
        print("LOGGED IN")
        if data['user_type'] == 'customer':
            return '1'
        elif data['user_type'] == 'employee':
            return '2'
        elif data['user_type'] == 'admin':
            return '3'
        else:
            return '0' # wrong user_type
        #'Logged In'


@app.route("/deposit")
def deposit():
    username = request.args.get('username')
    CCIn = request.args.get('CCIn')
    ExpirationIn = request.args.get('ExpirationIn')
    CCVIn = request.args.get('CCVIn')
    cardZIPIn = request.args.get('cardZIPIn')
    ammountIn = request.args.get('ammountIn')
    m, y = ExpirationIn.split('/')
    if len(CCIn) != 16 or (not CCIn.isnumeric()):
        return '-1' #CC not valid
    elif int(y) < 23 or (int(y) == 23 and int(m) < 6):
        return '-2' #Expiration not valid
    elif len(cardZIPIn) != 5 or (not cardZIPIn.isnumeric()):
        return '-3' #zip not valid
    else:
        balance = float(get_user_from_db(username)['info']['balance']) + float(ammountIn)
        update_user_in_db(username, 'balance', balance)
        return str(balance)


@app.route("/purchase")
def purchase():
    username = request.args.get('username')
    pc_id = request.args.get('pc_id')

    req_user = get_user_from_db(username)
    try:
        user_data = req_user['info']
    except:
        return '0' #'Wrong Username'
    pc_data = get_build_from_db(pc_id)['info']

    if user_data['balance'] < pc_data['price']:
        giveWarning(username)
        return '0'
    else:
        new_balance = user_data['balance'] - pc_data['price']
        update_user_in_db(username, 'balance', new_balance)
        builds_purchased = user_data['builds_purchased']
        builds_purchased.append(pc_id)
        update_user_in_db(username, 'builds_purchased', builds_purchased)
        return '1'


@app.route("/registration")
def register():
    username = request.args.get('username')
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    email = request.args.get('email')
    password = request.args.get('password')
    add_user_to_db(username, password, 'customer', email, firstName, lastName)
    update_user_in_db(username, 'account_is_active', 'pending')
    add_forum_to_db(username, 'employee', 'Waiting for approval', 'approveCustomer', 'open')
    return '1'


    

# def logOut(username):
#     update_user_in_db(username, 'logged_in', 'False')
#     return 'Home Page'


# def applyForCustomer(username, password, user_email):
#     req = get_user_from_db(username)
#     try:
#         data = req['info']
#         return 'Wrong Username'
#     except:
#         sendUserInfoToEmployee(username, password, user_email, 'customer')


# def approveCust(accept, username, password, email, user_type):
#     if accept:
#         add_user_to_db(username, password, user_type, email)
#     else:
#         denyCust(username, password, email, 'customer')


# def denyCust(username, password, email, user_type):
#     sendToOwner(username, password, email, user_type, 'Denied Customer App')


# def veto(approved, username, password, email, user_type):
#     if approved:
#         add_user_to_db(username, password, user_type, email)
#     else:
#         sendEmailToUser






    