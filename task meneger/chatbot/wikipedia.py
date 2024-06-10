
import wikipediaapi

wik_search = True
while wik_search:
    
    def search_wikipedia(query):
        # Create a Wikipedia API object
        wiki = wikipediaapi.Wikipedia('en')  # Use 'en' for English Wikipedia

        # Search for the query
        search_results = wiki.page(query)

        # Check if the search result exists
        if not search_results.exists():
            print("No search results found.")
            return

        # Display the article summary
        print("\nArticle Summary:")
        search_results_summery = search_results.summary
        print(search_results_summery)


        rewev_save_input = input("save/review:")
        file_path = 'wikipedia.txt'
        
        # writign in to file 
        if rewev_save_input == "save":
            with open(file_path, 'a') as file:
                file.write(f"\n {search_results_summery} \n" )
                print("file fas been saved seccesfully")
        

        # reading from file 
        if  rewev_save_input == "review":
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)



    if __name__ == "__main__":
        # break point
        query = input("Enter your Wikipedia search query: ")
        search_wikipedia(query)
        if query == "quit":
            wik_search = False
            break
            
