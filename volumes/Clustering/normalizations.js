$(document).ready(function(){
	
	$("form#form_normalizations").submit(function(e){
                e.preventDefault();
                var formData = new FormData();
		var fileFormInput1 = document.getElementById("arq_Dados").files[0];

                if(fileFormInput1 == null){
                        alertify.alert("Select your file!");
                        stopLoader("loader_Normalization");
                }

                var tmm = document.getElementById("tmm_normalization");
		var mrn = document.getElementById("mrn_normalization");
		var fpkm = document.getElementById("fpkm_normalization");
                var true_tpm = document.getElementById("true_tpm_normalization");
                var tpm = document.getElementById("tpm_normalization");
                var log = document.getElementById("log_normalization");
                var normalizacao = document.getElementById("normalizacao_normalization");
                var normalizacao2 = document.getElementById("normalizacao2_normalization");

		if ((tmm.checked==false) && (mrn.checked==false) && (fpkm.checked==false) && (true_tpm.checked==false) && (tpm.checked==false) && (log.checked==false) && (normalizacao.checked==false) && (normalizacao2.checked==false)){
			alertify.alert("Select at least one normalization!");
			stopLoader("loader_Normalization");
		}

		if (tmm.checked==true){
                        formData.append("tmm_normalization",1);
                }else{
                        formData.append("tmm_normalization",0);
                }

		if (mrn.checked==true){
                        formData.append("mrn_normalization",1);
                }else{
                        formData.append("mrn_normalization",0);
                }


		if (fpkm.checked==true){
                        formData.append("fpkm_normalization",1);
                }else{
                        formData.append("fpkm_normalization",0);
                }

                if(true_tpm.checked==true){
                        formData.append("true_tpm_normalization",1);
                }
                else{
                        formData.append("true_tpm_normalization",0);
                }

                if (tpm.checked==true){
                        formData.append("tpm_normalization",1);

                }else{
                        formData.append("tpm_normalization",0);
                }

                if (log.checked==true){
                        formData.append("log_normalization",1);
                }else{
                        formData.append("log_normalization",0);
                }

                if (normalizacao.checked==true){
                        formData.append("normalizacao_normalization",1);
                }else{
                        formData.append("normalizacao_normalization",0);
                }

                if (normalizacao2.checked==true){
                        formData.append("normalizacao2_normalization",1);
                }else{
                        formData.append("normalizacao2_normalization",0);
                }

		formData.append("file1", fileFormInput1);

		
                var conn = new XMLHttpRequest();
                conn.onreadystatechange = function(){
                        if(conn.readyState == 4 && conn.status == 200){

                                var response = conn.responseText.trim();
                                var data_obj = JSON.parse(response);
					
				alertify.alert("Your ID is " + data_obj.id + "!<br><br>Use this ID to check the status of your analysis.");
				
				document.getElementById("tmm_normalization").checked = false;		
				document.getElementById("mrn_normalization").checked = false;
				document.getElementById("fpkm_normalization").checked = false;
                                document.getElementById("true_tpm_normalization").checked = false;
                                document.getElementById("tpm_normalization").checked = false;
                                document.getElementById("log_normalization").checked = false;
                                document.getElementById("normalizacao_normalization").checked = false;
                                document.getElementById("normalizacao2_normalization").checked = false;

				 stopLoader("loader_Normalization");


                        }
                }
                conn.open("POST","file_upload_normalization.py", true);
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

	$("#runNormalization").click(function() {
                let _class = $(this).attr("action");
                console.log("starting loader...");
                startLoader("loader_Normalization");
        });

	

})
