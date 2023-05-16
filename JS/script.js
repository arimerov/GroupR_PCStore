
// For login.html
async function login(){
  	var user = document.getElementById('usernameIn').value;
 	var password = document.getElementById('passwordIn').value;
  	var response = await fetch('http://127.0.0.1:8002/login?username=' + user + '&password=' + password)
  	var ans = response.text()
  	ans.then(
  		// return value is an int (0 == index.html; 1 == home.html (for customer); 2 == admin.html (for Employee); 3 == admin.html
    	function(value) { 
    		logIn_Out();
    		var userText = parent.document.querySelector('userTypeText');
    		if(value == '3'){ 
    			document.style.backgroundColor = "#E3242B";
    			userText.innerHTML = "Owner";
    		}
    		if(value == '2'){ 
    			document.style.backgroundColor = "#99EDC3";
    			userText.innerHTML = "Employee";
    		}
    		if(value == '1'){ 
    			document.style.backgroundColor = "#B3C3F3";
    			userText.innerHTML = "Customer";
    		} else location.href("index.html");
    		console.log(value)
    	}, function(error) { console.log(error)}
    )
}


// For index.html, but called from within the iframe. 
// Toggles button from Login <-> LogOut 
function logIn_Out(){
	var logButton = parent.document.querySelector('logButton');
	var clickAtt = logButton.getAttribute("onClick");
	(logButton.innerHTML == 'Log-In') ? logButton.innerHTML='Log-Out' : logButton.innerHTML='Log-In';
	(clickAtt == "directiFrame('login.html')") ? logButton.setAttribute('onClick', 'logout()') : logButton.setAttribute('onClick', "directiFrame('login.html')");
}

// For index.html, log-out
function logout(){
	location.href("index.html");
	logIn_Out();
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