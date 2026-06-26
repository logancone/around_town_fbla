from services.user_services import get_users_bookmarked_business_ids, RecommendationService

from dataclasses import dataclass, field

# AppSession class stores pertinent session information, such as:
# the active user_id, current business_id (business_page), and lightweight per-user cached info(bookmark_list)
class AppSession():
    def __init__(self):
        self.user_id = -1
        self.business_id = -1
        self.users_bookmarks = set()

        # CHANGE TO DYNAMIC!!!
        self.cur_lat = 37.0479891178922
        self.cur_lon = -76.4984552293407

        self.recommendation_service = RecommendationService(None)

    def set_user_id(self, new_id):
        self.user_id = new_id
        self.users_bookmarks = get_users_bookmarked_business_ids(new_id)
        self.recommendation_service = RecommendationService(new_id)
    
    def update_user_bookmarks(self):
        self.users_bookmarks = get_users_bookmarked_business_ids(self.user_id)
        self.update_recommendation_service()

    def update_recommendation_service(self):
        assert self.recommendation_service
        self.recommendation_service.build_profile()
    
    def is_business_bookmarked(self, business_id):
        return business_id in self.users_bookmarks
    
    def logout_user(self):
        self.user_id = -1
        self.users_bookmarks = set()
        self.recommendation_service = RecommendationService(None)
    
    def set_business_id(self, new_id):
        self.business_id = new_id
    
    def leave_business(self):
        self.business_id = -1


# Initializes an instance of the AppSession class to store relevant info
app_session = AppSession()