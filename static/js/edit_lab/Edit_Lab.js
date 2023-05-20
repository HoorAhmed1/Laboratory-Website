function checkempty()
          
{var u=window.prompt("please enter num of lab you want to update?","1");
   
    var isempty=false,
    name=document.querySelector("[name='lab name']").value,
    labid=document.querySelector("[name='lab ID']").value,
    labbn=document.querySelector("[name='building number']").value,
    labfn=document.querySelector("[name='floor number']").value,
    labpcn=document.querySelector("[name='number of PCs']").value,
    labchn=document.querySelector("[name='number of chairs']").value,
    labcap=document.querySelector("[name='lab capacity']").value;

if(name==="")
{
    alert(" lab name cannot be empty,please enter the name!");
    document.getElementById("textname").focus();
    document.getElementById("textname").value=name;
    isempty=true;
}
else if(name.length>=10)
{
    alert(" lab name cannot be too long,please enter the name!");
    document.getElementById("textname").focus();
    document.getElementById("textname").value=name;
    isempty=true;
}
else if(labid==="")
{
    alert("ID cannot be empty,please enter the ID");
    document.getElementById("ID").focus();
    isempty=true;
}
else if(labbn==="")
{
    alert("Buildingnum cannot be empty,please enter the number of the building!");
    getElementById("buldingnum").focus();

    isempty=true;
}
else if(labfn==="")
{
    alert("floornum cannot be empty,please enter the number of the floor!");
    document.getElementById("floornum").focus();
    isempty=true;
}
else if(labpcn==="")
{
    alert(" Number of pcs cannot be empty,please enter the number of pcs !");
    document.getElementById("pcnum").focus();
    isempty=true;
}
else if(labchn==="")
{
    alert("Chairnum cannot be empty,please enter the number of chair!");
    document.getElementById("chairnum").focus();
    isempty=true;
}
else if(labcap==="")
{
    alert("Capicity cannot be empty,please enter the capicty of lab!");
    document.getElementById("cap").focus();
    isempty=true;
}
else{ alert("The lab  is updated successfully");}

return isempty;

}

function deleterow()
{
var r=window.prompt("please enter num of lab you want to delete?","1");
return confirm("Are you sure you want to delete this lab?");
table.deleteRow(r);
}
/*function openForm() {
document.getElementById("myForm").style.display = "block";
}

function closeForm() {
document.getElementById("myForm").style.display = "none";
}

function ValidateEmail(inputText)
{
// var mailformat = /^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/;
var mailformat = /^([a-zA-Z0-9\._]+)@([[a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/;
if(inputText.value.match(mailformat))
{
alert("You have entered a valid email address!");    //The pop up alert for a valid email address
document.form1.text1.focus();
return true;
}
else
{
alert("You have entered an invalid email address!");    //The pop up alert for an invalid email address
document.form1.text1.focus();
return false;
}
}
var myInput = document.getElementById("psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
// Validate lowercase letters
var lowerCaseLetters = /[a-z]/g;
if(myInput.value.match(lowerCaseLetters)) {  
letter.classList.remove("invalid");
letter.classList.add("valid");
} else {
letter.classList.remove("valid");
letter.classList.add("invalid");
}

// Validate capital letters
var upperCaseLetters = /[A-Z]/g;
if(myInput.value.match(upperCaseLetters)) {  
capital.classList.remove("invalid");
capital.classList.add("valid");
} else {
capital.classList.remove("valid");
capital.classList.add("invalid");
}

// Validate numbers
var numbers = /[0-9]/g;
if(myInput.value.match(numbers)) {  
number.classList.remove("invalid");
number.classList.add("valid");
} else {
number.classList.remove("valid");
number.classList.add("invalid");
}

// Validate length
if(myInput.value.length >= 8) {
length.classList.remove("invalid");
length.classList.add("valid");
} else {
length.classList.remove("valid");
length.classList.add("invalid");
}
}*/