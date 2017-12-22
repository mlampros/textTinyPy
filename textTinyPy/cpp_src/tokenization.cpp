
/**
 * Copyright (C) 2016 Lampros Mouselimis
 *
 * @file tokenization.cpp
 *
 * @author Lampros Mouselimis
 *
 * @date October - December 2016
 *
 * @Notes: the main class for tokenization and transformation of text files
 *
 * @last_modified: December 2017
 *
 **/



#include <boost/range/algorithm_ext/erase.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/locale.hpp>
#include <dirent.h>
#include <armadillo>

#include "porter2_stemmer.h"
#include "token_stats.h"
#include "tokenization.h"



// read either a file or a character string into c++
//

void TOKEN::read_file(std::string read_file_delimiter, bool FLAG_path) {

  if (FLAG_path) {

    char c_delimiter[1];

    c_delimiter[0] = read_file_delimiter[0];

    std::ifstream myfile(x);

    std::string line;

    std::vector<std::string> tmp_v;

    while (std::getline(myfile, line, c_delimiter[0])) {                      // file split in chunks  using the tab-delimiter

      tmp_v.push_back(line);
    }

    v = tmp_v;

    tmp_v.shrink_to_fit();
  }

  else {

    v.resize(1);

    v[0] = x;

    x.shrink_to_fit();
  }
}


// secondary function in case of conversion to lower or upper case if language is not english
//

std::string TOKEN::LOCALE_FUNCTION(std::string x, bool TO_lower, std::string LOCALE_UTF) {

  boost::locale::generator gen;

  std::locale loc = gen(LOCALE_UTF);

  std::locale::global(loc);                         // Create system default locale

  //std::cout.imbue(loc);                           // gives an error when I do cran-checking due to std::cout

  if (TO_lower) {

    return boost::locale::to_lower(x);}             // Make it system global

  else {

    return boost::locale::to_upper(x);
  }
}


// convert to lower case (special case : LOCALE)
//

void TOKEN::conv_to_lower(std::string LOCALE_UTF) {

  for (unsigned int i = 0; i < v.size(); i++) {

    std::string tmp_v = v[i];

    if (LOCALE_UTF == "") {

      std::transform(tmp_v.begin(), tmp_v.end(), tmp_v.begin(), ::tolower);}

    else {

      tmp_v = LOCALE_FUNCTION(tmp_v, true, LOCALE_UTF);
    }

    v[i] = tmp_v;

    tmp_v.shrink_to_fit();
  }
}


// open language-specific-file of stop-words
//

void TOKEN::read_stopwords(std::vector<std::string> language) {

  stop_words = language;
}


// removes all occurences of the specified 'any_character' in the string
//

void TOKEN::remove_all(std::string any_character) {

  for (unsigned int i = 0; i < v.size(); i++) {

    v[i] = boost::remove_erase_if(v[i], boost::is_any_of(any_character));
  }
}


// convert to upper case  (special case : LOCALE)
//

void TOKEN::conv_to_upper(std::string LOCALE_UTF) {

  for (unsigned int i = 0; i < v.size(); i++) {

    std::string tmp_v = v[i];

    if (LOCALE_UTF == "") {

      std::transform(tmp_v.begin(), tmp_v.end(), tmp_v.begin(), ::toupper);}

    else {

      tmp_v = LOCALE_FUNCTION(tmp_v, false, LOCALE_UTF);
    }

    v[i] = tmp_v;

    tmp_v.shrink_to_fit();
  }
}


// remove punctuation       [ removes all special characters ]
//

void TOKEN::remove_punctuation() {

  for (unsigned int i = 0; i < v.size(); i++) {

    std::string tmp_v = v[i];

    tmp_v.erase(std::remove_if(tmp_v.begin(), tmp_v.end(), &ispunct), tmp_v.end());

    v[i] = tmp_v;

    tmp_v.shrink_to_fit();
  }
}


// remove numbers
//

void TOKEN::remove_numbers() {

  for (unsigned int i = 0; i < v.size(); i++) {

    std::string tmp_v = v[i];

    tmp_v.erase(std::remove_if(tmp_v.begin(), tmp_v.end(), &isdigit), tmp_v.end());

    v[i] = tmp_v;

    tmp_v.shrink_to_fit();
  }
}


