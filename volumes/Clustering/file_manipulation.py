import math
import pandas as pd

def filemanipulation(file, ids, cabecalho):

	arquivo = open(file, 'r')
	arquivosaida = open(file + "_saida", 'w')
	linhas = arquivo.readlines()
	
	for l in (linhas[0].strip().split('\t')):
		cabecalho.append(l.replace(" ", "_"))
	
	for line in range(1, len(linhas)):
		arquivo_split = linhas[line].split('\t')
		ids.append(arquivo_split[0])
		s = ""
		for i in range(1, len(arquivo_split)):
			s+= arquivo_split[i].strip()
			if(i != len (arquivo_split)-1):
				s+=';'
		
		arquivosaida.write(s + '\n')
	
	arquivo.close()
	arquivosaida.close()
	return arquivosaida
#	print (ids)
#	print(cabecalho)



def FPKM(arquivosaida, ids, cabecalho):

	arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()

	iniciador = linhas[0].strip().split(';')

	soma = [0]* (len(iniciador))
	
	contador =0
	
	for line in (linhas):
		linha = line.strip().split(';')
		for x in range (0,len(linha)):
			soma[x] += float(linha[x])
	var2 = []
	for line in (linhas):
		linha = line.strip().split(';')
		var = []

		for x in range (1,len(linha)):
			var.append(str((  (float(linha[x]))  / (float(linha[0])*float(soma[x]))  ) * 1000000000))
			join = ';'.join(var)


		var2.append(join)
	join2 = '\n'.join(var2)
	arquivo.close()
	arquivo2 = open(arquivosaida + "_FPKM", 'w')
	arquivo2.write(join2)
	arquivo2.close()

	table = ''
	arquivouser1 = open(arquivosaida + "_FPKM", 'r')
	arquivouser2 = open(arquivosaida + "_FPKM_user", 'w')

	for x in range(0,len(cabecalho)-1):
			if(x != 1):
				table += cabecalho[x] + "\t"
	arquivouser2.writelines(table + cabecalho[-1] + "\n")
	linhas3 = arquivouser1.readlines()
	i = 0
	for line3 in (linhas3):
			tabulacao = line3.replace(";", "\t")
			arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
			i = i+1
	arquivouser1.close()
	arquivouser2.close()

	return (arquivosaida+"_FPKM")



def TPM(arquivosaida, ids, cabecalho):

	arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()
                
	iniciador = linhas[0].strip().split(';')
        
	soma = [0]* (len(iniciador))
        
	contador =0
	tpm = [[0]*(len(iniciador)) for i in range(len(linhas))]
        
	for line in (linhas):
		linha = line.strip().split(';')
		for x in range (0,len(linha)):
 			soma[x] += float(linha[x])
	var2 = []
	for line in (linhas):
		linha = line.strip().split(';')
		var = []
            
		for x in range (0,len(linha)):
 			var.append(str((float(linha[x])/float(soma[x])) * 1000000))
 			join = ';'.join(var)

		var2.append(join)
	join2 = '\n'.join(var2)    
	arquivo.close()
	arquivo2 = open(arquivosaida + "_TPM", 'w')
	arquivo2.write(join2)
	arquivo2.close()
	
	table = ''
	arquivouser1 = open(arquivosaida + "_TPM", 'r')
	arquivouser2 = open(arquivosaida + "_TPM_user", 'w')
	
	for x in range(0,len(cabecalho)-1):
		table += cabecalho[x] + "\t"
	arquivouser2.writelines(table + cabecalho[-1] + "\n")
	linhas3 = arquivouser1.readlines()
	i = 0
	for line3 in (linhas3):
		tabulacao = line3.replace(";", "\t")
		arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
		i = i+1
	arquivouser1.close()
	arquivouser2.close()
	
	return (arquivosaida+"_TPM")

