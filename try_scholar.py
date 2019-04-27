import scholar

run_by_name_and_one_word = False
run_by_name_and_fill_article_name = True

querier = scholar.ScholarQuerier()
settings = scholar.ScholarSettings()
querier.apply_settings(settings)
query = scholar.SearchScholarQuery()

if run_by_name_and_one_word:
    query.set_author("Alan Turing")
    query.set_words("computing")
    query.set_num_page_results(1)

    querier.send_query(query)
    # Print the URL of the first article found
    print(querier.articles[0]['url'])

if run_by_name_and_fill_article_name:
    article_name = "The psychological asymmetry of Islamist warfare"
    author_name = "Mordechai Kedar"
    query.set_author(author_name)
    query.set_phrase(article_name)
    query.set_num_page_results(1)

    querier.send_query(query)
    scholar.txt(querier, True)   # Print article data in text format
