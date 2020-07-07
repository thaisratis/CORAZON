$(document).ready(function(){
	
	$("form#Login2").submit(function(e){
                e.preventDefault();
                var formData = new FormData();
                var login = document.getElementById("Usuario").value;
                var Senha = document.getElementById("SenhaLogin").value;
		formData.append("Usuario", login);
                formData.append("SenhaLogin", Senha);
                var conn = new XMLHttpRequest();
                conn.onreadystatechange = function(){
                        if(conn.readyState == 4 && conn.status == 200){

                                var response = conn.responseText.trim();
                                var data_obj = JSON.parse(response);

                                if(data_obj.message == "Login successful"){
					

                                        alertify.alert("Login Successful!");
					stopLoader("loader_login")
					document.getElementById("Usuario").value = '';
					document.getElementById("SenhaLogin").value= '';
					$("#myModallogin .close").click();
                                        sessionStorage.setItem("user", data_obj.username);
                                        var Logado = document.getElementById("Logado");
                                        Logado.innerHTML="Logged as " + sessionStorage.user;
					
                                        var Result = document.getElementById("Result");
                                        var Result2 = document.getElementById("Result2");
                                        var Result3 = document.getElementById("Result3");
					Result3.classList.remove('index_footer');
                                        Result.innerHTML = data_obj.jobtable;
                                        Result2.innerHTML = data_obj.jobtable2;
                                        Result3.innerHTML = data_obj.jobtable3;
					window.reload(true);

                                }
	                        else{
	                                alertify.alert("Incorrect username or password!");
					stopLoader("loader_login")
					document.getElementById("SenhaLogin").value= '';

                                }
                        }
                }
                conn.open("POST","authenticate.py", true);
                conn.send(formData);

        })

	 function startLoader(id)
        {
                $("#"+id).show();
        }

        function stopLoader(id)
        {
                $("#"+id).hide();
        }
        $(".submissao_login").click(function() {
                let _class = $(this).attr('class');
                console.log("starting loader...");
                startLoader("loader_login");
        });
	

})
