$(document).ready(function(){
	wow = new WOW(
      {
        animateClass: 'animated',
        offset:       100,
        callback:     function(box) {
          console.log("WOW: animating <" + box.tagName.toLowerCase() + ">")
        }
      }
    );
    wow.init();


});



/*Calculator*/


$(function(){

	calc();

	$('#calc_plan').on('change', calc);
	$('#inv_amount').bind('change keyup', calc).on('keypress', isNumberKey);

});

function isNumberKey(evt) {
	var charCode = (evt.which) ? evt.which : event.keyCode;
	if (charCode > 31 && (charCode < 48 || charCode > 57))
		return false;
	return true;
}

function calc() {

	var plan = $('#calc_plan').val();
	var amount = $('#inv_amount').val();
	var percent;

	switch (plan) {
		case '1':
			switch (true) {
				case (amount<=10):
					percent = 100;
					break;
					case (amount<=1999):
						percent = 150;
						break;
					case (amount>1999):
						percent = 100;
						break;	
				
				default:
					percent = 150;
			}
			break;
		case '2':
			switch (true) {
				case (amount<=1999):
					percent = 100;
					break;
				case (amount<=9999):
					percent = 165;
					break;
				case (amount>9999):
					percent = 100;
					break;	
				
				default:
					percent = 165;
			}
			break;
		case '3':
			switch (true) {
				case (amount<=9999):
					percent = 100;
					break;
				case (amount<=50000):
					percent = 180;
					break;
				
				default:
					percent = 180;
			}
			break;
		
		

	}

	$('#assign_per').val(percent+'%');
	var total = amount*percent/100;
	$('#total_return').val('$'+total);
	$('#net_profit').val('$'+(total-amount).toFixed(2));

}
