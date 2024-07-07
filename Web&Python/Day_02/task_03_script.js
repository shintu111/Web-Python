// // Task 3: Utilize JavaScript to add features like policy sorting and displaying detailed views on the dashboard.

// $(document).ready(function() {
//     // render policy list
//     $.ajax({
//         url: 'api/policies',
//         method: 'GET',
//         success: function(data) {
//             $.each(data, function(index, policy) {
//                 $('#policy-list').append(`
//                     <tr>
//                         <td>${policy.id}</td>
//                         <td>${policy.policyholder}</td>
//                         <td>${policy.type}</td>
//                         <td>${policy.status}</td>
//                     </tr>
//                 `);
//             });
//         }
//     });

//     // handle policy details modal
//     $('#policy-list').on('click', 'tr', function() {
//         var policyId = $(this).find('td:first').text()});
//     });