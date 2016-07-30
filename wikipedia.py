def search(l):
    print("Searching...")
    l.client.get("/w/index.php?search=Google&title=Special\%3ASearch&go=Go")

    # Way to get response code
    # print("Response Code: %s" %(response.status_code))

def open_main_page(l):
    print("Opening main page...")
    l.client.get("/wiki/Main_Page")

    # Mark a response as failure based on elapsed time
    # if response.elapsed.seconds > (1/100000):
    #     print("Failure")
    #     response.failure("Time elapsed !!!")
