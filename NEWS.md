
## textTinyPy 0.0.4

I modified the *OpenMP* clauses of the .cpp files to address the ASAN errors.
I added the *triplet_data()* method in the *docs_matrix* class


## textTinyPy 0.0.3

I removed the *ngram_sequential* and *ngram_overlap* stemmers from the *Term_Matrix*, *transform_vec_docs* and *vocabulary_parser* methods of the corresponding *tokenizer*, *docs_matrix* and *utils* classes. I overlooked the fact that the n-gram stemming is based on the whole corpus and not on each vector of the document(s), which is the case for the *Term_Matrix*, *transform_vec_docs* and *vocabulary_parser* methods. 
I also updated the package documentation.
I modified the *secondary_n_grams* of the *tokenization.cpp* source file due to a bug.


## textTinyPy 0.0.2


I modified the *adj_Sparsity()* function of the *term_matrix.cpp* file to avoid UBSAN-memory errors (the errors happen if any of *all_indices*, *adj_col_indices* is an empty std::vector)


## textTinyPy 0.0.1

