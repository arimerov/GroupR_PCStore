var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.7.0.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);


// For login.html
async function login(){
	var user = document.getElementById('usernameIn').value;
   	var password = document.getElementById('passwordIn').value;
	var response = await fetch('http://127.0.0.1:8002/login?username=' + user + '&password=' + password)
	var ans = await response.text()
	// loadPage("use", ans)
	// loadPage('use', ans)
	var userText = parent.document.getElementById('userTypeText');
	var userName = parent.document.getElementById('userName');
	var back = parent.document.getElementById('navBar');
	
	if(ans == '3'){ 
		back.style.backgroundColor = "#E3242B";
		userText.innerHTML = "Owner";
		userName.innerHTML = user;
		logIn_Out()
		window.location.href = 'admin.html'
	}
	else if(ans == '2'){ 
		back.style.backgroundColor = "#99EDC3";
		userText.innerHTML = "Employee";
		userName.innerHTML = user;
		logIn_Out()
		window.location.href = 'admin.html'
	}
	else if(ans == '1'){ 
		back.style.backgroundColor = "#B3C3F3";
		userText.innerHTML = "Customer";
		userName.innerHTML = user;
		logIn_Out()
		window.location.href = 'home.html'
	}
	else {
		alert("Wrong username or password")
	}
}

async function register(){
	var first = document.getElementById('registerFirstNameIn').value;
	var last = document.getElementById('registerLastNameIn').value;
	var email = document.getElementById('registerEmailIn').value;
	var username = document.getElementById('registerUsernameIn').value;
	var password = document.getElementById('registerPassIn').value;
	var confirmPass = document.getElementById('registerConfPassIn').value;
	if(password != confirmPass){
		alert("Passwords don't match.")
		return;
	}
	var response = await fetch(
		  'http://127.0.0.1:8002/registration?username=' + username 
		  + '&firstName=' + first
		  + '&lastName=' + last
		  + '&email=' + email
		  + '&password=' + password);
	var ans = await response.text()
	alert('Success')
	window.location.href = "home.html";
}

async function getProfile() {
	var userName = parent.document.getElementById('userName');
	var US_name = userName.innerHTML
	var name = document.getElementById('accountName');
	var email = document.getElementById('accountEmail');
	var funds = document.getElementById('accountFunds');
	var uType = document.getElementById('userType');
	var compli = document.getElementById('userCompliments');
	var warn = document.getElementById('userWarnings');
	var tenOff = document.getElementById('10off');
	var cBuilds = document.getElementById('associatedBuilds');
	var response = await fetch(
		'http://127.0.0.1:8002/getuser?username=' + US_name);
  	var ans = await response.json()
	name.innerHTML += ans['firstname'] + ' ' + ans['lastname']
	email.innerHTML += ans['user_email']
	funds.innerHTML += ans['balance']
	uType.innerHTML += ans['user_type']
	compli.innerHTML += ans['compliments']
	warn.innerHTML += ans['warnings']
	tenOff.innerHTML += ans['_10off']
	cBuilds.innerHTML += ans['builds_created']
}


async function fillForum() {
	var response = await fetch(
		'http://127.0.0.1:8002/getforums');
  	var ans = await response.json()
	ans = ans['info']
	for (var i = 0; i < ans.length; ++i) {
		var fillBy = ans[i]['filled_by']
		var fillFor = ans[i]['filled_for']
		var text = ans[i]['text']
		var type = ans[i]['type']
		var status = ans[i]['status']
		
		fillInRow(fillBy, fillFor, text, type, status)
	}
}

async function fillCatalog() {
	var response = await fetch(
		'http://127.0.0.1:8002/getcatalog');
  	var ans = await response.json()
	ans = ans['info']
	for (var i = 0; i < ans.length; ++i) {
		var fillBy = ans[i]['filled_by']
		var fillFor = ans[i]['filled_for']
		var text = ans[i]['text']
		var type = ans[i]['type']
		var status = ans[i]['status']
		fillInRow(fillBy, fillFor, text, type, status)
	}
}

