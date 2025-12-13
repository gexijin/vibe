#!/usr/bin/env python3
"""
PubMed paper retrieval script using Biopython's Entrez module.
"""

from Bio import Entrez
import sys

# Set your email (required by NCBI)
Entrez.email = "your.email@example.com"

def search_pubmed(query, max_results=10):
    """
    Search PubMed for papers matching the query.

    Args:
        query (str): Search query string
        max_results (int): Maximum number of results to retrieve

    Returns:
        list: List of paper dictionaries with details
    """
    print(f"Searching PubMed for: '{query}'")
    print(f"Retrieving up to {max_results} results...\n")

    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()

    id_list = record["IdList"]
    print(f"Found {record['Count']} total papers, retrieving {len(id_list)} papers.\n")

    if not id_list:
        print("No results found.")
        return []

    # Fetch details for each paper
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="xml", retmode="xml")
    records = Entrez.read(handle)
    handle.close()

    papers = []
    for i, paper in enumerate(records['PubmedArticle'], 1):
        article = paper['MedlineCitation']['Article']

        # Extract paper details
        pmid = paper['MedlineCitation']['PMID']
        title = article.get('ArticleTitle', 'No title')

        # Get authors
        authors = []
        if 'AuthorList' in article:
            for author in article['AuthorList'][:3]:  # First 3 authors
                if 'LastName' in author and 'Initials' in author:
                    authors.append(f"{author['LastName']} {author['Initials']}")
        authors_str = ", ".join(authors)
        if len(article.get('AuthorList', [])) > 3:
            authors_str += " et al."

        # Get journal and date
        journal = article.get('Journal', {}).get('Title', 'Unknown journal')
        pub_date = article.get('Journal', {}).get('JournalIssue', {}).get('PubDate', {})
        year = pub_date.get('Year', 'Unknown year')

        # Get abstract
        abstract = ""
        if 'Abstract' in article:
            abstract_texts = article['Abstract'].get('AbstractText', [])
            if isinstance(abstract_texts, list):
                abstract = " ".join(str(text) for text in abstract_texts)
            else:
                abstract = str(abstract_texts)

        paper_info = {
            'pmid': str(pmid),
            'title': title,
            'authors': authors_str,
            'journal': journal,
            'year': year,
            'abstract': abstract[:300] + "..." if len(abstract) > 300 else abstract
        }

        papers.append(paper_info)

        # Print paper info
        print(f"[{i}] PMID: {paper_info['pmid']}")
        print(f"    Title: {paper_info['title']}")
        print(f"    Authors: {paper_info['authors']}")
        print(f"    Journal: {paper_info['journal']} ({paper_info['year']})")
        print(f"    Abstract: {paper_info['abstract']}")
        print(f"    URL: https://pubmed.ncbi.nlm.nih.gov/{paper_info['pmid']}/")
        print()

    return papers

if __name__ == "__main__":
    # Get query from command line or use default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "immunotherapy melanoma"

    # Search PubMed
    papers = search_pubmed(query, max_results=10)

    print(f"\n{'='*60}")
    print(f"Retrieved {len(papers)} papers successfully!")
