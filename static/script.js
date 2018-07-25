$(document).ready(function(){
  $("#occassion1").click(function(){
    $(".leakGroup").prop('checked', false);
    $("#occassion8").prop('checked', false);
  });
  $(".leakGroup").click(function(){
    $("#occassion1").prop('checked', false);
  });
  $("#occassion8").click(function(){
    if (this.checked){
      $("#occassion1").prop('checked', false);
      $(".leakGroup").prop('checked', true);
    };
  });
  $("#iciqui").change(function(){
    var score = 0
    $("#iciqui div input:checked").each(function(){
      score += parseInt(this.value);
    });
    score += parseInt($("#leakRange").prop('value'));
    $("#score").html(score);
  })
});
