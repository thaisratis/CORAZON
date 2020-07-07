def Remove_Files(user,id):

	import os
	import shutil

	remove_files = '/var/www/html/users/' + str(user) + "/" + str(id) + '/'

	for x in os.listdir(remove_files):
		if( (user == 'Guest') ):
			if( ('result' not in (str(x))) and ( 'Resultados' not in (str(x)) ) and ('boxplot' not in str(x)) and ('Clustering' not in str(x)) and ('tmm' not in str(x))):
				os.remove(str(remove_files) + str(x))

		else:
			if ( ('user' not in (str(x)) ) and ( 'result' not in (str(x)) ) and ( 'Resultados' not in (str(x)) ) and ('boxplot' not in str(x)) and ('Clustering' not in str(x)) and ('tmm' not in str(x))):
				os.remove(str(remove_files) + str(x))

	remove_results_files = '/var/www/html/users/' + str(user) + "/" + str(id) + '/Resultados'
	if( (os.path.exists(remove_results_files)) == True ):
		shutil.rmtree(remove_results_files)


