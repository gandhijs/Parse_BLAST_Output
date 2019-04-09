for OUT_FILE in *.out
do
	python3 parse_blast_output.py $(basename ${OUT_FILE})
done

mkdir "blast_aln_count"
mv *.csv > /gpfs_fs/home/shnakes/blast_alignments/blast_aln_count

echo done!
