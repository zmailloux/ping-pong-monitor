
function submitFeedback() {
    let body = document.getElementById("data").value;
    $.ajax({
        type: 'POST',
        contentType: 'text/plain',
        data: body,
        url: '/api/feedback',
        success: function (e) {
            console.log(e);
            alert('Feedback sent');
            location.reload();
        },
        error: function (error) {
            console.log(error);
            alert('Invalid');
        }
    });
}

// function refreshPage(userUpdating){
//     fetch('/api/check_update_page').then(response => response.json()).then(response => {
//         console.log(response.refresh_page)
//         console.log(userUpdating)
//         if (response.refresh_page && !userUpdating){
//             location = ''
//         }
//     })
// }
