#!/usr/bin/env python3
import argparse, sys
from collections import Counter
from itertools import islice
from math import log2

def read_fastq_sequences(fq):
    with open(fq) as f:
        while (lines := list(islice(f,4))):
            if len(lines) < 2: continue
            yield lines[1].strip().upper()

def is_valid_dna(seq): return all(b in 'ATCG' for b in seq)

def shannon_entropy(seq):
    if not seq: return 0
    c = Counter(seq)
    l = len(seq)
    return -sum((v/l)*log2(v/l) for v in c.values())

def count_kmers(fq, k):
    counts = Counter()
    reads = 0
    for seq in read_fastq_sequences(fq):
        reads += 1
        if len(seq) < k: continue
        for i in range(len(seq)-k+1):
            kmer = seq[i:i+k]
            if is_valid_dna(kmer): counts[kmer]+=1
    print(f"Counted {len(counts)} unique {k}-mers from {reads} reads.")
    return counts

def filter_kmers_by_entropy(kmer_counts, min_e):
    filtered = {k:v for k,v in kmer_counts.items() if shannon_entropy(k)>=min_e}
    print(f"Filtered kmers by entropy >= {min_e}: {len(filtered)} remain out of {len(kmer_counts)}")
    return filtered

def find_best_extension(kmers, seq, k, forward=True):
    overlap = seq[-(k-1):] if forward else seq[:k-1]
    candidates = [(b, overlap+b) if forward else (b, b+overlap) for b in 'ACGT']
    valid = [(kmer, kmers[kmer]) for _, kmer in candidates if kmer in kmers]
    if not valid: return None
    return max(valid, key=lambda x:x[1])

def extend_contig(seed, kmers, k, min_e):
    contig, used, max_len = seed, {seed}, k*10
    prev_count = kmers[seed]

    for direction in [True, False]:  # forward, backward
        while len(contig) < max_len:
            ext = find_best_extension(kmers, contig, k, direction)
            if not ext: break
            kmer, count = ext
            if kmer in used or count < prev_count/2 or not is_valid_dna(kmer): break
            contig = contig + kmer[-1] if direction else kmer[0] + contig
            used.add(kmer)
            prev_count = count
        prev_count = kmers[seed]

    return (contig, used) if shannon_entropy(contig) >= min_e else (None, used)

def inchworm_assemble(kmers, k, min_e):
    contigs, used = [], set()
    sorted_kmers = sorted(kmers.items(), key=lambda x: x[1], reverse=True)
    print(f"Starting assembly with {len(sorted_kmers)} unique kmers ...")

    for kmer, count in sorted_kmers:
        if kmer in used or shannon_entropy(kmer) < min_e: continue
        contig, used_kmers = extend_contig(kmer, kmers, k, min_e)
        if contig is None: continue
        used.update(used_kmers)
        contigs.append((contig, len(contig), count))
        if len(contigs) % 10 == 0:
            print(f"  Built {len(contigs)} contigs so far ...")

    print(f"Assembly complete: {len(contigs)} contigs built.")
    return contigs

def main():
    p = argparse.ArgumentParser(description="Toy Inchworm assembler with entropy filtering and DNA-only contigs.")
    p.add_argument("fastq")
    p.add_argument("k", type=int)
    p.add_argument("--min_entropy", type=float, default=1.0)
    p.add_argument("--top", type=int, default=None)
    p.add_argument("--min_length", type=int, default=100)
    if len(sys.argv)==1:
        p.print_help()
        sys.exit(1)
    args = p.parse_args()

    kmers = count_kmers(args.fastq, args.k)
    if not kmers:
        print("No kmers counted. Check FASTQ or use smaller k.")
        sys.exit(1)

    kmers = filter_kmers_by_entropy(kmers, args.min_entropy)
    if args.top:
        kmers = dict(sorted(kmers.items(), key=lambda x: x[1], reverse=True)[:args.top])
        print(f"Using top {args.top} most abundant kmers.")

    contigs = inchworm_assemble(kmers, args.k, args.min_entropy)

    print("#contig_id\tlength\tseed_count\tsequence")
    filtered = [c for c in contigs if c[1]>=args.min_length]
    print(f"Outputting {len(filtered)} contigs with length >= {args.min_length}")

    for i,(seq,l,count) in enumerate(filtered,1):
        print(f"contig_{i}\t{l}\t{count}\t{seq}")

if __name__=="__main__":
    main()
