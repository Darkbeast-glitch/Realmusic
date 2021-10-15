var $form = $('form#email-form'),
    url = 'https://script.google.com/macros/s/AKfycbydi5ie1jlCsAuJhqoXJtRu4-CB4MJLDuNDhGH26GeN-fNqp9f8_mXgCFehxSkSCDurzQ/exec'

$("input[type$='button']").on('click', function(e) {
    var x = document.forms["email-form"]["email"].value;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length) {
		e.preventDefault();
		modalError();
    }
	else {
		modal();
		  e.preventDefault();
		  var jqxhr = $.ajax({
			url: url,
			method: "GET",
			dataType: "json",
			data: $form.serializeObject()
		  }).success(
			// do something
		  );
		}
})
