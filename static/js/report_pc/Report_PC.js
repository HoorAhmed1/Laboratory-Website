/*const hideButton = document.getElementById("hideButton");
const home = document.getElementById("paragraph");
const sideBar = document.getElementById("sideBar");
const sideNav = document.getElementById("sideNav");
const showButton = document.getElementById("showButton");


hideButton.addEventListener("click", function hideSideBar(){
    if (sideNav.style.display!="none")
    {
        console.log("here");
        sideBar.style.display ="none";
        showButton.style.display = "flex";
        hideButton.style.display = "none";

    }
})

showButton.addEventListener("click", function showSideBar(){
    if (sideNav.style.display!="flex")
    {
        sideBar.style.display = "flex";
        hideButton.style.display = "flex";
        showButton.style.display = "none";

    }
})*/
function checkForm(){ 
   
    /*let form = form.problemForm;*/
    var labId = document.getElementById("LabID").value;
    var IsEmpty = false;
    var PCNumber = document.getElementById("PCnumber").value;
    if (labId == "" /*|| labId === null || labId >= 20*/) { 
        alert("Error: enter valid lab ID");
        document.getElementById("labId").focus();
        IsEmpty = true;
    }
    else if (PCNumber == "" /*|| PCNumber === null*/) {
        alert("Error: enter valid PC number");
        document.getElementById("PCNumber").focus();
        IsEmpty = true;
    }
    else if (document.getElementById("hardware").checked== false && document.getElementById("software").checked==false) {
        alert("Error: you must choose one problem type at least!");
        IsEmpty = true;
    }
    return IsEmpty;
    /*return true;*/
    /*alert("Submitted successfully!");*/
    /*alert("asdg");*/
}
