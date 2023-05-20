const hideButton = document.getElementById("hideButton");
const home = document.getElementById("paragraph");
const sideBar = document.getElementById("sideBar");
const sideNav = document.getElementById("sideNav");
const showButton = document.getElementById("showButton");
const barIcon = document.getElementById("barIcon");

barIcon.addEventListener("click", function editSideBar(){
    if (sideBar.style.display =="none" || sideBar.style.display=="")
    {
        console.log("here");
        sideBar.style.display ="block";

    }
    else if (sideBar.style.display !="none" )
    {
        sideBar.style.display = "none";
        console.log("here");
    }
})

