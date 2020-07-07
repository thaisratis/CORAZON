$(document).ready(function(){
	console.log("entrou1")
	$("form#Registration").submit(function(e){
		e.preventDefault();

//		console.log("Entrou");
		var Nome = document.getElementById("Login").value;
		var Senha = document.getElementById("Senha").value;
		var Senha2 = document.getElementById("Senha2").value;


		if(Senha == Senha2){
			var formData = new FormData();
			formData.append("Login", Nome);
			formData.append("Senha", Senha);
			
			var conn = new XMLHttpRequest();
			conn.onreadystatechange = function(){
				if(conn.readyState == 4 && conn.status == 200){
					
					alertify.alert(conn.responseText + "!");
                                        stopLoader("loader_submissao");
					document.getElementById("Login").value= '';
					document.getElementById("Senha").value= '';
					document.getElementById("Senha2").value= '';
										
					if(conn.responseText == 'New user created successfully'){
						 $("#myModalsignup .close").click();
					}

				}

			}
			conn.open("POST", "make_usr.py", true);
			conn.send(formData);

	}
		else{
			alertify.alert("Passwords do not match!");
                	stopLoader("loader_submissao");
			document.getElementById("Senha").value= '';
			document.getElementById("Senha2").value= '';

		}

	})


	
	function startLoader(id)
	{
		$("#"+id).show();
	}
	
	function stopLoader(id)
        {
                $("#"+id).hide();
        }
	$(".submissao_signup").click(function() {
		let _class = $(this).attr('class');
    		console.log("starting loader...");
 	   	startLoader("loader_submissao");
	});

})
