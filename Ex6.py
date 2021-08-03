# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

arquivo = pd.read_csv("https://drive.google.com/open?id=1W6b-E1FWL5gImlf2sFASuCNEGriMygCJ", sep=';')

del arquivo['Cod_Municipio']

cod_Ano = pd.Categorical(arquivo["Ano_Inicio_Curso"], ordered=True)


T_int = np.where(arquivo["Qtd_Transf_Interna"].isnull(), 0, arquivo["Qtd_Transf_Interna"])
T_ext = np.where(arquivo["Qtd_Transf_Externa"].isnull(), 0, arquivo["Qtd_Transf_Externa"])
arquivo["Qtd_Transf_Interna"] = T_int
arquivo["Qtd_Transf_Externa"] = T_ext

arquivo["Total_transferencia"] = arquivo["Qtd_Transf_Interna"] + arquivo["Qtd_Transf_Externa"]
del arquivo["Qtd_Transf_Interna"]
del arquivo["Qtd_Transf_Externa"]

print(arquivo)