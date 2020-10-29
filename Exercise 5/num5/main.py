def k_mer(dna_strings, kmer_counts):
    count = {}
    for x in range(len(dna_strings)-kmer_counts+1):
        for_kmer = dna_strings[x:x+kmer_counts]
        count.setdefault(for_kmer, 0)
        count[for_kmer] += 1
    return count

def main():
    dna_strings = input("Enter the DNA strings: ")
    kmer_counts = int(input("Enter the value of k: "))
    print(k_mer(dna_strings, kmer_counts))

main()