def LOG(arquivosaida, ids, cabecalho):

	arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()
	var2 = []
	for line in linhas:
		var = []
		linha = line.strip().split(';')
		
		for x in range(0,len(linha)):
			if(float(linha[x]) == 0):
				linha[x] = 0.000001
			if(float(linha[x]) ==1):
				linha[x] = 1.000001
			logg = math.log(float(linha[x]),2)
			logg2= str(logg)
			var.append(logg2)
		
		join = ";".join(var)
		var2.append(join)
		
		
	join2 = '\n'.join(var2)
	arquivo.close()
	arquivo2 = open(arquivosaida + "_LOG", 'w')
	arquivo2.write(join2)
	arquivo2.close()

	table = ''
	arquivouser1 = open(arquivosaida + "_LOG", 'r')
	arquivouser2 = open(arquivosaida + "_LOG_user", 'w')

	for x in range(0,len(cabecalho)-1):
		table += cabecalho[x] + "\t"
	arquivouser2.writelines(table +  cabecalho[-1] + "\n")
	linhas3 = arquivouser1.readlines()
	i = 0
	for line3 in (linhas3):
		tabulacao = line3.replace(";", "\t")
		arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
		i = i+1

	arquivouser1.close()
	arquivouser2.close()

	return (arquivosaida + "_LOG")

def NORMALIZACAO(arquivosaida, ids, cabecalho):
	#print('entrou')
	arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()
	soma = [0]* (len(linhas))
	
	i = 0
	for line in (linhas):
		linha = line.strip().split(';')
		for x in range (0,len(linha)):
			soma[i] += float(linha[x])
		i+=1
	var2 = []
	i = 0
	
	for line in (linhas):
		linha = line.strip().split(';')
		var = []
 
		for x in range (0,len(linha)):
			var.append(str(float(linha[x])/(float(soma[i]))))
			join = ';'.join(var)
		i+=1
                
		var2.append(join)
	join2 = '\n'.join(var2)
	arquivo.close()
	arquivo2 = open(arquivosaida + "_normalizacao", 'w')
	arquivo2.write(join2)
	arquivo2.close()
	
	table = ''
	arquivouser1 = open(arquivosaida + "_normalizacao", 'r')
	arquivouser2 = open(arquivosaida + "_normalizacao_user", 'w')
	
	for x in range(0,len(cabecalho)-1):
		table += cabecalho[x] + "\t"
	arquivouser2.writelines(table +  cabecalho[-1] + "\n")
	linhas3 = arquivouser1.readlines()
	i = 0
	for line3 in (linhas3):
		tabulacao = line3.replace(";", "\t")
		arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
		i = i+1

	arquivouser1.close()
	arquivouser2.close()

	return (arquivosaida + "_normalizacao")

def NORMALIZACAO2(arquivosaida, ids, cabecalho):
	#print('entrou2')
	arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()
	maior = [0]* (len(linhas))
	i = 0

	for line in (linhas):
		linha = line.strip().split(';')
		for x in range (0,len(linha)):
			if (float(linha[x]) > (float(maior[i]))):
				maior[i] = float(linha[x])
			
		i+=1    
	var2 = []
	i = 0
	
	for line in (linhas):
		linha = line.strip().split(';')
		var = []
 
		for x in range (0,len(linha)):
			var.append(str(float(linha[x])/(float(maior[i]))*100))
			join = ';'.join(var)
		i+=1
                
		var2.append(join)
	join2 = '\n'.join(var2)
	arquivo.close()
	arquivo2 = open(arquivosaida + "_normalizacao2" , 'w')
	arquivo2.write(join2)
	arquivo2.close()
	
	table = ''
	arquivouser1 = open(arquivosaida + "_normalizacao2", 'r')
	arquivouser2 = open(arquivosaida + "_normalizacao2_user", 'w')

	for x in range(0,len(cabecalho)-1):
		table += cabecalho[x] + "\t"
	arquivouser2.writelines(table +  cabecalho[-1] + "\n")
	linhas3 = arquivouser1.readlines()
	i = 0
	for line3 in (linhas3):
		tabulacao = line3.replace(";", "\t")
		arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
		i = i+1

	arquivouser1.close()
	arquivouser2.close()

	return (arquivosaida + "_normalizacao2")

import numpy as np
from sys import stderr
from scipy.stats import rankdata

