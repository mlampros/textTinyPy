
/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file UTILS.h
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: utility functions
 * 
 * @last_modified: December 2016
 * 
 **/



#ifndef __UTILScpp__
#define __UTILScpp__


//------------------------------
// include dependencies:

#include <boost/algorithm/string.hpp>
#include <boost/property_tree/xml_parser.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/foreach.hpp>
#include <fstream>
#include <vector>
#include <streambuf>

using boost::property_tree::ptree;

//------------------------------



struct keep_idx {                                           // struct for 'l1', 'l2' normalization
  
  long long idx;
  
  double count;
};


struct adjusted_sp_mat {                                   // struct for adjusted sparse matrix

  std::vector<std::string> adj_struct_terms;

  std::vector<long long> index_sparse_mat;
};


struct struct_term_matrix_double {                        // struct to return the terms, sparse-matrix
  
  std::vector<std::string> terms_out;
  
  std::vector<long long> col_idx_;
  
  std::vector<long long> row_idx_;
  
  std::vector<double> docs_cnt_;
};


struct struct_term_matrix {                               // struct to return the terms, sparse-matrix
  
  std::vector<std::string> terms_out;
  
  std::vector<long long> col_idx_;
  
  std::vector<long long> row_idx_;
  
  std::vector<long long> docs_cnt_;
};


struct struct_update_vars {
  
  std::vector<long long> COL_IDX;
  
  std::vector<long long> ROW_IDX;
  
  std::vector<double> COUNT_DOUBLE;
  
  std::vector<long long> COUNT;
};


struct xml_struct {                                     // struct for the 'xml_child_attributes' function 
  
  std::vector<std::string> KEYS;
  
  std::vector<std::string> VALUES;
};




// class utils_cpp
//


class utils_cpp {
  
  private:
    
    std::vector<std::string> ks;
    
    std::vector<std::string> vls;
  
  public:
    
    utils_cpp() { }

    
    // sort function for 'l1', 'l2' normalization ( term_matrix.h )
    //
    
    static bool sort_by_norm(const keep_idx &a, const keep_idx &b) {
      
      return a.idx < b.idx;
    }
    

    // secondary function for xml_boost_traverse ( it splits a path into sub-paths )
    //
    
    std::vector<std::string> split_path_xml(std::string x) {
      
      std::vector<std::string> tmp_vec;
      
      boost::split( tmp_vec, x, boost::is_any_of("/"), boost::token_compress_on );
      
      tmp_vec.erase(tmp_vec.begin());
      
      return tmp_vec;
    }
    
    
    // xml parser for subchildern's elements and attributes using boost
    // https://akrzemi1.wordpress.com/2011/07/13/parsing-xml-with-boost/
    //
    
    std::vector<std::string> xml_subchildren_attrs_elems(std::string input_path_file, std::string xml_path, std::string output_path_file = "", std::string empty_key = "") {
      
      std::vector<std::string> create_path = split_path_xml(xml_path);
      
      std::filebuf fb;
      
      fb.open(input_path_file, std::ios::in);
      
      std::istream is(&fb);
      
      using boost::property_tree::ptree;                                              // populate tree structure pt
      
      ptree pt;
      
      read_xml(is, pt, boost::property_tree::xml_parser::no_comments | boost::property_tree::xml_parser::trim_whitespace);
      
      std::vector<std::string> ans;                                                  // traverse pt
      
      std::ofstream out;
      
      if (output_path_file != "") {
        
        out.open(output_path_file, std::ios::app);
      }
      
      for (const auto& kv : pt.get_child(create_path[0])) {                          // C++11 loop rather than BOOST_FOREACH
        
        if (kv.first == create_path[1]) {
          
          if (output_path_file == "") {
            
            std::string tmp = kv.second.get<std::string>(create_path[2], empty_key);
            
            ans.push_back(tmp);}
          
          else {
            
            out << kv.second.get<std::string>(create_path[2], empty_key) + "\n";
          }
        }
      }
      
      if (output_path_file != "") {
        
        out.close();
      }
      
      fb.close();
      
      return ans;
    }
    
    
    // helper for the 'xml_child_attributes' function 
    //
    
    const ptree& empty_ptree() {                             
      
      static ptree t;
      
      return t;
    }
    
    
    /// xml parser for child's attributes using boost
    // http://stackoverflow.com/questions/14010473/parsing-xml-attributes-with-boost
    //

    void xml_child_attributes(std::string input_path_file, std::string xml_root, std::string output_path_file = "") {

      std::ofstream ofs(output_path_file);
      
      ptree tree;
      
      read_xml(input_path_file, tree);
      
      const ptree & formats = tree.get_child(xml_root, empty_ptree());
      
      BOOST_FOREACH(const ptree::value_type & f, formats) {
        
        const ptree & attributes = f.second.get_child("<xmlattr>", empty_ptree());
        
        BOOST_FOREACH(const ptree::value_type &v, attributes){
          
          ks.push_back(v.first.c_str());
          
          vls.push_back(v.second.data().data());
          
          if (output_path_file != "") {
            
            ofs << v.first.c_str() << "  " << v.second.data().data() << "\n";
          }
        }
      }
      
      ofs.close();
    }
    
    
    // return data for the 'xml_child_attributes' function
    //
    
    xml_struct output_xml_data() {
      
      return {ks, vls};
    }
    
    
    ~utils_cpp() { }
};



#endif

