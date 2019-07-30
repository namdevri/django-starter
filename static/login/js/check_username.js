$(document).ready(function(){
	$('#id_email').change(function(){
		var email = $(this).val();
		$.get('/check_availability',
			{'email': email},
			function(response){
				if (response.msg == 'found'){
					$('.form-error').show();
					$('.form-error-msg').text("Email already has an associated account");
				} else{
					$('.form-error').hide();
				}
			}
	  );
	});
});
