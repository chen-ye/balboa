#downloads all fasta files from phagesDB 
#parses the list of phage names downloaded from phagesDB
#for each name, attempts to download once
#if the request is successful (status_code != 404), go on to the next name
#else, try other stuff (in progress)