// trim token
//

void TOKEN::trim_token() {

  for (unsigned int i = 0; i < v.size(); i++) {

    std::string tmp_v = v[i];

    boost::trim(tmp_v);

    v[i] = tmp_v;

    tmp_v.shrink_to_fit();
  }
}


// split a string sentence using multiple separators example : TOKENIZER("abc-*-ABC-*-aBc")
//

void TOKEN::TOKENIZER(std::string separator, bool remove_punctuation) {

  std::vector<std::string> new_vec;

  for (unsigned int i = 0; i < v.size(); i++) {

    std::string tmp_x = v[i];

    std::vector<std::string> tmp_vec;

    boost::split( tmp_vec, tmp_x, boost::is_any_of(separator), boost::token_compress_on );

    tmp_x.shrink_to_fit();

    if (remove_punctuation) {

      for (unsigned int i = 0; i < tmp_vec.size(); i++) {

        tmp_vec[i].erase(std::remove_if(tmp_vec[i].begin(), tmp_vec[i].end(), &ispunct), tmp_vec[i].end());
      }
    }

    new_vec.insert(std::end(new_vec), std::begin(tmp_vec), std::end(tmp_vec));

    tmp_vec.shrink_to_fit();
  }

  v.shrink_to_fit();

  v = new_vec;

  new_vec.shrink_to_fit();
}


// remove stopwords
//

void TOKEN::remove_stopwords(int threads) {

  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif

  std::unordered_map<std::string, std::vector<int> > counts;

  for (unsigned int i = 0; i < v.size(); i++) {

    counts[v[i]].push_back(i);
  }

  for (unsigned int j = 0; j < stop_words.size(); j++) {

    std::vector<int> tmp_word = counts[stop_words[j]];

    if (!tmp_word.empty()) {

      counts.erase (stop_words[j]);
    }
  }

  std::vector<std::string> vec_words;
  vec_words.reserve(counts.size());                                 // improves slightly the efficiency

  for(auto imap: counts) {

    vec_words.push_back(imap.first);                                // retrieve the keys from an unordered map
  }

  std::vector<int> insert_vals;                                     // flatten map-values and build an indices-vector

  for (unsigned int k = 0; k < vec_words.size(); k++) {

    std::vector<int> tmp_vec = counts[vec_words[k]];

    insert_vals.insert(std::end(insert_vals), std::begin(tmp_vec), std::end(tmp_vec));
  }

  std::unordered_map<std::string, std::vector<int> >().swap(counts); // release memory of the 'counts' object  [ http://stackoverflow.com/questions/10464992/c-delete-vector-objects-free-memory ]

  vec_words.shrink_to_fit();                                        // http://en.cppreference.com/w/cpp/container/vector/shrink_to_fit

  std::sort(insert_vals.begin(), insert_vals.end());                // sort the indices vector

  std::vector<std::string> result(insert_vals.size());              // subset [ to preserve the words order using indexing ]

  unsigned int f;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(insert_vals, result) private(f)
  #endif
  for (f = 0; f < insert_vals.size(); f++) {
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      result[f] = v[insert_vals[f]];
    }
  }

  insert_vals.shrink_to_fit();

  v = result;

  result.shrink_to_fit();
}


// keep strings within a specific range of characters
// [ If the 'v' vector includes a single string --meaning I return without applying the tokenization function-- then in case
//   that I use the 'keep_n_char' function it's possible that the output result will be an empty vector ]
//

