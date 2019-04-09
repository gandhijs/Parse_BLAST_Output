import sys
import os
import csv

class parse_blast(object):
	""" Given a tab-delimited BLAST output file. The program parses and outputs a csv file with the query ID and number of subjects that aligned to it. 
	"""
	def __init__(self, infile):
		#BLAST File
		self.infile = infile
		#dict for storing alignments
		self.aln_dict = {}	

	def parse_aln(self):
		"""method that parses BLAST tabular format 6 and count number of subjects that matched to a query and output that to a csv file. Below is the order of contents for each value in the blast alignment"""	
		# 0. query
		# 1. subject
		# 2. percentage of identical matches
		# 3. alignment length
		# 4. number of mistmatch
		# 5. number of gap openings
		# 6. start of alignment in query
		# 7. end of alignment in query
		# 8. start of alignment in subject
		# 9. end of alignment in subject
		# 10. evalue
		# 11. bit score

	 	# open the input blast alignment file	
		with open(self.infile) as aln_file:
			# continue until the end of the file
			while True:
				# read the next line
				self.line = aln_file.readline() 
				# EOF
				if not self.line:
					break
				# remove white space
				self.line = self.line.strip()
				# split line based on tab
				self.info = self.line.split('\t')
				# assign variable neames to each value of the alignment
				query, subject, percent_id, aln_len, mismatch, gap_opening, q_aln_start, q_aln_end, s_aln_start, s_aln_end, evalue, bit_score = self.info[0], self.info[1], self.info[2], self.info[3], self.info[4], self.info[5], self.info[6], self.info[7], self.info[8], self.info[9], self.info[10], self.info[11]
				# store the alignment information in a dict
				if query not in self.aln_dict:
					# append the first query to the dict
					self.aln_dict[query] = []
					# append the first subject to the list 
					self.aln_dict[query].append(subject)
				else:			
					# append the remaining subjects to the list
					self.aln_dict[query].append(subject)
	def write_out(self):
		"""writes to an outfile (csv) the count of subjects that correspond to a query."""
		# gets the file extension 
		blast_file, blast_file_ext = os.path.splitext(self.infile)
		# writes the output to a csv file
		with open(blast_file+'.csv', mode='w') as out_file:
			# writer object that writes delimited by a ',' 
			blast_writer = csv.writer(out_file, delimiter=',')
			# each query and subject in the alignmment dict
			for q, s_list in self.aln_dict.items():
				# write the output of the counts a csv file
				blast_writer.writerow([q, len(s_list)])
	
# MAIN		
def main():
	
	try:
		# returns the basename of the blast alignment file
		blast_aln_file = (os.path.basename(sys.argv[1]))
	except:
		# no BLAST input file 
		quit("BLAST alignment file not detected!")
	a = parse_blast(blast_aln_file)
	a.parse_aln()
	a.write_out()

if __name__ == '__main__':
	main()

