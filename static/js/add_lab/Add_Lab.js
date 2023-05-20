function checkempty()
{
    var isempty=false,
    name=document.querySelector("[name='textnames']").value,
    labid=document.querySelector("[name='labId']").value,
    labbn=document.querySelector("[name='buildingnumber']").value,
    labfn=document.querySelector("[name='floornumber']").value,
    labpcn=document.querySelector("[name='pcnumber']").value,
    labchn=document.querySelector("[name='chairnumber']").value,
    labcap=document.querySelector("[name='capacity']").value;

if(name==="")
{
    alert(" lab name cannot be empty,please enter the name!");
    document.getElementById("textname").focus();
    
    isempty=true;
}
else if(name.length>=10)
{
    alert(" lab name cannot be too long,please enter the name!");
    document.getElementById("textname").focus();
    isempty=true;
}
else if(labid==="")
{
    alert("id cannot be empty,please enter the ID");
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
// alert("The lab  is added successfully");
return isempty;
}