// async function getPCBuild() {
// 	var userName = parent.document.getElementById('userName');
// 	var US_name = userName.innerHTML
// 	var name = document.getElementById('accountName');
// 	var email = document.getElementById('accountEmail');
// 	var funds = document.getElementById('accountFunds');
// 	var uType = document.getElementById('userType');
// 	var compli = document.getElementById('userCompliments');
// 	var warn = document.getElementById('userWarnings');
// 	var tenOff = document.getElementById('10off');
// 	var cBuilds = document.getElementById('associatedBuilds');
// 	var response = await fetch(
// 		'http://127.0.0.1:8002/getuser?username=' + US_name);
//   	var ans = await response.json()
// 	name.innerHTML += ans['firstname'] + ' ' + ans['lastname']
// 	email.innerHTML += ans['user_email']
// 	funds.innerHTML += ans['balance']
// 	uType.innerHTML += ans['user_type']
// 	compli.innerHTML += ans['compliments']
// 	warn.innerHTML += ans['warnings']
// 	tenOff.innerHTML += ans['_10off']
// 	cBuilds.innerHTML += ans['builds_created']
// }

async function deposit(){
	var userName = parent.document.getElementById('userName');
	var US_name = userName.innerHTML
	var CCIn = document.getElementById('CCIn').value;
	var ExpirationIn = document.getElementById('ExpirationIn').value;
	var CCVIn = document.getElementById('CCVIn').value;
	var cardZIPIn = document.getElementById('cardZIPIn').value;
	var ammountIn = document.getElementById('ammountIn').value;
	var response = await fetch('http://127.0.0.1:8002/deposit?username=' + US_name + '&CCIn=' + CCIn + '&ExpirationIn=' + ExpirationIn + '&CCVIn=' + CCVIn + '&cardZIPIn=' + cardZIPIn + '&ammountIn=' + ammountIn)
	var ans = await response.text()
	if(ans == '-1'){ 
		alert("Credit Card is not valid")
	}
	else if(ans == '-2'){ 
		alert("Expiration date is not valid")
	}
	else if(ans == '-3'){ 
		alert("zip code not valid")
	}
	else {
		alert("Success, your balance now is:" + ans)
		window.location.href = 'profile.html'
	}
  }

// For index.html, but called from within the iframe. 
// Toggles button from Login <-> LogOut 
function logIn_Out(){
	let logText = parent.document.getElementById('logText');
	let logButton = parent.document.getElementById('logButton');
	
	var clickAtt = logButton.getAttribute("onClick");
	(logText.innerHTML == 'Log-In') ? logText.innerHTML='Log-Out' : logText.innerHTML='Log-In';
	(clickAtt == "directiFrame('login.html')") ? logButton.setAttribute('onClick', 'logout()') : logButton.setAttribute('onClick', "directiFrame('login.html')");
	
}

// For index.html, log-out
function logout(){
	window.location.href = "index.html";
	US_name = '';
}

// For index.html, Allows nav to make change html nested in iframe
function directiFrame(link){
      $( '#iframe' ).attr('src', link);
}


// comment(user, text)

// pushAvailableParts(custom.html)

// pushDeviceDetails(device.html)
// pushCommentsOnPage(device.html)
// pushRating(device.html)

// customBuild(user)

// confirmBuild(user)
// Ask to add custom build to catalog
// addToCatalog()

// pushRegistrationForm() -> admin.html

// pushProfileInfo()

// Administration side of things!! *Maybe don't show o.O*

// checkCommentBadWord()


// if value == 0 -> warning(); Check this is working
// After purchase ask customer to rate. Not practical but gets free 10 points
async function purchase(){
      var username = document.getElementById('username').value;
      var pc_id = document.getElementById('pc_id').value;
      var response = await fetch('http://127.0.0.1:8002/purchase?username=' + user + '&pc_id=' + pc_id)
      var ans = response.text()
      ans.then(
        function(value) { console.log(value)}, // return value is 0 if error, 1 if ok
        function(error) { console.log(error)}
      )
    }