def percentile(matrix, p, saving_memory=False):
    """
    Estimation of percentile for each column without zero-rows.
    
    Parameters
    ----------
    matrix : array_like
        Matrix to calculate percentile.
    p : float in range of [0,100]
        Percentile to compute, must be between 0 and 100 inclusive.
    saving_memory : bool
        Parameter for activation of RAM saving mode. This may take longer.
        
    Returns
    -------
    array_like
        Calculated percentile for each column.
    """
    if saving_memory:
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
        mask = [np.any(r > 0) for r in matrix] 
        return np.array([np.percentile(c[mask], p) for c in matrix.T])
    
    return np.percentile(matrix[np.any(matrix > 0, axis=1)], p, axis=0)


def tmm_norm(matrix, index_ref=None, trim_fold_change=0.3, trim_abs_expr=0.05, saving_memory=False):
    """
    Trimmed mean of M-values normalization
    
    Parameters
    ----------
    matrix : array_like
        Matrix to normalize.
    index_ref:
        Index of reference column.
    trim_fold_change:
        Percent of trimmed for folder change.
    trim_abs_expr:
        Percent of trimmed for absolute expression.
    saving_memory : bool
        Parameter for activation of RAM saving mode. This may take longer.
        
    Returns
    -------
    array_like
        Normalized matrix.
    """
    matrix_np = np.array(matrix)                      # better speed of calculating
    np.seterr(divide='ignore', invalid='ignore')      # for divide on zeros in log2
    
    # Calculation log2(tmm_factor)
    def log2_tmm(index_vec):
        # select the necessary vectors
        curr_vec = matrix_np[:, index_vec]
        ref_vec = matrix_np[:, index_ref]
        
        # total number molecules in cells
        total_curr_vec = np.sum(curr_vec)
        total_ref_vec = np.sum(ref_vec)
        
        # select significant genes
        check_inf = (~np.isinf(matr_a[:, index_vec])) & (~np.isinf(matr_m[:, index_vec]))
        ranks = rankdata(matr_a[:, index_vec][check_inf], method='ordinal')
        bool_a = (ranks > len(ranks) * trim_abs_expr) & (ranks < len(ranks) * (1 - trim_abs_expr))
        ranks = rankdata(matr_m[:, index_vec][check_inf], method='ordinal')
        bool_m = (ranks > len(ranks) * trim_fold_change) & (ranks < len(ranks) * (1 - trim_fold_change))
        curr_vec = curr_vec[check_inf]
        ref_vec = ref_vec[check_inf]
        bool_curr_vec = curr_vec > 0
        bool_ref = ref_vec > 0
        bool_result = bool_curr_vec & bool_ref & bool_a & bool_m
        
        # calculation of required values
        w_vec = 1 / ((total_curr_vec - curr_vec[bool_result]) / (total_curr_vec * curr_vec[bool_result]) + 
                     (total_ref_vec - ref_vec[bool_result]) / (total_ref_vec * ref_vec[bool_result]))
        m_vec = np.log2(curr_vec[bool_result] / total_curr_vec) - np.log2(ref_vec[bool_result] / total_ref_vec)
        
        # calculation log2(tmm_factor)
        w_sum = np.sum(w_vec)
        if np.isclose(w_sum, 0) or np.isinf(w_sum):
            #print("Unexpected sum of weights for vector {}: '{}'".format(index_vec, w_sum), file=stderr)
            return 0
        
        return np.sum(w_vec * m_vec) / w_sum
        
    # find index of reference column
    f75 = percentile(matrix_np, 75, saving_memory)
    if index_ref is None:
        index_ref = np.argmin(abs(f75 - np.mean(f75)))
    elif not isinstance(index_ref, int) and isinstance(matrix, pd.DataFrame):
        index_ref = np.where(matrix.columns.values == (index_ref))[0][0]
    
    # find matrix A and M described expression levels of genes
    matr_norm = matrix_np / np.sum(matrix_np, axis=0)
    matr_a = np.log2(matr_norm * matr_norm[:, index_ref].reshape(matr_norm.shape[0], 1)) / 2
    matr_m = np.log2(matr_norm / matr_norm[:, index_ref].reshape(matr_norm.shape[0], 1))
    
    # calculation tmm_factor and normalization of input data
    tmm_factor = 2 ** np.array([log2_tmm(i) for i in range(matrix_np.shape[1])])
    return matrix / tmm_factor




