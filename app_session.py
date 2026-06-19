from services.user_services import get_users_bookmarks

# AppSession class stores pertinent session information, such as:
# the active user_id, current business_id (business_page), and lightweight per-user cached info(bookmark_list)
class AppSession():
    def __init__(self):
        # self.user_id = -1
        self.user_id = 1
        self.business_id = -1
        self.users_bookmarks = set()

    def set_user_id(self, new_id):
        self.user_id = new_id
        self.users_bookmarks = get_users_bookmarks(new_id)

    def get_user_id(self):
        return self.user_id
    
    def get_user_bookmarks(self):
        return self.users_bookmarks
    
    def update_user_bookmarks(self):
        self.users_bookmarks = get_users_bookmarks(self.user_id)
    
    def is_business_bookmarked(self, business_id):
        return business_id in self.users_bookmarks
    
    def logout_user(self):
        self.user_id = -1
        self.users_bookmarks = set()
    
    def set_business_id(self, new_id):
        self.business_id = new_id
    
    def get_business_id(self):
        return self.business_id
    
    def leave_business(self):
        self.business_id = -1




# Initializes an instance of the AppSession class to store relevant info
app_session = AppSession()