void TOKEN::keep_n_char(long long max_length, int min_length, int threads) {

  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif

  std::unordered_map<int, std::vector<int> > counts;

  for (unsigned int i = 0; i < v.size(); i++) {

    int tmp_size = v[i].size();

    if (tmp_size >= min_length && tmp_size < max_length) {

      counts[tmp_size].push_back(i);
    }
  }

  std::vector<int> insert_vals;                                     // flatten map-values and build an indices vector

  for (unsigned int k = 0; k < counts.size(); k++) {

    std::vector<int> tmp_vec = counts[k];

    insert_vals.insert(std::end(insert_vals), std::begin(tmp_vec), std::end(tmp_vec));
  }

  std::unordered_map<int, std::vector<int> >().swap(counts);

  std::sort(insert_vals.begin(), insert_vals.end());

  std::vector<std::string> result(insert_vals.size());

  unsigned int f;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(insert_vals, result) private(f)
  #endif
  for (f = 0; f < insert_vals.size(); f++) {
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      result[f] = v[insert_vals[f]];
    }
  }

  insert_vals.shrink_to_fit();

  v = result;

  result.shrink_to_fit();
}



// porter-2-stemmer
// https://github.com/smassung/porter2_stemmer
//

/**
* @file porter2_stemmer.h
* @author Sean Massung
* @date September 2012
*
* Implementation of
* http://snowball.tartarus.org/algorithms/english/stemmer.html
*
* Copyright (C) 2012 Sean Massung**/

void TOKEN::porter2_stemmer(int threads) {
  
  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  unsigned int i;
    
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) private(i)
  #endif
  for (i = 0; i < v.size(); i++) {
    
    std::string tmp_prt = Porter2Stemmer::stem(v[i]);
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      v[i] = tmp_prt;
    }
  }
}


// sequential n-gram-stemmer
//

void TOKEN::NGRAM_SEQ(int min_n_gram, double gamma, int round_dec_places, int batches, int threads, bool verbose) {

  v = nst.frequency_seq_ngram(v, min_n_gram, gamma, round_dec_places, batches, threads, verbose);
}


// overlapping n-gram-stemmer
//

void TOKEN::NGRAM_OVERLAP(int n_grams, bool verbose) {

  v = nst.n_gram_stemming_frequency(v, n_grams, verbose);
}



// inner function for the 'secondary_n_grams' function
//

std::string TOKEN::inner_str(int n_gram, int i, std::vector<std::string>& vec, std::string& n_gram_delimiter) {
  
  std::string tmp_string;
  
  for (int j = i; j < i + n_gram; j++) {
    
    if (j == i) {
      
      tmp_string += vec[j];}
    
    else {
      
      tmp_string += n_gram_delimiter + vec[j];
    }
  }
  
  return tmp_string;
}



// secondary function for the n-grams-function
//

std::vector<std::string> TOKEN::secondary_n_grams(std::vector<std::string> vec, int n_gram, std::string n_gram_delimiter, int threads) {
  
  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  int vec_size = vec.size() - n_gram + 1;
  
  if (vec_size < 0) {
    
    vec_size = 0;
  }
  
  std::vector<std::string> out(vec_size);
  
  int i;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(vec_size, n_gram_delimiter, vec, n_gram, out) private(i)
  #endif
  for (i = 0; i < vec_size; i++) {
    
    std::string tmp_in = inner_str(n_gram, i, vec, n_gram_delimiter);
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      out[i] = tmp_in;
    }
  }

  return out;
}


// build n-grams using an std::vector
//

void TOKEN::build_n_grams(int min_n_gram, int max_n_gram,std::string n_gram_delimiter, int threads) {

  std::vector<std::string> insert_n_grams;

  for (int i = min_n_gram; i < max_n_gram + 1; i++) {

    std::vector<std::string> tmp_vec = secondary_n_grams(v, i, n_gram_delimiter, threads);

    insert_n_grams.insert(std::end(insert_n_grams), std::begin(tmp_vec), std::end(tmp_vec));
  }

  v = insert_n_grams;

  insert_n_grams.shrink_to_fit();
}



// build a sequence-vector specifying the start-point, the length
// of the vector and the distance between numbers (similar to the seq() in R but with different parameters)
//

std::vector<int> TOKEN::SEQ(int start, int length, int by) {

  std::vector<int> sqz(length);

  int count = 0;

  while(true) {

    if (count == 0) {

      sqz[count] = start;}

    else {

      start += by;

      sqz[count] = start;
    }

    count++;

    if (length < count) {

      break;
    }
  }

  return sqz;
}


