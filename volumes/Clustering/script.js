$(document).ready(function(){
	var botao = document.getElementById("logout");
	botao.onclick=function(){
		sessionStorage.user = "Guest";
		location.reload(true);
		stopLoader("loader_logout");
		
	}

	if((sessionStorage.user==undefined) || (sessionStorage.user=="Guest")){
		sessionStorage.setItem("user", "Guest");

		var Logado = document.getElementById("Logado");
		Logado.innerHTML="Logged as " + sessionStorage.user;
	}
	else{
		var Logado = document.getElementById("Logado");
                Logado.innerHTML="Logged as " + sessionStorage.user;
		var formData = new FormData();
		formData.append("usuario", sessionStorage.user);

		var fileConn = new XMLHttpRequest();
                fileConn.onreadystatechange = function(){
                        if(fileConn.readyState == 4 && fileConn.status == 200){

                                var response = fileConn.responseText.trim();
                                var data_obj = JSON.parse(response);
                        }

                }
                console.log(formData);
                fileConn.open("POST", "atualizacao.py", "true");
                fileConn.send(formData);
	}

    $("form#form1").submit(function (e){
        e.preventDefault();

        var formData = new FormData();
        var fileFormInput1 = document.getElementById("arqDados").files[0];
                
		if(fileFormInput1 == null){
			alertify.alert("Select your file!");
			stopLoader("loader_meanshift");
		}

		var testcluster_all = document.getElementById("ca_true");
		var cluster_all_false = document.getElementById("ca_false");
		var discretized_points = document.getElementById("points_true");
		var disc_points_false = document.getElementById("points_false");
		var escolha = document.getElementById("escolha");
		var tmm = document.getElementById("tmm");
		var mrn = document.getElementById("mrn");
		var fpkm = document.getElementById("fpkm");
		var true_tpm = document.getElementById("true_tpm");
		var tpm = document.getElementById("tpm");
		var log = document.getElementById("log");
		var normalizacao = document.getElementById("normalizacao");
                var normalizacao2 = document.getElementById("normalizacao2");

		if (escolha.checked==true){
                        formData.append("escolha",1);
		}else{
			formData.append("escolha",0);
		}
		if (tmm.checked==true){
                        formData.append("tmm",1);
                }else{
                        formData.append("tmm",0);
                }

		if (mrn.checked==true){
                        formData.append("mrn",1);
                }else{
                        formData.append("mrn",0);
                }


		if (fpkm.checked==true){
                        formData.append("fpkm",1);
                }else{
                        formData.append("fpkm",0);
                }
		
		if(true_tpm.checked==true){
			formData.append("true_tpm",1);
		}
		else{
			formData.append("true_tpm",0);
		}

		if (tpm.checked==true){
			formData.append("tpm",1);

        	}else{
            		formData.append("tpm",0);
       		}
		if (log.checked==true){
            		formData.append("log",1);
        	}else{
            		formData.append("log",0);
        	}

		if (normalizacao.checked==true){
            		formData.append("normalizacao",1);
        	}else{
            		formData.append("normalizacao",0);
        	}
        	if (normalizacao2.checked==true){
			formData.append("normalizacao2",1);	
		}else{
            		formData.append("normalizacao2",0);
		}

		

		if (testcluster_all.checked==true){
			formData.append("testcluster_all",1);
		}
		else{
			formData.append("testcluster_all",0);
		}
		if (discretized_points.checked==true){
            		formData.append("discretized_points",1);
		}
        	else{
	        	formData.append("discretized_points",0);
	    	}


		var testbandwidth= document.getElementById("auto_bandwidth");
		if(testbandwidth.checked==true){
			formData.append("testbandwidth", true);
		}
		else{
			formData.append("testbandwidth", false);
		}

		var txt= document.getElementById("bandwidth_value").value;
		formData.append("txt", txt);


	        formData.append("file1", fileFormInput1);
		formData.append("user", sessionStorage.user);
		
                var fileConn = new XMLHttpRequest();
                fileConn.onreadystatechange = function(){
                        if(fileConn.readyState == 4 && fileConn.status == 200){

				var response = fileConn.responseText.trim();
				var data_obj = JSON.parse(response);
                                
				alertify.alert("Your ID is " + data_obj.id + "!<br><br>Use this ID to check the status of your analysis.");
					
				document.getElementById("arqDados").value = "";				
				document.getElementById("ca_true").checked = false;
				document.getElementById("ca_false").checked = false;
				document.getElementById("points_true").checked = false;
				document.getElementById("points_false").checked = false;
				document.getElementById("auto_bandwidth_off").checked = false;
				document.getElementById("auto_bandwidth").checked = false;
				document.getElementById("tmm").checked = false;
				document.getElementById("mrn").checked = false;
				document.getElementById("fpkm").checked = false;
				document.getElementById("true_tpm").checked = false;
				document.getElementById("tpm").checked = false;
				document.getElementById("log").checked = false;
				document.getElementById("normalizacao").checked = false;
				document.getElementById("normalizacao2").checked = false;
				document.getElementById("escolha").checked = false;
				document.getElementById("bandwidth_value").value = "";

				stopLoader("loader_meanshift");
				
                }

            }
                fileConn.open("POST", "file_upload.py", "true");
                fileConn.send(formData);
        


	var bandwidth = document.getElementById("bandwidth_value");
	bandwidth.disabled = true;

	var bandwidth_off = document.getElementById("auto_bandwidth_off");
	var bandwidth_on = document.getElementById("auto_bandwidth");

	bandwidth_off.onchange = function(){
	bandwidth.disabled = false;
	}
	
	bandwidth_on.onchange = function(){
	bandwidth.disabled = true;
	}
	
	})
	console.log(formData)

	$("form#kmeans").submit(function (e){

		e.preventDefault();
		var formData = new FormData();
		var fileFormInput1 = document.getElementById("valores").files[0];

		if(fileFormInput1 == null){
                        alertify.alert("Select your file!");
                        stopLoader("loader_kmeans");
        }

		
	        var num_cluster = document.getElementById("cluster").value;
		console.log(num_cluster)
		
		if(num_cluster == 0){
			alertify.alert("Select the number of clusters!");
			stopLoader("loader_kmeans");
		}
		
		var max_iter = document.getElementById("max_iter").value;
		var tmm2 = document.getElementById("tmm2");
		var mrn2 = document.getElementById("mrn2");
		var fpkm2 = document.getElementById("fpkm2");
		var true_tpm2 = document.getElementById("true_tpm2");
		var tpm2 = document.getElementById("tpm2");
	        var log2 = document.getElementById("log2");
        	var escolha2 = document.getElementById("escolha2");
		var normalizacao3 = document.getElementById("normalizacao3");
		var normalizacao4 = document.getElementById("normalizacao4");
		
		formData.append("cluster", num_cluster);
		formData.append("max_iter", max_iter);
	        formData.append("file1", fileFormInput1);
		formData.append("user", sessionStorage.user);
		
		if (escolha2.checked==true){
            		formData.append("escolha2",1);
       		}else{
            		formData.append("escolha2",0);
        	}
		if (tmm2.checked==true){
                        formData.append("tmm2",1);
                }else{
                        formData.append("tmm2",0);
		}

		if (mrn2.checked==true){
                        formData.append("mrn2",1);
                }else{
                        formData.append("mrn2",0);
                }


		if (fpkm2.checked==true){
                	formData.append("fpkm2",1);
                }else{
                        formData.append("fpkm2",0);
                }
		if (true_tpm2.checked==true){
			formData.append("true_tpm2",1);
		}
		else{
			formData.append("true_tpm2",0);
		}
		if (tpm2.checked==true){
            		formData.append("tpm2",1);
        	}else{
            		formData.append("tpm2",0);
        	}

		if (log2.checked==true){
            		formData.append("log2",1);
        	}else{
			formData.append("log2",0); 
		}

		if (normalizacao3.checked==true){
            		formData.append("normalizacao3",1);
        	}else{
            		formData.append("normalizacao3",0);
        	}
		if (normalizacao4.checked==true){
            		formData.append("normalizacao4",1);
        	}else{
            		formData.append("normalizacao4",0);
        	}

        var conn = new XMLHttpRequest();
        conn.onreadystatechange = function(){
            if(conn.readyState == 4 && conn.status == 200){
				
		var response = conn.responseText.trim();
                var data_obj = JSON.parse(response);
				
				if(num_cluster != ''){
					alertify.alert("Your ID is " + data_obj.id + "!<br><br>Use this ID to check the status of your analysis.");
			
					document.getElementById("valores").value = "";
					document.getElementById("tmm2").checked = false;
					document.getElementById("mrn2").checked = false;
					document.getElementById("fpkm2").checked = false;
					document.getElementById("true_tpm2").checked = false;
                			document.getElementById("tpm2").checked = false;
                 			document.getElementById("log2").checked = false;
                    			document.getElementById("normalizacao3").checked = false;
                    			document.getElementById("normalizacao4").checked = false;
                    			document.getElementById("escolha2").checked = false;
                    			document.getElementById("cluster").value = "";
					document.getElementById("max_iter").value = "300";

					stopLoader("loader_kmeans");
				}
				else{
					alertify.alert("Choose the number of clusters!");
		            		stopLoader("loader_kmeans");
				}
			}
		}
		conn.open("POST","file_upload_kmeans.py", true);
		conn.send(formData);
		
	})
	
	$("form#Hierarquico").submit(function (e){

		e.preventDefault();
		var formData = new FormData();
		var fileFormInput1 = document.getElementById("Arquivo").files[0];

		if(fileFormInput1 == null){
            		alertify.alert("Select your file!");
            		stopLoader("loader_Hierarchical");
        	}

		
        var numero_cluster = document.getElementById("cluster2").value;
	var link = document.getElementById("linkage");
	var linkage = link.options[link.selectedIndex].value;
	var tmm3 = document.getElementById("tmm3");
	var mrn3 = document.getElementById("mrn3");
	var fpkm3 = document.getElementById("fpkm3");
	var true_tpm3 = document.getElementById("true_tpm3");
	var tpm3 = document.getElementById("tpm3");
        var log3 = document.getElementById("log3");
        var escolha3 = document.getElementById("escolha3");
	var normalizacao5 = document.getElementById("normalizacao5");
	var normalizacao6 = document.getElementById("normalizacao6");
	console.log(true_tpm3);
	
	if(numero_cluster == 0){
		alertify.alert("Select the number of clusters!");
		stopLoader("loader_Hierarchical");
	}

	
	formData.append("cluster2", numero_cluster);
	formData.append("linkage", linkage);
        formData.append("file1", fileFormInput1);
	formData.append("user", sessionStorage.user);
		
		if (escolha3.checked==true){
           		 formData.append("escolha3",1);
         	}else{
            		formData.append("escolha3",0);
        	}
		if (tmm3.checked==true){
                        formData.append("tmm3",1);
                }else{
                        formData.append("tmm3",0);
                }

		if (mrn3.checked==true){
                        formData.append("mrn3",1);
                }else{
                        formData.append("mrn3",0);
                }

		 if (fpkm3.checked==true){
                        formData.append("fpkm3",1);
                }else{
                        formData.append("fpkm3",0);
                }
		if (true_tpm3.checked==true){
			formData.append("true_tpm3",1);
		}
		else{
			formData.append("true_tpm3",0);
		}


		if (tpm3.checked==true){
			formData.append("tpm3",1);
        	}else{
            		formData.append("tpm3",0);
        	}

		if (log3.checked==true){
            		formData.append("log3",1);
        	}else{
			formData.append("log3",0); 
		}

		if (normalizacao5.checked==true){
            		formData.append("normalizacao5",1);
        	}else{
            		formData.append("normalizacao5",0);
        	}
		if (normalizacao6.checked==true){
            		formData.append("normalizacao6",1);
        	}else{
            		formData.append("normalizacao6",0);
        	}
	console.log(formData);

        var conne = new XMLHttpRequest();
        conne.onreadystatechange = function(){
            if(conne.readyState == 4 && conne.status == 200){
				
		var response = conne.responseText.trim();
		//console.log(response)
                var data_obj = JSON.parse(response);
		
				
				if(numero_cluster != ''){
					alertify.alert("Your ID is " + data_obj.id + "!<br><br>Use this ID to check the status of your analysis.");
			
					document.getElementById("Arquivo").value = "";
					document.getElementById("tmm3").checked = false;
					document.getElementById("mrn3").checked = false;
					document.getElementById("fpkm3").checked = false;
					document.getElementById("true_tpm3").checked = false;
                			document.getElementById("tpm3").checked = false;
                    			document.getElementById("log3").checked = false;
                    			document.getElementById("normalizacao5").checked = false;
                    			document.getElementById("normalizacao6").checked = false;
                    			document.getElementById("escolha3").checked = false;
                    			document.getElementById("cluster2").value = "";
					document.getElementById("linkage").value = "Ward.D";

					stopLoader("loader_Hierarchical");
				}
				else{
					alertify.alert("Choose the number of clusters!");
				        stopLoader("loader_Hierarchical");
				}
			}
		}
		conne.open("POST","file_upload_hierarchical.py", true);
		conne.send(formData);
		
	})
	
	
	
	 function startLoader(id)
        {
                $("#"+id).show();
        }

        function stopLoader(id)
        {
                $("#"+id).hide();
        }
	
	$("#sub_btx").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_meanshift");
        });

	$("#runKmeans").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_kmeans");
        });
	
	$("#runHierarchical").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_Hierarchical");
        });

	$("#logout").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_logout");
        });




})
