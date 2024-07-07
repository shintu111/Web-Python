// Task 2: Leverage Bootstrap's JavaScript components like tabs and modals for enhancing the policy management interface. 

// script.js
$(document).ready(function() {
    // initialize bootstrap tabs
    $('#policy-tabs').tabs();

    // initialize bootstrap modal
    $('#policy-modal').modal({
        show: false
    });

    // handle policy list sorting
    $('#policy-list').tablesorter();
});

// Task 3: Utilize JavaScript to add features like policy sorting and displaying detailed views on the dashboard.

$(document).ready(function() {
    // render policy list
    $.ajax({
        url: 'api/policies',
        method: 'GET',
        success: function(data) {
            $.each(data, function(index, policy) {
                $('#policy-list').append(`
                    <tr>
                        <td>${policy.id}</td>
                        <td>${policy.policyholder}</td>
                        <td>${policy.type}</td>
                        <td>${policy.status}</td>
                    </tr>
                `);
            });
        }
    });

    // handle policy details modal
    $('#policy-list').on('click', 'tr', function() {
        var policyId = $(this).find('td:first').text()});
    });