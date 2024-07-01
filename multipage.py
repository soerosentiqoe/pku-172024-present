import streamlit as st

class MultiPage: 
    def __init__(self) -> None:
        """Constructor to store variables."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages.
        Args:
            title ([str]): The title of page to add.
            func: Python function to render this page.
        """
        self.pages.append({
            "title": title, 
            "function": func
        })

    def run(self):
        # Dropdown to select the page to run  
        page = st.sidebar.selectbox(
            'Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        # Run the selected page
        page['function']() 