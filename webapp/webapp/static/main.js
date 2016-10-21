var data = [];
$("#results-table").hide();

$(function(){
    $('#timestamp').combodate({
          minYear: 2016,
          maxYear: moment().format('YYYY')
    });
});

$(function() {
    //
    console.log("ready!");
    $("#GoButton").click(function() {
        $("#results").empty();
        $("#results-table").hide();
        $("#results-table").show();
        console.log("pressed!");
        $.ajax({
            type: "POST",
            url: "/evaluations/search_best_models",
            data: $("form").serialize(),
            success: function(result) {
                console.log("load data!");
                console.log(result.results);
                var data = result.results;
                // show table
                $("#results-table").show();
                console.log(data.length);
                // loop through results, append to dom
                for (i = 0; i < data.length; i++) {
                    $("#results").append('<tr><th>'+(i+1)
                                          +'</th><td><a href="'+'/evaluations/individual">'
                                          +data[i]['run_time']+'</a></td><td>'
                                          +data[i]['model_type']+'</td><td>'
                                          +data[i]['metric']+'</td><td>'
                                          +data[i]['parameter']+'</td><td>'
                                          +data[i]['value'].toPrecision(4)+'</tr>')
                };
            }
        });
        });
    });

