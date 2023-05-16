let username = "";
let uType = "";

function updateUsername(name){
	username = name;
}
function returnUsername(){
	return username;
}




export {username as USERNAME};
export function updateUsername(name);
export function returnUsername();