def file_tmm_user(arquivosaida, ids, cabecalho):

	table = ''
	arquivouser1 = open(arquivosaida, 'r')
	arquivouser2 = open(arquivosaida + "_user", 'w')
	
	for x in range(0,len(cabecalho)-1):
		table += cabecalho[x] + "\t"
	arquivouser2.writelines(table + cabecalho[-1] + "\n")
	linhas3 = arquivouser1.readlines()
	i = 0
	for line3 in (linhas3):
		tabulacao = line3.replace(";", "\t")
		arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
		i = i+1
	arquivouser1.close()
	arquivouser2.close()
	
	return (arquivosaida+"_TMM")



def file_mrn_user(arquivo1,arquivo2, ids, cabecalho):

		table = ''
		arquivouser1 = open(arquivo1, 'r')
		arquivouser2 = open(arquivo2, 'w')

		for x in range(0,len(cabecalho)-1):
			table += cabecalho[x] + "\t"
		arquivouser2.writelines(table +  cabecalho[-1] + "\n")
		linhas3 = arquivouser1.readlines()
		i = 0
		for line3 in (linhas3):
			tabulacao = line3.replace(";", "\t")
			arquivouser2.writelines(str(ids[i])+ "\t" + tabulacao)
			i = i+1

		arquivouser1.close()
		arquivouser2.close()

def mrn_norm(arq, ids, cabecalho):

	#Primeira parte

	arquivo = open(arq, 'r')
	#arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()
	pseudo = 1
	var = []
	for line in linhas:
		
		pseudo = 1
		linha = line.strip().split(';')
		
		for x in range(0,len(linha)):
			pseudo *= float(linha[x])
			#print(pseudo)
		
		sqrt1 = math.sqrt(pseudo)
		var.append(sqrt1)
	#print(var)
	arquivo.close()

	#Segunda parte

	arquivo = open(arq, 'r')
	#arquivo = open(arquivosaida,'r')
	linhas = arquivo.readlines()
	var2 = []
	row = []

	for (line, sqr_pseudo) in zip(linhas, var): 
		linha = line.strip().split(';')
		
		elements = []
		
		for x in range(0,len(linha)):
			if(float(sqr_pseudo) == 0):
                                sqr_pseudo = 0.000001
			ratio = float(linha[x])/sqr_pseudo
			elements.append(str(ratio))

		join = ";".join(elements)
		row.append(join)
	
	join2 = '\n'.join(row)
	#print(join2)
	
	arquivo.close()
	arquivosaida = open(arq + "_secondpart", 'w')
	arquivosaida.write(join2)
	arquivosaida.close()

	arquivo1 = arq + "_secondpart"
	arquivo2 = arq + "_secondpart_user"

	file_mrn_user(arquivo1,arquivo2,ids,cabecalho)

	
	#Terceira parte

	matrix = pd.read_table(arq + '_secondpart_user', sep='\t')
	matrix.index = matrix.iloc[:,0]
	df = matrix.drop(matrix.columns[0], axis=1)
	median_dataframe = df.median()
	median_dataframe.to_csv(arq + "thirdpart.txt",sep='\t', header = False, index = False)

	#Quarta parte

	arquivo = open(arq + "_secondpart", 'r')
	arq_mediana = open(arq + "thirdpart.txt", 'r')
	teste = []
	counts = []
	list_of_count = []

	for l in arq_mediana:
		teste.append(l[:-1])
	

	for line in arquivo:
		linha = line.strip().split(';')
		counts = []
		
		for x in range (0,len(linha)):
			if(float(teste[x]) == 0):
				teste[x] = 0.000001
			final_count = float(linha[x])/float(teste[x])
			counts.append(str(final_count))

		join = ";".join(counts)
		list_of_count.append(join)

	join2 = '\n'.join(list_of_count)
	#print(join2)
	
	arquivo.close()
	arquivosaida = open(arq + "_MRN", 'w')
	arquivosaida.write(join2)
	arquivosaida.close()
	
	arquivo1 = arq + "_MRN"
	arquivo2 = arq + "_MRN_user"
	
	file_mrn_user(arquivo1,arquivo2,ids,cabecalho)

	return(arquivo1)


