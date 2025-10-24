#!/usr/bin/env python3 

### Downloaded and unzip uniprot_sprot using Unix, commands below
# curl -OL ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
# gunzip uniprot_sprot.fasta.gz

### Added it to .gitignore

### Check how the file looks, commands below
# Has 4325736 lines (given by wc -l uniprot_sprot.fasta)
# Has 573661 records (given by grep ">" uniprot_sprot.fasta | wc -l)

### Imports
import Bio
from Bio import SeqIO

### Definition of variables
filename = ""

### Creation of blast
for record in SeqIO.parse(file, "fasta"):