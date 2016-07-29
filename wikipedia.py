def search(l):
    l.client.get("/w/index.php?search=Google&title=Special\%3ASearch&go=Go")

def open_main_page(l):
    l.client.get("/wiki/Main_Page")