// creates skip-n-grams
//

std::vector<std::string> TOKEN::secondary_skip_n_grams(std::vector<std::string> v, int n_gram, int skip, std::string n_gram_delimiter) {

  std::vector<std::string> out_skip_n_gram;

  int v_size = v.size();

  for (int i = 0; i < v_size; i++) {

    std::vector<int> sqz = SEQ(i, n_gram, skip + 1);

    bool flag_break = false;

    std::string string1;

    for (unsigned int j = 0; j < sqz.size(); j++) {

      if (sqz[j] < v_size) {

        if (j == 0) {

          string1 += v[sqz[j]];}

        else {

          string1 += n_gram_delimiter + v[sqz[j]];
        }
      }

      else {

        flag_break = true;

        break;
      }
    }

    if (!flag_break) {

      out_skip_n_gram.resize(i + 1);

      out_skip_n_gram[i] = string1;}

    else {

      break;
    }
  }

  return out_skip_n_gram;
}


// creates skip-n-grams: if skip = 0 it creates simple n-grams otherwise it adds iterative n-grams to a
// vector using the 'skip-parameter' as a distance between the words
//

void TOKEN::skip_n_grams(int n_gram, int skip, std::string n_gram_delimiter, int threads) {

  std::vector<std::string> insert_n_grams;

  for (int i = 0; i < skip + 1; i++) {

    if (i == 0) {

      std::vector<std::string> tmp_n_grams = secondary_n_grams(v, n_gram, n_gram_delimiter, threads);

      insert_n_grams.insert(std::end(insert_n_grams), std::begin(tmp_n_grams), std::end(tmp_n_grams));}

    else {

      std::vector<std::string> tmp_skip_grams = secondary_skip_n_grams(v, n_gram, i, n_gram_delimiter);

      insert_n_grams.insert(std::end(insert_n_grams), std::begin(tmp_skip_grams), std::end(tmp_skip_grams));
    }
  }

  v = insert_n_grams;

  insert_n_grams.shrink_to_fit();
}



// saves vocabulary counts in a single file
//

void TOKEN::vocab_counts_save(std::string output_path_file) {

  std::unordered_map<std::string, long long> myLines;

  for (unsigned int k = 0; k < v.size(); k++) {

    myLines[v[k]] += 1;
  }

  std::ofstream ofs;

  ofs.open(output_path_file, std::ios::app);

  for (auto& it : myLines) {

    ofs << it.first << "\t" << it.second << "\n";
  }

  ofs.close();
}


// concatenate an std::vector<std::string> to a single string
//

void TOKEN::concatenate(std::string delimiter) {

  std::string tmp_str = boost::algorithm::join(v, delimiter);

  v.clear();

  v.resize(1);

  v[0] = tmp_str;

  tmp_str.shrink_to_fit();
}


// save an std::string to a file
//

void TOKEN::save_2file(std::string folder, std::string path_extend) {

  std::string tmp_file = folder + path_extend;

  std::ofstream out(tmp_file);

  out << v[0];

  v.clear();

  v.resize(1);

  v[0] = "";      // in case that the output is saved to a file, then return "" in R-session

  out.close();
}


// std::ios::app is the open mode, "append" means new data will be written at the end of the file.
// http://stackoverflow.com/questions/6932409/writting-a-string-to-the-end-of-a-file-c
//

void TOKEN::append_2file(std::string folder, std::string CONCAT, bool tokenize_vector, std::string path_extend) {

  std::string tmp_file = folder + path_extend;

  std::ofstream out;

  out.open(tmp_file, std::ios::app);

  if (tokenize_vector) {

    out << CONCAT + v[0];}           // is needed if the append_2file() function is called inside a for-loop [ SEE token_big_files.cpp -> 'res_token_vector' AND 'res_token_list' ]

  else {

    out << v[0];
  }

  v.clear();

  v.resize(1);

  v[0] = "";      // in case that the output is saved to a file, then return an empty string ("") in the R-session
}


// return std::vector<std::string> in any case
//

std::vector<std::string> TOKEN::_object_vector() {

  return v;
}


