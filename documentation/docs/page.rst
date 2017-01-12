**Text Processing Functions for Small or Big Data Files in Python**
===================================================================

Description
-----------

The advantage of the package lies in its ability to process big text data files in batches efficiently. For this purpose, it offers functions for splitting, parsing, tokenizing and creating a vocabulary. Moreover, it includes functions for building either a document-term matrix or a term-document matrix and extracting information from those (term-associations, most frequent terms). Lastly, it embodies functions for calculating token statistics (collocations, look-up tables, string dissimilarities) and functions to work with sparse matrices. The source code is based on C++11 and wrapped in Python using Cython.


classes
--------

The following classes and methods are included in the textTinyPy:


* **big_text_files**: 

	* big_text_splitter()
	* big_text_parser()
	* big_text_tokenizer()
	* vocabulary_accumulator()

* **docs_matrix**: 

	* Term_Matrix()
	* document_term_matrix()
	* term_document_matrix()
	* corpus_terms()
	* Sparsity()
	* Term_Matrix_Adjust()
	* most_frequent_terms()
	* term_associations()

* **token_stats**: 

	* path_2vector()
	* freq_distribution()
	* count_character()
	* print_count_character()
	* collocation_words()
	* tks.print_collocations()
	* string_dissimilarity_matrix()
	* look_up_table()
	* print_words_lookup_tbl()

* **tokenizer**: 

	* transform_text()
	* transform_vec_docs()

* **utils**: 

	* vocabulary_parser()
	* utf_locale()
	* bytes_converter()
	* text_file_parser()
	* dice_distance()
	* levenshtein_distance()
	* cosine_distance()
	* read_characters()
	* read_rows()
	* xml_parser_subroot_elements()
	* xml_parser_root_elements()










