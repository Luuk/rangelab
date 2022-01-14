$(document).ready(function () {

    if (localStorage.getItem("menuIsClosed") === null) {
        localStorage.setItem("menuIsClosed", 'false');
    } else {
        if (localStorage.getItem("menuIsClosed") === 'true') {
            $("#wrapper").addClass("toggled");
        } else {
            $("#wrapper").removeClass("toggled");
        }
    }

    $("#menu-toggle").click(function (e) {
        if (localStorage.getItem("menuIsClosed") === 'true') {
            localStorage.setItem("menuIsClosed", 'false');
        } else {
            localStorage.setItem("menuIsClosed", 'true');
        }

        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    var productsTable = $('#products-table').DataTable({
        "sDom": 'rt<"bottom"flp><"clear">',
    });

    $('#products-table').on('page.dt', function () {
        $(function () {
            $('[data-bs-toggle="popover"]').popover({
                placement: 'top',
                html: true,
                trigger: 'focus'
            })
        });
    });

    $('#products-table').on('search.dt', function () {
        $(function () {
            $('[data-bs-toggle="popover"]').popover({
                placement: 'top',
                html: true,
                trigger: 'focus'
            })
        });
    });

    var membersTable = $('#members-table').DataTable({
        "sDom": 'rt<"bottom"flp><"clear">'
    });

    $('#members-table').on('page.dt', function () {
        $(function () {
            $('[data-bs-toggle="popover"]').popover({
                placement: 'top',
                html: true,
                trigger: 'focus'
            })
        });
    });

    $('#members-table').on('search.dt', function () {
        $(function () {
            $('[data-bs-toggle="popover"]').popover({
                placement: 'top',
                html: true,
                trigger: 'focus'
            })
        });
    });

    $('#searchbox').on('keyup click', function () {
        membersTable.search($('#searchbox').val()).draw();
        productsTable.search($('#searchbox').val()).draw();
    });

    $(function () {
        $('[data-bs-toggle="popover"]').popover({
            placement: 'top',
            html: true,
            trigger: 'focus'
        })
    });
});

