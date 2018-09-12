import os

resourcesPath="../Resources/"

transformacionFile='baseTransformacion/TRANSFORMACION.xls'
soporteFile='baseSoporte/CERTIFICACIÓN.xlsx'

casosPruebaPath='Queries Qc/QC 12/'
defectosPath='Queries Qc/QC 12/DEFECTOS/'

defectosPath=os.path.join(resourcesPath,defectosPath)
casosPruebaPath=os.path.join(resourcesPath,casosPruebaPath)

defectosFiles=[]
casosPruebaFiles=[]

transformacionFilePath=os.path.join(resourcesPath,transformacionFile)
soporteFilePath=os.path.join(resourcesPath,soporteFile)


for file in os.listdir(defectosPath):
    if file.endswith(".xlsx"):
        defectosFiles.append(os.path.join(defectosPath, file))

for file in os.listdir(casosPruebaPath):
    if file.endswith(".xlsx"):
        casosPruebaFiles.append(os.path.join(casosPruebaPath, file))

