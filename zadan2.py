import csv
import io


with io.open('the_matrix.txt', 'w') as csvfile:
    writer = csv.writer(csvfile)
    columns = ['сокращение', 'русский', 'якутский']
   
   

   
