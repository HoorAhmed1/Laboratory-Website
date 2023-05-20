const search = document.getElementById('engine');
const table = document.getElementById('container');
const xhttp = new XMLHttpRequest();
xhttp.open('get', 'active');
xhttp.send();
let data = [];
xhttp.addEventListener('load', () => {
    data = JSON.parse(xhttp.responseText);
    // table.innerHTML += `
    //     <tr class="table-header">
    //         <th class="col col-1">Lab Name</th>
    //         <th class="col col-2">Lab ID</th>
    //         <th class="col col-3">Building Number</th>
    //         <th class="col col-4">Floor Number</th>
    //         <th class="col col-5">Number of PCs</th>
    //         <th class="col col-6">Number of Chairs</th>
    //         <th class="col col-7">Lab Capacity</th>
    //         <th class="col col-8">Status</th>
    //     </tr>`;
    for (let i = 0; i < data.length; i++) {
        console.log(data[i]);
        table.innerHTML += `<tr>
        <tr class="table-row">
        <td class="col col-1" data-label="labName">${data[i].labName}</td>
        <td class="col col-2" data-label="labId">${data[i].labID}</td>
        <td class="col col-3" data-label="buildingNum">${data[i].buildingNum}</td>
        <td class="col col-4" data-label="floorNum">${data[i].floorNum}</td>
        <td class="col col-5" data-label="numOfPC">${data[i].numOfPC}</td>
        <td class="col col-6" data-label="numberOfChair">${data[i].numberOfChair}</td>
        <td class="col col-7" data-label="labCapacity">${data[i].labCapacity}</td>
        <td class="col col-8" data-label="Status">${data[i].Status}</td>
        </tr>`;
    }
    // const change = document.querySelectorAll(".st");
    
});
search.addEventListener('keyup', () => {
    
    table.innerHTML = `<hr>
        <tr class="table-header">
            <th class="col col-1">Lab Name</th>
            <th class="col col-2">Lab ID</th>
            <th class="col col-3">Building Number</th>
            <th class="col col-4">Floor Number</th>
            <th class="col col-5">Number of PCs</th>
            <th class="col col-6">Number of Chairs</th>
            <th class="col col-7">Lab Capacity</th>
            <th class="col col-8">Status</th>
        </tr>`;
        for (let i = 0; i < data.length; i++)
            if (String(data[i].labName.toLowerCase()).includes((search.value.toLowerCase()))) {
                console.log(data[i].labName)
                table.innerHTML += `<tr class="table-row">
                <td class="col col-1" data-label="labName">${data[i].labName}</td>
                <td class="col col-2" data-label="labId">${data[i].labID}</td>
                <td class="col col-3" data-label="buildingNum">${data[i].buildingNum}</td>
                <td class="col col-4" data-label="floorNum">${data[i].floorNum}</td>
                <td class="col col-5" data-label="numOfPC">${data[i].numOfPC}</td>
                <td class="col col-6" data-label="numberOfChair">${data[i].numberOfChair}</td>
                <td class="col col-7" data-label="labCapacity">${data[i].labCapacity}</td>
                <td class="col col-8" data-label="Status">${data[i].Status}</td>
                </tr>`;

}});