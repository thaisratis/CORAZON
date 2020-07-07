$(document).ready(function(){
	
	var Result3 = document.getElementById("Result3");
	Result3.classList.add('index_footer');

	var botao = document.getElementById("logout");
        botao.onclick=function(){
                sessionStorage.user = "Guest";
                location.reload(true);
                stopLoader("loader_logout");

        }

        if((sessionStorage.user==undefined) || (sessionStorage.user=="Guest")){
                sessionStorage.setItem("user", "Guest");

                var Logado = document.getElementById("Logado");
                Logado.innerHTML="Log as " + sessionStorage.user;
        }
        else{
		Result3.classList.remove('index_footer');
		var Logado = document.getElementById("Logado");
                Logado.innerHTML="Log as " + sessionStorage.user;
                var formData = new FormData();
                formData.append("usuario", sessionStorage.user);

                var fileConn = new XMLHttpRequest();
                fileConn.onreadystatechange = function(){
                        if(fileConn.readyState == 4 && fileConn.status == 200){

                                var response = fileConn.responseText.trim();
				console.log(response)
				var data_obj = JSON.parse(response);
                                var Result = document.getElementById("Result");
                                var Result2 = document.getElementById("Result2");
				//Result3.classList.remove('index_footer');
				//var Result3 = document.getElementById("Result3");
                                Result.innerHTML = data_obj.jobtable;
                                Result2.innerHTML = data_obj.jobtable2;
                                Result3.innerHTML = data_obj.jobtable3;



                        }

                }
                console.log(formData);
                fileConn.open("POST", "atualizacao.py", "true");
                fileConn.send(formData);
        }

	 $("form#Guest").submit(function (e){
                e.preventDefault();
                var formData = new FormData();
                var Guest = document.getElementById("GuestJob").value;

                formData.append("GuestJob", Guest);
		
                var conn = new XMLHttpRequest();
                conn.onreadystatechange = function(){
                        if(conn.readyState == 4 && conn.status == 200){
                                var response = conn.responseText.trim();
                                var data_obj = JSON.parse(response);
                                var resposta = document.getElementById("GuestResult");
				var img1 = document.getElementById("GuestImg1");
				var img2 = document.getElementById("GuestImg2");
				var imgPCA = document.getElementById("GuestImgPCA")
                                resposta.innerHTML = data_obj.message;
				img1.innerHTML = data_obj.message2;
				img2.innerHTML = data_obj.message3;
				imgPCA.innerHTML = data_obj.message4;

                                stopLoader("loader_guestjob");
                        }
                }
                conn.open("POST","guest.py", true);
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
	

	 $("#Sub").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_guestjob");

        });
	

	 $("#logout").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_logout");
        });


})



